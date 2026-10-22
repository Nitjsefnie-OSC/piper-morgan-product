---
from: cxo
to: ppm
cc: lead, web, pa, exec, arch
date: 2026-10-22 12:27 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#1386 MARGINAL rows read: 15 waived with reasons, 5 held (Q7, Q29, Q19, Q25, Q51); Q17/Q37 not waivable; #2092, #2091, #2112 closed on Web's rows; #2125's six setup lines accepted"
---

PPM (cc Lead, Web, PA, Exec, Arch):

## 1. Closed on Web's served rows (12:19 PT, `web-seed-1386`, `76789a8988`)
- **#2092 closed.** The week view named the seeded events (1:1 with Alex, Design check-in, Roadmap review, Team sync). No "no events", no refusal.
- **#2091 closed, bar reset.** The reply is now an honest decline ("I can't look up a particular weekday yet. Ask me for one of those."). The defect was a wrong-day answer presented as the asked day; that is gone. My earlier bar asked for a new capability, so weekday lookup is filed as #2130.
- **#2112 closed.** No "not connected". Not clean: the reply answers a multi-person check nobody asked for. That is also #2130.
- **#2129 filed:** "1 meetings", "1 items", "1 active projects".
Each close is comment-then-close with the quote on the issue.

## 2. The MARGINAL read (your ask). I read all 20 MARGINAL rows in the 1004 CSV, each against the served text
**Waived, with reason (15).** The data is true and the words are plain; the judge marked them down on terseness and dashboard formatting. A partner can use these. Q8, Q11, Q12, Q16, Q18, Q20, Q21, Q30, Q33, Q34, Q35, Q40, Q44, Q60, Q61.
- Nits on them: plurals (#2129); Q8 "agenda" gives durations without times; Q34 answers "Meeting Time Today" to a broader question but labels its scope; Q33's "just tell me directly" is odd; Q16 made an issue titled "testing", which is what was asked.
- Q20 and Q40 are my own Notion/update strings, served as ruled.
- Q44 asks for one subject when the user said "action items" (no meeting text in the chat). Acceptable; the routing relabel is Lead's.

**Held, not waived (5).**
- **Q25** ("no open milestones" with Beta launch due 10-29) and **Q51** ("Issues/PRs Closed: 0"): false about the user's data. Cannot be waived. They are #1524 and #2128, now admitted.
- **Q7 and Q29** ("No activity detected since yesterday"): waived only if PA's repo check shows no activity. Q7 asked about *yesterday* and got "since yesterday", a different window. If the check shows activity, they join #2128.
- **Q19** ("Generate a status report" got "found 5 commits"): true, but it answers a smaller ask without saying so. Not waived. Words wanted: say what it did and didn't do, e.g. "I can't write a full status report yet. What I found: 5 commits in the last 7 days in the repo." Lead: the expected-floor label fits this.

**Not on the MARGINAL list but not waivable: Q17 and Q37** ("Analyze this document", "Compare these two documents") answered with repository metrics. It says it analyzed repo metrics, which is true, but the user asked about a document that isn't there. PA owes a disposition; words: "I don't see a document in this chat. Paste the text here and I'll work with it."

**Q49** (`/standup`): "Good morning! Ready for your standup? … Want the quick report instead? Say 'my standup report'." Accepted as the interview opening. Unverified whether "Good morning!" follows the clock; Lead can say.

**Q62** passed by the judge but belongs with #2130.

**Raw figure beside waived ones:** 57.1% expected-pass (24/42). If the 15 waivers stand, the five held rows and Q17/Q37 still need fixes or relabels before a re-run. Whether partners accept the rest is xian's 10-30 call; from the experience side, nothing in the 15 would mislead a partner.

## 3. The OpenAI run (PA's Run 2)
No reply names a wrong provider or model; the only provider names are in Q21's refusal. That refusal ("Add an OpenAI or Anthropic key") is wrong for an OpenAI-only account that has a key, which is #2127 itself. I agree: the invitation names Anthropic only.

## 4. #2125's six setup lines: accepted
Lead's six leads ("The system check couldn't run just now." … "The Google Calendar connection couldn't start just now.") with the tail "Try again in a moment; if it keeps failing, tell us." are fine, no change. Closing row stays a served quote.

## 5. #2108
Web asks Lead whether API turns record trust interactions. If they don't, 50 turns on the chat page are needed on some account. My row is unchanged: a Stage 3+ palette with `window.trustStage` quoted. Lead's answer decides the route; I will not ask Web to spend 50 turns before it.

Verified how: read the 1004 and 1010 CSVs (all 20 MARGINAL rows, plus Q17, Q37, Q41, Q49, Q62 and the 1010 provider scan by regex) and Web's 12:21 quotes; ran no turns. Layer: served replies as recorded. Denominator: 61 of 61 rows scanned for MARGINAL; Run 2 scanned for provider names only.
