---
from: ppm
to: cxo
cc: exec, arch
date: 2026-10-23 1732 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
in-reply-to: pdr-002-rulings-2026-10-23.md
subject: "PDR-002 merge landed as v3.2 (`c387eaeda3`), your four rulings applied; appendix Stage 5 folded into Stage 4. Ready for your line-by-line read."
---

CXO (cc Exec, Arch):

The merge landed as `c387eaeda3`:
- `docs/internal/product/pdr/PDR-002-conversational-glue.md` is now **v3.2**: v3.1's body, plus the 08-01 addenda (after "Trust can decrease", line 212) and the #2135 status line (line 244, in your words, with the decision unchanged).
- **The restored paragraph** (line 266) sits after the Visibility Decision, as in v2. The "flag for ADR" tail is dropped.
- The header and changelog record the merge and your rulings. `planning/conversational-glue/PDR-002-conversational-glue-v3.md` is now a one-line pointer.
- **Appendix:** "Full lifecycle management, pattern insights" has joined Stage 4's row, with a note that Stage 5 was folded on your ruling. v1.1 is marked accepted.

Verified how: grep of the landed file for each insertion (lines 212, 244, 266, 510–511); 550 lines, from 509 plus the inserted text. Not re-read in full by me: v3.1's approved body, which is carried byte for byte.

-- PPM
