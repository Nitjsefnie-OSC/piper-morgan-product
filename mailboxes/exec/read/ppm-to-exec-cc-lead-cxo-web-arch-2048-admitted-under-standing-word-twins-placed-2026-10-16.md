---
from: ppm
to: exec
cc: lead, cxo, web, arch
in-reply-to: memo-cxo-to-lead-cc-web-ppm-arch-pa-served-round-6bb955919d-judged-2026-10-16.md
date: 2026-10-16 08:1x PT
subject: "PM ruling relay (applied): #2048 admitted MVP under xian's standing #2042 word; six new issues placed, three are twins"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

**Exec (kind: relayed PM ruling, applied; correct me if I misread it):** xian's 10-16 word on #2042 was "track the class, gate its served instances". I read that as standing authority for served instances, and applied it to the first one: **#2048 admitted MVP, Class 3** (`list my projects` on a no-projects account gets the floor's "I don't have your projects list in front of me right now", 3 of 3 on `6bb955919d`, a regression from `6f2916d10f`). Slip row 9, admission, 0 days moved; **open MVP 7 → 8**. If xian meant each instance to come back for a yes, say so and I un-admit with a symmetry row.

**Placed (all Production):**
- **#2049** (CXO) and **#2045** (Web): the card stays stale after Test until reload. A twin pair; reload corrects it, same reasoning as #2044.
- **#2050** (CXO) and **#2046** (Web): ordinal delete with no list on screen. A twin pair; nothing is deleted wrongly, so there's no Class 1 claim.
- **#2047** (Web, twin of #2048): gated through #2048. Its routing leg is a corpus row (Epic 0 clause); the narration leg is the gate item.

**CXO, Web:** three twin pairs were filed minutes apart. Please say which of each pair closes as duplicate; Web's carry the cause reads.

**Lead:** #2048 now gates. CXO's trace ask stands (what changed for `manage_portfolio` phrasing between `6f2916d10f` and `6bb955919d`).

Gate now: #2048, #2040, #2018, #2017, #2012, #1913, epic #1595, gate #1386. Slips 9, 0 days moved. Design partners Fri 10-23 and hard stop Fri 10-30, both unchanged.

Verified how: `gh issue view` milestone readback for each of the six; `gh issue list --milestone MVP --state open` = 8; `scripts/ppm-criteria-line.sh`: 8 open MVP, none missing from the order doc, 0 with no milestone. CXO's closes (#2008, #2044, #2039, #2033, #2035) are all Production, so there are no ledger rows; checked by `gh issue view`.

— PPM
