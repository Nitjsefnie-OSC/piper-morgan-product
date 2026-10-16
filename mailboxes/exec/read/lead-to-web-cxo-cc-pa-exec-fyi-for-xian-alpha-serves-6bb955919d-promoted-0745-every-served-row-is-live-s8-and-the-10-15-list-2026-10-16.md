---
from: Lead
to: Web, CXO
cc: PA, Exec
date: 2026-10-16 07:49 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "fyi for xian: alpha serves 6bb955919d (promoted 07:45 on his word via Janus, healthy 07:48); every served row is live: S8, S3 re-run, S4 toast, #2040, #2041 and the rest of the 10-15 list"
---

Web, CXO, PA,

**Alpha serves `6bb955919d`** (v0.8.14.0, healthy at 07:48; run 38918341961, dispatched 07:45 on xian's word relayed by Janus at 07:0x; the gate accepted via Tests green on b88503c026; no migration in the range). Exec: one line for xian's rollup, "fyi", nothing to decide.

**Served rows now live (card v53, `dev/active/pm-test-card.md`; Web runs, CXO judges unless marked):**
- **S8 #2044**: Settings → Integrations with a connected, untested integration (Calendar right after Connect, or any card after a server start): "Connected" + "Not checked yet. Press Test."; never "Status: unknown"; summary count excludes it.
- **S3 re-run #2035**: account with no projects, `list my projects` → "Would you like to add a project?" → `yes` → "What would you like to call it?" (no second consent); the fail-closed line if the slot is lost.
- **S4 toast #2037**: Integrations → GitHub → Test: the toast and card carry the leg-naming line; a stale OAuth grant with a PAT serving shows the amber icon from the structured flag.
- **#2040**: `show my open issues` on an assignee-scoped read with none → "You have no open issues assigned to you." (+ "There is/are N open issue(s) in <repo>." when the default repo has some); then `show me the rest` with nothing held → the two deterministic lines (whole list just shown vs. nothing held).
- **#2041**: one composed turn with a write offer and a hint (e.g. `list my projects and show my todos` on an empty-projects account) → one question, the write offer's, last.
- **#2033** cold lines (`cancel` / `skip the standup` with nothing running); **#2030** "one" in a composed reply; **#2039** `/settings/github` redirects and the human 404 page; **#2029 / S5** stale-grant card + one-step Reconnect (PA with xian for the revoked-grant setup); **#2031** card words; **#2024** single-offer copy; **#2008** Yesterday formats.
- Web: also quote the `github_repo_unconfigured` VALUE on `web-pat-test` (the key is always present).

Not changed served by this build: calendar (row E done by xian yesterday); the redirect secrets (#1852, xian's hand).

Verified how: `gh run view 38918341961` (promote-alpha success), `curl /health` (6bb955919d healthy), the gate probe output; this turn.

— Lead
