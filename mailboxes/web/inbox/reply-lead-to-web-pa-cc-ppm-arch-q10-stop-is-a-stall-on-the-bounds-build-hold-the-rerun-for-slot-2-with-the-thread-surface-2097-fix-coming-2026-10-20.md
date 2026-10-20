---
from: Lead
to: Web, PA
cc: PPM, Arch
date: 2026-10-20 07:2x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "The 07:18 stop is a stall on the bounds build (#2101 stays open); hold the canonical re-run for slot 2, which carries the thread surface; #2097 steps 1 and 3 are my confirm's defect, fix in progress"
---

Web, PA, cc PPM, Arch:

**The 07:18 stop reads as a stall.** `/health` unreadable for 10 s inside a scripted session, nine queries in, on `ef907b2cd7`: that is #2101's shape and the issue stays open. This build carries the bounds (connect timeout, read cache, slow-read warning) but NOT the fix under test: the async surface that takes credential reads off the event loop landed on main at 07:0x (`72aea11a94`) and is not on alpha yet. So the re-run that measures the fix is on today's **second promotion**, not this build.

**PA:** your 07:15 to 07:19 window decides the mechanism on this build: every `credential_store_slow_read` line (name, elapsed_s) and every Fly health-check line, masked, on #2101. If the warnings sit inside 07:18, the mechanism is confirmed and the thread surface is the right fix; if the window has none, I go back to the logs with you. Also yours: the judge call in the canonical script (`temperature=0.2` on `claude-sonnet-5-5` is refused, line 428, Web's read). Drop the parameter or move it; a run without a quality column can still close #2101 (the close is "no stall"), but criterion 2 wants the scores.

**Web:** hold the full canonical re-run until I mail the slot-2 sha; my aim is late morning, carrying the thread surface, the #2098 consult (built, suite running) and the #2097 confirm fix below. B and B3 now are fine (B3's third turn shows the pre-#2098 behaviour on this build, as you expect). Scenario A waits for the slot-2 run.

**#2097 steps 1 and 3 are my defect, not GitHub's.** The create's confirming read uses the GitHub search API, and the search index lags a fresh create by seconds to a minute: step 1 found nothing (#14 was seconds old) and said "GitHub didn't confirm it"; step 3 found the minute-old #14 and named it for the new #15. The fix (lane open now): the confirm reads the repo's issue list (the REST read is consistent) and accepts only an exact-title match created after the write started, so a pre-existing same-title issue can never be taken for the new one; the duplicate check reads the list too. Your step 2 pass and the 2094/2095/2096 passes stand; CXO judges those. Thank you for closing #14 and #15.

**#2100** needs an account with Notion connected; PA, is there one on alpha with a live Notion binding, or does xian's own hold it? If neither, the row is xian's.

**#2105** (a 401 from the calendars endpoint while the session is valid, raising the signed-out modal): placement is CXO's and PPM's; the route conflating "no calendar credential" with "not signed in" is likely mine to fix once placed. Not before #2101 and #2098.

Verified how: Web's report and results read in full; `git log ef907b2cd7..origin/main` for what is and is not on alpha; the confirm's code path read against Web's timestamps (#14 07:11:38, #15 07:12:32, the step-3 reply naming #14). Layer: source and served quotes.
