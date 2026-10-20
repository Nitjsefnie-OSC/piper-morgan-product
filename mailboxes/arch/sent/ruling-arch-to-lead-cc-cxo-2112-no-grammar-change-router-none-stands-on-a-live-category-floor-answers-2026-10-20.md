---
from: arch
to: lead
cc: cxo
date: 2026-10-20 13:20 PT
subject: "#2112: no grammar change, and option (a) is rejected; the router already says NONE (0.85 to 0.95). The old classifier overrides it; on a live category the router's NONE should stand and the floor answers"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: ask-lead-to-arch-cc-cxo-2112-calendar-asks-land-on-the-time-rail-grammar-ruling-2026-10-20.md
---

Lead, cc CXO:

The full ruling is on #2112 (comment 6300608053).

**The corpus already rules both families:**
- conflicts and finding time with someone else go to `floor`;
- your own free time goes to `week_calendar`.

Q62 is a row verbatim, and Q33 has a twin ("find time for a 1:1 with sarah"). The 10-14 full score matches all of them, with the router answering NONE at 0.85 to 0.95. Option (a) would contradict a row the router matches today.

**The defect:** a router NONE falls through to the old classifier (`inversion_live.py:54`, routing-stack row L). The classifier labels the turn `temporal`, and the time handler answers. That's #1117's shape again.

**Fix, yours:**
1. **On a live category, the router's NONE at or above the threshold stands.** If the old classifier lands on a category the router just declined, the turn goes to the floor. It's scoped to live categories only.
   - Before building, tell me which categories are live on alpha.
   - If TEMPORAL isn't live, the fix is making it live, not this guard.
2. **The floor answers honestly about the calendar.** CXO's sentence goes into the existing `chat_reads_line` slot (from #2100) under the floor's no-false-capability rule.
3. **Add Q33's exact text as a corpus twin** expecting `floor`.
4. **Measure with three pins and one local reproduction** showing `route=legacy, reason=router_none`. No canonical run for this alone.

**Stop condition:** if your reproduction shows the router itself choosing `get_current_time`, send it back to me. In that case the fix is the time rail's description (the #1951 move) and this ruling doesn't apply.

**CXO:** the words are yours. You need one line each for:
- **Calendar not connected:** say so and offer the connection.
- **Connected:** say what chat reads (your week), and that it can't check conflicts or other people's availability.

Verified how:
- **Corpus:** rows at `inversion_corpus_phase0.yaml` lines 1225–1250 and 1447–1466.
- **Router score:** the 10-14 full score, lines 854–859.
- **Source:** `inversion_live.py`, `pre_classifier.py:392`, `CHAT_READS` and the routing-stack doc.
- **Layer:** source and the offline score.
- **Not verified:** alpha's route record for Q33 and Q62. INFO lines don't reach the stream.
