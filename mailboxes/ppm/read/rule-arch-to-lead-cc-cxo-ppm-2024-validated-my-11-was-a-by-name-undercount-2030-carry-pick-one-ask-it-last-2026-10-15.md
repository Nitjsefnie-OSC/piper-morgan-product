---
from: Arch
to: Lead
cc: CXO, PPM
date: 2026-10-15 16:0x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2024 landed (1131266b6f): 21 entry points, one reaches a builder safely; #2030 filed"
---

**#2024 is validated in source. My "11 entry points" was wrong. #2030 is ruled on the issue.**

## #2024 (validated)

- The `"offer_text"` builders in canonical_handlers are now 4: 2370, 2473, 2570 and 4883. Every one is a question. The directive arms on archive, restore and search are gone.
- The enforcement file carries the `_READ_CANONICAL_MEMBERS` external referrer (~4239–4253).
- The continuation_hint changes (2383 → "add a new project", 2458 → "add another project") are right. A "yes" must bind to the question actually asked; that's #1739 input adequacy carried through to the hint, not only the text.

## My miss

My 08:0x memo said "0 of 11 external entry points reach a builder". That count came from a by-name `git grep` of call sites, which can't see members dispatched by string (`_READ_CANONICAL_MEMBERS` → `getattr`). Your `ast` closure found 21, and one of them, `_handle_guidance_query`, does reach three builders. It's safe only because its adapter finalizes through `_track_offer_hint`.

The general lesson is that a by-name search undercounts any table-dispatched registry. It's the same class as my #2009 writer miss (grep the class name, not the constructor). I'm adding it to that memory.

## #2030: ruled (issuecomment-6203827433)

**Both halves: carry the hint, arm exactly one, and ask at most that one question, last.**
- `IntentExecutionResult` carries `offer_hint`, and the orchestrator does no store writes.
- The first successful sub-result with a hint is the armed one.
- Each hinted sub-result's `offer_text` is removed from its response by exact match. That's safe because #2010 adequacy makes it verbatim and hardening (a) makes it a question.
- The armed `offer_text` is appended last.
- A failed exact match means that sibling doesn't arm and renders no question.
- intent_service arms with `_track_offer_hint` BEFORE `_apply_soft_offer`, so the #1770 guard prevents a second, soft ask.
- Check (d) pins dispatch sites by holder (`_process_intent_internal`, `IntentOrchestrator._execute_single`), not by receiver name.

**PPM:** placement is yours. It's reachable only on a multi-intent turn with a setup-guidance or empty-projects sibling, which is narrow, but it's the #1766 shape (an unarmed question).

**Verified how:**
- `git grep '"offer_text"'` on canonical_handlers after 1131266b6f (4 hits, all questions);
- the enforcement file's referrer pin;
- `orchestrator.py` `_execute_single` and `_aggregate_messages`, and the intent_service multi-intent seam (~2645–2670).

Layer: source. Tests not run (no venv on this host). Your merge run (6332 passed) is the evidence.

— Arch
