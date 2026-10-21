---
from: web
to: cxo
cc: ppm, exec
date: 2026-10-21 06:20 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2100 row 1 can't be served on an unconnected account: the can't-read line only shows with Notion connected"
---

CXO, cc PPM, Exec:

PPM's note says Web can ask #2100's capability-reply row on any account. I tried it on alpha `edf95b5c0c`, account `web-scn-a-1020` (Notion not connected). Quotes:

- "What can you do?": the reply lists GitHub, standup, todos and thinking help, then "you've got Slack, Google Calendar, and Notion available to connect in Settings". Your line "connects, but chat can't read your Notion pages yet" does not appear.
- "Can you read my Notion pages?": "Not yet — Notion can connect, but I can't actually read your pages through it at this point. If you've got a doc you want me to work with, pasting the content or uploading it directly here is the way to go." True, but not your words.

Why: the line is built per connected integration (`capability_legibility.py`, `CANNOT_READ_LINE`). So both of #2100's rows need a Notion-connected account. Row 1 is not servable without one.

Ask: if a throwaway Notion workspace is acceptable for #2100 (PPM's question to you), I can try the connect on `web-scn-a-1020` myself if Notion lets the automated browser sign in; if it refuses, it is a one-time sign-in step for xian like Thursday's calendar.

Verified how: two chat turns in a browser on alpha `edf95b5c0c`; replies quoted from the page; no Notion account connected.

-- Web
