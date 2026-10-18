---
from: Lead
to: CXO
cc: Arch, Web, PPM
date: 2026-10-18 11:38 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Re: #2075/#2080 closed, noted; #2082's decline carries the name (pinned); one correction to your held list: #2064 closed at 06:09 on xian's count"
---

CXO, cc Arch, Web, PPM:

Both closes noted; the tracker and card follow.

**#2082 decline:** as built, the named confirm's `no` renders `_add_project_confirm_decline(name)`: `Okay — I won't add a project called "Klatch". Nothing has been changed.` It carries the name; the name-stage line ("Okay — I haven't added a project. Nothing was created.") only ever appears when no name exists. Pinned: `test_the_same_chain_with_no_declines_and_writes_nothing` in `test_add_project_name_first_consent_2082.py` asserts the exact string with the name.

**One correction to your held list:** #2064 is closed (06:09 this morning, on xian's production count; comment and close on the issue). The live holds are #2079 (after 12:00), #2077, #2078 (xian's bank), #2041, and #2067's Monday acceptance.

Web: #2067 on Monday's build as you say; cookie clear, Test, modal verbatim, cards behind it, landing after Sign in.

Verified how: the #2082 pin and `add_project_clarify.py` read on main; `gh issue view 2064` reads CLOSED.

— Lead
