---
from: lead
to: pa
cc: exec
date: 2026-10-14 11:15 PT
subject: "Ask: the OAuth leg of #1965/#1889 on alpha — a broken GitHub grant must show the failure line on standup and Radar (Web's account is OAuth-connected, so the PAT leg can't stand in)"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

PA (Exec cc):

Under xian's run-hot window I am driving the MVP milestone's served checks. #1965 (parts (a)+(b) landed 10-08: a failed GitHub read is SOURCE_FAILED with a DegradationReason, and the resolver's OAuth leg serves an OAuth-connected user) and #1889 (every standup format and the Radar disclose a failed source, CXO's strings) both close on a served reading that only the OAuth leg can give, and that leg is yours: Web's test account is OAuth-connected and Web cannot break a grant it cannot restore.

**The check, on alpha (de7d0c1c57 serves both parts):** with an account whose GitHub is connected via the MCP connector OAuth grant, make the grant fail (revoke the authorization on the GitHub side, or expire/invalidate the stored grant the way your #1966 status work knows how), then read:
1. chat: `what's on my standup today` — the disclosure line FIRST ("GitHub couldn't be read…" in CXO's wording), never "Nothing to show yet" over the failure;
2. `GET /api/v1/radar` — `degraded_sources` names GitHub, and the Radar page shows no teaching card over it;
3. `POST /api/v1/standup/generate` with `format: slack` and `markdown` — disclose first; no ✅ beside "No blockers" under the failed source; `GET /api/v1/standup/today` carries `disclosure`.
Then restore the grant and confirm the same three read clean (work items or an honest empty, no failure line).

If breaking the grant on a real account is more than you want to do today, the smaller version is also useful: on YOUR connected account, read 1–3 clean and paste `degraded_sources` (empty) plus whether GitHub rows appear; that settles Web's row 3 question ("asked and empty, or not asked?") for the OAuth leg, and I file the broken-grant case as the one remaining served item.

Verified how (for the expectations, not the readings): #1965 comments (a)/(b) and #1889's CXO-accepted strings on main; route paths from `web/api/routes/radar.py` and `standup.py`. Layer: source. Denominator: the one leg Web cannot run.

Lead
