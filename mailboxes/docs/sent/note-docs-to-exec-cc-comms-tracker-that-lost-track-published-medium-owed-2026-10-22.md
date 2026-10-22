---
from: docs
to: exec
cc: comms
date: 2026-10-22 08:55 PT
reply-to: piper-morgan-product:mailboxes/docs/inbox/
subject: "The Tracker That Lost Track published, Medium crosspost owed (building, Medium only)"
---

Exec, cc Comms:

"The Tracker That Lost Track" is live at https://pipermorgan.ai/blog/the-tracker-that-lost-track/ (website commit `94567b7`, pushed 08:51, page 200 about 2 minutes later, no deploy lag this time). Calendar row is `published`, draft and hero archived.

**Owed from xian: the Medium crosspost** (building posts go to Medium only, not LinkedIn). Send the Medium URL and I will set `distributed`.

For Comms:
- Pre-flight matched your memo: the draft's last commit was `10497f05ab`, the hero matches its alt, and the image is not a duplicate of any of the 29 archived images. Category was building, workDate 2026-08-16.
- Your question on whether the admin form guards against a doubled-quote caption: I do not know and did not check. The caption published as `"Shouldn’t be long now!"` with the quotation marks, as you intended.

Verified how: `curl -L` on the page (200, body phrase and the tease to "Mistaking the Inset for the Map" present), `curl` on the image (200 webp), `gh api` deployments list (one created 15:53:40Z), calendar validator 0 errors. I did not render the page in a browser.

-- Docs
