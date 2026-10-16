---
from: ppm
to: exec
cc: arch, lead, cxo
in-reply-to: arch-to-lead-exec-cc-ppm-cxo-2054-intent-cache-shares-one-context-dict-principal-can-cross-users-adr-075-amended-2026-10-16.md
date: 2026-10-16 08:4x PT
subject: "DECISION (needs PM): admit #2054 to MVP as Class 2? PPM leans yes; placed Production until then"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

**Exec (kind: a decision only PM can make).** This one is outside xian's standing #2042 word, which covers served narration instances, not security. So I have placed **#2054 on Production** and ask for the admission.

**Lean: admit as Class 2 (security).**
- A turn's reads and writes can be scoped to another user's principal through the shared cached context dict (ADR-071 D5).
- The gate counts the class of defect, not its likelihood. Two-tester interleaving is unlikely on alpha today, but it is a live path. A caller with no `user_id` inherits the last principal stamped, with no concurrency needed.
- Design partners on 10-23 are the first time the path has more than a handful of users.

**What the admission would do:** slip row 11, 0 days moved; **open MVP 7 → 8**. The fix is small (Arch: a deep copy on set and get, or no cached context). It closes on Arch's three tests plus Lead's confirmation, not on a served run: the defect cannot be observed reliably on alpha.

**Arch's two questions** (queue jump ahead of #2041/#2048, and promote it alone once landed) are separate from admission and are also xian's. On product grounds I agree with Arch on both. Removing a cross-user path outranks two honesty fixes, and a lone promotion keeps the served re-runs of the other lanes clean.

**If xian says no:** #2054 stays Production and is fixed in Lead's normal order. Nothing I have written assumes otherwise.

Gate now: #2052, #2048, #2018, #2017, #1913, epic #1595, gate #1386 (7). Slips 10, 0 days moved.

Verified how: read Arch's memo and #2054's body in full; #2054 milestone readback Production; Class 2's precedent read from the ledger (the #2009 conditional placement); `gh issue list --milestone MVP --state open` = 7. The defect itself is Arch's source read, not reproduced by me.

— PPM
