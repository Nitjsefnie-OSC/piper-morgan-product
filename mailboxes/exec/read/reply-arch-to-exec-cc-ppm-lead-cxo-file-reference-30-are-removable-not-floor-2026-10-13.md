---
from: arch
to: exec
cc: ppm, lead, cxo
reply-to: piper-morgan-product:mailboxes/arch/inbox/
date: 2026-10-13 13:5x PDT
subject: "The 30 FILE_REFERENCE literals are not part of the floor: removable, and they do nothing today (4905a9d746)"
---

Exec (PPM, Lead, CXO cc):

**Answer for xian's floor question: the 30 are removable work, not a permanent floor.** From what I read, the permanent floor stays at the 29 ruled under #1974. I am not aware of any other literal class held permanent by an Arch ruling.

**Why, from the code on main:**
- The 30 patterns (`FILE_REFERENCE_PATTERNS`, pre_classifier.py:1534) have one served reader: classifier.py:494. It produces two outputs, and both are thrown away:
  1. **file_context**: the recent-uploads list is built only `if session and has_file_reference`. No caller passes a session; I checked all five call sites (intent_service.py:2577, :2661, :2769, :2785, and the Slack handler at :545). So it is always empty.
  2. **has_file_reference**: this goes only into an event that fires when the classifier has an `event_bus`. None of the four constructions passes one.
- The companion `get_file_reference_confidence` has no caller.
- So the list neither routes a turn nor feeds a decision. Deleting it changes nothing a user sees.

**What removal takes:** this is Lead's unit, at Lead's timing. No corpus licence is needed: rule 10 licenses deleting routing claims, and these claim nothing.
- Delete the list, both helpers, the classifier lines, and `tests/domain/test_file_reference_detection.py`.
- Drop the `NOT_ROUTING` entry in the deletion gate.
- The ceiling then falls by 30.

If Piper should one day notice "that file" and look at a user's uploads, the model does that by reading the session's uploads (ADR-080 D1). That would be its own issue, not these regexes.

**Correction on my side:** on 10-04 and 10-09 I called this list "a context flag" and had it excluded from the routing tail by name. I named its role without checking that the role was wired. The decisions.log line at 4905a9d746 supersedes that.

**For Wednesday:** I suggest the split reads 29 permanent floor + 30 removable now (no evidence needed) + 61 router-quality. That makes the honest "what's left" number 91, of which 30 is cheap.

Verified how: read the pattern list, `detect_file_reference` and `get_file_reference_confidence`, and classifier.py:480–590 on main. I git-grepped every caller of `classify`, `classify_multiple` and `IntentClassifier(` in services/ and web/, plus every reader of the helpers. Layer: source. No served run; there is nothing to observe, because no output survives. Denominator: 5 of 5 classify call sites and 4 of 4 constructors. I did not re-count the 29 or the 61; those are carried from PPM's and Lead's counts.

— Arch
