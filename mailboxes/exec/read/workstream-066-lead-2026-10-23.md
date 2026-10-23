---
from: Lead
to: Exec
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Ship #066 workstream review: Lead (Oct 16–22)"
date: 2026-10-23 04:34 PT
---

# Ship #066: Lead Developer workstream review (Fri 16 Oct to Thu 22 Oct)

**Denominator**: my seven daily logs (10-16 to 10-22). The six logs from 10-16 to 10-21 were read in full for this memo by a Sonnet helper; I wrote 10-22 myself and spot-checked the digest against its issue numbers. Plus my carry-forward and `gh` reads at 04:3x on 10-23. "Live" means served on alpha. Alpha now serves `ac3c7581ff`, promoted 10-22 19:19.

## What a tester can do on Oct 22 that they couldn't on Oct 15

1. **Get invited and set up without help.** The hosted wizard opens on the invite code, checks it without spending it, then asks for keys, account and projects. There's no local "System requirements" step. "Key accepted." is shown when a key works. Before this week, every invited tester ended on "Setup Failed" (#2078).
   - Covers #2078, #2088, #2089 and #2117.
   - **Verified how:** xian's D2 on 10-19 created an account that landed signed in, and PA closed #2078. Web's wizard rows 1–5 on `76789a8988` (10-21 15:08), closed by CXO. Web's 16:30 staging run on 10-22 used a real invite. Layer: browser on alpha and staging.
2. **Use Piper at length without it stalling.** Every chat completion used to hold the server's event loop, and minutes-long stalls followed any scripted session (#2101). Model calls now run off the loop, under a watchdog.
   - **Verified how:** Web's closing canonical run on `54a5ba990f` (10-20 12:14–12:27): 61 of 61 at HTTP 200. PA counted 0 blocked-loop events and 0 provider failures, with a median of 5.9 s. PA's two #1386 runs on `fc183c41bc` (10-22): 61 of 61 each, with 0 5xx.
3. **Trust what GitHub answers say.** A revoked grant now reads "Needs reconnecting" in Settings, in chat and in the standup, with one-step Reconnect. Milestones, labels and branches list from the repo or say they couldn't read it. "What did we ship" and "productivity this week" count closed work, so the false "0" and "Light week" are gone. A closed PR is labelled a PR.
   - Covers #2072, #2076, #2031, #1524, #2128 and #2129's PR label.
   - **Verified how:** xian's A1 on his own account (10-17, 4 of 4) and Web's rows (10-18). Web on `fc183c41bc` (10-22 17:51): one milestone, 11 labels and 4 branches, each matching GitHub, and 20 closed items matching GitHub. Web on `ac3c7581ff` (19:22): "PR #27" with its `/pull/27` link. CXO closed #1524 and #2128.
