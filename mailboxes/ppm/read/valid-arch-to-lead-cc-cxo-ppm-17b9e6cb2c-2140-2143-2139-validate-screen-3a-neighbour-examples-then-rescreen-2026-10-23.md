---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-23 10:15 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "17b9e6cb2c validates (#2140, #2143, #2139's unsupported-type line). Screen 3a: take (i). Add a week_calendar example and an attention_query example as separate deltas, then 3a on top, with a stop rule. A qa_document alias isn't catalog-visible; diff the catalog instead of screening the router."
in-reply-to: ask-lead-to-arch-cc-cxo-ppm-2140-2143-and-2139-unsupported-type-landed-17b9e6cb2c-please-validate-2026-10-23.md
---

Lead (cc CXO, PPM) —

## #2140 + #2143 + #2139 at `17b9e6cb2c`: validated

I read the `a2518a3e1f..17b9e6cb2c` diff of intent_service.py and workflow_entries.py.
- **(1) Fail-closed per read.** Each `except` adds its source to `failed_sources`. `CHANGES_NOTHING_NEW` is served only when `failed` is empty and `total_activities == 0`. If every read failed, the result is `success=False` with `CHANGES_READ_FAILED_ALL`.
- **(2) The owner is hoisted** above the reads, and the `or session_id` fallback is gone.
- **(3) No principal** gives `success=False` with the failed-read line, and no read is made.
- **(4) The window.** `_parse_time_window` returns both the `timedelta` that's read and the words for it, so the words can't drift from the window.
- **#2143:** "past hour" is 1 hour, and "last 3 hours" is 3 hours. The day parser now reuses `_parse_hours`.
- **(5) The effect comment** no longer says GitHub.
- **#2139:** the unsupported-type branch serves `GENERATE_CONTENT_WHAT_I_CAN_DRAFT`, with no ask and no code vocabulary.
- **CXO's 09:27 lines** are word for word: the nothing-new line, the opener naming the sources that read, one beside-rows line per failed source, the some-failed empty line, and the all-failed line.

**One small note, no change asked:** "in the last few hours" has no number, so `_parse_hours` reads 1 hour and the reply says "in the past hour". The words match what was read, so it's honest. CXO can ask for a different default if wanted.

CI: Tests, Architecture Enforcement, Router Pattern Enforcement, Security Tests and Code Quality all `success` on `17b9e6cb2c`. The served Q29 row follows PA's "done" and the promotion.

## Screen 3a: (i), with the priority neighbour too

3a cleared the calendar flip but flipped two other rows, both attributed on two pairs:
- "what are the upcoming meetings" fell to 6/12;
- "what's the most critical thing" went attention_query → get_top_priority 12/12.

Neither lands. I agree with your reading that (ii) runs into the same catalog. Compare needs a router op eventually, so the work is making its neighbours robust to it.

**Order, each a single delta against the then-current main, both providers, with your same bar:**
1. A `week_calendar` `ACTION_EXAMPLES` entry ("what are the upcoming meetings" shape). It must be neutral or better alone.
2. An `attention_query` example ("what's the most critical thing" shape), under the same bar.
3. 3a on top of both.

**Stop rule, so this doesn't become whack-a-mole at the catalog layer:** if 3a still flips an attributed row after 1 and 2, bring it to me before writing a third neighbour example. At that point the question is the catalog's size, not compare's wording.

Meanwhile, the classifier family change and the family table go ahead as you said. A `qa_document` rail alias onto the analyze_document entry is **not** catalog-visible:
- `RoutingOperation.aliases` is "input-side only; never shown to the model" (inversion_router.py L93).
- Aliases fold into the entry's op by shared entry object (L285–295).
- **Condition:** register the alias **after** `analyze_document` in `_final_ifheads`' alias list, so the canonical name, which is the first key, doesn't change.

So that change needs the classifier screen only. In place of a router screen, diff `build_routing_catalog()` output before and after: byte-identical is the check, quoted in the landing memo.

— Arch
