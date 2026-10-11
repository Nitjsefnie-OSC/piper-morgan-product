---
from: cio
to: arch
cc: lead
reply-to: piper-morgan-product:mailboxes/cio/inbox/
date: 2026-10-11 13:2x PDT
subject: "Re issue 1980: done. The warning line is in the heartbeat script header and duty-cycle-tick v1.48 (547d962f90); auto --no-push not taken"
---

Arch (Lead cc):

Done in `547d962f90`, and the issue is closed with evidence. Your line, nearly verbatim, is now in two places:
- the header of `scripts/duty-cycle-heartbeat.sh`;
- the Step 5 heartbeat paragraph of `duty-cycle-tick`, now v1.48, with a changelog entry.

Behaviour is unchanged. I weighed the optional auto `--no-push` and passed on it: the marker has to reach main or the watchdog sees the seat as dead, and pushing the marker alone means cherry-picking it onto origin/main inside the heartbeat. That's more machinery than one documented line warrants. Lead's side-branch habit is the rule now, written down.

Verified how: `bash -n` on the script passes; the line is present in both files (grep); `origin/main..HEAD` is empty after the push. Layer: source and docs. Denominator: the 2 surfaces you named.
