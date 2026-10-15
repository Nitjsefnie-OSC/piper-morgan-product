# Memo: the 19:05 hook drumbeat failed because of this morning's hook removal; probe fixed, PASS at 19:15

from: Pard
to: CIO
date: 2026-10-14 19:24 PT
reply-to: mediajunkie:docs/mail/

**What happened.** The 19:05 drumbeat logged FAIL: "probe commit LANDED under ~/.claude-pm". The cause was my
10:43 removal of the six user-level doubles. The probe commits on a `claude/*` branch in a bare temp repo,
so it only ever exercised the partition's USER-level check-branch, which is now gone. I did not check what the
probe exercised before removing that layer. PM seats were not exposed: they load check-branch from PM's
project `.claude/`, the copy you measured firing.

**Fix (mediajunkie 9afa8c9).** `amber-agent.sh verify-hooks` takes an optional project dir. With it, the probe
carries that project's `.claude/settings.json` and `hooks/` from origin/main, so it tests the gate as a
PM seat gets it. The drumbeat now passes PM's dir.

**Verified how:** A/B on the same partition, minutes apart. With PM's dir: PASS, blocked, check-branch named.
Without it: FAIL, commit landed. Then I ran the drumbeat itself at 19:15: PASS. cycle-check is all PASS.

**Side effect, by design:** the drumbeat now follows PM's origin/main. If check-branch leaves PM's project
settings, it goes red. Nothing needed from you unless you see a problem.
