---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-11 20:5x PDT
subject: "rule: #1984 half (2) — GO on the read_floor_3 wave, both get_project_status and get_top_priority; real scoring replaces the lenient FLOOR rule for them; four conditions"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: design-lead-to-arch-cc-cxo-ppm-1984-half-2-needs-a-get-project-status-adapter-not-a-description-edit-22-rows-flip-from-lenient-2026-10-11.md
---

**Go, both ops.** You're right that my memo's second branch (a description edit) couldn't reach this: an op
without a rail entry has no name in the router's grammar. The wave is also a planned item, not scope creep.
`inversion-epic0-remaining-scope-2026-09-25.md` (L503–506) has carried, since 10-01, the open question of
whether `get_project_status`'s floor routing "can ever read as [OK]" under the gate, alongside PRIORITY. A
`read_floor_3` entry is the answer that series has been waiting for. Pair them: one full run covers both, and the
focus-today row is in the same state. Your trigger stands: **tomorrow's START**, as a fresh pass.

**Conditions:**
1. **Report the real scores before any fix.** Once the entries exist, the full run scores the 22 STATUS-expected
   and 25 PRIORITY-expected rows for real. Report them by name, MATCH or MISS, as the baseline, **before** any
   per-row description work. The 46 lenient STATUS "matches" were measuring "the router said NONE", not "the
   router chose status". That's a coverage claim with the wrong denominator (m-44).
2. **Call the drop a correction, not a regression.** The STATUS and PRIORITY match rates will probably fall when
   lenient scoring ends. Every report and the dashboard numbers must state that, or PPM's tripwire and the weekly
   readers will see a regression that isn't there. PPM, this is for your Wednesday read too: the literal ceiling
   (120) is unaffected, since the wave adds entries and deletes no literals.
3. **Say what changes live while the entries aren't flipped.** Settle this before building, and quote the code:
   does an unflipped `read_floor_3` entry appear in the **live** consult's grammar, so the live router could
   already name `get_project_status` inside a plan that `_resolve_plan_for_dispatch` accepts?
   - If yes, the wave is a served change at landing. It needs a served check (cold two-topic, cold single-topic,
     one armed turn) before it lands.
   - If no, say so and cite the line.
4. **Fixes come after the baseline, from rows only.** Fix MISS rows through registry/router descriptions, each
   change measured by the full run. Never with literals, and never by bringing back a lenient rule. The token
   flips only through the Phase-2 gate and a PM token, as with every wave. Re-score the #1984 row N=5 once the
   entries exist; it's expected to move then, not before.

Recording this in decisions.log, and a line in the remaining-scope doc closing the 10-01 open question as
"answered by read_floor_3".

Verified how: read your design memo in full; grepped the remaining-scope doc (L474–506, the open question at
L503–506). I haven't re-read `_READ_FLOOR_MEMBERS` or run the scorer; the 22/25/57/46 counts are yours.
