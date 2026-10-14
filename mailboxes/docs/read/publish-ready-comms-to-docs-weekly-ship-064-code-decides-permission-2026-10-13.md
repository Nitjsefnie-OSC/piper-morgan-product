---
from: comms
to: docs
date: 2026-10-13
subject: "PUBLISH-READY: Weekly Ship #064 'Code Decides Permission' (Wed 10-14)"
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

# PUBLISH-READY: Weekly Ship #064, "Code Decides Permission"

- **Draft**: `docs/public/comms/drafts/weekly-ship-064-draft-2026-10-12.md` (final at `84cb38ac74`)
- **Calendar row**: renamed to the full title "Weekly Ship #064: Code Decides Permission", `ready-for-docs`, window 10-02..10-08, pubDate **Wed 2026-10-14**, theme ship
- **Frontmatter**: `piper-ship.png`, standard alt, empty caption (Ship convention, as #063)
- **In-post image**: the elephant-on-a-scale from "Three Failures Inspire One Law", under "Published this week". `https://pipermorgan.ai/assets/blog-images/three-failures-inspire-one-law.webp` returns 200. Alt and caption are verbatim from that post.

## Review
Exec drafted it 10-12. xian edited it 10-13 in the admin UI, then asked Comms for an editorial review. Changes, all with xian's OK:
1. xian's two inline notes resolved: the ChatGPT/Claude connection item rewritten in plain language, and the CI item now answers "green by Thursday night?" (yes: Architecture Enforcement failed again Wed 18:44 PT, was caught at the next check and fixed, then passed 10 of 10 runs through Thursday).
2. Facts: beta gate 31 → 14 (bullet now matches the paragraph); dropped an unsupported "acceptable limit" for the pattern count; default-repo line restated; Blockers updated, since the four privacy decisions were answered 10-13.
3. Typos (an unclosed quote, an unclosed parenthesis, "escaped", "OAuth", "so", "give off", "scaffold").
4. A jargon pass at xian's request (router, promotion, deletion lanes, resolver, hook, ledger row and others).
5. Six trims.

**Audit (Ship calibration)**:
- 0 semicolons. 0 cohort/CoS/load-bearing/honest. 0 brackets.
- Title case. Sentence-case headings. Metrics as bullets. Phase tag present.
- Previous-Ship link (#063 "Check Before You Leap") returns 200.
- #11: 6 matches, all PASS (5 are users, 1 a generic "anyone").
- Numbers: 29 closed / 46 filed, recounted.
- 1,959 words (#063 1,450, typical about 1,630). xian accepted the length after the trims.

Syndication: ship → LinkedIn only.

Verified how: the audit greps and the frontmatter parse ran on the final file this session. `curl -sL` returned 200 on all 8 URLs in the post. Issues were recounted with `gh api search/issues` over the Pacific-bounded window (UTC 2026-10-02T07:00Z..10-09T07:00Z): 29 closed, 46 created. External list: 5 of 5 match the calendar (checked 10-12, list unchanged since). Layer: file text and HTTP status, not a render.
