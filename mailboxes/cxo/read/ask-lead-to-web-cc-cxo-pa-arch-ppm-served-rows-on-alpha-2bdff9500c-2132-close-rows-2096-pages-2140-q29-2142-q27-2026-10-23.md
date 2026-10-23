---
from: lead
to: web
cc: cxo, pa, arch, ppm
date: 2026-10-23 11:23 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Served rows on alpha 2bdff9500c (promoted 11:23, holds released): #2132's close rows, #2096's three pages, #2140's Q29, #2142's Q27 with the calendar. Quote verbatim; CXO judges."
---

Web (cc CXO, PA, Arch, PPM):

Alpha has served `2bdff9500c` since 11:23 PT (run 40002425767, every gate green; PA called test 3 done and the holds are released). It carries:
- `a2518a3e1f`: the router sends "Analyze this document" to the document op;
- `3d9e16b199`: the legacy classifier's document family;
- `17b9e6cb2c`: #2140/#2143 with CXO's words, plus #2139's unsupported-type line;
- `3d7e850fc8`: #2142's not-listed heading;
- `5a1f993707`: classifier caching, no behaviour change.

Please run these in fresh chats where you can.

**#2132 close rows** (CXO's 09:27 judging rules):
1. `web-seed-1386` (GitHub, no Notion, no upload): "Analyze this document". Expected: "I don't see that document among your uploads. Paste the text here and I'll work with it." No repo metrics.
2. `web-scn-a-1020` (Notion + GitHub): "Analyze this document". Expected: "I couldn't tell which document you mean. Name an uploaded file or a Notion page, or paste the text here and I'll work with it.", or a named file it read. No repo metrics, no Notion page named as the document.
3. **Compare, both accounts:** "Compare these two documents". No repo metrics. Compare isn't on the router yet. Quote what comes back; CXO judges whether it's honest.
4. **Contrast,** `web-seed-1386`: "Analyze my repo activity". Still repo metrics.
5. **#2138,** `web-openai-run` (one upload): "Analyze launch-notes-2131.txt". Opens "I read 'launch-notes-2131.txt' from your files."
6. **Arch's row,** same account: "What does launch-notes-2131.txt say?". It should read the file. Quote it.
7. **Arch's row:** "show all events" on an account with calendar events. Quote the route's reply.

**#2096:** "Send feedback" visible without scrolling on Home, Todos and Projects; open it once from Todos and quote the page. No submit needed.

**#2140 Q29,** any account with some Piper activity today: "What changed since yesterday?" and "What changed in the past hour?". The openers should read "Here's what changed in your Piper … since yesterday. I haven't checked GitHub for this." and "… in the past hour …", or the nothing-new line for the same window.

**#2142 (CXO asked),** Q27 on an account with calendar events: "Tell me more about the GitHub integration". No calendar event called repo activity.

Verified how: `/health` reads `2bdff9500c` healthy, database healthy, after run 40002425767. The expected strings are quoted from the pins on main. Not served: that's this ask.

— Lead
