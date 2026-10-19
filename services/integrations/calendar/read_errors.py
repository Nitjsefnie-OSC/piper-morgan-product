"""#2092: classify a failed Google Calendar read without importing the adapter.

Lives outside ``services.mcp.consumer`` so both the adapter and the OAuth
handler's Settings-Test probe can share it under the router pattern gate
(``scripts/check_direct_imports.py``: callers never import the adapter module).
"""


def classify_calendar_read_error(exc: BaseException) -> str:
    """A short, user-safe class for a failed Google Calendar read.

    "insufficient_scope" when Google refused for missing permission (the 2026-10-19
    alpha shape: HTTP 403 "Request had insufficient authentication scopes");
    "unauthorized" for a rejected or expired token (401 / invalid_grant);
    "not_found" for a calendar id the account cannot see (404); else "error".
    Never carries the exception text (it can hold URLs and ids).
    """
    text = str(exc).lower()
    if "insufficient" in text and ("scope" in text or "permission" in text):
        return "insufficient_scope"
    if "401" in text or "invalid_grant" in text or "unauthorized" in text:
        return "unauthorized"
    if "404" in text or "not found" in text:
        return "not_found"
    return "error"
