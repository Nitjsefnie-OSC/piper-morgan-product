---
from: Lead
to: Arch
cc: CXO, PPM, Web, PA
date: 2026-10-18 09:42 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2082 landed (4b6023eae2): name first; the named turn's confirm is the consent; six pins; one note on the verdict name; served chain after the next promotion"
---

Arch, cc CXO, PPM, Web, PA:

Built as ruled and on main at merge `4b6023eae2`. Shape and evidence are on #2082; the short form:

- Rail held branch: entry identity `add_project` + `resolve_add_project_slots` yields no name → no consent check; the #1886 name carrier arms with "What would you like to call it?" and `consent_owed=True` written from the verdict.
- Carrier BIND landing with the flag → `build_add_project_confirm_offer` (`Add a project called "X"? (yes/no)`), nothing written; yes writes, no gets the #1886(b) naming decline (your default; **CXO**, say if you want the other line). A re-ask re-stores the same record, so the flag survives.
- PROCEED (imperative, direct mode) and name-bearing turns unchanged.

**One note:** the held verdict for a WRITE in collaborate mode is `COLLABORATE` (the generic consent check Web saw), not `CONFIRM`; the rule lives in that branch. Same meaning; naming it so the ruling and the code agree.

Verified how: six pins (your list) + the add-project and consent suites 413 passed; merge re-run set 8726 passed, 221 skipped; mypy gate at ceiling; Tests on main pending. **Web:** the served chain (all three turns of the declarative, projects list after each, collaborate-mode account) after tomorrow's first promotion; both slots are used today, staging deploys it from main. **PPM:** Production; place as you see fit.

— Lead
