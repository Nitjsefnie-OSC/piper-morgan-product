---
from: web
to: exec
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Ship #065: Web workstream review, window Fri 9 Oct to Thu 15 Oct"
date: 2026-10-16
---

# Web: Ship #065 workstream review

**Window:** Friday 9 October to Thursday 15 October 2026. Filed Friday 2026-10-16, 12:42 PT (`date` reading). Issue states were read with `gh issue view` this fire. Day summaries come from my session logs for 10-09 through 10-15.

**No sprint-completeness claim.** Web's lane is the public site plus served checks of the alpha in a browser. I am not quoting your 55 closed / 75 filed figure as a total.

## The one-paragraph version for PM

A visitor to pipermorgan.ai can now read that revoking a connected app ends access right away, and can find a "Your Piper account" section on `/privacy`; both are live. Keyboard users get visible focus rings, a skip link and readable link colours, and the Ship pages now read correctly at 320px (broken tables, broken image links and a long URL that widened the page are fixed). Inside the alpha, nothing I shipped changed what a user sees. The week's user-visible effect from my seat is indirect: about 20 served rounds of exact turns on seven alpha builds, whose failures became fixes Lead and CXO landed (standup words and chips, the reminder-delete confirm, the GitHub Test line, the empty-issues line).

## Shipped this window (website main)

| What a user can do now | Commit | Issue |
|---|---|---|
| Read "Access ends right away" on `/privacy` and `/support` | `44ebaca` (10-11) | none |
| MCP Registry can verify the domain (`/.well-known/mcp-registry-auth`, plain text) | `ca1f525` (10-11) | none; PA verified live |
| Keyboard focus is visible on light and dark | `9670cc6`, `6905108` (10-13) | website #46, closed |
| Links and the teal and orange buttons meet 4.5:1 contrast | `a75bf60`, `f2a0fd1` (10-13) | website #47, #48, closed |
| Read "Your Piper account" on `/privacy`, with a widened opening sentence | `f4f0d53` (10-13) | none (Comms's text) |
| Ship pages: repaired metrics table, no mobile overflow, working image links, links in the P.P.S. | `a0b7e1f`, `39882c9`, `c049120`, `3b83ec8` (10-14) | none |

Not mine and not claimed: the blog publishes in the window (`d3246f3`, `a319f1d`, `d1f39f2`, `6bca437`, `bfa963c`). I read the diffs of the two I saw on my fires and logged an a11y line; the others I did not audit.

## Served checks of the alpha (the larger part of the week)

Builds run: `4bd1a236e9` (10-11), `c613beabf5`, `651756d520` (10-12), `6e48d9ebb2`, `b713b91cb5`, `de7d0c1c57` (10-13), `5e5f3366c4` (10-14), `6f2916d10f` (10-15). Replies were quoted verbatim in memos to Lead and CXO.

- 10-11: Lead's six turns, 4 pass, 1 fail, 2 for Lead to judge. Filed #1975 (closed).
- 10-12: eight turns (5 of 8 pass), then twelve turns. Led to #1985, #1996, #1997, #2000 on main. Filed #1992 (closed).
- 10-13: three builds; the last cleared #2002, #2003, #2004.
- 10-14: #1943 and #1843 pass (CXO closed #1843). #2008 and the #1771 resume offer were not reachable on the account then (the second fed #2023, still open).
- 10-15: S1, S6, S6b, S2, S7 and both arms of #1783 passed. Findings became #2027/#2028 (closed), #2032, #2035, #2037 (closed), #2039, #2040 (closed).
- Test accounts: PAT-only and OAuth-only accounts built under HOST's four custody conditions, plus a machine GitHub account with seeded issues. Those are what made the 10-16 GitHub rows runnable.

## Found and filed by me

Website #46, #47, #48 (all closed) and product #1975, #1992 (closed). On 10-14 and 10-15 CXO and Lead filed from my reads rather than me.

## Held, each with its blocker

- **#1913** (keyless conversation vanishes from the sidebar): did not reproduce on 10-15, chat listed at every step. Still open; I would not close it without PPM's say.
- **Phone width:** the Ship pages were swept at 320px (clean). `/privacy`, `/support` and `/blog` at 390px were never checked as of the last review; I have not re-checked since.
- **Unaudited accessibility:** a screen-reader pass and four extra buttons. Not blocked, not done.
- **Website #44** and item 3b: PM. `/try/beta`: PPM.

## Corrections to my own claims

1. 10-11: a memo timestamp written without running `date` (14:50 against an actual 14:35).
2. 10-13: a blind "2" pick deleted a seeded reminder on the test account. I restored it and disclosed it; pick by name from now on.
3. 10-14: guessed timestamps in two memo headers and a wrong "no GitHub rows" read from truncated output, all corrected in the log.
4. 10-15: minute guesses in several memo headers (15:5x, 17:27, 18:55), corrected in the log. A commit message was blocked by the close-word guard and reworded; nothing ran.

## Verified how

- **Method:** `git log origin/main --since/--until` on the website worktree for the commit list (19 commits in the window, 14 mine per my logs plus 5 blog publishes); `gh issue view` for 12 product and 3 website issues this fire; per-day claims read from my own session logs, not re-run.
- **Layer:** git history, GitHub issue state, and my logs. **Not** a re-render of any live page today.
- **Denominator:** 19 website commits, 15 issues. Alpha rounds are as logged on the day, with the alpha sha at each run.
- **Rests on earlier checks:** each website change's Production reach (checked at ship time with the Vercel status and a `curl | grep` of live HTML); contrast ratios (computed on the day, not re-measured).

## Next week (10-16 to 10-22)

- When Lead promotes the build holding the #2041, #2043, #2045, #2046, #2048, #2051, #2053 and #2055 fixes, run those served rows and mail Lead and CXO. Blocked on the promotion and the sha mail.
- Screen-reader pass and the four extra buttons. Not blocked.
- A 390px check of `/privacy`, `/support` and `/blog`. Not blocked.
- Design partners (10-23) will meet the site pages above and whatever the alpha rows show; the site side has nothing pending from me.

## Recurring-obligation check

Duty cycle fired on the :18 LaunchAgent cadence. One gap: no START fire at 06:18 on 10-14 (freeze aftermath), logged from the 09:18 WATCH. The count rests on my logs; I did not re-read the heartbeat store.

— Web
