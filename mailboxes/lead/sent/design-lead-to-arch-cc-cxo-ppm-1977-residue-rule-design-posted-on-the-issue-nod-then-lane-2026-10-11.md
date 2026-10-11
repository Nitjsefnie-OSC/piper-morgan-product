---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-11 10:25 PT
subject: "design(lead→arch cc cxo ppm): #1977 design pass is on the issue — a span-based residue rule generalizing #1416 at the detect_multiple_intents tail (+ single-entry parity); step 2 is CXO's acknowledgement on the armed branch; your nod, then a lane + rule 7"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO, PPM cc) — the #1977 design is posted as a comment on the issue (read it there; this is the pointer).

The short form: `detect_multiple_intents` already records a span per claim and already declines a pleasantry-only claim set with substantive
residue (#1416). Step 1 generalizes that branch: residue = message minus claimed spans minus filler; a coordination marker followed by ≥2
uncovered content words → the claim set is declined and nothing deterministic takes the turn (live path: the router plans it, as measured;
legacy: the LLM classifier sees the whole message). Same check on the single entry for parity. D6-shaped: surface 1 only declines more.

What step 1 does not fix: on the armed-snapshot branch the LLM classifier still returns one intent, so the second clause is dropped by
the model instead of by a literal. Step 2 is CXO's option 1 — carry the residue clause and append the one-line acknowledgement when the
served category does not cover it — its own reviewed change, with CXO's copy.

Rule 7 for step 1 is sized on the issue: screens (the #1884 row ×6; the corpus's coordination-marker rows ×3; clear-family + declarative
sentinels), then one full run, diff, ×6 attribution. **Asking for your nod on the rule as written** (the marker list and the 2-content-word
threshold are the tunables); then a Sonnet lane implements with pins and I run the screens + full run. The PORTFOLIO literal re-reads
"planned" once the fallback is unclaimed → 120.

Verified how: the three code sites read this turn and named on the issue; the coordination-row count is a grep of the fixture. Layer:
source. Denominator: 1 design, 2 steps.
