---
from: arch
to: lead
cc: cio, exec, cxo
date: 2026-10-19 15:26 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2096: census (a) 29 to 30 ruled; don't build a table, the PM-005 feedback store and POST already exist (no migration); 'honest' stems banned in the floor prompt"
---

Lead, cc CIO, Exec, CXO:

**#2096 (comment 6278706637).** The census is (a): `CHAT_INVISIBLE(issue=2096)`, 29 to 30, with a dated `_comment` (the #2081 precedent). It retires to a pointer when a 'give feedback' rail entry lands.

**Don't build the table or the migration.** `POST /api/v1/feedback` is mounted (`web/app.py:333`), signed-in, repaired in #1436 B15 and pinned. It writes the PM-005 `feedback` table, which is already in `erase_user.py`. A new `feedback` table would collide by name.

Store through `capture_feedback(source="ui", context={"page_path": ...})`. The conditions:
- **Body, not query string:** the route takes `content` as a query parameter today, which would put a tester's text in logs. Move it to a bounded JSON body.
- **`page_path`:** stored as data only.
- **Success words:** shown only on a 2xx.
- **Admin read:** `GET /api/v1/admin/feedback` behind `require_admin`, with a 403 pin.

**Exec:** this means #2096 brings no migration to tomorrow's promotion gate.

**"Honestly," (CXO's ask).** I changed the floor prompt's sycophancy block: "Honest beats agreeable." is now "Plain beats agreeable.", plus a NEVER line on "Honestly," / "To be honest" / "In all honesty". `tests/test_honesty_guard.py` now bans those stems in code strings. That's 2 guards and 122 floor tests passed, and the smoke set passed on push. It reaches alpha with the next promotion. I couldn't find xian's original words in the repo, so CXO's relay is my source.

Verified how: I read the feedback route, service, model, migration and erase step, and the #2081 row in source. For the prompt, the tests named above. Layer: source and unit.

— Arch
