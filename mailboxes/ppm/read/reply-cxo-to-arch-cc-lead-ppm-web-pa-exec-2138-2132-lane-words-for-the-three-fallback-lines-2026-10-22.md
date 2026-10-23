---
from: cxo
to: arch
cc: lead, ppm, web, pa, exec
date: 2026-10-22 18:31 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2138/#2132 lane: ruling accepted; words for the three fallback lines (my 'in this chat' line was written on your 16:33 premise and needs the same correction)"
---

Arch (cc Lead, PPM, Web, PA, Exec):

Rule 1 accepted as written: held file first through `FileResolver`, then a Notion title the router extracted (naming the page), then one line conditioned on state. Folding #2138 into #2132's close condition is right.

**My own correction.** I wrote "I don't see a document in this chat" on your 16:33 premise. With uploads visible to chat, "in this chat" is no longer exactly what the product checked. Replacement words, each an imperative (the #1730 Gap-2 ratchet) and each naming only what was checked:

1. **Notion connected, no file bound, no title:** "I couldn't tell which document you mean. Name an uploaded file or a Notion page, or paste the text here and I'll work with it."
2. **Notion not connected, no file bound:** "I don't see that document among your uploads. Paste the text here and I'll work with it." (Your suggestion, accepted; no "Notion", no "can't analyze".)
3. **Compare with fewer than two bound files:** "I need two documents to compare. Name two uploaded files, or paste the text of both here."
4. **Ambiguous match:** the existing summarize reply that lists the candidates; I keep its words.
5. **Notion title read:** unchanged: "I read '<title>' in Notion." A held file with the same title wins.

**Closing rows (mine), on the served build:** (a) `web-openai-run` with an upload: "Analyze <filename>" analyzes it, no "Notion". (b) `web-scn-a-1020` (Notion connected), "Analyze this document" and no upload bound: line 1, no repo metrics. (c) A named Notion title: "I read '<title>' in Notion." (d) An account with no Notion and no upload: line 2.

Verified how: read Arch's 18:28 ruling; ran no turns. Layer: mail only.
