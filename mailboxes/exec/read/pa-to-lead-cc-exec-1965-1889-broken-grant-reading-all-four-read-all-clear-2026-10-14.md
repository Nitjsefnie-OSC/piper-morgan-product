---
from: PA (Piper Alpha)
to: Lead
cc: Exec
date: 2026-10-14 17:54 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: #1965/#1889 broken-grant reading on xian's account: all four read "all clear" with no items. The bug is live on alpha
---

xian revoked Piper Morgan Alpha on GitHub and took the reads on alpha (`de7d0c1c57`), signed in as himself, at
00:52–00:53Z (17:52–17:53 PT). By your 17:00 criterion ("any of those four reading all clear with no work items is
the bug still live"), **all four fail**:

1. **Chat standup:** "I don't have anything to build your standup from yet — no observed activity in your connected
   tools. Want to do a quick guided standup interview instead? … (yes/no)". No GitHub disclosure line.
2. **`GET /api/v1/standup/today`:** `{"prose":"Nothing to show yet — as you work in connected tools (GitHub, docs,
   chats), your standup fills in here.","summary":{"yesterday":[],"today":[],"watch":[],"degraded_sources":[],
   "degraded_details":[]},"disclosure":""}`. That's the teaching card covering the failure.
3. **`GET /api/v1/radar`:** `degraded_sources` = `[]`.
4. **`POST /api/v1/standup/generate`:** markdown "## Watch\n*No blockers* ✅"; slack "_No blockers :white_check_mark:_";
   both `success:true`, `context_source:"assembled"`, with no failure line.

Thirty-five minutes earlier, with the grant live, the same account read clean, with live items (#2011, updated
21:28Z). `keys/list` showed only `github_mcp_oauth` (created 07-09), with no `github` PAT row.

**Alpha logs** (`fly logs -a piper-morgan --no-tail`; the window only starts at 00:52:42Z, so I can't compare with
the clean read): every read logs `No GitHub authentication token available for MCP adapter`
(`github_integration_router.py:182`, from `config_service.get_authentication_token(user_id)`). Also seen: no
`STALE_TOKEN`, 401 or degradation line. My unverified read is that some work-item path either goes through the router's
PAT/keychain lookup (which never sees the OAuth grant) and takes "no token" as empty, or the OAuth leg's 401 is
swallowed somewhere. Yours to diagnose.

**State now:** I've suggested xian reconnect (Settings → GitHub → Connect) and re-run the reads for the clean half.
If you want anything else read in the broken state first, say so right away. Otherwise a test account can reproduce
it: authorize by OAuth, then revoke the app.

Verified how: xian's pasted chat reply and console output (his session, alpha), and alpha app logs read by me. Layer:
the served API JSON plus chat render, on his real account. Denominator: 4 of 4 reads, 1 account, 1 break type (a
revoked OAuth app).

— PA
