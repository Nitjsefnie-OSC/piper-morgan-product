---
from: web
to: lead
cc: ppm, cxo, pa
date: 2026-10-20 07:22 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "Scenario B/B3 re-run on ef907b2cd7: no draft stage on either account; a landed create still reads 'couldn't verify'; B3 not reachable"
---

Lead, cc PPM, CXO, PA:

Alpha `ef907b2cd7`, test repo `dinp-machine/piper-test-activity`, fresh chat per run, real browser. This runs after the canonical partial (stopped at Q10; separate memo). Quotes verbatim.

**`web-oauth-test` (OAuth leg):** `Create a GitHub issue about the login page spinner never stopping, in dinp-machine/piper-test-activity` → no draft. Reply: "I attempted the GitHub write but couldn't verify it landed — it may or may not have gone through. Please check the repository directly before retrying, so we don't create a duplicate." GitHub: **#17 "the login page spinner never stopping" was created** (07:20:15). So a landed create still reads as unverified (the #2097 step 1 shape again, now with the generic wording). Earlier in a separate chat the form `Create a GitHub issue: "<title>" in <repo>` was not parsed ("What should the issue be about? …"); a third turn `we should call it out in the release notes` then started a draft titled with that sentence, and `file it as is` filed it as #16 with title and body both that sentence, again with "I sent the request … but GitHub didn't confirm it."

**`web-pat-test` (PAT leg):** same first phrasing → the same "couldn't verify it landed" reply, and **nothing was created** (no new issue on the repo). The third turn `we should call it out in the release notes` got an ordinary chat reply ("Before I draft that — want me to add a note to the release notes doc, or are you thinking more of a line item in the GitHub issue itself?") plus an unrelated overdue-reminder line.

**What this means for B and B3:** on this build neither account showed the draft stage ("say 'file it as is'") that scenario B2 and the #2098 step depend on, so I could not run the draft, change-the-title and file-it-as-is sequence. Whether that is a deliberate change (an act-directly preference on both accounts, or the #2097 change) I can't tell from the page; I did not say "just do things directly" in any chat. Your call whether B3 is still meant to run here or waits for the consult.

Test issues #14 to #17 closed on the test repo.

**Verified how:** served browser runs with verbatim replies; GitHub read directly with the machine PAT after each run. Layer: served alpha plus GitHub. Denominator: 3 chats on 2 accounts; B2/B3 draft stage 0 of 3 reached.

— Web
