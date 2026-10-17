"""#1982 — the user's GitHub PAT, encrypted at rest under the GitHub-only context.

Settings → GitHub has always saved the PAT through ``KeychainService`` under the
user-scoped name ``<uid>_github_token_api_key``. On the hosted box that is the
``secure_credentials`` table, encrypted under a PER-USER HKDF context
(``secure_credentials.<name>``) that no fixed subkey list can name. The MCP app
holds exactly one subkey, ``user_api_keys.secret.github`` (Arch's ruling,
2026-10-11), so a PAT-only user was ``CONNECT_REQUIRED`` there.

Arch's resolution (same day): a DUAL WRITE. The save route also stores the PAT
through ``UserAPIKeyService.store_user_key(provider="github", validate=False)``,
which lands the ``user_api_keys`` row under the GitHub context the MCP app can
read (``github_adapter._user_pat_at_rest`` reads it first). The keychain copy
stays: alpha's sync readers (``GitHubConfigService``) use it. Disconnect deletes
both. ``scripts/backfill_github_pat_rows_1982.py`` copies the PATs saved before
this landed.

``validate=False`` and ``security_check=False`` on purpose: the route already
verified the token with GitHub (``verify_github_token``) before storing it. A
second provider check is a wasted call, and the #268 format/strength/leak
validator (which ``validate=False`` does NOT skip) would be a second way for the
save to fail, landing after the keychain write as a half-save.
"""

from __future__ import annotations

import structlog

GITHUB_PAT_PROVIDER = "github"
KEYCHAIN_PAT_PROVIDER = "github_token"  # the KeychainService provider label Settings uses

logger = structlog.get_logger(__name__)


async def store_user_pat_at_rest(user_id: str, token: str) -> None:
    """Write the user's PAT to ``user_api_keys`` (provider ``github``) under the
    GitHub-only context. Raises on failure: a silent half-save would leave the MCP
    app unable to serve a PAT the Settings page reports as connected."""
    from services.database.session_factory import AsyncSessionFactory
    from services.security.user_api_key_service import UserAPIKeyService

    async with AsyncSessionFactory.session_scope_fresh() as session:
        await UserAPIKeyService().store_user_key(
            session=session,
            user_id=str(user_id),
            provider=GITHUB_PAT_PROVIDER,
            api_key=token,
            validate=False,
            security_check=False,  # verified live with GitHub by the caller (see module doc)
        )
    logger.info("github_pat_stored_at_rest")  # no identifiers, no token


async def delete_user_pat_at_rest(session, user_id: str) -> bool:
    """Delete the at-rest PAT row (and the key service's own keychain copy) for
    ``user_id``. ``False`` when there was no row. Used by disconnect so a revoke
    leaves no row the MCP app could still read."""
    from services.security.user_api_key_service import UserAPIKeyService

    return await UserAPIKeyService().delete_user_key(session, str(user_id), GITHUB_PAT_PROVIDER)
