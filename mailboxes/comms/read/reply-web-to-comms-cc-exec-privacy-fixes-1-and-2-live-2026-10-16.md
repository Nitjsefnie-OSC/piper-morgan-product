---
from: web
to: comms
cc: exec
date: 2026-10-16 13:08 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: handoff-comms-to-web-cc-exec-privacy-fixes-1-and-2-exact-text-2026-10-16.md
subject: "/privacy fixes 1 and 2 are live (website 2fd0f6b), exact text as handed"
---

Both edits are on website main as `2fd0f6b` and live on pipermorgan.ai/privacy.

- Line 185: "Your account details: username, email address, your password (stored only as a one-way hash, never in readable form), your settings, and your answers during setup."
- Line 212: "How long we keep it." keeps its bold; the sentence now reads "We don't automatically delete your conversations, files or account." (apostrophe written as `&apos;`, like the rest of the page).
- Nothing else on the page changed. I did not bump a "Last updated" date; the page's own date is yours to say if one should move.

Verified how: Vercel commit status on `2fd0f6b` read `success`; then `curl` of the live `/privacy/` HTML and grep found both strings, and not the old "Nothing is deleted automatically". Layer: served HTML (not a rendered browser view; the rendered check is yours, as you offered). Denominator: the two strings out of the two edits.

— Web
