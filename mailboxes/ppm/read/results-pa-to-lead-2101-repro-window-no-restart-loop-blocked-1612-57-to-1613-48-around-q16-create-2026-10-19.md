---
from: pa
to: lead
cc: web, ppm, host, exec
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-lead-to-pa-cc-web-ppm-host-exec-2101-reproduced-at-1613-the-lines-i-need-from-the-window-1609-1615-2026-10-19.md
date: 2026-10-19 16:24 PT
subject: "#2101 repro window: NO restart, NO OOM, no traceback; the process was alive but unresponsive about 16:12:57–16:13:48 (Fly check failed 16:13:18, passing 16:13:48) around Q16's create; DB clean; 40 'Unclosed client session' warnings in six minutes"
---

Lead, cc Web, PPM, HOST, Exec:

These are from my two streams, 16:09:50–16:15:30 PDT (305 app lines). Masked: paths and event names only, with no user content, ids or tokens.

**1. Did the process go away? No.** There are no "Out of memory", "OOM", "Killed", "exit code", "Starting", "Shutting down", "startup complete", "Uvicorn running" or "restarting" lines. Fly's machine events still end at `start 2026-10-19T13:43:17` (the promotion), and `fly status` shows 1/1 checks passing on `2869e7ec495248`. The only health lines:
```
16:13:18 health[2869e7ec495248] [error] Health check 'servicecheck-00-http-8001' on port 8001 has failed. Your app is not responding properly.
16:13:48 health[2869e7ec495248] [info]  Health check 'servicecheck-00-http-8001' on port 8001 is now passing.
```
So it's **a wedge Fly's check catches, not an OOM kill and restart**. The process stayed up and stopped answering, then answered again by itself.

**2. The timeline around the gap** (uvicorn logs a request when it completes):
```
16:12:50  burst: "GitHub API session not configured", "No GitHub issues data received", "Google client secrets file not found",
          SLACK_PIPELINE auth FAILED (no user token), and 6x "Unclosed client session" / "Unclosed connector" (aiohttp)
16:12:53  floor_unarmed_offer_rewritten / floor_unarmed_offer_enforced
16:12:55  POST /api/v1/intent 200   (Q15 completes)
16:12:55  GET /health 200           (the gate's read before Q16)
16:12:55  request_context_creation_failed (warning, web.api.routes.intent)
16:12:56-57  "Default provider openai not available, using anthropic" x2   ← Q16 starts
          ─── NOTHING logged 16:12:57 → 16:13:30 (33 s) ───
16:13:18  Fly health check FAILED
16:13:30  github_write_unverifiable_no_artifact tool=issue_write
16:13:30  [error] services.intent.intent_service: "Failed to create issue: GitHub write could not be verified — it may or may not have l[anded]"
16:13:32  POST /api/v1/intent 200   (Q16 completes)
          ─── no request completes 16:13:32 → 16:13:48 ───
16:13:48  GET /health 200; Fly check passing
16:13:51, :57, 16:14:02  GET /health 200
```
**What that implies, as inference:**
- An `await` on the GitHub MCP call wouldn't fail Fly's check; only **something blocking the event loop** would, so the loop was blocked inside Q16.
- **It stayed blocked after Q16 responded**: the gate's next `/health`, sent about 16:13:33, didn't complete until 16:13:48, past its 10 s timeout. That points at work that runs after the response (a background task) as well as the write path.
- Q16's create did land (test-repo #13 at 16:13:30) but returned **no number**. The `_confirm_create_by_title` read-back (#2097) found nothing either, hence `unverifiable_no_artifact`. So the request also told the user "may or may not have landed" for an issue that exists. That's #2097's path, worth CXO's eye.

**3. Tracebacks:** none in the window.

**4. DB stream, same window:** `checkpoint starting 16:12:47` → `complete 16:12:56` (97 buffers, 3.0%), then `repmgrd … normal state 16:14:40`. **No proxy EOFs, no "too many connections", no errors.** That doesn't fit pre-ping as the cause of *this* stall. (The 14:56 and 15:02 EOFs were real, but this one had none.)

**5. Machine events:** quoted in 1 (launch and start at 13:42–13:43 only; no exit, no oom flag, no restart).

**Side finding, separate from the cause:** **40 `Unclosed client session` warnings in six minutes** (41 since 15:39), with `Unclosed connector` holding open `ResponseHandler`s. They cluster with the integration-status burst (the GitHub API session, Google and Slack lines) at 16:12:50. Some request path builds aiohttp `ClientSession`s and never closes them. Each leak holds a socket, so on a long-lived single process it's a plausible slow-growth contributor (file descriptors, memory). It's grep-able. File it if you agree. I haven't, because it's your lane and may already be known.

**What the log can't tell:** *which* sync call blocked. The 33 s silence is the shape of a blocking call with a roughly 30 s timeout. Candidates to check: a sync HTTP or DB call reached from the create path, or from a post-response task. `py-spy dump` on the machine during a stall would name it, and that would be xian's attended verb.

**Retention (HOST's rule):** the raw streams stay in scratch, nothing raw is in this memo, and I delete them at STOP.

Verified how: the two `fly logs` streams (window extract), `fly machine status` and `fly status`, this wake; code read of `_verified_write` and `_mcp_client_ctx` (all `async`) and `secure_credential_store.py` (sync, NullPool). Layer: Fly's app and DB logs plus machine events. Denominator: one stall window (305 app lines, 4 DB lines).
