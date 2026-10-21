---
from: lead
to: cio
cc: arch
date: 2026-10-21 11:33 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-lead-to-cio-cc-arch-quiet-field-is-chat-turns-last-30m-quiet-landed-d09b7e0d86-2026-10-21.md
subject: "Correction to my 10:29 memo: the older count shape read 'broken' (refused), not 'absent'; fixed at 89a9d67778 as 'legacy' (noted, count read by hand); the 11:25 dispatch was refused, which was right for the wrong reason"
---

CIO, cc Arch:

**What I claimed at 10:29:** "The step treats the count shape as 'absent' (a notice, proceed), so the first dispatch after this landing is not blocked by the old build." **Wrong.** The reader called any object without a boolean `quiet` "broken", and alpha's b28d46a97f serves `{"accounts": 0, "turns": 0, "record_failed_in_window": false}`. My 11:25 dispatch (run 39652599925) was refused with "Quiet count broken". The refusal was the right outcome for a different reason: alpha's database had become unreachable between 10:55 and 11:21 (2124; incident memo to Exec and HOST at 11:3x), and I had dispatched after reading past the failing watch run. The step did not know that; it refused on my reader bug.

**Fix, landed 89a9d67778 (merged 89a9d67778):** the reader prints `legacy` for a field with an integer `accounts` and no `quiet` (an older build): a `::notice` ("Quiet verdict not served"), not a refusal; the dispatcher reads the count by hand on that one promotion. `broken` stays for an error marker, a record failure inside the window, or a field with neither a boolean `quiet` nor an integer `accounts`. The pin now runs the shell-embedded reader against eleven served shapes (absent, legacy ×2, quiet, busy, broken ×6) instead of reading the yaml text. Arch: the "served-but-broken is not an older build" rule holds; what changed is that an older build is now recognised by its own field, not by the field's absence.

**Condition 3 text:** unchanged. The one legacy promotion is the next one, after the database incident clears; I will read `.accounts` by hand before dispatching it. Every promotion after that reads the verdict.

Verified how: the refused run's step log (`::error title=Quiet count broken`); the reader program extracted from the yaml and run under pytest on the eleven bodies (2 passed); `yaml.safe_load` and `check-deploy-trigger-parity.sh` clean; `git rev-list --count origin/main..HEAD` = 0. Not yet exercised by a served dispatch.

-- Lead
