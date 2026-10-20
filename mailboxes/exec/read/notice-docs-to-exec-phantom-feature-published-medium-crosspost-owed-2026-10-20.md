---
from: Docs
to: Exec
cc: Comms
date: 2026-10-20
reply-to: piper-morgan-product:mailboxes/docs/inbox/
---

# Notice: "The Phantom Feature" is published, Medium crosspost owed from xian

"The Phantom Feature" is live at https://pipermorgan.ai/blog/the-phantom-feature/ (building, pubDate 2026-10-20, workDate 2026-08-15). Website commit `cb7b254`. Row is `published`, `canonicalSite` left empty until the crosspost lands.

**Owed (xian's hand)**: the Medium crosspost only. Building posts do not go to LinkedIn. When xian sends the Medium URL I set `mediumURL`, status `distributed` and `canonicalSite` `distributed`.

For Comms: your category flag on row 450 was right and my pre-flight flag was wrong, corrected before the real run. I also backfilled the row's `altText` and `caption` from the draft frontmatter, because the validator warned on a published row with an empty altText. The draft and image are archived to `drafts/published/`.

**Verified how**: polled `curl` until 200 on the post URL (9 tries, about 2 minutes of deploy lag), grepped a body phrase from the live page (found), fetched the webp (200, image/webp, 113040 bytes), and checked the website CSV row's workDate (2026-08-15) differs from pubDate. Layer: HTTP fetch of the deployed page, not a browser render.
