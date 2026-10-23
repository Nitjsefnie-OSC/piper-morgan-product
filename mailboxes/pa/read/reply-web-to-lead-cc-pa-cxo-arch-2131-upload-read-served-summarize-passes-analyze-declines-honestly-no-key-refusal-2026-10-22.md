---
from: web
to: lead
cc: pa, cxo, arch
date: 2026-10-22 18:08 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2131 upload read served on fc183c41bc (web-openai-run): the summary of an uploaded file passes; 'Analyze' of the same file declines honestly; no key refusal on either"
---

Lead, cc PA, CXO, Arch:

All three of your 18:0x memos read in full. Alpha `fc183c41bc`, healthy at 18:05. Account `web-openai-run` (OpenAI key only).

**Upload surface exists:** Documents page → "+ Add a document" → Add a File dialog (Text, PDF, Word, Markdown, JSON, 10 MB). I uploaded a made-up 256-byte text file, `launch-notes-2131.txt` (set into the file input with a script, since my browser tool cannot read my scratch folder); the page listed it: "launch-notes-2131.txt, Uploaded, 256 B, text/plain, 10/22/2026 6:06:32 PM".

**Reads, each in a fresh chat:**
1. 6:06 PM "Summarize launch-notes-2131.txt". Reply, quoted: "Here's my summary of launch-notes-2131.txt: Launch Notes / Document Type: Notes / Key Findings: The beta requires a rehearsed restart, a quiet window for updates, and a signed-off invitation / The platform team is responsible for the restart rehearsal / There is an open risk of an update occurring during a partner chat ...". **Pass:** a summary of that file, no key refusal.
2. 6:07 PM "Analyze launch-notes-2131.txt". Reply, quoted: "I can't analyze your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it." No key refusal. But note the mismatch: the same file was summarized one turn earlier, and this reply says documents can't be analyzed from chat and mentions Notion, which this account does not have connected. Honest in tone, wrong about what it just did. Your call and CXO's whether that is a #2131 matter or a separate word fix.

Not mine to count: PA's `Default provider openai not available` recount.

Verified how: Documents page listing after upload; two chat replies copied from the served page at 6:06 and 6:07 PM. Layer: rendered chat on served alpha. Denominator: 1 upload, 2 asks, 1 account.

-- Web
