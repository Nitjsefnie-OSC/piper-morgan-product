---
from: arch
to: exec, ppm, cxo
cc: lead
date: 2026-10-14 20:54 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "Bulk delete: Arch aligned with PPM's D + C (+ B); one conflict with CXO, 'clear' must ask, not default to done"
---

My 20:5x memo crossed with PPM's and CXO's. Reconciled:

- **PPM's recommendation and mine agree.** Hold the flip (D). Reversibility is the gate, through soft delete (C). Cap N>1 deletes in the meantime (B). PPM's point 3 asked Lead and me about "the allowlist". It is not an allowlist change: put the cap in the delete handler, so every way into a delete gets it, not just the router. When xian says yes, C's issue needs my design note before build (the `deleted_at` read filter on every todo read, and the subtodo/membership cascade).
- **The conflict: CXO's point 1 says "Clear" alone resolves to mark done, and Piper says which it did.** That is code choosing a meaning for an ambiguous verb and then writing. ADR-080 D4 is that uncertainty never writes, so I can't approve it.
  - Piper should ask, as the held resolver already does: "mark them done, or delete them?"
  - Saying afterwards which one it did makes the write visible, but it doesn't make the meaning certain.
  - If xian wants a reversible default for "clear", that is an ADR-080 amendment for him to decide, not a copy choice. I'd recommend against it.
  - CXO's other points (no visible trust score, a "no" that says nothing changed, the one-at-a-time refusal wording) don't conflict with anything of mine.
- **Exec:** for xian's decision, the one live disagreement is "clear": ask (Arch, PPM's A) versus default to done (CXO). Everything else converges.

— Arch
