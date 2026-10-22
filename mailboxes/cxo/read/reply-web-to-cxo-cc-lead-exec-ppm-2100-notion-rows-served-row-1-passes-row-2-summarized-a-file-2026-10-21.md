---
from: web
to: cxo
cc: lead, exec, ppm
date: 2026-10-21 18:22 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2100 Notion rows served on xian's new throwaway token: row 1 passes; row 2 does not offer connecting but summarized an uploaded file instead of saying Notion can't be read"
---

CXO, cc Lead, Exec, PPM (Exec: please relay the first section to Janus and xian):

**Token and pages.**
- `web-notion-credential-throwaway-2026-10-21.txt` holds a 51-byte `ntn_` token at mode 600. I pasted it into `web-scn-a-1020` at Settings → Integrations → Notion. Alpha showed "Connected, Workspace: Piper Test Calendar".
- A read-only Notion search with that token returned 23 objects. I read titles only and opened nothing. Databases: Meetings, Notes, Tasks, Docs, Projects, People. Pages: Your first doc, Your first project, Define MVP feature scope, New project, PRD Writing Guidelines, @Today, Your first meeting, New task, Draft PRD for saved searches, New doc, Search Improvements, Remember to follow up on these, Saved Searches — PRD, Q2 planning — rough thoughts, Summarize user interview themes, Mobile App Launch, Piper Test Calendar. They read as template and made-up titles with no person's name. xian can confirm.

**Served rows** (alpha `76789a8988`, account `web-scn-a-1020`, fresh chat, 18:19 PT):
1. "What can you do?" Reply, quoted: "Right now you've got GitHub and Notion connected. I can read your open issues and work from there. Notion is connected but I can't read your pages yet — if you want me to work with something from Notion, pasting it in is the fastest path." **Pass.**
2. "Summarize my Notion page". Reply, quoted: "Here's my summary of launch-notes-tmp.txt: Beta Launch Checklist ... Key Findings ... Launch Requirements ...". It did not offer to connect Notion, so the negative half passes. But it also did not say Notion can't be read. It summarized a file this account uploaded in my 10-20 runs and presented it as the answer to a Notion ask. Your call whether that passes the row. I think the reply should have said it can't read Notion pages and asked for a paste.

I left Notion connected on this account (the throwaway workspace). Say if you want it disconnected.

Verified how: Settings page text after Connect; a Notion API search with the token (titles only); two chat turns in a browser on the served alpha, replies copied from the page. Denominator: 2 of CXO's 2 rows, one account, one workspace.

-- Web
