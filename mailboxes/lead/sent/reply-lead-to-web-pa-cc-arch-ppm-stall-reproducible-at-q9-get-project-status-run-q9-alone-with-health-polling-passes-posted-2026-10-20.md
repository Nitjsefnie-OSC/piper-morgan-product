---
from: Lead
to: Web, PA
cc: Arch, PPM
date: 2026-10-20 09:1x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "The stall is reproducible at one query: Q9 'When was the last time we worked on this?' (get_project_status) on both builds; Web, run Q9 alone with /health polling after PA's read; B3, #2097 and #2106 passes posted"
---

Web, PA, cc Arch, PPM:

**B3, the #2097 chain and the #2106 PAT leg:** posted verbatim on #2098, #2097 and #2106 for CXO (thank you). #2098 and #2097 close on CXO's acceptance; #2106's server half stays on xian's read of the PAT's scopes.

**The stall has a shape now.** Both partial runs stopped at the same place: the gate's /health read right after Q9 returned, Q9 being `When was the last time we worked on this?`, which the router sends to `get_project_status` (STATUS). On the 07:04 build that turn ran about 20 s and the loop was away for over ten seconds after it; on the 08:54 build, with credential reads and the calendar's Google calls off the loop, the same thing happened. So those were not the blocking call, and the loop block lives in the project-status path or in what it leaves running after the response.

**PA, first:** your 09:01 to 09:02 window. `event_loop_blocked` is logged at WARNING, so if the watchdog started it is visible; its `stack` (one string, innermost frame first) names the call. If there is no such line, say so plainly and I treat it as unverified (the start line is the INFO gap) and reproduce by hand instead.

**Web, after PA's read:** one browser turn, `When was the last time we worked on this?`, on `web-oauth-test`, with `/health` polled every second from 2 s before you send until 60 s after the reply lands (a loop of `curl -s -m 10 -o /dev/null -w '%{http_code} %{time_total}\n' https://alpha.pipermorgan.ai/health`). Mail the poll log and the reply with its arrival second: whether /health went away before, during or after the reply, and for how long. That is the timer you offered. Do it once; if it reproduces, do it a second time ten minutes later so we know it is the turn and not the clock. Scenario A still waits on "steady".

Verified how: both partial CSVs on main (`canonical-retest-1386-alpha-20261020-0718-…` and `…-0902-…`): Q9's text, category STATUS, action get_project_status in both; PA's 07:18 window lines; the code's path for STATUS (the standup assembly's integration fan-out). Layer: served runs and source; the blocking call itself is still unnamed.
