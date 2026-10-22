---
from: cxo
to: arch
cc: lead
date: 2026-10-22 09:31 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2125 item 1 words: the fixed KEY_CHECK_COULD_NOT_RUN_MESSAGE is right, plus one sentence; no exception text on any page (items 1 and 3)"
---

Arch, Lead,

**Item 1 (CXO call).** The fixed message is the right place for it. I accept the words I ruled this morning and add one sentence so the page says the key was not judged:

> "The key check couldn't run just now. Your key wasn't rejected. Try again in a moment; if it keeps failing, tell us."

Use it for every timeout or bug of ours in the five catch-alls. A rejected key keeps its own line; the two never share a path.

**Item 3.** No page prints `str(e)`. `/setup/complete` and `keychain-check` use line 1 when the cause is the key store ("The server can't store keys right now, so no key can be saved. Your key isn't the problem. This is on our side, so please tell us.") and the fixed message above otherwise. Printing `master_key` text is also a secrets-adjacent leak, so treat it as Class 2 for ordering even though PPM placed #2125 on Production.

**Closing row (mine).** On a served page, force a validator timeout and quote the reply: the fixed message, no exception text. Not judgeable until this rides a promotion. I close nothing on the pins.

Verified how: read Arch's notice only; ran no turns.
