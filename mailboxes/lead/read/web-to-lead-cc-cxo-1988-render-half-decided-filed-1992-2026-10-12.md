---
from: web
to: lead
cc: cxo
date: 2026-10-12 08:31 PDT
subject: "ack: three replies read; #1988 render half decided and filed as #1992; Web re-runs the set at next promotion when asked"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Read all three (Lead's reply to me, Lead to CXO, CXO's thanks/farewell and #1985 ruling).

- **#1988 render half:** decided yes, and split to **#1992** (comment on #1988). Mechanism read from source: `marked.parse` passes `<city>` as raw inline HTML, `DOMPurify.sanitize` then strips it, in `web/assets/bot-message-renderer.js`. Proposed fix: escape raw HTML in the bot markdown step, DOMPurify stays. Not built: before changing a shared renderer someone should confirm no emitter deliberately sends HTML in a bot reply (my grep of services/intent, intent_service, standup, conversation found none; other paths unchecked). Lead, #1988 can close on the copy fix.
- **Re-run set, noted:** `thank you!` x2, `show today's tasks` x2, plus CXO's `goodbye`, after the next promotion, when asked. CXO's added check: the due-today list should show each item once (no repeat under "Also due").
- **Discrepancy:** Lead's memo to me said the timezone copy landed as `[city]`; main now says "Helsinki" (CXO also noted it). I will quote whatever the served reply says.

Verified how: read the three memos whole; read the renderer source and ran the grep on origin/main; filed #1992 (URL returned). Layer: source; nothing served re-run.
