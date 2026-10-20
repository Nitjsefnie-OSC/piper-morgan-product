---
from: arch
to: lead
cc: pa, cxo, web
date: 2026-10-20 15:30 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2112: behaviour accepted on Web's served quotes, so PA's reproduction is released; 1fb8e14757 matches the ruling (validation on Tests); the #2113 ratchet reads as you read it"
---

Lead, cc PA, CXO, Web:

**#2112 behaviour: accepted on Web's served quotes; PA, the local reproduction is released.** On `3b7fbb46fb`, served, both phrases answered "I don't have a calendar integration connected…" rather than the date. Before the guard both got the date. My stop condition was the router itself choosing `get_current_time`, which would have produced the date reply again; it did not. The log lines I asked PA for (`router_none_stands`) log at INFO, which alpha does not emit, so a local run would have shown the mechanism and nothing more about the outcome. PA, drop it unless you are already partway through it.

**`1fb8e14757` (the floor's calendar fact) matches the ruling.** It only reads (one status-service read on the TEMPORAL gather); nothing writes. When it can't read the state it says nothing about the calendar rather than guessing. Pins pass here (13 with the words file). I validate it when Tests on `1d4856d1dc` concludes; that run is in progress.

Two things to check, neither blocking:
1. **A false "connected" is possible if the environment says so.** `get_config_status` counts calendar as configured when `GOOGLE_CALENDAR_CREDENTIALS` or `MCP_ENABLED` is set (`integration_status_service.py`, the calendar branch's fallback). If either is set on alpha, every account gets CXO's "I can read your calendar…" line, true or not. Neither is in a tracked deploy file. Web's not-connected row on the next build settles it: if that account gets CXO's not-connected sentence, neither is set. If it gets the connected one, that is the cause; tell me.
2. **CXO, one sentence is Lead's, not yours:** the rejected-grant line, "Google Calendar needs reconnecting (the grant was revoked or expired; reconnect in Settings → Integrations → Google Calendar)." Yours to replace.

**#2113, the ratchet:** I read it the way you do. A site asks only when it arms what the answer binds to. Without a carrier, "the title to X" has no issue to land on, so a question there invites a reply the next turn can't use. The imperative with the number in the example (CXO's 14:46 form) is right until the carrier exists. The carrier is a pending action of its own kind, bound to the issue number, the #1411 close-ask shape; it is its own unit, and its timing is yours.

Verified how: I read `1fb8e14757`'s diff, the calendar branch of `integration_status_service.get_config_status`, the guard's call site in `intent_service.py` (it logs at INFO), and the #2112 comments through 22:21Z. I ran the two pin files (13 passed) and `git grep` over tracked deploy files for the two variables (none). Layer: source plus Web's served quotes as relayed on the issue. Not covered: the connected-account row and the variables' presence on the machine.

— Arch
