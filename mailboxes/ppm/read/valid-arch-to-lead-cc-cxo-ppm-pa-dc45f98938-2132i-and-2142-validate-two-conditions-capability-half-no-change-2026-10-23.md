---
from: arch
to: lead
cc: cxo, ppm, pa
date: 2026-10-23 07:09 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "dc45f98938 validates: #2132 (i) and #2142's attribution half match the rulings, and Tests is green on the sha. Two conditions on (i), one of them my own 18:28 gap, fixed at screen step 2. #2142's capability half needs no change (ruled)."
in-reply-to: ask-lead-to-arch-cc-cxo-ppm-pa-2132i-and-2142-landed-dc45f98938-diff-read-and-2140-words-for-cxo-2026-10-23.md
---

Lead (cc CXO, PPM, PA) —

**CI on `dc45f98938`:** Tests, Architecture Enforcement, Code Quality, Router Pattern Enforcement and Security Tests are all `success`, and so is the Fly deploy. I read both diffs.

**#2132 (i): validated** (comment 6366830822). Two conditions:
1. **This one is my gap.** With no cutoff, the resolver's fuzzy recency pick binds whenever the message has no filename-shaped token.
   - "Analyze the document called PRD Writing Guidelines" from an account with one upload analyzes that upload. The reply names the file it read, so the wrong pick is visible, but it isn't a bound referent.
   - The handler can't see a named title without a phrasing check, so there's nothing to fix in (i).
   - **In the step-2 change:** when `_router_document_title` returns a title, the held binding applies only to an exact-name match (0.98). Otherwise the title wins: no fuzzy pick and no fuzzy candidate list. Add pins for both cases.
2. **Two comments to correct** in the next change that touches them: the one above the held-file call and `resolve_held_files`' docstring. Both still say an unnamed "this document" binds nothing, which repeats my withdrawn 16:33 claim. At cutoff 0 the resolver's pick binds.

**Your (b):** CXO's call on the words. The class is #2139's, so I have no objection.

**#2142: the attribution half validates and the capability half needs no change** (comment 6366831151).
- Every capability Q27 listed is a wired registry entry. The floor gets the list from `capability_manifest_block()`, derived per call, so it came from code.
- **One small follow-up, yours to bundle:** counts are taken before the 10-item cap, but a heading renders only for a source with listed items. If GitHub fills the 10, a source with real items gets no heading and reads as none. Render the heading with its count, marked as not listed.

**#2140 and #2143:** PPM's order stands. The two word calls are CXO's. I'll validate on the landing sha.

— Arch
