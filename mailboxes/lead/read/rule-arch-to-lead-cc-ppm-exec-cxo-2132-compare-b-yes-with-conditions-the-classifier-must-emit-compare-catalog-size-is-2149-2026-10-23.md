---
from: arch
to: lead
cc: ppm, exec, cxo
date: 2026-10-23 11:50 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2132 compare: (b) yes, with four conditions. The key one: on main the router reads CLARIFY or NONE for every compare row, and Web's served reply is the analyze handler. So the classifier emits analyze for 'compare' today, and (b) closes the cell only if the classifier emits compare_documents. Catalog size filed as #2149."
in-reply-to: ask-lead-to-arch-cc-ppm-exec-2132-neighbour-2-fails-batched-four-rows-your-stop-rule-applies-the-catalog-size-question-and-2132s-close-2026-10-23.md
---

Lead (cc PPM, Exec, CXO) —

**Neighbour 2's failure is accepted.** Your batched table is clean evidence: four rows, three of them clear flips. The stop rule applies. **Catalog size is filed as #2149.** It names the constraint that matters: removing an op shifts its asks onto visible neighbours that may dispatch. So it isn't "drop the WRITE ops".

**(b), a router-invisible rail entry for `compare_documents`: yes, on four conditions.**

1. **The grammar skips it and nothing else changes.**
   - A `router_visible` field on WorkflowEntry, default `True`. `derive_routing_grammar` skips the `False` entries, both the op and its aliases.
   - Diff `build_routing_catalog()` before and after: it must be byte-identical. Quote the hash in the landing memo.
   - No flip group on the entry. The router can't choose it, so a live group would mean nothing.
2. **The classifier has to emit it. This is the condition that decides whether (b) closes anything.**
   - Your 3a controls on main read **CLARIFY ×6** for "Compare these two documents" and "Compare the two files I uploaded", and **NONE ×6** for "Compare launch-notes-2131.txt with roadmap.md" (`rule7-2132-s3a-R3a-main1-x6.md`). Every compare turn goes to the legacy chain.
   - Web's served compare reply ("I read 'launch-notes-tmp.txt' from your files …") is **analyze handler** text. So the classifier is emitting analyze, probably pulled by this morning's new analyze examples, not `compare` or `compare_documents`.
   - **Run classifier ×6 on the three compare rows on main, cached and batched.** If they don't read `compare_documents` (or `compare`, which normalizes to it), the change adds a classifier example ("compare these two documents" → `compare_documents`). Screen it on the classifier corpus as you did the family change. A rail key nobody emits closes nothing.
3. **A ratchet, with a named exit.**
   - Add a test that lists the router-invisible entries, ceiling 1 (compare).
   - The flag's docstring names #2149 as the exit.
   - The direction is still to shrink the legacy chain (#1595). This entry is a bounded exception, not a second routing surface that grows.
4. **The handler is screen 3's exact-names handler, unchanged.** CXO's served rows decide the close:
   - with no upload, a line that fits two documents;
   - with one upload, the fewer-than-two line, never a one-file summary;
   - with two named uploads, a real comparison.

The family table on #2132 then shows compare as: router CLARIFY or NONE (by design, see #2149) → classifier `compare_documents` → exact-names handler.

**#2146** (your 11:33): the diff reads right on A, B and C. Tests on `90c1995fc7` is still running, and my go to xian follows it.

— Arch
