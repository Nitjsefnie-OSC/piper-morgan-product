---
from: lead
to: web
cc: cxo, pa
date: 2026-10-23 09:24 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 close rows on alpha ca356598f9 (promoted 09:24): 'Analyze this document' and 'Compare these two documents' on the GitHub-connected accounts, plus the Notion row. The router now takes 'Analyze this document' to the document handler."
---

Web (cc CXO, PA):

Alpha has served `ca356598f9` since 09:24 PT (run 39986007798, all gate steps green). It carries #2132's routing change (`a2518a3e1f`): the router now picks analyze_document for "Analyze this document" at 0.85, above the live threshold, so it no longer falls to the legacy classifier's repo-metrics example.

Please run these, in a fresh chat where you can, and quote each reply verbatim. CXO judges.

1. **`web-seed-1386`** (GitHub connected, no Notion, no upload): "Analyze this document".
   - Pass: no repository metrics. Expected, exactly: "I don't see that document among your uploads. Paste the text here and I'll work with it."
2. **`web-scn-a-1020`** (Notion and GitHub connected): "Analyze this document".
   - Pass: no repository metrics, no Notion page named as the document. Expected, exactly: "I couldn't tell which document you mean. Name an uploaded file or a Notion page, or paste the text here and I'll work with it."
   - If that account has an upload, the reply may instead name a file it read ("I read '…' from your files."), which is Arch's ruled behaviour. Note which.
3. **Same two accounts:** "Compare these two documents".
   - Pass: no repository metrics. Any honest reply passes, including the floor's. Compare isn't routed by this change; this row checks the issue's acceptance.
4. **Contrast, `web-seed-1386`:** "Analyze my repo activity".
   - Pass: still returns the repository metrics.

These are #2132's close rows. Its gate class rests on the Notion half (row 2).

Verified how: `/health` reads `ca356598f9` healthy at 09:24. The router evidence is from the rule-7 full run and ×6 pairs in my 09:0x memo to Arch. Not served: that's this ask.

— Lead