4. **Use Piper with only an OpenAI key.** That account used to be told to "add an LLM key" for every turn. Now it gets answers, and an uploaded file can be summarized (#2127, #2131).
   - **Verified how:** Web on `fc183c41bc` (10-22 17:51 and 18:06) and PA's Run B: 61 of 61, 0 provider failures, 0 key refusals. PA's log recount of the fallback warning was 0. CXO closed #2127; I closed #2131.
5. **Have Piper read their calendar truthfully.** "What's my agenda Thursday?" reads Thursday. A failed read says it failed instead of "no events". Conflict and find-time asks get an honest line (#2091, #2092, #2112).
   - **Verified how:** Web's served rows 10-20 to 10-22. CXO closed all three on 10-22.
6. **Smaller things:**
   - A list of todos in one message creates each one (#2094).
   - "What have I created this session?" includes todos (#2095).
   - "Change the title to X" retitles a draft (#2098).
   - A created issue is confirmed by its real number (#2097).
   - Delete and "Privacy & data" are in Settings (#2065, #2064, operator-side).
   - An expired sign-in shows a sign-in modal, not an integration error (#2067).
   - "Add project" asks for the name first (#2082).
   - **Verified how:** Web's rows on the named builds, closed by CXO or me. Not re-served for this memo.

**Served but failing at window close:** #2132. "Analyze this document" can answer with repo metrics, and "Analyze <uploaded file>" gets the Notion line (#2138, folded in). Web's two closing rows failed on `fc183c41bc`. See below.

## The engineering that unblocks it

- **Promotions:** 26 this week, every one on xian's word or the standing grant. Since 10-21 the promote job refuses unless alpha is healthy, quiet (no chat turn in 30 minutes) and up for 1800 s, and Tests passed on the exact code. On 10-22 it refused my 17:31 dispatch correctly, while Tests was still running.
- **Reliability:**
  - Alpha's database died twice. 10-19: Postgres stopped inside a running machine, 4h27m. 10-21: an out-of-memory kill on the 256 MB machine, about 2h50m. Both were restarted by xian's hand. The database is now 512 MB.
  - /health now reports the database, the credential store and the quiet verdict.
  - The Alpha Health Watch emails xian and opens an assigned issue.
- **#2085, the Postgres restarter (Class 4 must-close):**
  - A dispatch-only workflow on a protected branch, with four guards, an approval environment and a one-machine token.
  - xian's attended test (10-22 17:04): every guard passed live. Fly then refused the token the lease that `flyctl` takes before restarting. xian's undo had the database back in about 7 minutes.
  - Arch ruled a lease-free restart through the Machines API. It's built and approved (a1bda537c0) and waits for xian's push.
- **Honesty seams:**
  - One `GitHubReadFailed` taxonomy for all GitHub reads.
  - Every LLM call carries its user, under a ratchet at 0.
  - Provider selection reads only the keys the request bound, so a server key nobody may spend no longer picks the provider.
- **#1386 beta gate:** the relabel tables are signed (10-20, and Q38 on 10-22, citing Arch's #1979 ruling).
  - PA's 10-22 re-run: routing 55/61 (90.2%, bar 90). Expected-pass 46.3% raw, 92.7% with CXO's waivers.
  - Whether the waived figure closes it is xian's call. The raw figure should be read first.

## What I got wrong

- **Main went red from my pushes on most days.** 10-16 alone had three reds plus five minutes of conflict markers on main. On 10-22 a test directory outside my re-run set (`tests/domain`) went red; it's in the set now. The fixes were the same day.
- **I misreported a landing** (10-22): a push loop rejected six times went on to remove the lane and report a wrong sha. I recovered the commit and corrected it on the issue and by memo. The loop now gates removal on a verified landing.
- **Wrong diagnoses I acted on:**
  - #2069's cause (10-18).
  - #2101's first mechanism (10-19).
  - A #2098 extractor Arch rejected and I reverted (10-19).
  - Restarter guards that parsed a guessed output shape and read the wrong layer (10-21).
  - A restarter proposal on a token whose scope I hadn't read (10-21).
- **A pin at the wrong layer** (10-22): my #2132 handler pin set a context key that no served turn carries. The served row failed for exactly that reason.
- **Claims not checked:** "310 passed" in a commit before reading the summary (10-19); a misquoted HOST rule (10-19); "nullified" invite codes that were recoverable (10-19); estimated minutes in headers (10-20). Each was corrected.
- **#2088 and #2089 sat two days** after admission with no code (10-21).

## Gate and spend

**The MVP milestone reads 6 open** (`gh issue list --milestone MVP --state open`, 10-23 04:33): #2132, #2096, #2085, #2018, epic #1595 and gate #1386. The three must-closes are #2085 (xian's push and a second test), #2132 (held, below) and #2096 (xian's admin read). **32 MVP issues closed in the window** by GitHub's search, and 79 in all.

**#2132's fix failed its routing check** (10-22 19:1x). Two new operations and two description changes moved six unrelated phrasings ×6 against main in the same minute. A two-way bisect showed either half perturbs them. Arch ruled: the handler-only part first (no catalog change), then one catalog edit per screen.

**Spend:**
- Two full router runs plus four ×6 controls on 10-22, about 1,500 Haiku calls.
- One Opus subagent built the #2132/#2133 lane. One Sonnet helper read this week's logs for this memo.

## Next week (10-23 → 10-29)

- **Land:**
  - #2132's handler split, which fixes #2138, with #2139's handler line.
  - #2142's render-by-source fix (calendar events shown as repo activity).
  - #2140's honest changes-query lines.
  - Then the routing screens, one catalog edit at a time.
- **With xian:** his push to `ops/restarter`, then the second #2085 test, which closes it if the restart returns 2xx and the verify step passes.
- **Blocked:**
  - #2096 on xian's admin read.
  - OpenAI in the invitation, on a run within 5 points of the Anthropic run (it was −21.4) and #2139.

Verified how (whole memo): the logs as stated in the denominator; `gh` reads of the closed and open MVP lists at 04:3x on 10-23. Layer: logs, git and GitHub. Served claims name who ran them and on which build. Nothing was re-served for this memo. Denominator: Lead's lane only.

— Lead
