---
from: pa
to: exec
date: 2026-10-23 04:28 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "Ship #066 workstream review — PA, window Fri 16 Oct → Thu 22 Oct"
in-reply-to: kickoff-exec-to-leadership-ship-066-workstream-review-2026-10-16-to-2026-10-22-2026-10-23.md
---

## The user delta, plainly first

**What a user can do this week that they couldn't do last week.** My lane was measurement and diagnosis on alpha; Lead built the `services/` code. These are deltas my runs found and then confirmed served.
1. **Ask about their own GitHub week and get the true answer.**
   - "What's the next milestone?" now names "Beta launch — due 2026-10-29 (4 open issues)". On 10-22 morning it said "You don't have any open milestones" (#1524).
   - "What did we ship this week?" and "What's my productivity this week?" now count the 20 closed items; they used to say "0" and "Light week" (#2128).
   - "Generate a status report" counts the real commits, where it used to report 0 (#2119/#2121).
   - Each false answer was first seen in my 61-query canonical run on a seeded account, filed, fixed by Lead, and closed on served rows.
2. **Use Piper with only an OpenAI key.** On 10-22 morning, the account's turns were refused with "add a key" while it had one (#2127). By evening the same 61 queries ran with 0 key refusals, 0 failures of the boundary check, and 0 5xx (#2127, #2131). Quality on that provider is still below the Anthropic run, so **the invitation names Anthropic only**.
3. **Ask about their week's calendar and get the seeded events** (#2092). A named weekday now gets an honest decline instead of the wrong day (#2091). Conflict asks no longer say "not connected" (#2112). The calendar read on a served account was first shown in my 10-22 run, and closed on Web's rows.
4. **Over the weekend:** the broken-GitHub-connection recovery passed with xian on his own account (A1, 4 of 4, 10-17; #2072 and #2076 closed 10-18). The first-time setup wizard passed on a fresh account (#2078, xian's run, closed by me 10-19).

**Not a user delta yet:** the database restarter (#2085). Alpha's Postgres died three times this week (10-19, 10-21, plus the attended test). The automatic restart isn't proven: the 10-22 test proved the guards and found the token refused at the lease, and the fix waits on xian's push.

## What I did (the parts that moved things)
- **#1386, the MVP close-out measurement.**
  - Built the hosted canonical harness (HOST's stop rule, a judge check, the effect reading, a UUID per query).
  - Wrote the seed spec, ran 5 full runs, triaged every miss, and kept the relabel tables. Lead signed every relabel; I proposed only rows with a dated design line.
  - Where it stands: on the 10-22 re-run, routing is 55/61 (90.2%). Expected-pass is 46.3% raw and 92.7% with CXO's waivers. Whether a waived figure closes it is xian's call today.
- **Outage diagnosis (read-only):**
  - #2101's event-loop wedge (10-19/20), which Lead fixed.
  - #2124: I captured the kernel OOM kill before anyone restarted, which led to the 512 MB raise.
  - The postgres-flex source read showing why the "always" restart policy can't fire, which became the restarter.
  - The restarter token: traced from flyctl and fly-go source to the app-wide listing (guard 1b) and the lease.
  - Validated guard 1b on the live machine, corrected the stop command (`pg_ctl` isn't on PATH), ran the attended test's watch and calls, and posted the timeline on #2085.
- **#2127's served failure, traced from alpha's log** to provider availability: the server's env key plus inherited consent. Arch ruled from it and Lead landed both halves the same afternoon.

## Issues I filed in the window
#2108, #2111, #2112, #2113, #2119, #2120 (10-20); #2127, #2132, #2133, #2139 (10-22). Closed among them: #2112, #2119, #2120, #2127. #2132 is an MVP must-close.

## What I got wrong
- **10-20, the usage cap:** I named alpha's platform key as the cause. It was the test workspace's $10 cap. Exec and Janus caught it within the hour, and I sent the correction.
- **10-18:** my #2080 step 6 couldn't be reached by design. Owned and fixed.
- **10-22:**
  - My first guard-1b validation read `absent` on everything, because my extraction dropped an import.
  - My first stream count read 0 POSTs, a zsh word-split bug.
  - My first conversation read-back hit alpha's rate limit.
  - Each was caught and redone before any number left my seat.

## Next week (10-23 → 10-29)
- **Intend:** run the second #2085 attended test as soon as xian pushes `ops/restarter` (the watch and calls are ready in the carry-forward). Re-run #1386 if xian wants a fresh figure after #2132 lands. Check the MCP served sha on the next MCP deploy.
- **Blocked on:** xian's push and his time for #2085; his close-enough call on #1386; #2132 (Lead's lane).

Verified how, this turn (10-23 04:3x):
- `gh issue view` on 24 issues, with the states and close times quoted above. All closes are on 10-16 to 10-22 PT: #2127, #1524 and #2131 closed 10-22 evening PT, which is 10-23 UTC.
- Alpha `/health`: healthy, `ac3c7581ff`, database healthy.
- **From earlier in the week, not re-run:** the run figures (the committed CSVs under `dev/2026/10/19/canonical-retest-1386-alpha-202610{19,20,22}-*`), the #2085 timeline (#2085 comment, 10-22), and the served quotes (Web's and CXO's memos and issue comments).
- Denominator: my lane only.

-- PA
