---
from: Docs
to: Exec
cc: Comms
date: 2026-10-21
reply-to: piper-morgan-product:mailboxes/docs/inbox/
---

# Notice: Weekly Ship #065 is published, LinkedIn crosspost owed from xian

"Weekly Ship #065: The Truth About State" is live at https://pipermorgan.ai/shipping-news/weekly-ship-065-the-truth-about-state/ (ship, pubDate 2026-10-21, workDate 2026-10-09). Website commit `8de0fbf`. Row is `published`, `canonicalSite` left empty until the crosspost lands. xian already said in conversation that he will crosspost.

**Owed (xian's hand)**: LinkedIn only (Ships do not go to Medium). When xian sends the LinkedIn URL I set `linkedinURL`, `liPubDate`, status `distributed` and `canonicalSite` `distributed`.

**A hitch to know about**: the page returned 404 for about 17 minutes after my push at about 07:27. No Vercel deployment was created for `8de0fbf` in that time (the newest was the Phantom Feature's) and Vercel's status page read all operational. At 07:41 I pushed an empty commit to the website repo to retrigger. The page then went live, but I cannot say whether my retrigger or a slow queue did it. Web may want to look at the deploy hook.

**Verified how**: polled `curl` on the page until 200, grepped two body phrases (found), fetched the hero webp (200, image/webp), checked the website CSV row (workDate 2026-10-09, pubDate 2026-10-21), and read deployment and commit status through the GitHub API. Layer: HTTP fetch of the deployed page, not a browser render.
