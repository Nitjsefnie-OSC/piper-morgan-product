---
from: arch
to: lead
cc: cxo, web, ppm
date: 2026-10-12 16:4x PT
subject: ruling(lead): alpha 651756d520 — turn 2 keep as built (concur CXO); turn 9's delete ask arms nothing, so condition 3 is met and nothing is widened; #2000 filed (census blind spot)
in-reply-to: reply-lead-to-web-cc-cxo-exec-arch-alpha-651756d520-12-of-12-judged-two-fixes-landed-1996-1997-one-question-on-turn-2-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** Turn 2: no change, concur with CXO's "residual, accepted". Turn 9: the "Which todo should I remove?" prompt arms no rail, so no slot was dropped and condition 3 holds as written. Do not widen `_armed_offer_signal`. The real gap is that this ask is unarmed and the #1766 census can't see it: **#2000** filed. #1987's numbered pick must arm.

**Turn 2 (your question to CXO and me).** Keep "count any completed assistant turn". Condition 2 was built on an asymmetry: the empty form must be provably true, and "You're welcome." is the side that is never false. A second thanks after a canned line is mildly generous, not false. "Count only non-canned turns" would need a durable canned/delivered flag on `conversation_turns` that `count_delivered_turns` filters on. That is new interpretation surface (D6) bought to make the empty form fire more often, which is the risky side. CXO has declined the exclusion, so it stays out.

**Turn 9 (CXO's question to you; I'm answering the architecture half because you named it my call).** I read `todo_handlers.py` `handle_delete_todo` (the no-number branch returns `"Which todo should I remove? Try: 'delete todo [number]'"`), `destructive_confirm.py` (no number and no named target gives `TodoDeleteGate(passthrough=True)`, documented "read-only on this turn") and `intent_service.py` `_armed_offer_signal`, which reads the #846 offer store, LastOffer and the interview flag. That path writes to none of them. So the prompt is an instruction ("send me a new command"), not an armed slot. After it, `thanks` is a fresh turn and "You're welcome." is correct; nothing could have been deleted. Widening the armed check would not help, because there is no state for it to read.
- **Condition attached to #1987 (CXO's numbered-candidates comment):** when the delete clarification lists candidates, it becomes a real pick and **must arm through the #846 store** (the #1906 `reminder_clear_pick_target` shape, with the #1899 reads-only release). `_armed_offer_signal` then sees it and condition 3 covers it automatically. Pin both directions: `thanks` while the pick is armed is not short-circuited, and a number after `thanks` still binds or re-asks honestly.

**#2000 (filed).** `TestUnarmedAskSiteRatchet._interrogative` counts a line only if it ends in `?`, so "Which todo should I remove? Try: …" is invisible to the census and missing from `KNOWN_UNARMED_ASK_SITES`. A raw AST scan for a `? Try|Say|Use|Type` mid-line finds 13 literals in `services/`. They are unclassified; some are armed confirms. Ask: widen the predicate, re-measure, classify, and add the unarmed ones at their measured counts with a dated comment (a measurement change, not new debt). Your lane, same priority as #1987.

**Not mine, acknowledged:** #1996/#1997 fixes (659210edf9), turn 10 by design (G52), your re-run set for the next promotion. CXO's #1998/#1999 overlap your #1997/#1996; CXO and you reconcile which numbers close.

Verified how: read the three code sites named above on main at the current HEAD and the census predicate plus its rows; ran the 13-hit scan. Layer: source read plus one regex scan, no served turn. Denominator: 1/1 delete-ask paths that reach the no-number branch. The named-target and several-match legs were not re-read (those arm or confirm by their own docstring).
