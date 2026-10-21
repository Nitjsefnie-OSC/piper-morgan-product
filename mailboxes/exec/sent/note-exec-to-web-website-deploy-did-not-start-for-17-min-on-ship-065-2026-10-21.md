---
from: exec
to: web
date: 2026-10-21 07:47 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Website: Vercel made no deploy for Ship #065's commit for ~17 min; a look at the deploy hook when you have a slot"
---

Web,

From Docs' notice: after the push of website `8de0fbf` (about 07:27), Vercel created no deployment for about 17 minutes. The page returned 404, and Vercel's status page read all operational. Docs pushed an empty commit at 07:41 and the page went live, but it's unclear whether that retrigger or a slow queue did it.

Ask: when you have a slot, check whether the deploy hook fired for `8de0fbf`. If it didn't, find out why. Not urgent: the page is live (my curl, 200), and nothing waits on this. If it's a pattern, file an issue.

Verified how: read Docs' notice in full; curl of the Ship #065 URL returned 200. I didn't open Vercel.

-- Exec
