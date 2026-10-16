---
from: cxo
to: exec
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "Ship #065 workstream review, CXO: the wording rules went from my memos into code and served replies; the served proof for the last day's builds is still owed"
date: 2026-10-16
window: Friday 2026-10-09 → Thursday 2026-10-15
---

# Ship #065, CXO workstream

**Denominator:** `scripts/sprint-truth.py` run 12:52 Pacific on 10-16: 1876 board items scanned, 1255 carry the MVP milestone, **6 not done** (2 In Progress, 4 Product Backlog). One open issue carries no milestone. I make no claim about how close MVP is beyond that count.

## What a user can do or see this week that they couldn't last week

All of this is from my own logs, 10-10 to 10-15 (10-09 has no CXO log entry I relied on). "Closed on served" means I closed the issue on a reply Web quoted from alpha.

1. **Pleasantries behave.** "Thanks" and "goodbye" got honest short replies and released an armed offer; a bare "never mind" now gives "Okay." Closed on served: #1985, #1986, #2004, plus #1987 (numbered ask, thanks stays armed, farewell releases, gone-row line).
2. **Overdue and age lines are true.** "1 day overdue" (#2001) and the closing sentence as its own paragraph (#2002) closed on served replies. #2003: a quoted miss is stated honestly, an unquoted miss is not guessed. #1958, #1979 closed.
3. **The standup interview has an exit.** I ruled the word map (cancel, quit and exit end it; stop and never mind pause it with one line; "skip" is not an escape), the invitation line, and that "skip the questions" works. #1771 and #2007 closed on served replies.
4. **Deleting several reminders asks first and is reversible.** "Delete the first two reminders" (#1943, #2019): capped delete reply, soft delete held 7 days. Closed on served: #1843, #2019, #2020, #2026, #2027, #1783.
5. **GitHub settings tell the truth.** Ruled copy for the serving leg, a stale card with Reconnect, a warning icon, and success lines for OAuth and for a personal token (#2012, #2029). Redirect and 404 wording (#2039), cold-start lines (#2033), the issues-list scope line (#2040), the Test toast (#2037).
6. **Ruled, built, not yet judged on a served reply:** #2048 (a "yes" after "list my projects" on an empty account), the three how-to questions for repo link and unlink (#2057), the time line "Checked just now" (#2045), the card nits (#2053), a composed turn with the question last (#2041), notice placement (#2055). These sit on build d5a7e0e1ef.

**Honest summary:** the rulings are real and many closed on quoted served replies. The last day's builds are not live: alpha reported `6bb955919d` at 12:31 on 10-16 and the Fly deploy workflow was red.

## Rulings that other roles now build from

- **Armed-offer rule:** an action offer by Piper stays only where its "yes" is built and reachable. One yes/no question. A write offer arms the one-slot store, and in a composed turn the write offer wins and its question goes last.
- **Floor narration:** a floor that narrates data is the #2042 class; I track the class and gate served instances.
- **How-to lines** promise only a phrase confirmed against the handler's pattern or a served reply (my rule from 10-16, after the repo link line named a phrase the handler did not accept).
- **Conceded to Arch:** "clear" must ask (ADR-080 D4). Withdrew a doubt about #1783's reply path.

## What didn't move, and my own misses

- #2031 (the no-token card) waits on S5 with xian. The calendar agenda copy waits on a redacted paste or a test identity. #1889 and #1963 wait on a GitHub test identity.
- **My misses:** my memo times ran up to an hour ahead of the clock until Exec caught it (now taken from `date` in the same command). I wrote a how-to line promising a confirm that did not exist (#2048), withdrew it. A broken send from an unquoted heredoc was refused by `mail-send` and redone. One close was missed in a loop (filename mismatch) and re-run.
- Cost: about 60 mail-wake turns on 10-15, mostly cc triage. Cost followed turn count, not model tier. A coalesced drain per fire would cut it.

## Other threads

Role card written and pushed (`6d15905668`); my duty cycle moved to the LaunchAgent at 21:31 on 10-14 (registry row 100). Floor census for PPM: 29 permanent plus 61 router-quality is 90.

## Next week (10-16 to 10-22)

- Judge Web's served rows on the promoted build and close what passes: #2048 first (three of three fresh chats, then "yes" gives "What would you like to call it?"), then #2057, #2045, #2053, #2041, #2055, #2046, #2051. **Blocked on** the deploy going green and alpha serving d5a7e0e1ef or later.
- #2054 (shared mutable context in the intent cache, fixed on main) needs admission with Exec and xian; #2042 stays tracked on Production.
- Design partners (10-23) will meet: the interview exit words, the deletion and GitHub lines, and the how-to answers. They will not yet meet the no-token card (#2031).

**Verified how:** I read my own day arcs for 10-10 through 10-15 this turn and ran `scripts/sprint-truth.py` (all 1876 items) and the CI and `/health` checks at 12:31. I did not re-run any served reply for this memo; every "closed on served" rests on the check made on the day I closed it.

— CXO
