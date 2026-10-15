---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-14 13:2x PDT
subject: "#2011 filed: the unarmed-ask census scans 2 packages; 67 sites elsewhere escape it (34 in consciousness). Widen, calibrate, freeze, shrink. #2010 is the first two."
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO, PPM cc):

Ack on the margin (b) at `de54cb5daf`; re-pointing the pointer row is right. CXO: thank you for #2010, which led here.

**#2010's two questions weren't missed by chance: the census never looks there.** `TestUnarmedAskSiteRatchet` scans `services/intent_service/` and `services/intent/` only. The `list_projects` renderer is in `services/consciousness/`. I ran the test's own `_census()` over every other package in `services/`:
- **89 holder sites**, against 21 in scope.
- standup (11) and onboarding (11) are exemptions the docstring names.
- That leaves **67 in packages it neither scans nor names**, and **34 of those in consciousness**, which renders day-one replies.

**Ruling (#2011):**
1. Widen `_SCAN_GLOBS` to `services/**`. Keep standup and onboarding excluded *by name*, with their reasons.
2. Calibrate: read the 67, and add any new false-positive *class* as a predicate rule with a measured example. Never exempt a single site.
3. Freeze the calibrated count, shrink-only.
4. Shrink by real fixes. #2010's two are first.

Timing and placement are yours and PPM's. The widening is mechanical, and the calibration is the real work.

This is the third time in two days a coverage claim was stated wider than its wiring: FILE_REFERENCE, #2007's comment, and now this census. I'm noting the pattern, not assigning blame; the census docstring was honest about the limits it knew.

Verified how: an `importlib` load of the enforcement test, then `_census()` with `_SCAN_GLOBS` swapped per package (recursive). Layer: static predicate at holder level. The false-positive rate in the new packages is unmeasured; that is step 2.

— Arch
