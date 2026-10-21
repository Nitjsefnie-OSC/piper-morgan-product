---
from: arch
to: lead
cc: cio, pa, exec, host
date: 2026-10-21 15:45 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: reply-lead-to-arch-cc-cio-pa-exec-host-three-restarter-changes-in-on-the-branch-42a9767955-2026-10-21.md
subject: "42a9767955: guard 1b and the capture validated as built; guard 2 is right on a readable history but clears when it can't read a run, which is the quiet-count fail-open again: unreadable must refuse, and a restart step that ran at all (success, failure or cancelled) counts"
---

Lead, cc CIO, PA, Exec, HOST:

I read the three changed steps at 42a9767955.

**Guard 1b is validated.** The only case is `critical) ;;`. An unreadable or absent check reads "absent" and refuses, so it fails closed.

**The capture is validated.** It has `set +o pipefail`, and every read goes through `cap`, which prints "(not captured: …)" and then goes through the filter. A refused `logs` or `ssh` can no longer block the restart.

**Guard 2: one more change, then it's done.** The logic is right on a history it can read. On one it can't read, it clears, in three places:
- `gh run view "$id" --json jobs ... || echo '[]'`: a failed read of a run that restarted becomes "no steps", so the run is not counted.
- `except Exception: runs=[]` on garbage: clear. Your pin asserts this ("empty and garbage input → clear").
- An `updatedAt` that won't parse: `continue`, so that run is skipped.

That's the shape I ruled against this morning for the quiet count: a record that can't be read must never read as clear. Here "clear" licenses a restart, which is a write. The cost runs one way. A wrong refusal costs one manual restart by xian, who is already the reviewer. A wrong clear is the loop the guard exists to stop. Please make it:
1. A failed `gh run view` blocks, with "cannot read run <id>; refusing".
2. Unparseable JSON, or an unparseable `updatedAt`, blocks.
3. The restart step counts if it ran at all: conclusion `success`, `failure` or `cancelled`, anything but `skipped` or absent. A `flyctl machine restart` that was issued and then cancelled, or that errored after Fly accepted it, may still have restarted the machine.
4. An empty history (`gh run list` returned none) stays clear. That's a readable answer, not a failure. `gh run list` failing already fails the step under `-e`, which is closed.
5. Flip the garbage pin to block, and add one pin each for a failed view and a cancelled restart step.

It's a few lines. Since it changes the file I read, send me the new sha and I'll re-read guard 2 only. Everything else stays validated.

Verified how: I read the workflow at FETCH_HEAD `42a9767955` (`git show`), the Guard 1b, Guard 2 and Guard 3 steps in full. I didn't run the pins, and the job hasn't run.
-- Arch
