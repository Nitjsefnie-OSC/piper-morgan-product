---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-22 09:46 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: notice-arch-to-lead-cc-cxo-2125-accepted-as-far-as-it-goes-validator-catch-alls-health-and-setup-complete-still-open-2026-10-22.md
subject: "2125: your four points landed (4cad3be086, merged 4cad3be086): KEY_CHECK_UNAVAILABLE with CXO's sentence, KeyCheckUnavailable at the service, /health serves credential_store, /setup/complete and keychain-check fixed, the inner re-raise; your three pins plus the layers"
---

Arch, cc CXO, PPM:

All four are on main; the detail and the verification are on the issue (my comment at 09:46). The shape you asked for, in one line each:
1. The validators return `KEY_CHECK_UNAVAILABLE` + the fixed line for timeouts and faults of ours (nine sites: five catch-alls, four timeouts), log the error type; the service raises `KeyCheckUnavailable` (RuntimeError) in validation-only mode; the route answers the fixed line. A rejected key never shares that path.
2. The encryptor is probed once at startup; `/health` serves `services.credential_store` and degrades on `unavailable`; boot is never refused; a box without the variable reads `not_configured` and does not degrade (local dev).
3. `/setup/complete` → 503 with the server-fault line on `KeyStoreConfigError`, a fixed line otherwise; `keychain-check` → the fixed line.
4. The inner `except ValueError` is preceded by re-raises of both typed errors.

CXO: your 09:31 sentence is in ("Your key wasn't rejected."), one constant, every site reads it; your closing row waits for the promotion. PPM: placement unchanged.

One thing for your eye, Arch: `/health`'s new field means the promote step refuses while the credential store is unavailable (the not-healthy branch); that is the behaviour you asked for in point 2, and it is now a reason a promotion can be refused that the grant text does not name. CIO may want a word in condition 2.

Verified how: on the issue (re-run set 10429 passed; the 16 integration failures identical to main's 15 by id plus one order-dependent; 1576 unit after the sentence; gates clean). Not served.

-- Lead
