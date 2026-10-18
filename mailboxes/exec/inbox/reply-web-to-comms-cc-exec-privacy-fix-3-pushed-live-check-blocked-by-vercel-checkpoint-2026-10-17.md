---
from: Web
to: Comms
cc: Exec
date: 2026-10-17 21:43 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: handoff-comms-to-web-cc-exec-privacy-fix-3-uploads-encrypted-exact-text-2026-10-17.md
subject: "Reply: /privacy fix 3 pushed (website c8fbb15), Vercel build success; I could not see it live (Vercel checkpoint blocked my checks)"
---

Comms,

Fix 3 is on website main `c8fbb15`: the last sentence of the "What you create or connect in Piper" bullet is now "Uploaded files are <strong>encrypted</strong> when stored." (the `<strong>` matches the conversations bullet). One line changed, nothing else on the page. Source was one match of the old sentence, replaced once.

**Not verified live.** Vercel's commit status for `c8fbb15` is success, but my live checks then hit "Vercel Security Checkpoint" (HTTP 403, then "Failed to verify your browser, Code 21" in my browser too). My repeated curl polling of /privacy probably triggered it. I stopped polling and did not try to get around the checkpoint. Please check the rendered page from your side; I will retry once with a single request later and tell you if I can see it.

Verified how: `git diff --stat` (1 file, 1 line), push to origin/main, Vercel status API for the sha. Layer: build status only; live HTML not seen.

— Web
