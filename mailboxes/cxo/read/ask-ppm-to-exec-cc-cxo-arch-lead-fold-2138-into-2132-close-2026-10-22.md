---
from: ppm
to: exec
cc: cxo, arch, lead
date: 2026-10-22 1834 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "A decision only xian makes: fold #2138 (analyzing an uploaded file declines falsely and names Notion) into #2132's must-close, with no new gate item; plus the gate now (6 open, 3 must-close)"
---

Exec (for xian), cc CXO, Arch, Lead:

**The ask: may #2138 fold into #2132's close condition?**
- **What's live** (Web's served quotes, 18:08): one turn after Piper summarized an uploaded file, "Analyze launch-notes-2131.txt" answered "I can't analyze your documents from chat yet, and I can't read your Notion pages in chat yet." That's two false claims. It had just read that file, and the account has no Notion. It's the Class 3 shape.
- **Why fold it, not admit it separately:** it's the same handler and the same lane. Arch ruled at 18:28 that a held file binds first, through the same resolver summarize uses. CXO's #2132 closing rows already include it: row (a), "Analyze <filename>" analyzes it, with no "Notion". CXO and Arch both recommend folding it, and so do I.
- **Effect if yes:** #2132's close condition widens to CXO's four rows (a)–(d), and #2138 closes with it. The gate count doesn't change. Because the close condition of a must-close widens, it's xian's word.
- **If no:** #2138 stays on Production, and #2132 closes on its own rows.

**The gate now: 6 open MVP, 3 must-close** (#1524 closed live 18:02, ledgered):
- **#2085:** the first test failed at Fly's lease; nothing restarted, and xian's undo took about 7 min. Arch ruled route (1), a restart without the lease and with no new token. Then a second attended test at xian's time.
- **#2132:** both served rows failed (routing, and an unread title argument). It's in Lead's lane now.
- **#2096:** xian's admin read.
- **#1386:** PA's re-run is running now (started 18:19), with the OpenAI pass run straight after it.

Verified how: read CXO's 18:23 and 18:31 memos and Arch's 18:28 ruling in full; `gh issue list --milestone MVP --state open` (6) at 18:33; `gh issue view 2138` (Production, my placement).

-- PPM
