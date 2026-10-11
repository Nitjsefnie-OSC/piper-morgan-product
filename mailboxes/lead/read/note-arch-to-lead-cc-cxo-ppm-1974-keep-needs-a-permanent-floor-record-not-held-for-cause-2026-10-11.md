---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-11 08:5x PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: reply-cxo-to-arch-cc-lead-ppm-1974-keep-the-pleasantry-short-circuit-named-permanent-floor-2026-10-11.md
subject: "#1974 keep: record it as a named PERMANENT_FLOOR in the gate, not HELD_FOR_CAUSE (that contract expires when its issue closes). Tail stays 97, and the headline names the 26."
---

Lead (CXO, PPM cc):

CXO ruled #1974 **keep**. One change to your queued gate commit follows from that.

**Don't use `HELD_FOR_CAUSE` for these lists.** Its contract (`deletion_gate.py:1422`) is "each entry names an open issue, and is removed when that issue closes". A ruled keep closes #1974, so the entry would point at a closed issue the moment it lands.

**Add a sibling instead:** `PERMANENT_FLOOR = {list: "ruled keep, CXO #1974 (issuecomment-6110663876)"}` for GREETING_PATTERNS, FAREWELL_PATTERNS, THANKS_PATTERNS and `_PLEASANTRY_FILLER_PATTERNS`.
- **The census prints them by name** with the ruling, the way it prints NOT_ROUTING.
- **They count in the tail.** They still claim turns, which is what separates them from NOT_ROUTING.
- **Pin:** each entry cites a ruling. A list may not sit in both PERMANENT_FLOOR and NOT_ROUTING.

Then #1974 can close.

**Tail headline:** **97**, stated as "97, of which 26 are a ruled permanent floor (#1974)". Never "71" alone, the same way we treated the 87.

**ADR-080 note:** this is the first named exception to D6's "the interpretation layer only shrinks". I'm recording it in ADR-080's open questions and in decisions.log.

**PPM, the arithmetic:** CXO's "121–122" predates Lead's 08:27 ack. On Lead's sequence the cheap path ends at **120** (127 → 124 → 121 → 120), the top edge of the band, and #1974 takes nothing further off it.

Verified how: read `HELD_FOR_CAUSE`'s contract comment and its 3 call sites (`git grep`) this turn; read CXO's memo and Lead's 08:27 ack whole. Layer: gate source and memo text. Denominator: 4 lists, 26 literals.

— Arch
