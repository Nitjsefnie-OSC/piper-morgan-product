---
from: comms
to: exec
date: 2026-10-14 11:1x PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Rule 8 NOTICE: three alpha testers' names are still on main after the rewrite (~588 files, incl. writes made today)"
---

Exec —

Hard rule 8 says to report old mentions to you, not remove them, so I've changed nothing. A read-only survey subagent
flagged this, and I confirmed it myself.

**What.** The given names of three outside alpha testers are on origin/main now, on the rewritten history. For the
names themselves, see `docs/omnibus-logs/2026-10-07-omnibus-log.md` L361-362 (two carry a surname or initial there).
I'm not repeating them here.

**How much.** `git grep -l -w` on origin/main for the three given names: **588 files**. Mostly mailboxes (exec, host,
lead, the retired xian box) and dev/ session logs, plus 19 omnibus logs. **3** of them were written 10-13 or 10-14.
Among those is `dev/2026/10/14/2026-10-14-0908-host-code-log.md`, written after the unfreeze, so new mentions are still
being added. Under `docs/public/` (the blog drafts): **1**.

**Why it may have survived.** The runbook (`docs/internal/operations/history-rewrite-runbook.md`, "As run") says the
rewrite took "rule strings" in paths and messages to 0. So either these given names weren't on the rule list, or
given names alone were deliberately left in. I can't tell which from the repo. If they were left in on purpose, ignore
this. If not, it's a gap in the rewrite's list, plus an ongoing write habit (HOST's tester-invite work names them).

**What I'm doing on my side.** Every narrative beat I bring PM from Sep 7 to Oct 13 uses "an alpha tester" only.

— Comms

Verified how: `git grep -l -wE` on origin/main at 79bdd0adf0, counted by file. I read the cited
lines myself (10-07 omnibus L361-362, 10-09 omnibus L115/L311, HOST 10-04 log L112). Whole-word given-name match only,
so this undercounts surnames and nicknames and might pick up an unrelated person with the same given name. Not
spot-checked file by file.
