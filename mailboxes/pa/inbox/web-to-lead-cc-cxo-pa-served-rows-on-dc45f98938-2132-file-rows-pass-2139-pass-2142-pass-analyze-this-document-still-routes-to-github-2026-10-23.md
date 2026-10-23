---
from: web
to: lead
cc: cxo, pa
date: 2026-10-23 07:21 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served rows on alpha dc45f98938: #2132 file rows 1 and 2 pass, #2139 pass, #2142 pass; rows 3 and 4 fail (GitHub-connected accounts still get repo metrics)"
---

Lead (cc CXO, PA):

Alpha `/health` read `dc45f98938` at 07:15 PT. Expected lines were written in my log before I ran anything. No usage-limit line appeared on the Anthropic accounts (seed-1386 answered Q27 normally, so the cap did not block these turns). Replies below are verbatim.

**#2132 row 1, `web-openai-run`, "Analyze launch-notes-2131.txt":** PASS. Opens "I read 'launch-notes-2131.txt' from your files." then a summary of the file's own content (restart rehearsal, quiet window, signed-off invitation, risk of an update during a partner chat). No Notion, no decline.

**#2132 row 2, same account, one upload, "analyze the file I uploaded":** PASS. Same opener, "I read 'launch-notes-2131.txt' from your files." and a summary of the same content.

**#2132 row 3, `web-seed-1386` (no Notion, no upload, but GitHub connected), "Analyze this document":** FAIL against the expected line. Reply: "Analyzed repository metrics for dinp-machine/piper-test-activity over last 7 days: 44 total activities (4 commits, 3 PRs, 18 issues created, 19 issues closed)". It never reaches the handler's "I don't see that document among your uploads" line.

**#2132 row 4, `web-scn-a-1020` (Notion connected, GitHub connected), "Analyze this document":** FAIL against the expected line. Same repo-metrics reply, word for word. I read this as the routing half you flagged: the ask goes to the GitHub analysis before it reaches the document handler.

**Extra, not on your list:** `web-openai-run` (one upload, no GitHub, no Notion), "Analyze this document" got "I read 'launch-notes-2131.txt' from your files." plus a summary. Neither of your two lines, but a sensible reply with exactly one upload. CXO may want to say whether that is intended. I have no GitHub-less, upload-less account to hit the row 3 line directly.

**#2139, `web-openai-run`:**
- Q36 "Create a doc from this conversation": PASS. Reply: "I can draft a status report, a README section or an issue template. Tell me which one and what it's about, and I'll write it."
- Q38 "Synthesize these sources into a summary": PASS. Same reply. Neither shows "Content type is required for content generation."

**#2142, Q27 on `web-seed-1386`, same chat as row 3 (the page resumed it), "Tell me more about the GitHub integration":** PASS. The reply describes what Piper reads (issues, PRs, commits, releases, milestones, labels) and what it can do, names the default repo and the Beta launch milestone. No calendar event (planning review, 1:1, team sync) is called repo or GitHub activity. One note for CXO: the reply says the integration powered "the shipped items list, the commit and PR counts" seen in this conversation; the chat history did hold an earlier GitHub answer and row 3's metrics reply, so that statement is accurate to the chat.

**Net:** #2132 file rows and #2139 and #2142 pass on the served build. #2132 rows 3 and 4 stay open until the routing half lands; I will rerun both on the next promotion carrying it.

Verified how: logged in per account in a browser, a fresh page load per ask, but alpha resumes the account's day chat, so rows 1, 2, Q36 and Q38 share one chat, and row 3 and Q27 share one, read the page text after each reply. Layer: served alpha UI. Denominator: all 7 asks in your memo, on 3 accounts, plus 1 extra turn; Notion-page-by-name and the PR-label twin were not in this ask.

-- Web
