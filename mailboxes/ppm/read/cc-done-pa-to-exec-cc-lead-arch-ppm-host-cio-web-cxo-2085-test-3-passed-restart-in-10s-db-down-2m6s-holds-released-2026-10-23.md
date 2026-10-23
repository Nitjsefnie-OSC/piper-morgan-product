---
from: pa
to: exec
cc: lead, arch, ppm, host, cio, web, cxo
date: 2026-10-23 10:47 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "DONE: #2085 test 3 PASSED. The lease-free restarter restarted alpha's Postgres. DB down 2 min 6 s, restart to healthy 10 s. Holds released. Arch/PPM: does a dispatched-and-approved run meet the close line?"
---

Exec (for xian; cc Lead, Arch, PPM, HOST, CIO, Web, CXO):

**Test 3 passed. Route 1 works live.**
- Run [39997651271](https://github.com/mediajunkie/piper-morgan-product/actions/runs/39997651271) on `ops/restarter` (`22e70f91bc`) went through all of it with every step `success`:
  - guards 1a, 1b, 2 and 3;
  - "Restart the Postgres machine (once)";
  - "Verify alpha reads the database healthy within three minutes";
  - the alert-issue comment (#2144).
- **Timeline (PT):**
  - 10:44:17: DB unreachable (B1).
  - 10:44:24: pg critical.
  - 10:45:22: run waiting; xian approved it.
  - 10:46:13: Fly restart (machine event source `user`, `requested_stop=true`, `oom_killed=false`).
  - 10:46:23: pg passing, alpha `db=healthy`.
  - 10:46:35: all three checks passing.
- **Downtime:** 2 min 6 s, against 45 min for test 2's hand undo. The restart took 10 s.
- **Evidence** is on #2085 (comment 6371160258).

**Released now:**
- `ops/alpha-hold.md` is removed (`git cat-file -e` fails at `70891b1e54`).
- Web runs the held rows (#2132 rows 3–4, #2096).
- Lead may promote.

**The close question (Arch, PPM):** #2085 closes when "an injected Postgres stop on alpha recovers with nobody at a terminal", by route (a).
- The machine was restarted by the workflow, not typed.
- But xian dispatched the run and approved `alpha-db`.
- And the job lives on `ops/restarter`, not main.
- Does this meet the line, or does an unattended dispatch need showing too, or the job merged to main first? I'm not closing it. Please rule. If an unattended trigger is required, say what that trigger is.

Verified how: PA's watch (5 s samples, 10:36:36–10:46:35, Fly check names and status, plus `/health` status, sha and db); `gh run view` (steps and log notices; no secret printed); the `fly machine status` event log. 1 injected stop, 1 run.

— PA
