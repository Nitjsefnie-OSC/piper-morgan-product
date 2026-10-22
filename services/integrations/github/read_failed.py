"""One exception for "a GitHub read that did not happen" (#1965, #2128, #1524; unified by
Arch's ruling of 2026-10-22).

Raised by the adapter's reads (strict and list), propagated by the router, caught by the
handlers that would otherwise report "none" or a zero. ``[]`` from a list read means the
repo answered and has none; this exception means it did not answer for us.

``reason`` is the connector taxonomy (``DegradationReason``), one taxonomy for every
GitHub failure, so "re-authorize", "not found" and "down" stay distinct downstream:

| condition                          | reason                        |
|------------------------------------|-------------------------------|
| no repository resolved             | ``REPO_UNRESOLVED``           |
| no response, or a transport error  | ``UNREACHABLE``               |
| an HTTP status                     | ``_reason_for_status`` (#1965) |
| no credential for the account      | ``None`` (CXO: no credential is not "not connected") |
| anything else                      | ``None`` (unclassified)       |

``repo`` (``owner/name``) is for the sentence the person reads; ``detail`` is a short code
or exception type name for the log. Neither ever carries a token or response text.
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:  # the connector package imports the adapter, which imports this module
    from services.mcp.consumer.connector import DegradationReason


class GitHubReadFailed(Exception):
    """A GitHub read that did not happen."""

    def __init__(
        self,
        message: str = "",
        reason: Optional["DegradationReason"] = None,
        *,
        repo: Optional[str] = None,
        detail: Optional[str] = None,
    ):
        super().__init__(message or detail or "GitHub read failed")
        self.reason = reason
        self.repo = repo
        self.detail = detail

    @property
    def reason_code(self) -> str:
        """``reason.value`` or ``"unclassified"``: what ``intent_data`` and logs carry."""
        return self.reason.value if self.reason is not None else "unclassified"


def transport_reason(exc: BaseException) -> Optional["DegradationReason"]:
    """UNREACHABLE for a transport fault (timeout, connection, OS error); None otherwise."""
    import aiohttp

    from services.mcp.consumer.connector import DegradationReason

    transport = (asyncio.TimeoutError, TimeoutError, OSError, aiohttp.ClientError)
    return DegradationReason.UNREACHABLE if isinstance(exc, transport) else None


def repo_unresolved() -> GitHubReadFailed:
    """No repository resolved for the read (REPO_UNRESOLVED). A factory so callers
    need not import the connector package (the import cycle above)."""
    from services.mcp.consumer.connector import DegradationReason

    return GitHubReadFailed(
        "no repository resolved", DegradationReason.REPO_UNRESOLVED, detail="no_repository"
    )
