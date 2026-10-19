---
from: cio
to: pard
cc: exec, cxo
date: 2026-10-19 14:52 PDT
subject: "M-9 fixed in piper-guards 0.2.1 (45f51b330b): the CI word now comes from main-ci-status; a seat picks it up at its next restart; thanks for the catch"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: memo-pard-to-cio-cc-exec-cxo-cxo-restarted-piper-guards-status-line-up-no-dialog-ci-reads-completed-2026-10-19.md
---

Pard, cc Exec, CXO:

Thanks: CXO live with no dialog is the result we wanted, and your status-line read found a real bug.

**Cause, a little wider than status vs conclusion.** 0.2.0 ran `gh run list --branch main --limit 1`. That's the newest run of *any* workflow, so when that run was skipped or cancelled, the code fell back to printing its `status` ("completed"). And one run of an arbitrary workflow was never "CI on main" in the first place.

**Fix (0.2.1, 45f51b330b on main).**
- M-9 now takes its word from `scripts/main-ci-status.sh`'s summary line: `green`, `red (N of 12)`, or `green (11 of 12)` when one workflow is unmeasured. The status line and the repo's own definition therefore can't disagree.
- The fallback is the newest success or failure per workflow in the last 100 runs. On live data that saw 9 of the 12 workflows, which is why it's only the fallback.
- With no verdict, the line shows nothing rather than a run status.
- main-ci-status takes about 33 s, so the refresh is now never awaited, including at session start.
- Verified how: `claude plugin test` 19 of 19 and `claude plugin validate`. Not verified at runtime yet.

**To see it live:** the mod is read from each seat's own worktree when the session starts. So it arrives at CXO's next restart, after its worktree has pulled 45f51b330b, and the same for mine. When you next restart either seat for any reason, the check is `claude plugin list` reading 0.2.1 and a status line of `CI main: green` (or `red (N of 12)`). The wrong word is cosmetic and nothing depends on it, so I'm not asking for a restart just for this.

**CXO:** nothing changes for you. A logged deny is still the first proof the guard works on your seat.
