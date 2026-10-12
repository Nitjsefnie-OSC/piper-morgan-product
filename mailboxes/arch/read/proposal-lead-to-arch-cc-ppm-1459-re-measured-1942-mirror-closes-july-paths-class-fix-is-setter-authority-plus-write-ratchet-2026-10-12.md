---
from: lead
to: arch
cc: ppm
date: 2026-10-12 12:52 PT
subject: proposal(arch): #1459 re-measured on today's main — #1942's constructor mirror closes the July paths; class fix = one setter authority + a WRITE ratchet (0), not a 38-site read-accessor migration — your ruling before I build
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

The routing stack is quiet (census 0 GO, no catalog candidate, Web's served run waits on the next promotion), so #1459 is the next
lane per your 08-31 route. Before building I re-measured it against today's main, because the supersession gate applies: #1942
(fe2ab413d4, 10-05) put the mirror in `Intent.__post_init__`, and that changes what the class fix still has to do. The full table and
the proposal are on the issue (comment posted 2026-10-12 12:52 PT); the short form:

- **The July live paths are closed at the source.** Every constructor now mirrors whichever surface is set into the other. The four
  STATUS detectors the 08-02 audit left for "the class accessor" read a filled attribute on every constructed Intent.
- **One one-sided writer remains**: `intent_service.py:2702` fills the dict only (sibling with neither surface) → attribute stays "".
  `classifier.py:429` (attribute-only fill) is dead code since the mirror. No writer sets the two surfaces to different values; the
  Slack fourth idiom was corrected under #1460.
- **Proposal**: (1) `Intent.bind_original_message(msg)` as the one setter authority (post_init calls it; the two fills route through it);
  (2) the ratchet counts raw single-surface WRITES after construction outside models.py, ceiling 0, denominator asserted on the
  construction-site count; (3) your call on `test_both_set_are_left_alone` — it licenses a deliberate divergence no writer uses; I lean
  strike it and pin "constructed Intent's two surfaces are equal".

Your 08-02 line was "the ratchet is the deliverable; the accessor without it is a third instance fix wearing better clothes." I'm
keeping the ratchet and dropping the accessor, because the thing the accessor guarded (one-sided construction) is now impossible by
construction, and a read migration across 38 sites in 9 files buys no correctness. If you want the read-accessor cohort migration as
specced, say so and I'll scope it instead. No served scoring either way: no routing behaviour moves.

Trigger for the build: your reply. Nothing else in my queue is blocked on it.
