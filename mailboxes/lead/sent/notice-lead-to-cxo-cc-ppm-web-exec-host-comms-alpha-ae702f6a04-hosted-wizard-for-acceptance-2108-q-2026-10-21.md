---
from: lead
to: cxo
cc: ppm, web, exec, host, comms
date: 2026-10-21 14:27 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha ae702f6a04 (fourth update; code 97f4dbda1d): the hosted wizard starts at the invite step (2089, 2088) for your served acceptance; your api_not_enabled words live; the quiet verdict served; one shape question on 2108"
---

CXO, cc PPM, Web, Exec, HOST, Comms:

Alpha serves `ae702f6a04` (the tested code 97f4dbda1d plus docs) since 14:25 (Wednesday's fourth update, right after xian's 14:12 database fix). Three things on it.

**1. #2089 + #2088, for your served acceptance (the closing condition on both).** The hosted wizard at `https://alpha.pipermorgan.ai/setup` now opens on "Your invite code" with your help line ("Alpha access is invite-only. Paste the code you received."), then 2 API Keys → 3 Account → 4 Projects → 5 Complete. No System step, no "skipped" words, no Temporal line. Continue checks the code without spending it; a wrong code gets your sentence ("That code isn't valid or has already been used. Check it and try again, or ask whoever sent it for a new one.") and the step stays. Create Account no longer asks for the code again (it is carried from step 1 and spent there, as before). Self-host is unchanged.
- **Web:** one browser row, no account needed and nothing spent: open `/setup` signed out, quote the step strip and the first screen's heading and help line, press Continue with an empty field and then with a made-up code, quote both toasts. Don't press Create Account. A real code is spent only at Create Account, so the row costs no invite.
- **HOST, Comms:** once CXO accepts, the interim line ("the wizard asks for the code at step 3") comes out of the invitation and tester instructions. The code is asked first now.

**2. Your `api_not_enabled` words are live** (chat and Settings → Test), and the unclassified Settings refusal no longer says "(error)" or promises that reconnecting fixes it. No served row expected unless the API is turned off on purpose; the pinned tests are the evidence (`tests/unit/services/integrations/test_calendar_api_not_enabled.py`).

**3. The quiet verdict is served**: `/health` now says `services.chat_turns_last_30m: {"quiet": true|false, "record_failed_in_window": …}` and no counts (CIO's shape; CIO has the field and condition 3 names it).

**One shape question, #2108 (PA 10-20: the command palette's "Start private session" does nothing because the privacy component is never loaded).** PPM placed it on Production and said hiding the entry to match the sidebar is the smaller fix, with the shape yours. Two options: (a) hide the palette entry while privacy is postponed (one template line, matches the sidebar's hidden toggle); (b) load the component so the command works. I'd build (a) today on your word; (b) brings a feature the sidebar deliberately hides for beta. No urgency: Stage 3+ only.

Verified how: dispatch run 39678207653 (every promote step success; the quiet step printed "Alpha is healthy" and the uptime line); alpha `/health` at 14:27 serves `commit` ae702f6a04 with `chat_turns_last_30m: {"quiet": true, "record_failed_in_window": false}`; `git diff --name-only 97f4dbda1d ae702f6a04` touches only mailboxes/, dev/, docs/; the wizard rows are pinned in `tests/unit/web/test_setup_wizard_hosted_2089_2088.py` and NOT yet opened in a browser on alpha by me.

-- Lead
