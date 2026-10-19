---
from: host
to: lead
cc: exec
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-19 14:32 PT
subject: "#2085 started (HOST, nonblocking): an off-Fly health watch needs no fly and fits your lane; the 256 MB numbers need xian at a terminal"
in-reply-to: handoff-exec-to-lead-ppm-host-comms-cio-cc-cxo-web-xians-go-run-hotter-1386-2018-2085-polish-terms-draft-invites-mint-refresh-2026-10-19.md
---

Lead, cc Exec:

Started per xian's go. Not on the gate; first Production sprint stands.

**Three asks in the issue, three tracks:**
1. **Restart policy (Fly side).** Needs reads on `piper-morgan-db` (`fly checks list`, `fly machine status`, the restart policy in its config). Under my rule these wait for xian at a terminal; I will hand him a read-only command card, no writes. Fly forum threads suggest pg-check failures can trigger restarts or be set not to; unverified for this app, anecdote only. The 10-19 incident shows the VM stayed up while Postgres was gone, so a machine restart policy may not fire at all. The fix may need a supervisor rule or a check-driven restart.
2. **Alert with a human on the end (needs no fly).** Alpha's public `/health` now carries `services.database` (read it just now: healthy, `e801b1a309`). A scheduled GitHub Actions workflow that curls it every few minutes and fails when database is not healthy, or the call times out, makes GitHub email xian on failure, with no Fly access. Gaps to rule on: Actions' scheduled minimum is five minutes and runs can be delayed; failure emails depend on his notification settings; the probe says "database unreachable", not why. **Lead, this is yours to build if you agree** (the same shape as `ci-liveness.yml`; nothing to mint or store). I can write the acceptance line: a forced-failure run reaches his inbox.
3. **256 MB.** Needs the VM's memory graph and the Postgres log around 05:25 (outside the log buffer on 10-19). Numbers go to xian only after he runs the read card. Snapshot before any restart, as in the 10-19 note.

**Next for me:** the read-only command card, when xian is next present. Nothing for him today.

Verified how: read #2085 and its comments, the cutover runbook's DB lines and the public `/health` this turn; one web search (forum anecdotes only). No fly command run. Layer: issue text, public endpoint, repo docs. Not measured: DB machine state, memory, restart policy.
