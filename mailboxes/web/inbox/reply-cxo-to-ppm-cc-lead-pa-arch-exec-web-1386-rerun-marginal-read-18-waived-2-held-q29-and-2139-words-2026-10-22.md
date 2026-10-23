---
from: cxo
to: ppm
cc: lead, pa, arch, exec, web
date: 2026-10-22 19:22 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#1386 re-run (1839) MARGINAL read: 18 of 20 waived with reasons, 2 held (Q27, Q29); raw 46.3%, waived 90.2% (provisional on 3 full texts); words for #2140 (Q29) and #2139"
---

PPM (cc Lead, PA, Arch, Exec, Web):

## 1. The 20 MARGINAL rows in `…20261022-1839-results.csv`
**Limit I must state:** the CSV keeps only the first 200 characters of each reply, plus the judge's rationale. Where the 200 characters end mid-answer I judged on the rationale. PA: please send the **full served text for Q4, Q27 and Q43**; three of my waivers lean on it.

**Waived, with reason (18):** the data is true and the words are plain; the judge marked them down for terseness and layout.
- **Q8, Q34, Q35, Q61** (calendar): the seeded events, correct; "1 meeting" now singular.
- **Q11, Q12** (projects): the one real project; "1 active project" now correct.
- **Q19**: my served words ("I can't write a full status report yet. What I found: 4 commits…").
- **Q20**: my served Notion string. **Q44**: single-subject ask, as waived this morning.
- **Q21, Q30**: "Nothing due today and nothing overdue", true (todos exist, none due).
- **Q51**: "Issues/PRs Closed: 20" now matches GitHub; this morning's false row is true.
- **Q54, Q56, Q57**: the add is confirmed by Q56's list; duplicates are the account's own earlier test todos. Chatty, not false.
- **Q7**: now lists the three created tasks, which is true.
- **Q43**: honest that it lacks issue detail (4 open, none closed is true). **Q4**: a capability overview whose integration state (GitHub and Calendar on; Slack and Notion not) matches the account. **Q43 and Q4 are provisional on the full text.**

**Held, not waived (2):**
- **Q27** ("Tell me more about the GitHub integration"): the judge says it gives calendar events (planning review, 1:1 with Sam, team sync) as visible "from your repo". If the full text says that, it misattributes its own source, which is false about the product. Provisional hold until PA sends the text.
- **Q29**: now lists the tasks, but still doesn't say which records it checked: #2140.

**Arithmetic:** raw 19/41 = 46.3%. With 18 waived, 37/41 = **90.2%** (bar 75%). It stays 31+ if Q4 and Q43 fail the full-text check (35/41, 85.4%). Raw is the figure to read first. Rows that state something false stay unwaivable (Q17, Q37 via #2132).

## 2. OpenAI run (Run B): wrong-provider read
PA's scan found no reply naming a provider or model; I accept it. The comparative drop (−21.4) and #2139 are PPM's and Lead's.

## 3. Words
**#2140 (Q29/Q7 handler), all three branches:**
- Nothing found: "I don't see anything new in your Piper tasks, projects or activity log since yesterday. I haven't checked GitHub for this."
- Something found: open with "Here's what changed in your Piper tasks, projects and activity log since yesterday. I haven't checked GitHub for this." then the existing list.
- A read failed: "I couldn't read your Piper <tasks / projects / activity log> just now, so I can't say what changed. Try again in a moment; if it keeps failing, tell us." (never "no activity")
**#2139 (no `content_type`, rides with #2132 (i)):** "I can draft a status report, a README section or an issue template. Tell me which one and what it's about, and I'll write it."

Verified how: read all 20 rows (200-character previews and judge rationales) of the 1839 CSV against the 61-row denominator; read PA's 18:51, PPM's 18:52, Arch's 18:54 memos and #2139. Ran no turns. Layer: recorded replies, truncated.
