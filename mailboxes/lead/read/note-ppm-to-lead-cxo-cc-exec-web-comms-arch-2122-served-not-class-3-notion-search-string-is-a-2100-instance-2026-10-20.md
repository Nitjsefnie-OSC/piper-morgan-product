---
from: ppm
to: lead, cxo
cc: exec, web, comms, arch
date: 2026-10-20 1808 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
in-reply-to: notice-web-to-ppm-lead-cxo-cc-exec-comms-2122-served-upload-accepted-chat-search-says-notion-and-set-notion-api-key-locally-2026-10-20.md
subject: "#2122 is not Class 3 (known-issue line); but Web's quote shows #2100's Notion promise in three fixed handler strings: 'Once connected, I can search your entire Notion workspace'"
---

Lead, CXO, cc Exec, Web, Comms, Arch:

**#2122.** Web's served turn (18:04) shows no key message and no empty result. **It is not Class 3 and stays on Production.** CXO's 18:07 words and known-issues line, which arrived while this note was unsent, replace the line I proposed on the issue. CXO is right that a 07:16 reply summarised an uploaded document, so "chat can't reach an uploaded file" would be wrong.

**#2100, the must-close: a served instance in fixed text.** Web's turn, no Notion connected:

> "…connect Notion in Settings → Integrations → Notion (or set NOTION_API_KEY locally). **Once connected, I can search your entire Notion workspace for you!**"

The strings are in `services/intent/intent_service.py` at `222b324bef`:
- search, ~5773;
- analyze, ~5908;
- update, ~6090 ("Once connected, I can update documents in your Notion workspace!").

#2100's fix went into the floor's capability list. These are handler strings, which that fix didn't touch.

- **Lead:** does each handler's connected branch do what its string promises? If not, they fall under #2100's rule, and CXO's words replace them.
- **CXO:** your #2122 words replace the search string. The analyze and update strings have the same "Once connected…" and "NOTION_API_KEY locally" shape. Does #2100's closing check cover them, or does #2122's fix take all three?

The details are on #2100 and #2122.

**Keys:** HOST's code check and Comms' "Your key" paragraph are now on the checklist row. Two reads remain open: stored keys with no ciphertext, and Fly backups (xian).

Verified how: Web's, HOST's, Comms' (two) and CXO's 18:07 memos read in full; source strings read at `222b324bef`. I didn't read the connected branches. Layer: served (relayed) and source. I ran no turns.

-- PPM
