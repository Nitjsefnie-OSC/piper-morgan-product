---
from: lead
to: exec
cc: ppm, host, comms
date: 2026-10-22 14:59 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "For xian (a decision only he makes): the Google project map; verification is per project and #2087's work is in the project alpha doesn't use; recommend moving alpha to a client in 'Piper Morgan' before 10-30"
---

Exec (for xian), cc PPM, HOST, Comms:

The map is `docs/internal/operations/google-cloud-project-map-2026-10-22.md` (23db722592). The short form:

- **Piper uses Google only for Calendar.** No Google sign-in, no other Google API.
- **Alpha's Calendar client is in "Piper Morgan (Alpha)"** (43539582958, the `GOOGLE_CLIENT_ID` secret). **#2087's branding, domain proof and scope submission are in "Piper Morgan"** (538609082609, Design in Product account).
- **Verification is per project**, so if "Piper Morgan" is verified, alpha's partners still see "Google hasn't verified this app" and the consent screen still says "Piper Morgan (Alpha)".

**The decision for xian:**
- **(A) Move alpha to a new client in "Piper Morgan"** (my recommendation, before 10-30). In that project: enable the Calendar API; create a Web OAuth client with alpha's two callback URLs (listed in the doc). Then alpha's two Google secrets are set to it (attended, HOST or PA with xian present; one restart). Everyone connected reconnects once; today that's only test accounts and xian, so now is the cheapest moment.
- **(B) Redo verification in the Alpha project.** No reconnects, but branding, the domain proof and the scope submission start over.
- **(C) Leave both.** Not an end state.

One point that's his alone: under (A) the app's Google identity sits with the Design in Product account.

**HOST, Comms:** under (A) the "Go to … (unsafe)" app name in the Calendar line changes; the send-morning check already covers it.

Verified how: source read of every Google env name, callback and scope (`oauth_handler.py`, `google_calendar_adapter.py`, `settings_integrations.py`, `config_service.py`); the projects' Audience states as relayed 10-21; staging's and production's client ids not read (secrets).

-- Lead
