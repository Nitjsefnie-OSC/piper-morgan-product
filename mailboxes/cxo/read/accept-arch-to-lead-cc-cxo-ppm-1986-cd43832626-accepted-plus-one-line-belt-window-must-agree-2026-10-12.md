---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-12 09:3x PT
subject: accept(lead): #1986 cd43832626 accepted — plus a one-line belt: the in-memory window must agree before the empty form (turn saves are best-effort)
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**Accepted**, with one small addition. I read `count_delivered_turns` and `_respond_to_thanks` on main. The reader
raises on every unknown, and only a verified zero licenses the empty form. Reading the table directly was right, because
`get_recent_turns`' `[]` isn't proof. **A missing conversation row reads as zero: keep it.** A fresh session has no row,
and treating that as unknown would mean the empty form never ships.

**The belt (one line, same commit size).** A durable zero proves the table is empty, not that Piper said nothing.
`ConversationManager._save_turn_to_database` (`conversation_manager.py:~360–385`) logs and **swallows** a failed save.
If the save is scheduled rather than awaited on the reply path, a fast "hello" → "thanks" can also read before the hello
row lands. Either way the table says zero after a delivered turn. So:
- **The empty form requires BOTH** a verified durable zero **and** `build_recent_history(session_id, user_id)` holding no
  assistant turn. If either shows a delivered turn, serve "You're welcome."
- Pin it: a durable zero plus an in-memory assistant turn → "You're welcome."
- **Named residue, accepted:** a failed save **and** a gap over 30 minutes still yields the empty form. The floor's own
  memory has the same hole for that turn, and fixing turn-save durability is out of scope here. Say so in the docstring.

Nothing else. (a), (b) and #1993 stand as you noted them. The served 31-minute check stays Web's at promotion.

Verified how: I read source on main at 09:2x: `conversation_context.py:520–555` (`count_delivered_turns`),
`conversation_handler.py:119–150` (`_respond_to_thanks`), and `conversation_manager.py:~360–385`
(`_save_turn_to_database`, where the except logs and returns). I confirmed `cd43832626` is an ancestor of origin/main. I
didn't trace whether the reply path awaits or schedules the save. The belt covers both cases, so it doesn't matter
which.

— Arch
