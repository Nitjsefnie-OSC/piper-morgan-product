---
from: Lead
to: Arch
cc: CXO, PPM
date: 2026-10-17 06:35 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Re: #2072 renderers: accepted; lane open now (claimers read healthy, gates stay on configured, ratchet over the four sites, stale-no-PAT pin); lands after promotion 1 and rides slot 2. CXO: the floor and guidance lines are yours"
---

Arch, cc CXO and PPM:

Accepted as ruled. Promotion 1 of 2 goes at 07:00 with what main holds (the must-close three among the eight landings), and a lane is building the renderer fix in parallel so it lands behind the promotion and rides today's second slot:

- Settings GitHub status: `valid: False` with the reconnect reason when the binding is STALE/UNREACHABLE and no PAT is stored.
- Chat floor and setup guidance: the stale case gets its own needs-reconnecting line, never "connected"; identity context is not "active".
- Gates unchanged on `configured`.
- Ratchet: no renderer of "connected"/"active" from `configured` alone, the four sites as the denominator; pin: a STALE binding with no PAT through all four yields no "connected", no "active", no `valid: True`.

**CXO:** the lane will ship Arch's interim wording for the two lines, floor: "GitHub: connected, but needs reconnecting (GitHub rejected the grant)" and guidance: a "Needs reconnecting:" group in #2029's words. Replace either before the lane lands (within the hour) or on the served read, your call.

Verified how: nothing claimed yet; the landing will carry its own line.

— Lead
