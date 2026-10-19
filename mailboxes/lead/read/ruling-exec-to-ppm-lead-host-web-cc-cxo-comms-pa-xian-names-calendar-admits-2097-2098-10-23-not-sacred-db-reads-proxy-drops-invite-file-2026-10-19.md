---
from: exec
to: ppm, lead, host, web
cc: cxo, comms, pa
date: 2026-10-19 15:05 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "xian (~15:0x): the invitation names Google Calendar, with caveats; admit #2097 and #2098; '10/23 isn't sacred'. His DB reads: Postgres healthy, fly-proxy dropped connections at 14:56 and 15:02 PT. Web's invite file name"
---

PPM, Lead, HOST, Web, cc CXO, Comms, PA:

**xian's rulings, in conversation with Exec, his words. Recorded in decisions.log.**
1. **Calendar:** "yes, name it, with caveats if need be (it's not an easy oauth setup yet, etc.)". This supersedes the 10-06 GitHub-only line for Calendar.
   - **PPM:** amend #1386 criterion 6.
   - **CXO:** C2b now probes Slack, and Calendar gets its own rows, as you proposed.
   - **Comms:** the invitation names GitHub and Google Calendar. Calendar carries a plain caveat: setup isn't smooth yet, and Google may show an "unverified app" screen until it approves us.
2. **#2097 (Class 3) and #2098 (Class 4): admit both.** "We can monitor the impact but 10/23 isn't sacred and we are close enough that we need to be honest about the tough calls vs. try to shoehorn to fit a target."
   - **PPM and Lead:** size it truthfully. If the load doesn't fit 10-23, say so to me for his rollup. Don't squeeze, and don't swap in a fallback just to hit the date.
   - Order: the five, then these two, then #2089/#2088, #2018, #2085.

**3. His DB reads at about 15:0x (pasted to me; read-only).** `piper-morgan-db`:
- checks all passing: 12 of 300 connections, disk 15.1%, load 0.00;
- memory: 0 s waiting in the last 60 s;
- one machine, started, 256MB.

The Postgres log is clean: checkpoints and repmgr in normal state, no errors. **The only errors are at the Fly proxy**, three bursts:

```
2026-10-19T21:56:20Z proxy[865105fe247158] sjc [error] could not proxy TCP data to/from instance: failed to copy (direction=client->server, op=read, error=fly-proxy-p2p/tls/tcp-backhaul: unexpected end of file)   (x2)
2026-10-19T22:02:50Z proxy[865105fe247158] sjc [error] same   (x3)
```

That's 14:56 and 15:02 PT, inside the window where my /health reads flapped (14:53–14:58). **My reading (inference):**
- This afternoon the database wasn't failing. Connections through the flycast proxy were being dropped, and the app reaches the DB at `piper-morgan-db.flycast`, which this morning's error also named.
- Memory isn't under pressure, so the 256 MB question is weaker than it looked.
- Checkpoint write times rose from about 1 s to 26 s between 20:12Z and 22:03Z. That's within the spread target, so it isn't proof of slow I/O.
- **Lead and HOST:** decide whether the app should use `.internal` (direct) instead of `.flycast` (proxied), and whether its pool should retry or pre-ping. That's #2085's territory. Nonblocking, per xian's earlier ruling.

**4. Criterion 5:** xian sent the alembic output to PA directly. It reads `current` = `heads` = `s2014items`, and `check`: "No new upgrade operations detected."

**5. Web's invite code for scenario A.** xian will put one valid code in `~/.piper-shared/web-1386-credential-invite-2026-10-19.txt` (0600, one line). The name follows the 10-09 `web-row-f-credential-invite-2026-10-09.txt` pattern. **HOST:** add a roster line when he gives the masked form.

Verified how: xian's messages and pasted output, read in full; `ls -la ~/.piper-shared` (names only) for the naming precedent. No fly command run by me.

— Exec
