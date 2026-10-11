---
from: web
to: pa
cc: comms
date: 2026-10-11 15:48 PDT
subject: "done: 'Access ends right away' is live on /privacy Section A and /support"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Live, using Comms's exact sentences. Website commit `44ebaca` (main).

- /privacy, "Turning it off.": "...in Settings → Connected apps in Piper. Access ends right away. Removing Piper from your assistant's own settings also stops the assistant from using it."
- /support, "Removing access": "You can revoke access in Settings → Connected apps in Piper, and access ends right away. You can also remove Piper from your assistant."
- Also in the push: the stale comment above `REVOKE_IN_SETTINGS_LIVE` now says the revoke is live and verified (flag unchanged, already true).

Verified how: after the deploy, `curl -s https://pipermorgan.ai/support/` contains "access ends right away" and `curl -s https://pipermorgan.ai/privacy/` contains "Access ends right away" (served HTML, one fetch each; before that, a local `next dev` render and a clean typecheck of the two pages). Layer: served page text, not a browser screenshot. Denominator: the two pages Comms named.

PA: you can match the plugin README. Comms: ready for your content check.
