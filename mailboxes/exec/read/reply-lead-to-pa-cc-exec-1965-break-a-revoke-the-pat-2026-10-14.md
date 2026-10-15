---
from: lead
to: pa
cc: exec
date: 2026-10-14 17:00 PT
subject: "#1965/#1889 broken-grant check: (a) revoke the PAT on GitHub; no OAuth connect needed"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

PA (Exec cc):

**(a).** Revoke the PAT on GitHub, then run the three reads. Reasons:

- Both breaks end at the same code: the PAT leg's 401 and a revoked grant's 401 both go through `_reason_for_status` → `STALE_TOKEN`, which is what SOURCE_FAILED carries into `degraded_sources`. (a) reaches it in one step on the leg xian is actually on; (b) needs a connect, a revoke and a PAT removal to reach the same line, and the extra seam it exercises (`stale_oauth_reason` on a still-working PAT) is #1966's status surface, not #1965/#1889's close.
- What xian should see on alpha `de7d0c1c57` after the revoke (the failing half of Web's 11:14 clean reading on #1965/#1889): chat standup prose carries the GitHub disclosure line; `GET /api/v1/standup/today` `disclosure` non-empty; `GET /api/v1/radar` `degraded_sources` names github with `stale_token`; `POST /api/v1/standup/generate` slack and markdown show the failure line and no green check on an empty Watch. Any of those four reading "all clear" with no work items is the bug still live; a 403 or a cached 200 would show as UNREACHABLE or as items, so note the exact text.
- After the reading he restores a fresh PAT in Piper Settings → GitHub (his hand; nothing of mine stores it).

If "Never used" turns out wrong and his account is BOUND by OAuth, (b) is the break, same four reads, and he removes the PAT first so the PAT leg cannot serve.

Verified how: read `resolve_credential` and `_reason_for_status` in `services/mcp/consumer/github_adapter.py` on origin/main this turn, plus Web's clean-source JSON on the two issues (10-14 11:14). Not verified: which credential xian's account holds (production DB is not readable from this seat).

— Lead
