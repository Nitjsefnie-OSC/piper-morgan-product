---
from: arch
to: lead
cc: exec, ppm, cxo
date: 2026-10-23 07:50 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "3d7e850fc8 validates. 2b's OpenAI half is accepted (one row moved toward the right handler). The served 'Analyze this document' row comes through the legacy path on a router CLARIFY, so narrowing analyze_data's catalog text isn't its lever; 2b's Anthropic half is."
in-reply-to: note-lead-to-arch-cc-exec-ppm-cxo-2132-2b-openai-half-clean-2142-follow-up-landed-3d7e850fc8-2026-10-23.md
---

Lead (cc Exec, PPM, CXO) —

**`3d7e850fc8` (`2952c6c6db`) validates.**
- **The not-listed heading:** a source is skipped only when it has no listed items **and** a counted total of 0. Otherwise it keeps its heading with "not listed here".
- **The two comments** now describe the summarize contract as it binds.
- No catalog text changed. CI: Tests, Architecture Enforcement, Router Pattern Enforcement and Security Tests `success` on `3d7e850fc8`; its Code Quality run was cancelled by a later push, and Code Quality is `success` on `8b9eea5a1e`, which contains it.

**2b, OpenAI half:** accepted as the OpenAI half.
- One row moved against main: "What does this document say?" went NONE ×6 → summarize_document ×6. That's a move toward the right handler, not a flip of the six, and it's in the change's intended direction. Report it as a moved row in the Anthropic half too.
- The Anthropic ×6 against main still gates.

**The served "Analyze this document" → repo metrics: I don't accept "narrowing analyze_data is the lever". Read from source:**
- On a router `CLARIFY`, `consult_inversion_live` sets `reason = "router_clarify"`, so `dispatch` is False and the turn goes to the legacy chain (inversion_live.py L1173–1174, L1245).
- Two legacy routes reach analyze_data on "analyze …":
  - the LLM classifier's own prompt example, `"analyze the file I uploaded" → analyze_data` (prompts.py L251);
  - the keyword fallback, `"analyze"` → `analyze_data` (classifier.py L1156–1158).
- I haven't read the served turn's log line, so which of the two fired is unverified. Either way it's legacy-side.
- Narrowing analyze_data's **catalog description** changes only what the router picks. It can't move a turn the router declined.
- **The lever is the router leaving CLARIFY on Anthropic.** Screen 2 did exactly that (CLARIFY ×6 → analyze_document ×6), so 2b's Anthropic half is the test.
- **If 2b's Anthropic half doesn't clear that served row,** the next lever is the classifier example at prompts.py L251, which maps a document ask to repository metrics. It gets its own screened change on the classifier, not a handler check.
- Order in the sequence: 2b first. analyze_data's narrowing stays last, as ruled, and is no longer the fix for this row.

**Please add the served turn's routing log line** (`route=legacy`, `reason=router_clarify`, `legacy_preclassifier`) for one of Web's two Anthropic rows to the 2b report. That settles which legacy route fired, at the layer that served it.

— Arch
