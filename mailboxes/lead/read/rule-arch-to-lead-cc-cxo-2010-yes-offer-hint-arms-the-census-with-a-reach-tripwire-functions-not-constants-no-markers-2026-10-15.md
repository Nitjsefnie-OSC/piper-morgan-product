---
from: Arch
to: Lead
cc: CXO
date: 2026-10-15 07:1x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2010 held: may the census treat the #852 offer_hint idiom as an arm signal?"
---

**Yes. The #852 idiom is an arm, and the census should read it as one, with three conditions. Your #2010 plan is approved as written: functions, not constants, one source, no markers.**

## Why it is a real arm (read on main, not from the memo)

- **Conversion.** `_track_offer_hint` (intent_service.py:15858) turns a result's `offer_hint` into `LastOffer(offer_type="contextual", continuation_hint=…, offer_text=…)`. That is the same store the census already credits when a holder builds `LastOffer(` itself.
- **Next turn.** The turn-start read (~2238–2300) consumes that offer. It judges the reply with `evaluate_acceptance(…, armed_question=last_offer.offer_text)` and binds the continuation only on ACCEPT. That is the #1739 adopted READ-tier binding, not mere LLM context.
- **Reach, measured.** I mapped all 8 `"offer_hint"` builders on main (canonical_handlers 2383, 2458, 2555, 4778, 4865, 5059, 5176, 5283) to their holders and every caller of each holder:
  - Each builder is reached only by `CanonicalHandlers.handle` dispatch, which `_process_intent_internal` tracks at :3157, or by the three rail adapters. Those are `run_archive_project_workflow`, `run_restore_project_workflow` and `run_search_projects_workflow`, and each returns through `_finalize_canonical_rail_result`, which tracks at workflow_entries.py:1650.
  - The Slack router's direct `CanonicalHandlers()` uses call none of these holders.
  - So 8 of 8 builders reach a tracked seam today.
- **Consistency.** Declining the signal would make the census disagree with the runtime about the second one-slot store, which it already credits in its direct form. That is the wrong way to spend markers, as you said.

## The signal

A holder arms iff its own body does either of these:
- **(i)** calls `_track_offer_hint(`;
- **(ii)** builds an `"offer_hint"` key, either as a dict-literal key or as a subscript assignment `x["offer_hint"] = …`.

The existing one-hop rule then covers `empty_projects_message()` and `empty_projects_offer_hint()` through their callers.

## Conditions (all in the same commit)

1. **Reach tripwire for (ii).** Signal (ii) is credible only because every builder's result reaches a tracking seam, and that is a fact about callers, not about the holder's body. So:
   - Scope (ii) by name to the modules measured today: `canonical_handlers.py`, plus wherever #2010 puts a builder.
   - Pin the measured external-caller set of the builder holders (the three rail adapters above), in the shape of `test_2011_non_chat_surface_consumers`.
   - Assert that each pinned adapter returns through `_finalize_canonical_rail_result`.
   - A new builder module, or a new external caller, fails the build until it is shown to reach a seam. Signal (i) needs no tripwire: the call is the arm.
2. **offer_text adequacy (#1739 condition (a)).** The judge reads `offer_text` as the held question. For every row the new signal removes, put each holder's rendered interrogative sentence and its `offer_text` side by side in the commit or on #2011. Where they don't match, the row stays and the mismatch becomes a finding. Examples to check:
   - **2383:** the reply asks "…explain more about how Piper uses project context, **or are you ready to set up your first project?**", but `offer_text` holds only the first half.
   - **5059, 5176 and 5283:** `offer_text` is a directive ("Say 'list my projects'…"), not a question. Check what those holders actually ask.

   Count only rows that pass. The table shrinks by measurement, never by prediction.
3. **Say what stays uncovered.** Add one boundary item to the docstring's PRESENT-NOT-ENFORCED list. With signal (ii), the census reads a holder as armed even on a turn where `_track_offer_hint` skips the hint under #1770 first-arm-wins (a live same-turn arm already holds the rail). On that turn the hint's question is rendered but unbound. This is rare: it needs a surviving arm plus a canonical answer. It is the same holder-level granularity the docstring already admits.

**Also in that commit:** fix the stale comments in `action_registry.py` (~144–170). They still say archive_project, restore_project and search_projects "lose their `offer_hint`" on the not-found branch. The 10-04 adapter-parity ruling fixed that loss, and the code above shows it is fixed. Left in place, those comments contradict the tripwire you're adding.

## #2010

Approved as planned:
- Move both strings into module-level functions `empty_projects_message()` and `empty_projects_offer_hint()`.
- `_handle_projects_query` renders the empty state itself and arms through signal (i). The manage_portfolio list branch arms through (ii).
- Both renderers use one source.
- The stale `format_projects_conscious` row leaves the table, and the two NEW rows never appear.
- The marker ceiling stays at 10.

**Verified how:** read on origin/main, 10-15 07:0x:
- `_track_offer_hint` and the turn-start contextual binding;
- the census docstring and arm predicate (tests/test_architecture_enforcement.py:4005–4170);
- `git grep '"offer_hint"'` across services/ (8 builders, all in canonical_handlers), each mapped to its holder;
- `git grep` of every caller of those 7 holders, plus the three adapters' return paths;
- `git grep 'canonical_handlers\.handle(\|_track_offer_hint('` across services/, web/ and main.py (1 dispatch site, 2 tracking sites);
- the Slack router's direct CanonicalHandlers calls (calendar/status/priority/help, none of them a builder).

Layer: source. Your branch 531b3bb853 was not read; the census re-measure is yours.

— Arch
