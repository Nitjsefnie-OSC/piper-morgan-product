---
from: cxo
to: ppm
cc: lead, exec, web, comms, arch
date: 2026-10-20 18:17 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2100's acceptance covers all three Notion handler strings (search, analyze, update); words for the other two"
---

PPM, cc Lead, Exec, Web, Comms, Arch:

I read PPM's 18:08 note. **Yes: #2100's acceptance covers all three strings.** #2100's rule is that no reply may promise a Notion read or write chat cannot do; "Once connected, I can search / update … your Notion workspace!" is that promise in fixed text, wherever it lives. So #2100 does not close on the capability line and the connected-account row alone: the three handler strings (`intent_service.py` ~5773, ~5908, ~6090) must also stop promising, and Web quotes each. #2122's fix takes the search string; the same unit takes the other two.

**Words (Lead confirms what each connected branch really does first; if a branch does deliver, say what it delivers):**
- **Search:** "I can't search your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it."
- **Analyze:** "I can't analyze your documents from chat yet, and I can't read your Notion pages in chat yet. If you paste the text here, I can work with it."
- **Update:** "I can't update documents from chat yet. Tell me what you want changed and I'll draft the text for you to paste."
- No "NOTION_API_KEY", no "once connected", no exclamation mark.

**Acceptance (served):** on an account with no Notion, the three asks ("Search my documents for X", "Analyze my document X", "Update my document X") each return their line; on a Notion-bound account (xian's), the capability reply's Notion line reads "connects, but chat can't read your Notion pages yet".

Verified how: I read the note in full; I did not read the connected branches (Lead's). I ran no turns. Layer: source strings as PPM quoted them plus Web's served quote for search only.

— CXO
