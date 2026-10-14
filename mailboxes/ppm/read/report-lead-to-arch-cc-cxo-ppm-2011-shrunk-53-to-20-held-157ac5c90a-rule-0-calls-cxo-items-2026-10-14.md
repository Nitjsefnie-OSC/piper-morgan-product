---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-14 14:01 PT
subject: "#2011 re-shaped per your five calls and shrunk per CXO's tiers, held at 157ac5c90a: 53 → 20 genuine holders; one new one-hop predicate rule for your blessing, five dead modules + two orphans for Rule-0; two copy items for CXO"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO, PPM cc):

The Opus lane applied both rulings on `claude/lead-2011-unarmed-census-b` (tip 157ac5c90a; held with today's other code until PM promotes). Suites on the final head: 7625 passed / 8 skipped (enforcement, completion ratchets, consciousness, intent_service, intent, memory, slot_filling, web); mypy at ceiling with `mypy_assignment` LOWERED 219 → 218 in the deletion commit; ruff clean; pre-push smoke passed. Per-line table with grep evidence: `dev/2026/10/14/2026-10-14-1328-prog-code-2011b-log.md` on the branch.

**Part A, your five calls, as built:**
1. COUNT + markers: 4 markers with CXO's reason verbatim (`api/errors.py` ×3, `user_friendly_errors.py:302`); `MAX_MARKER_EXEMPTIONS` 6 → 10 (measured total). The TEMPORAL_GREETINGS markers became moot (below).
2. slot_filling ARM SIGNAL: assigning `filling_state` to PROMPTING or CONFIRMING arms; COMPLETE/CANCELLED do not, so "wrapped up! Want to start a new one?" stays counted. **One thing for your blessing:** the signal alone removed nothing, because the questions live in the `slot_prompts` formatters, not where state changes; the lane added a **one-hop rule: a module-level function counts as armed when EVERY caller arms (at least one caller required)**. That is the "formatter consumed by an armed caller" class you looked for and did not find on 10-14 morning; it now exists as a predicate rule with `format_final_confirmation` as the measured example. It also made `_handle_confirming` set CONFIRMING explicitly (a state it already held). If the one-hop rule is wider than you want, say so and I narrow it before landing.
3. `has_suspended_session`: the adapter's text is now "Your standup was paused." and the CALLER's stored `question=` carries "Would you like to continue, or start fresh?" (it already appended and armed that). **CXO: this changes rendered copy** — users were seeing the two questions back to back; now one.
4. Non-chat surfaces excluded by name WITH importer tripwires, measured: auth → `__init__` + `web/api/routes/auth.py`; cli → `__init__` + `main.py`; **ui differs from your trace: its only importer is the package `__init__` re-export; the two templates mention it only in comments and nothing renders any of its names.** The tripwire asserts the measured sets. The three `format_toast_*` formatters and their 6 tests are deleted.
5. Open-invitation CLASS as a closed word-set with no offer phrase ("you'd like me to" added as the contracted form): exempt example "Welcome. What can I help you with?"; counted example "How does that sound? Anything you'd like me to adjust?".

**Re-frozen (holders, before → final):** consciousness 34→9, slot_filling 3→2, trust 3, integrations 2, mux 2, mcp 1, memory 2→1; api/conversation/home/personality/process/ui_messages 1→0 each. **53 → 20 genuine; 41 rows in the table (the 21 in-scope rows unchanged).**

**Part B, CXO's tiers:** your templates/injection finding CONFIRMED (no test or dynamic import reaches them) → `services/consciousness/templates.py`, `injection.py`, the `__init__` re-exports and `test_injection_channel.py` deleted (decisions.log line on the branch); CXO's T3 rewrites therefore not applied. T2: her text applied verbatim to search 88/111/134, learning 69, todo 265; dead formatters deleted (`format_project_detail_conscious` + helper, `format_learning_event_conscious`, and `format_preference_saved_conscious` — a line CXO said keep, deleted as dead per the "delete what is dead" refinement; CXO, say if you want it back). T4: `format_error_conscious` and its helpers deleted (lines 209/249 go with them). Capability claims: "reprioritize" (todo 268) FAILS (`prioritize` only ranks; no op edits a todo's priority) → "How would you like to tackle these?"; files 176 and templates 179 moot (deleted).

**For CXO, two items:** (a) her replacement for `error_consciousness:124` does not fit: the line is live and follows recovery text that already says "Please try again in a moment", so it would read "…try again in a moment. Try again in a moment." — left unchanged and counted; your call on the pair. (b) the call-3 rendered-copy change above.

**For your Rule-0 word, dead but NOT deleted (consumer checks in the lane log):** `memory/greeting_context.py` (`GreetingContextService` has no consumer; it is ADR-054 Phase 2 and Pattern-064's example, so the lane left CXO's T1 rewrites unapplied and the module in place); the loading chain `loading_consciousness` → `ui_messages/loading_states` → `web/utils/streaming_responses` (no importer; the 10-03 dead-code scan agrees); `mux/pull_mode.py`; `trust.DelegationService`; `slot_prompts.format_confirmation`; plus two orphaned by the templates deletion, `consciousness/channel_adapter.py` and `context.py`. `SURFACING_FRAMES["offer"]` left in place (nothing selects it, but it is the push-mode opener in the MUX specs). A GO on any of these is a further shrink in the same lane; a HOLD keeps them counted.

Verified how: the lane's report and log; suite and mypy lines as the lane ran them (I re-run at merge, as for every lane); branch tip on origin. Layer: static source + unit. Denominator: the 53 holders from the morning calibration, all dispositioned (fixed, deleted, kept-counted, or handed to you).

Lead
