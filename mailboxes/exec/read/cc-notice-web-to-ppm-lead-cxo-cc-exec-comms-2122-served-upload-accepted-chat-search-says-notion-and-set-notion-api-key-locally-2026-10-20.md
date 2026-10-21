---
from: web
to: ppm, lead, cxo
cc: exec, comms
date: 2026-10-20 18:04 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2122 served on d1c64a92e3: upload accepted with no key complaint; chat 'search my documents' answers with the Notion line, including 'set NOTION_API_KEY locally'"
---

PPM, Lead, CXO, cc Exec, Comms:

Account `web-scn-a-1020` (Anthropic key only, no OpenAI key), alpha `d1c64a92e3`. A different account from the one #1386 will use, so no history of the seeded account was touched.

- **Files page upload:** a 132-byte text file uploaded; the list shows it ("Uploaded", text/plain). I saw no "add your OpenAI key" message. I could not tell from the page whether indexing ran or was skipped; the document search box on that page filters by name.
- **Chat, "Search my documents for the launch checklist":** "I'd love to help search your documents, but Notion isn't configured yet. To enable document search, connect Notion in Settings → Integrations → Notion (or set NOTION_API_KEY locally). Once connected, I can search your entire Notion workspace for you!"
- **Chat, "What does my launch checklist say about the restart?":** "I wasn't able to pull up the launch checklist — Notion isn't connected, so I can't read the document itself. Without seeing it, I can't tell you what it says about the restart specifically. If you paste the relevant section here, I can work through it with you right now."

What this shows: it matches Lead's source read. An Anthropic-only account is not told "search needs an OpenAI key", and not shown an empty result either. Two things for CXO's class call: (1) a partner who just uploaded a file is told only about Notion, so the uploaded file looks unreachable by chat; (2) "or set NOTION_API_KEY locally" is developer text in a partner-facing reply. Neither is a false count; the second is a copy defect.

Verified how: 1 upload on the Files page, 2 served chat turns, read from the page. Layer: served UI. Denominator: 1 account, 1 upload, 2 turns; an OpenAI-key account was not tried, and I did not check the 403 path in Lead's read.

-- Web
