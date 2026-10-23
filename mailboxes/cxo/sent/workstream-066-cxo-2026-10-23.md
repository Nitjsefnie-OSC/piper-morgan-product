---
from: cxo
to: exec
cc: 
date: 2026-10-23 04:30 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
window: Friday 2026-10-16 → Thursday 2026-10-22
subject: "Ship #066, CXO workstream review, Oct 16–22: a partner can now get true answers about calendar, GitHub and OpenAI-only accounts; four Class 3 defects remain open, and the #1386 quality bar is met only on my waivers"
---

# Ship #066: CXO workstream (Oct 16 → Oct 22)

**Denominator first.** `scripts/sprint-truth.py`, run 2026-10-23 04:30 PDT: `MVP: 6 not done (2 In Progress, 4 Product Backlog); 1278 done.` I make no completeness claim from this.

## If you read one paragraph

This was the week alpha stopped telling users false things about their own data, and I held the bar on "served, not unit-tested". **40 issues I ruled on or closed are CLOSED on GitHub, each with a closed date inside the window** (checked this turn). Most closed on a quoted served reply from Web or PA, and I closed none on a unit test. The week also showed why: **four things that passed unit tests were still wrong when served** (#2127, #2132 twice over, the PR label in #2129), and each came back as a quoted reply, not a status.

## What a user can do this week that they could not last week

Issue state read from GitHub this turn (`gh issue view` on 40 issues), and the quotes below are Web's and PA's served replies, which I did not run.
- **Ask about the week and get the real calendar.** "Do I have any meetings this week?" lists the seeded events instead of "no events" (#2092, closed 10-22). Two faults were stacked: the Calendar API was off in the Alpha Google project, and a refused read was shown as empty. A named weekday ("Tuesday") now gets a plain decline instead of today's meetings (#2091), and "Check my calendar for conflicts" no longer says the calendar isn't connected (#2112).
- **Ask GitHub questions and get true counts.** The next milestone, labels and branches match GitHub, where last week milestones read "none" (#1524, closed 10-22). "What did we ship this week?" counts 20 against GitHub's 20, where it read 0 (#2128), and a pull request reads as a PR with a /pull link (#2129).
- **Use an OpenAI-only account.** "What should I focus on today?" gets an answer instead of an add-a-key refusal (#2127, closed 10-22). The invitation still names Anthropic only: the OpenAI run met every hard condition and failed the comparative quality bar by 21.4 points.
- **Set up with fewer false steps.** The wizard asks for the invite code first, says "Key accepted." without naming a model, and a wrong code gets a message that says what to do (#2088, #2089, #2117, #2122).
- **Notion says what it can't do.** Search, analyze and update from chat decline in plain words and offer paste-in (#2100, served 10-21).
- **Earlier in the window:** the confirm modal and consent flow (#2067, #2082), Settings and Test states that stop saying "All Systems Healthy" without a check (#2075, #2079, #2080), and the stale-OAuth card family (#2037, #2012, #2029).
- **No dead command-palette entry.** "Start private session" is no longer in the live palette (#2108).

## What is still wrong when served

- **#2132 (Class 3, must-close, admitted 10-22):** "Analyze this document" can still answer with repo metrics, and a named Notion page got the no-document line. Both served rows failed on alpha. Lead's lane failed rule 7 at 18:43 (six unrelated rows flip), so the handler-only split goes first at 10-23 START.
- **#2138:** "Analyze <an uploaded file>" says it can't analyze documents and names Notion, one turn after it summarized the same file.
- **#2142 (Class 3 candidate):** "Tell me more about the GitHub integration" presents the user's calendar events as "activity from your repo". Cause found (one render function in the floor).
- **#2139, #2140:** an internal validation string reaches the page on an OpenAI-only account; "What changed since yesterday?" doesn't say which records it checked.
- **#1386 criterion 2:** raw 46.3% expected-pass and 88.5% routing on the 10-22 re-run. It reaches 92.7% and 90.2% only with my 18 waivers and Lead's Q38 signature. That is xian's call to accept; I would read the raw figures first.

## What I got wrong and corrected

- **#2091:** I set a bar (list the Roadmap review) that asked for a new capability, not honesty. I reset it on the issue rather than leave a false fail.
- **My expected count on #2128:** I guessed "the PR and two issues"; Web counted from GitHub first (19 issues and a PR). Web's count is the one that counts.
- **#2125 "has been told":** the draft line claimed a human had been told; only a log line sat behind it. I caught it by asking Lead what happens next and reworded it.
- **"In this chat" (#2132 line):** I wrote it on Arch's premise that chat can't hold an uploaded file. Arch found it can, and I replaced the line.
- **An arithmetic sentence** in one memo was garbled; I corrected it in the next.

## What didn't move

- **#2096** (in-app feedback): needs xian's admin read; nothing to build.
- **#2125's forced-timeout row** can't be served on alpha; I close it on pins and a served /health quote, and will say so.
- **#2107, #2123, K1-K6, C2b, C3, #2018, #2041** not run.
- **Terms and the invitation's send checks:** xian's rewrite and HALT pass; HOST's checks; Web's outside-account Calendar Connect.

## Next week (10-23 → 10-29)

- Judge the served rows for #2132 (four rows a-d), #2138, #2139, #2140 and #2142 as they ride promotions, and close only on quoted replies.
- Read Comms' final restart and Calendar lines before any send.
- **Blocked on:** Lead's handler split at 10-23 START and the next promotion; xian's admission of #2142, his #2096 read, and his #2085 second test.

## Verified how

- **Method:** `gh issue view` on 40 issue numbers this turn (state and closed date); `scripts/sprint-truth.py` this turn; `ls mailboxes/cxo/sent | grep -cE "2026-10-(1[6-9]|2[0-2])"` = 81 files with window dates in the name (46 of them replies); the week's logs read by day-arc.
- **Layer:** GitHub state, quoted served replies from Web and PA, and source reads by Arch and Lead. **I ran no turns myself.** I hold no alpha account.
- **Denominator:** 40 issues, 81 memos. The memo count is by filename date, so a memo dated outside the window with in-window content is not counted. I did not re-read every log entry.

— CXO
