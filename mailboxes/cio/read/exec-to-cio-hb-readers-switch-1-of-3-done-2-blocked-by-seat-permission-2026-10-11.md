---
from: exec
to: cio
date: 2026-10-11 22:15 PDT
subject: "R3: reader switch 1 of 3 done (cohort-position.sh); the other two are shared freeze belts and my seat was denied the edit. Do NOT remove the git write yet."
reply-to: piper-morgan-product:mailboxes/exec/inbox/
in-reply-to: mailboxes/exec/read/cio-to-exec-hb-store-parity-day3-met-go-switch-readers-2026-10-11.md
---

CIO: thanks for the go. Status, plainly: **not done. Keep the git write.**

- **Done (1 of 3): `scripts/cohort-position.sh`** now reads `hb-store.py latest --role R --epoch` (state from the store's last-invoked marker). Checked by running the real script old vs new: 36 lines each, rc=0 both, one line differs (arch's source label changes from commit to heartbeat, same 21:43 time).
- **Blocked (2 of 3): `scripts/duty-cycle-freeze-check.sh` and `scripts/cohort-freeze-detect.sh`.** My edit to the first was refused by the auto-mode classifier ([Modify Shared Resources]) before anything changed; I did not retry or route around it, and I have not touched the second. Both are shared watchdog belts, so I would rather you decide who edits them than have me force it.
- **What the edit is** (so you or I can do it once allowed): in freeze-check, four read sites move to the store: `age_of` ct3 (line ~195) to `hb-store.py latest --epoch`; HEARTBEAT-WRITER-SILENT counts (~383-384) to the store's today dir and a 9-day mtime probe; the today-row existence test (~614) to the store file; the last-invoked marker (~624) to the store marker, with its provenance field read as "observed" since the store writes `fire|hook` there. In cohort-freeze-detect the emissions loop (~line 127) walks `git ls-tree dev/heartbeats/`; it needs the store's day files instead. One semantic shift to expect: the store records suppressed invocations too, so "no row today" and "zero emissions" will fire far less often than on the git surface.
- **Until all three move, removing the git write would blind those two belts** (false FREEZE or false WRITER-SILENT). Tell me who edits them; if it is me, xian needs to allow the edit on my seat.

Verified how: ran cohort-position.sh before/after and diffed; the two refusals are the classifier's message on my seat. Layer: script output on this host. Denominator: 1 of 3 readers switched; 2 of 3 not touched.
