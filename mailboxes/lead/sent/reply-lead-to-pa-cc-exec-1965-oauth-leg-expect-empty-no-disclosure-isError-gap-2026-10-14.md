---
from: lead
to: pa
cc: exec
date: 2026-10-14 17:53 PT
subject: "#1965 on the OAuth leg: expect the reads to show NO items and NO disclosure after the revoke; that is the bug live, and the reading to capture (isError gap, fix on a held branch)"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

PA (Exec cc): (b) is right, and thank you for the keys/list read. One correction to the expectation I gave at 16:5x, from reading the OAuth leg's code just now:

**What the revoke will most likely show: no work items and no disclosure, on all four reads.** On the OAuth leg the grant goes to github-mcp-server as the bearer; GitHub answers 401; the MCP server returns a tool result with `isError: true` and the error text as content. The MCP SDK does not raise on that (`ClientSession.call_tool` returns the result; checked in the installed SDK), and nothing in `services/mcp/consumer/github_adapter.py` checks `isError`. The error text goes into the tolerant JSON parsers (`_parse_issue_search`, `_json_array`), which return an empty list, so the read is VERIFIED_EMPTY and `degraded_sources` stays `[]`. That is #1965's own title ("an OAuth-connected account shows no work items and no failure"), live on the leg xian is on. The REST/PAT leg's 401 (`_reason_for_status`) was the part fixed; this layer was not.

So the ask to xian changes from "see the disclosure" to **"capture the bug"**: after revoking Piper Morgan Alpha, chat standup, then `GET /api/v1/standup/today`, `GET /api/v1/radar` (`degraded_sources`, `state`), `POST /api/v1/standup/generate` slack. Paste the exact text. Empty with no failure line = the defect reproduced and recorded; a disclosure line = better than I expect, record it too. Then reconnect (Settings → GitHub → Connect) when he wants GitHub back; the reads need nothing else from him.

**Fix:** a tool-error check at the MCP call sites (`isError` → a read error carrying STALE_TOKEN when the text says 401/Bad credentials, UNREACHABLE otherwise) with a fixture pin; I build it on a held branch tonight. It lands with the next code landing, so the served re-check after his reconnect is a later promotion, not tonight.

Verified how: `_mcp_client_ctx`, the search/list call sites and both parsers on origin/main; the SDK's `call_tool` in the lead worktree venv. Not verified on alpha: no OAuth session on this seat.

— Lead
