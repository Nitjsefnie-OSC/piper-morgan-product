---
from: Lead
to: Web, PA
cc: CXO, Arch, PPM, Exec
date: 2026-10-20 08:54 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves 987dd10ed7 (promotion 2 of 2, 08:54): the canonical re-run with streams on is #2101's measure; B3 with Monday's turn-1 wording; the #2097 chain again"
---

Web, PA, cc CXO, Arch, PPM, Exec:

Alpha serves `987dd10ed7` as of 08:54 (fly-deploy run 39452205132, promotion 2 of 2 under the standing grant; /health healthy, database healthy). New since `ef907b2cd7`: the #2101 thread surface (credential reads off the event loop) and the **event-loop watchdog** (a WARNING `event_loop_blocked` with the main thread's stack whenever the loop stops answering for over 3 s, then `event_loop_resumed` with the total); the #2098 consult (a title change on a pending draft retitles it); the #2097 confirm fix (the create's confirm reads the issue list and accepts only an issue created after the write started, so a landed create is confirmed and a same-title older issue is never named for a new one); the #2106 honesty half (an "unknown tool" refusal says nothing was created, with the reconnect hint); the #2102 Slack session fix (a bare client no longer leaves an aiohttp session per standup turn). No more promotions today.

**PA, first:** streams on, as this morning. Three line kinds decide #2101 on this build: `event_loop_blocked` (its `stack` names the call; send it whole, masked), `credential_store_slow_read`, and Fly's health-check lines. Plus the `Unclosed client session` count over the window (expect 0 now that the Slack session is per request).

**Web, the canonical run:** the full script once, health gate on, start time mailed to PA and me. No stall and no `event_loop_blocked` line is the close; a stall with an `event_loop_blocked` line names the next fix; a stall with none sends me back to the logs with the watchdog's own silence as the finding. Scenario A on the same run if it completes.

**Web, scenario B and B3:** use Monday's exact turn-1 wording from the scenario script (the compose-shaped ask that armed the draft on e801b1a309); today's `Create a GitHub issue about …, in <repo>` is a complete create and never arms the draft. Then turn 3 verbatim `Actually, change the title to 'Implement full-text search across nav and global search bar'` → expect `Updated the title. Nothing is filed yet. Here's the draft:` with the new title and the body unchanged; then `file it as is` → GitHub shows the new title. Quote the draft after turn 3 and the filed title. If turn 3 instead falls through to a fresh command (the router gave no title), quote that; it is the CONFIRM path and goes on #2098 as a finding, not a pass.

**Web, #2097 again:** the three steps from this morning on the test repo. Expect step 1 `Created issue #N, "<title>", in <owner/repo>.` for a landed create; step 2 the duplicate ask and `Okay — nothing new was filed. #N stays as it is.` on `no`; step 3 after `yes` a second issue with its own, newer number named. On the PAT account (`web-pat-test`), one create: expect `GitHub's server doesn't offer that write for this connection, so nothing was created. Reconnect GitHub from Settings → Integrations (the GitHub sign-in carries the write tools; a token may not).` and nothing on GitHub (#2106's honesty half; the server-side half stays open).

Verified how (mine): the standing-grant checklist by hand (Tests success on the tested ancestor 1cb1e79dc1, no code path changed between it and staging, 12 of 12 workflows green, no migration between the shas, no deploy in flight, inside the window, slot 2 of 2), then alpha's /health. Layer: served sha only; the rows above are the check.
