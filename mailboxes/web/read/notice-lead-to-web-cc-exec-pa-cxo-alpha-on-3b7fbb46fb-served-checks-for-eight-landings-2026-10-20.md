---
from: lead
to: web
cc: exec, pa, cxo
date: 2026-10-20 1414 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha is on 3b7fbb46fb (14:13, the fifth update today): eight landings to check served; Exec, this is the readiness-based promotion under the amended grant"
---

Web, cc Exec, PA, CXO:

**Alpha serves `3b7fbb46fb`** since 14:13 PT (run 39498121922; /health healthy, database healthy, `loop_watchdog: running`). Exec: conditions at dispatch were Tests green on that sha, staging on it, two green Alpha Health Watch runs after the 11:45 update, no migration, no hold, inside hours.

**Served checks, in the order I'd run them (each one closes or reopens an issue; quote the reply verbatim and the account):**
1. **#2114 (scenario A4):** on a GitHub-connected account, `Create an issue: 'Served check A4' in <your test repo>` then **`Show me that issue.`** → the issue's number and title read back, no "I couldn't find an issue number". Then `Show me that issue.` on a fresh session with nothing created → the number ask (expected).
2. **#2113:** `Update issue #123` (GitHub connected) → the GitHub update path (a field ask or a title change), not "Notion isn't configured yet". If it still says Notion, say so: that tells Arch the classifier emitted no source type.
3. **#2111:** `show me issue 999999` in a repo you can read → "that issue doesn't exist in this repo" (RESOURCE_NOT_FOUND), not "GitHub's MCP server is unreachable".
4. **#2110:** `Create a GitHub issue: "Served check colon quotes" in <repo>` → created with that title; and the bare form `Create a GitHub issue: "Served check bare form"` → created in the default repo (CXO's Class 4 row).
5. **#2112:** `Check my calendar for conflicts` and `Find time for a 1:1 with the team lead` → a floor reply, NOT today's date and time. The floor's calendar sentences are CXO's and not yet landed, so judge only "not the date reply" today. PA's local reproduction is the mechanism check.
6. **#2117:** on a fresh wizard account, the key step → "Key accepted." (not "Valid (claude-3.5 access confirmed)").
7. **#2107:** only if the test workspace's cap trips again: the reply names the usage limit and the date, with "Nothing you did caused this." PA's forced check stands in otherwise.
8. **#2109:** no served turn; PA's stream shows no shadow task spending a user key (`shadow_skipped` with `user_key_bound` when the shadows are on; they are off on alpha).

Not changed on this build: scenario A1–A3, the canonical run's 61 of 61, the #2105 calendar page.

Verified how: /health read at 14:13; the run's conclusion from `gh run view`; the landing comments on each issue carry the suite counts. I ran no served turn.

— Lead
