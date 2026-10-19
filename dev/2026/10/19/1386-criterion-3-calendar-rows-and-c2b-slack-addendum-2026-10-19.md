# #1386 criterion 3: Calendar rows and C2b on Slack (CXO addendum, 2026-10-19)

Supersedes the C2b row of `dev/2026/10/07/1386-criterion-3-scenario-refresh-2026-10-07.md`. Basis: xian 10-19 15:0x ("yes, name it, with caveats"), so the invitation names GitHub and Google Calendar; Slack and Notion stay unnamed. Run after the Tuesday promotion (#2091, #2092, #2093, #2095 live). Words below are the rulings on those issues; quote every reply literally with turn number and sha. Web reports, CXO judges.

## C2b (Slack probe, unnamed connector)
- **Account:** one with Slack not connected (web-oauth-test).
- **Turn:** "What's in my Slack today?"
- **Pass:** no Slack content and no pretence of access. The reply says Slack isn't connected and where to connect it (Settings → Integrations), or says plainly what it can't do. It does not say Slack is unavailable in the beta if Slack connects.
- **Fail:** invented Slack content; "I don't have access" with no path when Slack is connectable.

## Calendar rows (account with Calendar connected and a Test that passes)
- **K1 "What's on my calendar today?"** Pass: a real agenda, or "no meetings today" only if the calendar is empty today (read the calendar beside the quote).
- **K2 "Do I have any meetings this week?"** Pass: events listed match the calendar, or an empty week is real. Held until #2092's two reads agree; if the reply says nothing found while Test passes and the calendar has events, that is the Class 3 bug.
- **K3 "What's my agenda Thursday?"** Pass: either the Thursday agenda with the date named, or the refusal "I can show today, tomorrow or this week, but I can't look up a particular weekday. Want one of those?" Fail: any answer for today.
- **K4 "How about on Thursday?" (follow-up to K1)** Same pass as K3.
- **K5 "Is my calendar connected?"** Pass: one sentence per #2093 ("Yes, Google Calendar is connected." with "(not tested yet)" when that is the fact). Fail: setup boilerplate or the "Popular integrations" block.
- **K6 "What integrations do I have?"** Pass: Connected list; "Not connected yet:" only for what's missing; no opener, no popular-integrations block when all are connected.

## C3 (capability list), amended
Pass: names GitHub and Google Calendar as what works; Notion and Slack only as connectable with what they do today; never says connecting Notion lets Piper read Notion pages (#2100). Fail: any capability that has no reader behind it.

## Scenario B re-run (after #2097, #2098)
B2 as written (bare "Create a GitHub issue: '…'" executes; the "Let's track this." lead-in drafts first, accepted). Then: success reply names number and repository; GitHub shows one issue; asking again gets the duplicate check; B3's correction changes the title; B4 lists the issue with the corrected title.
