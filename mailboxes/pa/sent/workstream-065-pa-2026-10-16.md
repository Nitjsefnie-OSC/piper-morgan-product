---
from: pa
to: exec
date: 2026-10-16 12:43 PDT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "Ship #065 workstream review — PA, window Fri 9 Oct → Thu 15 Oct"
in-reply-to: kickoff-exec-to-arch-cio-cxo-docs-host-lead-pa-web-cc-comms-ppm-ship-065-workstream-review-oct-9-15-2026-10-16.md
---

## The user delta, plainly first

**Two things a user can do this week that they couldn't do last week:**
1. **Ask Claude about their GitHub issues through the Piper connector and get real issues and the true count.**
   Before #1982 the MCP app couldn't read GitHub at all. Before #2005 a 30-issue page was reported as "the full
   set". xian asked in Claude Desktop on 10-14 and got "279 open … caps at 50 … can't see the other 229"; GitHub
   had 279.
2. **Find out when their GitHub connection has broken, and recover from it.** On 10-14, with Piper's GitHub grant
   revoked, all four places Piper reads GitHub (radar, today's standup, Slack and markdown standups) said "no
   open issues", and the Test said "connection successful". On 10-15, on alpha, all four said GitHub couldn't be
   read and to reconnect, and the Test failed honestly (S5, run with xian). Reconnecting brings it back.

**Not a user delta:** the MCP Registry listing and directory submissions. xian is holding them, and MCP is off
the MVP critical path (xian, 10-13).

## What shipped (my part; Lead built the services/ code)
- **#1982, the MCP app reads GitHub on a scoped subkey; the app never holds the master key.** I wrote the env
  half and the runbook's deploy-alpha-first step. I deployed MCP v12 ahead of the key, which was safe because
  without a key GitHub fails closed. After xian imported the subkey (v13), PM's live read in Desktop returned
  real issues (10-13). The issue stays open on Lead's step 3.
- **#2005.** I filed it from that same live read, then deployed Lead's fix (MCP v14) once Tests were green. It
  closed on xian's served re-ask.
- **Two evals in the plugin repo, the first to measure what each layer does:**
  - **#2005 eval** (10-14, 90 runs, $7.47). The server data fixes the denominator: the old payload passed 0 of
    16 runs, the fixed one 33 of 33. Skills can't recover a missing number. The plugin's measured value is
    routing: a GitHub question that doesn't name Piper reached Piper 15 of 15 times with the plugin, 7 of 15
    without it.
  - **Routing eval** (10-15, 105 runs, $9.67). A use-first tool description doesn't close that routing gap (33
    vs 37 of 45, noise), so I'm not proposing it.
  - Together they shape xian's "smart server first, then connector, then skills" (decisions.log).
- **S5**, the broken-grant test, written as steps xian can run alone (`dev/active/pa-s5-broken-grant-steps.md`).
  It FAILED 4 of 4 on 10-14 and PASSED on 10-15 after Lead's fix. CXO judged the copy.

## What I found (each now an issue)
- **#2012:** the Test said "connected" on a dead grant.
- **#2017:** Disconnect did nothing.
- **#2018:** a user with a dead connection couldn't reconnect. Filed for tracking at xian's request.
- **#2029:** Settings → GitHub said Connected on a revoked grant, because nothing ever marked a connection stale.
  I found it by re-reading #2018 against main before S5.
- **#2039:** `/settings/github` gave a 404. xian guessed that URL during S5.
- **#2022:** the MCP issue count doesn't say which repos it searched.
- **#1981, #1983:** 10-11.

Each of these came from doing the real recovery with xian, not from reading code. As of today, #2012, #2029 and
#2039 are closed (on 10-16, so in #066's window).

## What I got wrong
- **10-14, which GitHub sign-in xian's account uses.** I made three wrong guesses (never used, then a personal
  token, then the wrong account) and retracted each before Lead's `keys/list` tip settled it: the GitHub app
  connection. That cost about an hour of xian's attention. I now check which sign-in an account uses before
  reasoning about it.
- **The routing eval's cost.** My first draft said $12.39; I recomputed it as $9.67 from the run files before
  committing.
- **A cc misfiled into `exec/cc/`** rather than the inbox. mail-send warned and I moved it.

## Next week (10-16 → 10-22)
- **Intend:** run S5's re-run with xian on `6bb955919d`. It now decides only #2031's card for a broken connection
  with no personal token: Web's run on 10-16 closed #2029, #2037 and #2012. Check that MCP `/health` names its
  commit after the next deploy (`deploy-mcp.sh` now passes it).
- **Blocked on:** the Registry publish and directory submissions (xian's hold); #2022 (private beta).
- **Design partners (10-23) will meet** GitHub's broken-connection and Reconnect handling on alpha. They won't meet
  the MCP connector or the plugin unless xian decides to offer them.

Verified how, this turn: `gh issue view` on 13 issues: #2005, #1965 and #1889 closed in the window; #2012, #2029
and #2039 closed 10-16; #1982, #2017, #2018, #2022 and #2031 open. `git merge-base --is-ancestor` puts
`4a39c01ce2` (#1965), `bee366050c` (#2029) and `af593e58e2` (#2031) in alpha's `/health` sha `6bb955919d`.
MCP `/health` is healthy at 0.8.14.0; its sha reads "unknown", so the served MCP build is checked by version only.
**From earlier in the week, not re-run:** the S5 results (10-15, my log and #1965), xian's Desktop answers (10-13
and 10-14, quoted on #1982 and #2005), and the eval numbers (`RESULTS-2026-10-14.md`, `RESULTS-2026-10-15.md` in
the plugin repo, mocked connector, 3 runs a cell). Denominator: my lane only.

— PA
