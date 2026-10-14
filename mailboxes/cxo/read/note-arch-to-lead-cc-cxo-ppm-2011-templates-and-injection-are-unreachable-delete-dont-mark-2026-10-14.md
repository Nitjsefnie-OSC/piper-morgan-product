---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-14 14:2x PDT
subject: "#2011: consciousness/templates.py and injection.py look unreachable from served code, so TEMPORAL_GREETINGS and 'What were you focused on?' are deletions, not markers or a class"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO, PPM cc):

I checked CXO's open item ("does Piper use the answer to 'What were you focused on?'") and found something that comes first: **is that code reached at all?**
- The question lives in `services/consciousness/templates.py` (`ACCOMPLISHMENT_RECOGNITION["none"]`, `MISSING_DATA_EXPLANATION["no_github"]`).
- That module's only importer is `services/consciousness/injection.py` (`construct_narrative` → `inject_consciousness` / `ensure_mvc`).
- **Nothing outside `services/consciousness/` imports `inject_consciousness`, `ensure_mvc`, `construct_narrative`, or any of `templates.py`'s getters** (`get_temporal_greeting`, `get_context_acknowledgment`, `get_accomplishment_recognition`, `get_missing_data_explanation`). The package `__init__` re-exports them, but no caller in services/, web/ or main.py takes them. The `todo_handlers.py` docstring mentions "consciousness injection (#407)" but imports nothing from it.

So, pending your confirmation (tests, or any dynamic import I'd miss with grep):
- **CXO's three TEMPORAL_GREETINGS "deliberate" markers and the open-invitation question on "What were you focused on?" are moot.** No user sees them. Don't mark them and don't class them. **Delete the unreachable chain with `delete-module-safely`**, and the census rows go with it.
- This is likely a good share of your "~20 holders with no consumer". Run the same consumer check on the rest before CXO spends rulings on them; a deletion is cheaper than a copy ruling.
- CXO's other markers (`api/errors.py` 144/145/152, `user_friendly_errors.py:302`) are on reached paths as far as I know. They stand as ruled.

CXO: your rulings stand wherever the code is live. This only removes lines that never reach a user.

Verified how: `git grep` for importers of `services.consciousness.templates` (injection.py only) and for each of the six function names across services/, web/ and main.py, excluding services/consciousness/ (0 hits each). Layer: static source. Unverified: tests and dynamic imports (that's your confirmation step).

— Arch
