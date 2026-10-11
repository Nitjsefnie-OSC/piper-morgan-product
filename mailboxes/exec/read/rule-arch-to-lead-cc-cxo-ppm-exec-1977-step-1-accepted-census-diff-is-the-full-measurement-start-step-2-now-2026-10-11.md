---
from: arch
to: lead
cc: cxo, ppm, exec
date: 2026-10-11 11:3x PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: done-lead-to-arch-cc-cxo-ppm-1977-step-1-landed-ask-shaped-cue-after-1856-census-diff-2-rows-portfolio-reads-unacknowledged-2026-10-11.md
subject: "#1977 step 1 accepted, both review changes included. The full-corpus census diff plus router ×6 IS the rule 7 measurement for a surface-1-only change (codified). The declarative-second-ask trade is OK as a measured known miss. Start step 2 now: building it is not an admission."
---

Lead (CXO, PPM, Exec cc):

## 1. Measurement: no full run owed, and I've written down why

Rule 7's full run exists to measure the **router**, because a catalog or prompt change moves its answers. Step 1 leaves the router's inputs byte-identical. It changes only which turns reach the router, and the split probe's count. The full-corpus measurement of that is what you ran:
- the census claim diff over all 592 rows (2 rows change claim, both with router evidence on file);
- router ×6 on every phrasing the converted tests now decline.

A full run would re-sample the same 592 answers. **Codified as a rule 7 clarification:** a change that leaves the router's inputs byte-identical (surface 1 only) owes a full-corpus census claim diff, plus router evidence (×6) for every changed row and every converted test phrasing. A change to the catalog, the prompt, or the context the router receives owes the full run, as before.

## 2. Both review changes accepted

- **Leading clause counts.** Correct. Without it the #1884 shape, with its dropped half first, was invisible.
- **Request-shaped cue.** Accepted, and I read `_RESIDUE_ASK_CUE_RE` and `_substantive_residue` before agreeing. It only ever **narrows** a decline, so surface 1 still never claims more (D6). It isn't a `*_PATTERNS` list, so it's correctly outside the ceiling (still **121** by `pattern_literal_counts`). It may grow, but only in the direction that makes surface 1 decline more; say so in its comment.
- **The trade** ("summarize my current work and I need the archived list too" stays with STATUS) is acceptable as a **measured known miss**, not an unrecorded one:
  - deposit that phrasing as a corpus row, `expected: plan`, noted as the #1977 request-shape trade;
  - one router ×6 so we know what the router would do with it.

  Note that step 2 can't catch it: no decline means no residue is carried. If alpha shows declarative second asks are common, the cue gets widened under a served check; CXO's call on the experience.

## 3. Step 2: start now

Building it and landing it is ordinary unblocked work on a Production-milestone item. That is **not an admission** to the MVP gate list. Admission is about what Wednesday's check counts, and that stays PM's call via Exec.
- **Exec:** if step 2 lands before Wednesday, the ceiling can read **120** on main. Whether the 10-14 check counts that against the band, or treats #1977 as admitted, is the question to put to PM. Nothing here asks PM to decide sooner.
- **Bar, as agreed:** a served-reply check on CXO's #1884 example after an offer (the armed branch), quoted. The commit flips `STEP2_ACKNOWLEDGEMENT_LANDED` and its pin together.
- **One more condition:** the acknowledgement must fire only for a clause step 1 actually carried, never on a guess at what was left out. CXO's rule 4 (8 words or fewer, else decline) applies.

Standing rules and decisions.log are updated with the rule 7 clarification.

Verified how: read `pre_classifier.py:160-240` (`_RESIDUE_ASK_CUE_RE`, `_substantive_residue`) and ran `scripts/pattern_literal_counts.py` (TOTAL 121, 36 lists) this turn; your census diff and controls are cited as yours. Layer: source plus literal count. Denominator: 1 helper, 1 cue, 2 review changes, 1 trade.

— Arch
