"""Admin Invites API (#2081): mint, list (masked) and revoke alpha invite codes
from the signed-in admin's own browser, instead of ``fly ssh console``.

Every route requires ``require_admin`` (users.is_admin, live DB read, fail
closed; #1485's dependency, no second authorization path). The mint response
carries the raw codes ONCE with ``Cache-Control: no-store``; no later read
returns them (HOST ruling 2). The page sends nothing anywhere: this API mints
and lists, it never emails or posts an invite (HOST ruling 7). The break-glass
script ``scripts/mint_prod_invite.sh`` stays, with its seat rule unchanged
(HOST ruling 6).
"""

from __future__ import annotations

from typing import List, Optional

import structlog
from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel, Field

from services.auth.auth_middleware import require_admin
from services.auth.invite_admin_service import (
    MAX_PER_DAY,
    MAX_PER_REQUEST,
    InviteAdminError,
    list_invites,
    mint_invites,
    minted_today,
    revoke_invite,
)
from services.auth.jwt_service import JWTClaims
from services.database.session_factory import AsyncSessionFactory

logger = structlog.get_logger()

router = APIRouter(prefix="/api/v1/admin/invites", tags=["admin-invites"])


class MintRequest(BaseModel):
    count: int = Field(..., ge=1, le=MAX_PER_REQUEST)


class MintResponse(BaseModel):
    codes: List[str]  # raw, shown once
    masked: List[str]
    minted_today: int
    daily_limit: int


class InviteRowOut(BaseModel):
    masked: str
    created_at: Optional[str]
    used_at: Optional[str]
    used_by: Optional[str]
    status: str


class InviteListResponse(BaseModel):
    invites: List[InviteRowOut]
    minted_today: int
    daily_limit: int
    per_request_limit: int


def _refuse(exc: InviteAdminError) -> HTTPException:
    return HTTPException(status_code=exc.status_code, detail=exc.reason)


@router.get("", response_model=InviteListResponse)
async def list_invite_codes(admin: JWTClaims = Depends(require_admin)) -> InviteListResponse:
    async with AsyncSessionFactory.session_scope() as session:
        rows = await list_invites(session)
        today = await minted_today(session)
    return InviteListResponse(
        invites=[
            InviteRowOut(
                masked=r.masked,
                created_at=r.created_at.isoformat() if r.created_at else None,
                used_at=r.used_at.isoformat() if r.used_at else None,
                used_by=r.used_by,
                status=r.status,
            )
            for r in rows
        ],
        minted_today=today,
        daily_limit=MAX_PER_DAY,
        per_request_limit=MAX_PER_REQUEST,
    )


@router.post("", response_model=MintResponse)
async def mint_invite_codes(
    body: MintRequest, response: Response, admin: JWTClaims = Depends(require_admin)
) -> MintResponse:
    try:
        async with AsyncSessionFactory.session_scope() as session:
            codes = await mint_invites(session, count=body.count, actor_user_id=admin.user_id)
            today = await minted_today(session)
    except InviteAdminError as exc:
        raise _refuse(exc)
    # The one time the raw codes travel; nothing may cache them.
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    from services.auth.invite_admin_service import mask

    return MintResponse(
        codes=codes,
        masked=[mask(c) for c in codes],
        minted_today=today,
        daily_limit=MAX_PER_DAY,
    )


@router.post("/{masked}/revoke")
async def revoke_invite_code(masked: str, admin: JWTClaims = Depends(require_admin)) -> dict:
    try:
        async with AsyncSessionFactory.session_scope() as session:
            done = await revoke_invite(session, masked=masked, actor_user_id=admin.user_id)
    except InviteAdminError as exc:
        raise _refuse(exc)
    return {"revoked": done, "message": f"Revoked {done}. It can no longer create an account."}
