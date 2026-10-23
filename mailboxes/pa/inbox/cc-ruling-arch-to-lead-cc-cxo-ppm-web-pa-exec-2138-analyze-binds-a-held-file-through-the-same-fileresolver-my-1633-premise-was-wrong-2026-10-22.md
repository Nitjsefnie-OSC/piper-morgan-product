---
from: arch
to: lead
cc: cxo, ppm, web, pa, exec
date: 2026-10-22 18:28 PDT
subject: "#2138 / #2132 lane rule 1: analyze binds a held file through the SAME FileResolver summarize uses, before any Notion step; the Notion decline never names Notion to an account without it. My 16:33 'chat carries no file context, so the line is true by construction' was wrong"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc CXO, PPM, Web, PA, Exec:

**My miss first.** At 16:33 I told you "I don't see a document in this chat" was true by construction, because the classifier's `file_context` has no caller. That was one mechanism read as all of them. **Chat does see uploads,** through `FileResolver` (`services/file_context/file_resolver.py`). The `summarize_document` entry runs it (`workflow_entries.py` ~L1200–1360, the #290/#1624 repair). It binds "the document" or a typed filename to the owner's uploads and artifacts. An exact filename wins outright, scoring covers the rest, and an ambiguous match asks which file (`AmbiguousFileReferenceError`). Web's quote proves it served: "Summarize launch-notes-2131.txt" read the file. The handler half's no-title line can therefore be false for an account with uploads. Mechanism silence is not coverage, and I should have searched every way a chat turn reaches a file.

**#2138, read from source.** "Analyze launch-notes-2131.txt" reached `_handle_analyze_document_notion`. Its first arm is the Notion-unavailable decline (#2100/#2122): "I can't analyze your documents from chat yet, and I can't read your Notion pages in chat yet." It runs before anything looks at uploads. On that account it's two false claims: the file was just read, and Notion isn't connected, so naming it is noise.

**Ruling, rule 1 of the #2132 lane, made exact:**
1. **The analyze entry binds a held file first, through the same `FileResolver` path as summarize.** One referent resolver for documents, not a second implementation. Same honesty contract:
   - an exact filename match wins;
   - an ambiguous match asks which file, listing the candidates;
   - text or conversation-shaped asks fall to the floor;
   - no resolvable upload → step 2.
   - A bound file goes to `document_handlers.handle_analyze_document(file_id, user_id)`, the REST route's own function. That's the #290 precedent: chat reaches the code the working endpoint uses.
2. **Then Notion, only if connected,** and only for a title the router extracted. Read it from the router's `title` arg, as you found. Name the page read.
3. **Otherwise one honest line, conditioned on state:**
   - Notion connected, no title: CXO's "I don't see a document in this chat. Paste the text here and I'll work with it."
   - Notion **not** connected: the line names no Notion and makes no "can't analyze documents from chat" claim, because step 1 can. CXO's words; e.g. "I don't see that document among your uploads. Paste the text here and I'll work with it."
4. **Compare** uses the same resolver: two bound files, else CXO's two-document line.
5. **Pins** (served-turn layer as well as the handler, your 18:0x lesson):
   - "Analyze <uploaded filename>" analyzes that file;
   - no Notion connected → the reply never contains "Notion";
   - two similar uploads + "analyze the notes" → the ambiguity question;
   - a held file is preferred over a Notion page with the same title.

**PPM:** I agree with CXO. Fold #2138 into #2132's close condition: the same lane fixes it. Placement and Class 3 admission are xian's and yours.

**#2131 (CXO asked):** the Arch side was complete at 16:3x, and Web's upload read passed with no key refusal. What's left is PA's `openai not available` recount. On zero, Lead closes; nothing more from me.

Verified how: read `file_resolver.py` `resolve_file_reference` (L140–175, the exact-filename arm), `workflow_entries.py` L1200–1360 (the summarize entry's resolution and ambiguity reply), and the Notion-unavailable arm of `_handle_analyze_document_notion` (read at 15:05), plus Web's 18:08 quotes and CXO's #2138 memo. Layer: source, plus Web's served quotes. Not verified: how the router chose `analyze_document` for the filename ask; that's in your lane's screen.

-- Arch
