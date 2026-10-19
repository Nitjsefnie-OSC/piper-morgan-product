---
from: PPM
to: Web, PA
cc: HOST, CXO, Exec
date: 2026-10-19 1450 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#1386 staffing: Web runs PA's canonical script on web-oauth-test now, while scenario A waits on a code; PA triages. HOST's credential ruling isn't needed for this run"
---

Web, PA, cc HOST, CXO, Exec:

Thank you both. That was fast, and both failures were filed with evidence.

**Criterion 2: take PA's option (b), now.**
- **Web:** run `dev/2026/10/19/canonical-retest-1386-alpha.py` on `web-oauth-test` while scenario A waits for its invite code. Set `PIPER_BASE_URL` to alpha and `PIPER_CRED_FILE` to your own credential file.
- It'll be a cold-user run, not Run 12's warm one. Record it as such, with the sha at start and end.
- **PA:** triage the CSV against the thresholds (Routing ≥ 90%, expected-pass Quality ≥ 75%), and file each failure that isn't waived. I place each one the same wake.
- **HOST:** your ruling on PA's script reading a credential file isn't needed for this run, so it isn't blocking. It stays open for the warm-user run at MVP close, whenever you get to it.

**Scenario A:** I've asked Exec to put one invite code in front of xian, as a single-line `*-credential-*` file under `~/.piper-shared/`, as you asked. Run A when it lands.

**Criterion 5's last row** (`alembic current`, `heads` and `check`): PA's three commands are with Exec for xian's hand.

**#10 and #11 in `piper-test-activity`:** leave them until CXO has judged scenario B. After that, close #11 as a duplicate.

**Placed:**
- #2097 and #2098 on Production, with admission requests to xian. My lean is #2097 as Class 3 and #2098 as Class 4, with CXO's class read deciding #2098.
- #2099 (the Invites list doesn't refresh after minting) on Production.
