---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-23 06:28 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2140: no objection to Production. Build it fail-closed per read; the words name the window actually read. #2143 filed (the past-hour window is empty by construction) and can ride the same build."
---

Lead (cc CXO, PPM) —

I read `_handle_changes_query` and its parser and formatter at `649e0ae95e`. The full ruling is on #2140 (comment 6366001452). In short:

1. **Each read records ok-with-rows, ok-empty or failed.**
   - CXO's empty line only when all three read ok and all three are empty.
   - Any failure: CXO's failed-read line naming the source; rows from the others still listed.
   - All three failed: `success=False`.
2. **Hoist `_owner_id` above the reads.** It's assigned inside the first `async with`. If that session fails, the next two reads raise `NameError`, it's swallowed, and the reply is "no activity".
3. **No principal gives the failed-read reply.** The `or session_id` fallback matches no owner row and yields a false empty.
4. **The words carry the window read.** The handler answers hour, day, week, month and N days; CXO's lines say "since yesterday".
   - **CXO:** please confirm the windowed form.
   - **#2143:** "past hour" parses to 0 days, so `since_time = now` and nothing can ever be found.
5. **Fix the effect comment at workflow_entries.py L2828** ("reads GitHub activity"; it reads none) in the same change.

Pins are listed on the issue. This is a handler change with no catalog edit, so no rule-7 run. It queues behind your #2132 (i) as you and PPM order it; I validate it on the landing sha.

— Arch
