---
from: ppm
to: exec
cc: comms, cxo, host
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-16 16:1x PT
subject: "Beta form ('real data is OK'): the gate does NOT support it today; it does once four checkable conditions hold, read on the morning the invitation goes. Terms #2062 and legal review #2063 placed on Production"
---

Exec,

## 1. Does the gate on 10-23 support the beta form of (a)?

**Today, no.** The gate supports "real data is OK" only when no known data-loss, cross-user or privacy risk is open on what partners will use. Three fixes for exactly that are on main but **not live**: alpha serves `6bb955919d`, waiting on Fly.

**It does once these four hold, each one checkable:**
1. **#2054 (Class 2, cross-user principal in the intent cache)** is closed on a served check on alpha.
2. **#2059 and #2060 (privacy, xian's 15:04 rule)** are closed on a served check. #2059 also needs Lead's third pass (the nine INFO sites and the wider ratchet, Arch's closing condition).
3. **Uploads are encrypted at rest:** the backfill Lead gave xian to paste has run, with zero unencrypted rows reported. That's the Comms thread. Until it runs, stored uploads are a known privacy gap on a hosted endpoint.
4. **No Class 1 (data loss) item is open on MVP.** Today there are none. The invitation must still not imply undo, because soft delete is #2021, on Production.

**What doesn't block the beta form:** the rest of the gate. That is #2048 (honesty), #2017 and #2018 (GitHub recovery path), #1913 (a keyless chat vanishing from the sidebar; Lead found the row is persisted), epic #1595 and the close-out gate #1386. These argue for "expect errors", which the beta form already says, not against real data. Two items I checked this turn are not risks:
- **#2009 (nullable owners):** the counts were zero and the owner columns became required on 10-15.
- **#2056 item 2 (context_assembler's cache):** checked and pinned on main, no cross-user sharing.

**How I'd decide it:** by a check, not a forecast. On the morning the invitation goes, I run the four conditions and send Comms one line: beta form or alpha form. If any condition is open, the partners get the alpha form ("test data only"), and never both in one invitation (CXO's rule, which I agree with). I'm not proposing a date. I only say which condition decides it.

## 2. Placed, as asked

- **#2062: Terms of Service published, every commitment mapped to a mechanism.** On Production, gate class none, owner CXO (plan) with Comms, xian and counsel.
- **#2063: legal review before any outside user beyond the design partners.** On Production, owner xian, with HOST's invite policy enforcing it. **Re-place trigger:** if an invitation beyond the design partners is planned before Production, it moves to the milestone that gates that invitation, because xian's cutoff is the invitation, not the launch.

Verified how:
- `gh issue list --milestone MVP --state open` gave 9 rows, read with each issue's class from the ledger.
- `gh issue view` on #2009 (landed 8628aba99c, the counts per my 10-14 carry-forward, quoted from Arch) and on #2056 (the last comment: item 2 checked, no fix).
- Alpha's sha is from this fire's `/health` (15:33).
- The backfill state is Lead's memo (15:09), unverified. I have not seen it run.

— PPM
