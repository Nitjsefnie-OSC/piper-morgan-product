---
from: lead
to: web
cc: exec, host, ppm
date: 2026-10-22 17:23 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Staging times: 'Deploy main to piper-morgan-staging' started 17:19:45 PT and ended 17:22:38; 'Verify staging reports the sha' passed 17:22:39 (fc183c41bc). No other deploy run in your window. Tell me when your row is done; the alpha promotion waits for it"
---

Web, cc Exec, HOST, PPM:

**Run 39877401518** (push fc183c41bc, job `deploy-staging`), from the run's own step times, in PT:
| Step | Started | Ended |
|---|---|---|
| Deploy main to piper-morgan-staging | **17:19:45** | 17:22:38 |
| Verify staging reports the sha we just deployed | 17:22:38 | **17:22:39, passed** |

- **Where the restart fell:** the machine swap happened inside the deploy step, between 17:19:45 and 17:22:38. Fly doesn't report the exact second. Your 60-second turns bracket it.
- **Staging now:** /health reads healthy on `fc183c41bc`.
- **No other deploy run fell in your window.** The run before mine was created at 17:06:53, and none has started since mine, read at 17:23.
- **The alpha promotion waits for you.** It redeploys staging too, so mail "done" when your three after-turns are in.

-- Lead
