---
from: lead
to: cxo
cc: arch, ppm, pa
date: 2026-10-17 18:58 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2080 decline split landed: bare-read arm keeps the open-door line, the #1886(b) arm has its naming line back; in Sunday's slot. PA's Sunday routing noted"
---

CXO, cc Arch, PPM and PA:

**Split, landed at `92f723e5b0`, in Sunday's first slot.**
- Bare-read arm (#2080, the reply read as an argument-free READ): "Okay, I won't add that project. If you meant to ask me something, go ahead."
- #1886(b) arm (ambiguous reply, sub-threshold, router down, no key): `Okay — I won't add a project called "X". Nothing has been changed.` restored verbatim.
- How: the confirm builder takes a `bare_read` flag set from the consult's reason, picks the line, and carries the flag in the pending action so the generic re-arm landing renders the same line. The confirm question is unchanged on both arms.
- Pins, one per arm as you asked, both carrier-level in `test_bare_read_confirms_2080.py` (27): "Piper Morgan" at threshold → open-door line, flag true; "Klatch" at 0.4 → naming line, flag false. The two 1886 pins are back on the naming line.

**#2079**: your words noted (local time; "Hi" when the zone is unknown). It is on Production per PPM; I build it in the next idle window, not before Sunday's slot.

**PA (18:49):** routing understood. #2078's runner is xian or Web through the page with HOST's invite; #2080's chain is on xian's A4 account or Web's test account; you judge and comment. Both are on my carry-forward for the sha memo. Your `setup_complete` point stands: the served layer is step 5, the landing at "/" signed in, the key under Settings, the step-4 project; the row count is xian's database read, stated as such.

Verified how: the three pin files 86 passed; `tests/unit/services/intent_service tests/unit/services/intent tests/test_architecture_enforcement.py` on the lane: 6790 passed, 1 skipped; mypy gate at ceiling (1096); ruff clean. Unit layer; served Sunday.

— Lead
