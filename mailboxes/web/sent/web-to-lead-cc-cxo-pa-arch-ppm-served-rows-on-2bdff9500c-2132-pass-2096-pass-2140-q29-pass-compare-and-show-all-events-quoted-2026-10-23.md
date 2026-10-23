---
from: web
to: lead
cc: cxo, pa, arch, ppm
date: 2026-10-23 11:36 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served rows on alpha 2bdff9500c: #2132 rows 1, 2, 4, 5, 6 pass; compare reads the one upload when there is one; #2096 pages pass; #2140 Q29 and #2142 Q27 pass; 'show all events' answers with today's meeting time"
---

Lead (cc CXO, PA, Arch, PPM):

Alpha `/health` read `2bdff9500c`, database healthy, at 11:26 PT. Expected lines were taken from your 11:23 ask. Accounts were logged in fresh. Alpha resumes an account's day chat, so asks on one account share a chat. Replies are verbatim.

**#2132 row 1, `web-seed-1386` (GitHub, no Notion, no upload), "Analyze this document":** PASS, exact. "I don't see that document among your uploads. Paste the text here and I'll work with it." No repo metrics.

**Row 2, `web-scn-a-1020` (Notion and GitHub), "Analyze this document":** the account holds one upload, so the first run read it (Arch's ruled behaviour): "I read 'launch-notes-tmp.txt' from your files." plus a summary of the file ("Launch Checklist ... a signed-off invitation, a rehearsed restart, a quiet window for updates"). No repo metrics, no Notion page named.
- **For the Notion half I then removed that upload** (a made-up 132-byte test file, from the account's own Files page) and asked again in a fresh page load: PASS, exact. "I couldn't tell which document you mean. Name an uploaded file or a Notion page, or paste the text here and I'll work with it."
- **I re-uploaded the same text** under the same name afterwards (132 B, same content; the file date is now 10-23). The account is back to its prior state apart from the upload date.

**Row 3, compare:**
- `web-seed-1386` (no upload), "Compare these two documents": "I don't see that document among your uploads. Paste the text here and I'll work with it." No repo metrics. CXO to judge: it speaks of "that document" for a two-document ask, and it is the floor with nothing bound.
- `web-scn-a-1020` with its one upload, same ask: "I read 'launch-notes-tmp.txt' from your files." plus a one-file summary. It does not say it was asked for two documents and only had one. CXO to judge whether that is honest.
- `web-scn-a-1020` with the upload removed, same ask: "I couldn't tell which document you mean. Name an uploaded file or a Notion page, or paste the text here and I'll work with it." No repo metrics.

**Row 4, contrast, `web-seed-1386`, "Analyze my repo activity":** PASS. "Analyzed 4 commits in dinp-machine/piper-test-activity over the last 7 days. Authors: dinp-machine (4)". Still repo analysis.

**Row 5, #2138, `web-openai-run`, "Analyze launch-notes-2131.txt":** PASS. Opens "I read 'launch-notes-2131.txt' from your files." with a summary of the notes. No Notion.

**Row 6, Arch's row, same account, "What does launch-notes-2131.txt say?":** PASS. It reads the file: "I read 'launch-notes-2131.txt' from your files." and the same summary shape.

**Row 7, Arch's row, `web-seed-1386` (calendar events), "show all events":** the reply is today's meeting time, not a list of events: "Meeting Time Today: 1 hour across 2 meetings / Meetings: / 1:1 with Alex (30 min) / Design check-in (30 min)". It routes to the meeting-time answer, not week_calendar. Seeded events this week also include Tuesday's Roadmap review and Thursday's Team sync, which it does not show. Quoted for Arch; I judge nothing.

**#2096, `web-seed-1386`, viewport 500 by 800 px:** PASS on all three. "Send feedback" is a link to `/feedback`, at top 713 and bottom 728 px on `/todos` and `/projects`, and 713 to 730 px on Home (`/`), so inside the 800 px viewport with no scroll. I clicked it from `/todos`: it opens `/feedback`, title "Send feedback - Piper Morgan", with "Your feedback", a Send button and "Prefer email? support@pipermorgan.ai". I did not submit.

**#2140 Q29, `web-seed-1386` (some Piper activity today):**
- "What changed since yesterday?": "Here's what changed in your Piper tasks, projects and activity log since yesterday. I haven't checked GitHub for this." then "Tasks (3): Created: 3 - review the deployment plan - review prs - review prs".
- "What changed in the past hour?": "I don't see anything new in your Piper tasks, projects or activity log in the past hour. I haven't checked GitHub for this."
- Both openers carry the window. PASS against your expected strings.

**#2142 Q27, `web-seed-1386` (calendar events), "Tell me more about the GitHub integration":** no calendar event is called repo or GitHub activity. The reply lists what the integration reads (commits, branches, PRs, issues, labels, milestones, releases, stale PRs) and what it can do, and names the default repo. It does add: "Also due — three review prs reminders all came due earlier today. Worth clearing those out before your Design check-in." That is a reminder and a calendar event sitting in a GitHub answer, though neither is called repo activity. CXO to judge whether that tail belongs.

Verified how: logged-in browser, one ask at a time, page text read after each reply; for #2096 the link's position read from the page in a 500 by 800 viewport and the click followed to the opened page. Layer: served alpha UI. Denominator: all 7 of your numbered rows (row 3 on both accounts, plus the Notion half), the three #2096 pages and the Todos click, Q29 both asks, Q27. The `show all events` row was asked once. One script timed out mid-run and I read the chat history afterwards to confirm all seven asks had answered.

-- Web
