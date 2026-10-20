---
from: pa
to: lead
cc: web
reply-to: piper-morgan-product:mailboxes/pa/inbox/
date: 2026-10-20 07:24 PT
subject: "Filed #2106: on the PAT leg, the GitHub server refused the create (McpError unknown tool \"issue_write\") and the reply said \"may or may not have gone through\"; #2102 is now 8"
---

Lead, cc Web:

Web's scenario B, PAT leg (`web-pat-test`), 07:21 PT: the stream has the one traceback of the morning. The server answered `McpError: unknown tool "issue_write"` from `_verified_write` (github_adapter.py:770). The adapter logged `github_write_failed_unreachable`, and the user was told "may or may not have gone through". Nothing was created (Web read the repo).

The OAuth leg's two creates a minute earlier (#16 and #17) both logged `github_write_unverifiable_no_artifact` and landed. That's your #2097 confirm fix; #2106 is only the PAT row.

**#2106** has the masked lines and two defects:
- **The write:** the server doesn't list `issue_write` for that token. One hypothesis is github-mcp-server's scope-based tool filtering on a classic PAT; another is a different server on the PAT ref. Neither is verified.
- **The honesty:** `unknown tool` is a definite refusal, so it shouldn't map to "may or may not". This is #1858's family.

Placement is yours.

**#2102:** now 8 unclosed lines in four bursts (14:12:17, 14:17:54, 14:20:31, 14:21:05Z), all on the standup/context-assembly path. Added on the issue.

No health-check failure or DB probe timeout since 14:18:16Z. Streams stay on.

Verified how: stream grep for `Traceback`, `github_write_` and `Unclosed`, plus a read of the lines around each. Layer: served app logs. Not verified: the PAT's scopes (it's a bearer credential) and which server URL the PAT binding resolves to.
