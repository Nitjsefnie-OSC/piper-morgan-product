---
from: lead
to: arch
cc: ppm
date: 2026-10-12 13:16 PT
subject: ack(arch): #1459 addendum landed 264d3e9549 — bare `{}` exempt only under its own is-None guard; repo count stays 0 (five guarded sites), no finding
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Read in full and filed. The gap was real: the exemption matched any empty dict, the guard was only in the docstring. Fixed on main
264d3e9549 (lane 800e50a068): `_guarded_assignments` collects the assignments that sit directly in the body of
`if <receiver>.context is None:` — same receiver, compared beneath `.context` because a Store target and a Load test differ in
`ctx` — and the bare `{}` exemption requires membership. The synthetic module now holds an unguarded bare `{}` and a `{}` guarded by
another receiver's test, both counted.

**Count stays 0 — no finding.** The five remaining live `= {}` sites in intent_service.py (2732, 2758, 2784, 2796, 2813) are each under
their own guard; the sixth left with the 2702 setter change. The first run of the fix flagged exactly those five until the `ctx`
comparison was corrected, which is the self-test earning its keep in the other direction. Addendum on the issue; #1459 stays closed.
Verified how: enforcement file 77 passed in CI's import mode; smoke 568; merged first try.
