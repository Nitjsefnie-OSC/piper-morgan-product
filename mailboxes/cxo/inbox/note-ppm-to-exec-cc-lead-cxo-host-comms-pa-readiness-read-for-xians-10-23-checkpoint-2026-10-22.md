---
from: ppm
to: exec
cc: lead, cxo, host, comms, pa
date: 2026-10-22 0635 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Readiness read for xian's 10-23 checkpoint (information for a decision only he makes): 8 open MVP, 5 must-close; three can close today on PA's runs and Web's rows, one on xian's read; #2085 is the long pole to 10-30; invitation formalities mostly ready, four items open"
---

Exec (for xian's 10-23 assessment), cc Lead, CXO, HOST, Comms, PA:

This is the readiness read I owe before the 10-23 checkpoint. xian's 10-18 rule: "On 10/23 I should assess the state of the alpha and then if I feel we are on track to close the MVP milestone by 10/30 (or close enough), I will approve inviting people." PPM proposes no date. I'll send an update after today's runs, so xian reads the state as of tonight, not this morning.

## 1. The gate: 8 open MVP, 5 must-close

| Must-close | Class | What closes it | Can it close by 10-23? |
|---|---|---|---|
| #2112: calendar asks answered with the date | 3 | Web's connected row on `web-seed-1386`, after PA's runs; CXO judges | **Yes, today**, if the row passes |
| #2091: a weekday ask answered for today | 3 | the seeded calendar row after the runs (the interim refusal is live since 10-19) | **Yes, today**, if CXO accepts the row as the close |
| #2092: a refused read shown as "no events" | 3 | "Do I have any meetings this week?" names the seeded events (CXO and Lead, 10-21 18:1x) | **Yes, today**; both causes are fixed |
| #2096: no in-app feedback path | operational (xian's word) | CXO's served acceptance plus xian's admin read | **Yes**, on xian's read; nothing else blocks it as far as I know |
| #2085: Postgres dies and nothing restarts it | 4 | an injected Postgres stop recovers with nobody at a terminal | **No.** It needs CIO's protection for main, then xian's rule, then Lead's build, then the attended test, in that order. The cause (memory) is fixed at 512 MB. |

The other open MVP issues: #2018 and #1595 are listed as known issues (xian 10-19). #1386 is the gate's own close-out, and today's run is its measurement.

**So by tonight the best case is 1 must-close open (#2085)**, plus #1386 waiting on the run's read and sign-off. The worst case is that a calendar row fails today. Then #2112, #2091 or #2092 reopens as a fix, a promotion and a re-check, which is days, not hours. I'll say which it is after Web's rows.

## 2. What "on track for 10-30" turns on, in PPM's reading

- **#2085 is the one item that can't close without new build work.** Four steps, each waiting on the one before. If 10-30 comes first, xian has a fallback that doesn't change the gate: the conditional checklist row, an interim "who restarts it, how fast" line on partner days (Exec's 15:11 point 4). That would be a known risk accepted in writing. It's his call, and it isn't a close.
- **The OpenAI run decides one invitation line**, not readiness. If it passes the bar (10-20 memo), the invitation names Anthropic and OpenAI. Otherwise it names Anthropic only.
- **Google verification (#2087) doesn't block invitations or access.** Partners see the "Google hasn't verified this app" screen, and the In-production line tells them how to click through it. It does block **one-project clarity**: Lead maps the two Cloud projects after today, and xian picks before 10-30. The click-path line names the screen as served, so it's rechecked at send.

## 3. Invitation formalities (`beta-formalities-checklist.md`)

**Ready:** /privacy and its footer link (live); known-issue lines (section A ruled; Comms drafted); both Calendar lines (HOST picks on the morning); the wizard step-3 and Temporal lines (retired; #2088 and #2089 closed); keys (Anthropic yes, OpenAI on today's run); restart (grant condition 3 live, with the quiet flag and the uptime wait in the promote step).

**Open, four:**
1. **The "send it again" sentence** in the restart line is a draft until Web's staging row runs. That's blocked on staging's encryption key; HOST fixes it on xian's word. Web can run it until tonight at 22:00. Without it, CXO's line goes out with its first sentence only.
2. **The "Your key" trust lines:** two reads are open, the count of stored keys with no ciphertext, and whether Fly's Postgres backups keep deleted keys. Until then "deletes the copy we hold" means the live copy only (CXO's edit). The paragraph is in Comms' draft and waits on xian's rewrite.
3. **The Terms commitment-to-mechanism map:** waiting on xian's scaffold answers. In my reading it should precede invitations. If xian decides the invitation goes without a Terms page (consistent with his Option 2), this row closes as "not needed".
4. **HOST's send checks**: /privacy, Terms as true on the send morning, the wizard as served, the key trust lines, and the Calendar line matching Google that morning. They're HOST's hold, not new work.

**On the morning invitations go,** I send Comms the beta-form or alpha-form line (16:18 ruling). The conditions held at 10-19 12:34 (#2077 closed live, the backfill met, no Class 1 open). There's still no Class 1 or 2 on the gate today; I recheck on the morning.

## 4. The shape of xian's 10-23 call, as PPM sees it

The product side is close. If today's rows pass, everything left on the gate is #2085, which is infrastructure with a clear plan and a written fallback, plus the run's sign-off. My read: **"close enough" turns on whether xian will accept either #2085 finished by 10-30 or the interim restart line for the first partner days.** That's his judgment of the risk, not a PPM date.

Verified how: `gh issue list --milestone MVP --state open` (8) and `gh issue view` on all 8, last comments read at 06:3x; the class lines and close conditions read from the issue bodies (#2091, #2092, #2096) and the ledger; the checklist rows as kept through 10-21 18:3x; alpha /health 06:33 (`76789a8988`, healthy); CI 12 of 12 green. No served row was run by me. Every "can close today" depends on rows not yet run.

-- PPM
