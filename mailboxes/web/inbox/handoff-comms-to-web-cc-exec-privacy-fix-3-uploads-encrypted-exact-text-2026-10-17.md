---
from: comms
to: web
cc: exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-17 21:19 PT
subject: "Hand-off: /privacy fix 3, uploads sentence, exact text (xian OK'd 07:03 10-17 in conversation with Comms; the count it waited on came back zero at 15:2x). One-line edit in privacy/page.tsx"
---

Web, xian OK'd correcting the uploads claim in conversation with me at 07:03 today ("Yes correct the encryption claim!"). It waited on his backfill count, which he ran at 15:2x (quoted on #1306): 0 plaintext, 0 missing. Exec, this relays that OK for the rollup.

The edit is in `src/app/(public)/privacy/page.tsx` on website origin/main, line 187 ("What we store", the "What you create or connect in Piper" bullet). Only the last sentence of the bullet changes. Nothing else on the page changes.

Before (last sentence):
> Uploaded files are stored as-is, not encrypted.

After:
> Uploaded files are **encrypted** when stored.

Wrap "encrypted" in `<strong>`, matching "These are <strong>encrypted</strong> when stored." in the conversations bullet just above.

Facts: every upload is encrypted with AES-256-GCM at the storage seam (`services/file_context/storage.py`, #1306). The key is set on alpha (xian, 10-16), and since #2061 (live) an upload is refused rather than stored without it. xian's production count found no older unencrypted files.

When it's live, tell me and I'll check the rendered page.

— Comms
