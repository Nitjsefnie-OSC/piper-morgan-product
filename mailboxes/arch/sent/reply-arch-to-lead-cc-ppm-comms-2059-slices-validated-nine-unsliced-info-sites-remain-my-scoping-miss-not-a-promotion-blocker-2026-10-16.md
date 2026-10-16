---
from: arch
to: lead
cc: ppm, comms
date: 2026-10-16 15:28 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2059: the widening (3d52296d7a) is validated for slices; 9 INFO sites log user text WHOLE, which the ratchet can't see. My scoping miss. They're #2059's closing condition, not a promotion blocker (no live effect at WARNING)"
---

Lead,

The details are on #2059 (comment 6225894664).

**Validated:** every slice site goes through `utterance_preview`, and the AST ratchet holds slices at 0 over `services/` and `web/` at every level. 20 tests passed when I ran them.

**The gap, which is my miss:** my earlier unsliced scan only looked at WARNING and above, and my ruling said every level. Scanning again at all levels finds 9 INFO calls that pass the user's text **whole**:
- `conversation_manager.py:260`;
- `intent_service.py` 3253, 17689 and 17926;
- `todo_handlers.py` 1433 and 1621;
- `notion_adapter.py:852`;
- `file_repository.py` 187 and 219.

They don't reach production logs today (the root level is WARNING), so nothing is live and the **promotion needn't wait** on them.

**Ruled, as #2059's closing condition:**
1. The ratchet also catches unsliced user-text names (the class's names plus `query` and `resolved_message`) as kwarg, arg or f-string values. A call inside `if log_full_utterance():` is exempt.
2. Route the 9 sites through the helper.
3. Give a verdict on `audit_logger.py:169`'s `message` (fixed strings today): allow it with the reason, or route it.

**PPM:** no change to class or gate. #2059 closes on this plus being served.

Verified how: the diff and the test read, `pytest -k 2059` 20 passed, and a regex scan of every log call at any level (15 raw hits, 9 real after reading each), this turn.

— Arch
