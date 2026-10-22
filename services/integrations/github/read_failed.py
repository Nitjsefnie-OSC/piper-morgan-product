"""#2128: a GitHub read that did not happen is a failed read, never an empty result.

Raised by the adapter's collection reads when the account has no credential, the
transport answered nothing, or the call errored; propagated by the router; caught by
the handlers that count, which then say the read failed instead of reporting zero.
The shape #2121 established for the activity read (a ``read_failed`` marker on a
dict) expressed as an exception for the list-returning reads.
"""

from __future__ import annotations

from typing import Optional


class GitHubReadFailed(Exception):
    """The read did not happen. ``reason`` is a short code (no_credential,
    no_response, no_repository, or an exception type name); ``repo`` is
    ``owner/name`` when known, for the sentence the person reads."""

    def __init__(self, reason: str, repo: Optional[str] = None):
        self.reason = reason
        self.repo = repo
        super().__init__(f"GitHub read failed ({reason})" + (f" for {repo}" if repo else ""))
