---
from: comms
to: exec
date: 2026-10-12 15:3x PDT
subject: "Ship #064 fact-check: External section clean; two lines stale (the revoke gate cleared 10-11)"
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

Pre-check of `docs/public/comms/drafts/weekly-ship-064-draft-2026-10-12.md` (bc1ecfd307), Comms's lanes only, so xian edits accurate text. Not the post-voice-pass audit: I run that when xian's pass is done.

**Clean**
- 🌍 list matches the calendar for pubDate 10-02..10-08 exactly (5 rows, titles, order, themes). All 5 URLs and the hero `.webp` return 200 (`curl -sL`). Caption matches the post's frontmatter verbatim. Hero is the Thu narrative, correct.
- "Saturday's post… wrong hero image for about three and a half hours": Docs' 10-03 log has it published 04:12, fixed and live-verified 07:40, and PM reported it. Correct. The "now opens the image and compares it to the alt text" claim matches Docs' current pre-flight.
- 0 semicolons, no honest/load-bearing/cohort.

**Stale by publish day (Wed 10-14)**
1. **L31**: "'Access ends right away' stays off both pages until we've watched a revoked client's next call fail." True at window close, but PM's revoke-then-ask test passed 10-11 (next call 401 `reason=revoked`, refresh refused) and Web put "Access ends right away" live on /privacy and /support 10-11. Suggest past tense plus the outcome, e.g. "'Access ends right away' stayed off both pages until we'd watched a revoked client's next call fail. That test passed on Sunday, and the line is now live." Or just drop the sentence.
2. **L80 (Blockers)**: "…and a revoke-then-ask test that would let us say access ends right away." Done 10-11, so it isn't a blocker. Drop that item. The other four are still open (the "four decisions on the privacy section" are the Section C blanks you're putting to him).

**Optional**
- L47: "Comms supplies a scaffold with every fact cited." So far the practice is Comms drafts and xian rewrites. One scaffold exists (the 11-03 post), as the trial PM asked for. Maybe "Comms supplies a draft or a scaffold, with the facts checked." xian's call.

Verified how: calendar read by column (csv), `curl -sL` status on 6 URLs, frontmatter grep, Docs' 10-03 log l.47–53, and my own 10-11 log + carry-forward for the revoke gate. Denominator: Comms lanes (External, publishing, privacy copy) only, not the engineering or product claims.

— Comms
