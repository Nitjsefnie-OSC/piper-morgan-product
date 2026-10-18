"""The one place the web session cookies are written (#2078).

Login, token refresh and the setup wizard's create-user all issue the same
pair of httponly cookies. Before #2078 the cookie code lived twice in
``web/api/routes/auth.py``; create-user needed it too (Arch, 2026-10-17:
"through the same helper login uses, don't copy the cookie code"), so it is
factored here, under ``services/auth`` so a route module never imports another.

``secure`` follows the edge protocol: behind fly-proxy the internal hop is
http, so the forwarded proto decides whether the cookie carries Secure on the
real HTTPS site (2026-07-12).
"""

from __future__ import annotations

from fastapi import Request, Response

AUTH_COOKIE = "auth_token"
REFRESH_COOKIE = "refresh_token"
AUTH_COOKIE_MAX_AGE = 86400  # 24 hours for alpha testing UX
REFRESH_COOKIE_MAX_AGE = 7 * 86400  # 7 days; matches JWTService's refresh_token_expire_days


def is_https_request(request: Request) -> bool:
    """True when the edge served this request over HTTPS (forwarded proto first)."""
    return request.headers.get("x-forwarded-proto", request.url.scheme).lower() == "https"


def set_session_cookies(
    response: Response,
    request: Request,
    *,
    access_token: str,
    refresh_token: str,
) -> None:
    """Set the ``auth_token`` and ``refresh_token`` cookies with the flags
    login has always used: httponly, samesite=lax, Secure on HTTPS."""
    secure = is_https_request(request)
    response.set_cookie(
        key=AUTH_COOKIE,
        value=access_token,
        httponly=True,
        secure=secure,
        samesite="lax",
        max_age=AUTH_COOKIE_MAX_AGE,
    )
    response.set_cookie(
        key=REFRESH_COOKIE,
        value=refresh_token,
        httponly=True,
        secure=secure,
        samesite="lax",
        max_age=REFRESH_COOKIE_MAX_AGE,
    )
