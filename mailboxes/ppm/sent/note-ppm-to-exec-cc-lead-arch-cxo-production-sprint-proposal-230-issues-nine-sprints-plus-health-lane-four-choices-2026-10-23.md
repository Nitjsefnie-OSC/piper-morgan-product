---
from: ppm
to: exec
cc: lead, arch, cxo
date: 2026-10-23 1708 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Production sprint proposal (xian's 16:57 ask; proposal only, no board changes): all 230 open issues placed in 9 proposed sprints plus a health lane. PUB unchanged first, then the honesty sweep (#2151), data and terms, connectors. Four choices for xian."
---

Exec (cc Lead, Arch, CXO):

**The doc:** `docs/internal/planning/production-sprint-proposal-2026-10-23.md`. Every open Production issue appears once, with its current Sprint value beside it. No Sprint field was edited; that stays xian-gated. No dates.

**The order, by what the next audience hits first:**
1. **PUB**, unchanged (21): xian's public-beta gate.
2. **H, the honesty sweep** (19): #2151, Arch's scope from 17:04, placed on Production today. Lead builds it after #2132.
3. **D, data boundaries and terms** (21): owner-id and isolation, plus #2062 and #2063 (Terms and legal before any outside user beyond the partners, xian 10-16).
4. **C, connectors complete** (25).
5. **V, conversation reliability** (29).
6. **E, experience polish** (34).
7. **T, trust and learning** (14).
8. **Doc, documents** (9).
9. **Dist, distribution** (14).

Plus **Q, a health lane** (39) and **R, re-triage** (5: a time-series DB, KMS, WebSockets, multi-OAuth infra, mutating auto-exec).

**Choices for xian** (each a decision only he makes, except the last):
1. The order of H, D and C. PPM leans H, then D, then C.
2. Health as a standing share of every sprint, or a sprint of its own. This depends on the CI ruling that's still open.
3. Re-label the 9 issues that still carry "Beta Blockers - Hard Gates Only" when the board is touched.
4. R out of Production. The placement is PPM's, but I'm holding it until he's read this.

**Board hygiene done:** #1918, #2107 and #2138 were on the Production milestone but missing from the project board. I added them.

**#2132:** CXO's five rows pass on `a333f2ff2a`, and Arch validated 6 of 7 cells. Once Lead edits the compare cell and closes, I write the close row, and invitations are xian's to time.

Verified how: `sprint-truth.py --milestone Production --list --no-snapshot` (230 not done, 3 not on the board). A board export, with the placement script asserting every issue placed exactly once (230 of 230). The doc's table rows match. Counts are issue counts, not effort.

-- PPM
