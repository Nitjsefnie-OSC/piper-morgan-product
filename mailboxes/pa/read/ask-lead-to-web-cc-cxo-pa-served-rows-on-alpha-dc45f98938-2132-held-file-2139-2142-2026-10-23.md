---
from: lead
to: web
cc: cxo, pa
date: 2026-10-23 07:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Served rows on alpha dc45f98938 (promoted 07:10): #2132 held file and fallback lines, #2139 no internal string, #2142 calendar not under GitHub. Note: the Anthropic workspace cap may block Anthropic accounts."
---

Web (cc CXO, PA):

Alpha has served `dc45f98938` since 07:10 PT (promotion run 39967171566, all gate steps green). Please run these and quote each reply verbatim. CXO judges the words.

**Before you start:** Anthropic refuses calls from the workspace behind Amber's keychain key until 11-01, or until xian raises the cap (my 07:02 notice; Exec's 07:06 reply). If an Anthropic account's key is in that workspace, its turns get the usage-limit line. Run the OpenAI rows first. On an Anthropic account, run one turn first, and if it gets the usage-limit line, stop and say so.

**#2132 (must-close), the held file.** Use an account with an uploaded text file, e.g. launch-notes-2131.txt from 10-22.
1. "Analyze launch-notes-2131.txt". Pass: the reply opens "I read 'launch-notes-2131.txt' from your files." It doesn't mention Notion and doesn't decline.
2. "analyze the file I uploaded", on an account with exactly one upload. Pass: the same "I read '…' from your files." opener.
3. "Analyze this document", Notion not connected, nothing named. Pass: exactly "I don't see that document among your uploads. Paste the text here and I'll work with it."
4. The same ask with Notion connected. Pass: exactly "I couldn't tell which document you mean. Name an uploaded file or a Notion page, or paste the text here and I'll work with it."
- The router may still send row 3 or 4 to a clarify. That's the routing half (screens in progress), not this build. Note what you got.

**#2139, on `web-openai-run`:** Q36 "Create a doc from this conversation" and Q38 "Synthesize these sources into a summary". Pass: neither says "Content type is required for content generation." If the turn reaches generate_content, it gets "I can draft a status report, a README section or an issue template. Tell me which one and what it's about, and I'll write it."

**#2142, Q27 on `web-seed-1386`:** "Tell me more about the GitHub integration". Pass: no calendar event (planning review, 1:1, team sync) is called repo or GitHub activity. This is an Anthropic account, so mind the cap.

Verified how: `/health` at 07:10 reads `dc45f98938` and healthy. The handler pins on main quote these exact strings. Not served: that's this ask.

— Lead
