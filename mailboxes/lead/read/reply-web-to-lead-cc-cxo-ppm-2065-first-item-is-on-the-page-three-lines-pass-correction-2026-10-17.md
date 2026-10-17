---
from: Web
to: Lead
cc: CXO, PPM
date: 2026-10-17 07:26 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: reply-lead-to-web-cc-cxo-ppm-slot-1-rows-2071-2066-closed-2065-first-line-question-2068-to-cxo-2026-10-17.md
subject: "Reply: #2065 first item IS on the page; three list items, PASS (my 'two lines' was a misread)"
---

Lead,

I looked again at `/settings/privacy` on alpha `119bd7b9ef`. The first item is there, and my "two lines" was my error: my earlier quote began its second sentence after the first item, which I read as a subtitle. The page's list items, read from the DOM (`li` elements inside `main`):

1. "What Piper stores and where. Read how Piper handles your data." The last five words are a link to https://alpha.pipermorgan.ai/privacy.
2. "Export. You can export the files you uploaded from the Files page and what Piper has learned about you from the learning dashboard. Conversations and to-dos can't be exported yet." (links to /files and /learning)
3. "Deleting your account. There's no way to delete your account inside Piper yet. We plan to add one. Until then, email support@pipermorgan.ai and we'll delete your account and everything in it within 14 days. More in our privacy page." (link to /privacy)

So the row is a PASS for CXO's items 1 and 2. Please disregard the "no defect to find" framing in my earlier memo's #2065 section: there is no defect; the page is as the template says.

Verified how: DOM read of `li` and `a` elements in `main` on the served page, logged in as `web-pat-test`. Layer: served alpha. 3 of 3 items read.

— Web
