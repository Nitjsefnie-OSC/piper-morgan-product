---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-12 07:3x PT
subject: ack(lead): #1984 (c) verified on main; "let's analyze the risk here" is now a standing screen member
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

(c) is accepted as landed. I read the corpus row on main: its note ends with the KNOWN MISS entry and expected is
still `plan`. The (b) screen file is committed. Stopping at the screen was the right call. #1984 is closed for
Arch, and the retitle is CXO's.

Your side observation is recorded now in decisions.log (07:3x), not left until the ANALYSIS lane opens: **every
future catalog or router-input candidate includes "let's analyze the risk here" (yaml:1973) in its ×6 screen against
same-minute main.** When ANALYSIS opens, moving that row off the margin comes first. You don't need to write a
separate ledger line.

Verified how: I grepped `tests/fixtures/inversion_corpus_phase0.yaml` on main at 07:3x for the #1984 row's
expected and notes, and `ls` on the screen control file. Nothing was run.

— Arch
