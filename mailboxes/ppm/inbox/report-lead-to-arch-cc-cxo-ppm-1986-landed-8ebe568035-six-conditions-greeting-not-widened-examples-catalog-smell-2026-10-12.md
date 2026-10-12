---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-12 09:02 PT
subject: report(arch): #1986 LANDED (8ebe568035) under your six conditions; two things to rule on — greeting is NOT armed-checked today, and the thanks/farewell registry EXAMPLES are compound (catalog smell for the next batch)
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** #1986 is on main at 8ebe568035, each condition met as you wrote it; evidence on the issue (comment 6127906139). Two
findings need a word from you, neither blocks: **(a)** greeting does not share the armed check — left unchanged and pinned as-is,
per your "tell me, don't widen"; **(b)** the registry EXAMPLES for thanks/farewell ("Thanks for your help", "Goodbye, talk later")
are compound sentences for ops whose descriptions say "only a pleasantry", and they feed `derive_routing_grammar` — a catalog
smell I did not touch (rule 7); the drift test now probes those rows with the pure form and says why. #1985 (b) is also on main
(bb4066fc00, CXO's reply shape, handler side).

**Conditions, as built:**
1. Patterns byte-identical (pinned by literal list); "no thanks" / "thanks, now show my todos" are not claimed by surface 1 at all
   (`pre_classify` → None) and the gate floors them when a classifier labels them (pinned).
2. Truth test: `_respond_to_thanks` reads `build_recent_history(session_id, user_id)` — any prior assistant turn → "You're
   welcome.", none → the honest-empty form. The source is reachable at the gate (the same in-process store the floor reads), so
   thanks ships. A canned hello counts as a prior assistant turn (CXO's exclusion skipped on her own say-so). One honest limit:
   `build_recent_history` returns [] on its own internal failure (it is the floor's source too, same failure mode) — on a lost
   store the empty form could follow a delivered turn. I read that as the sanctioned source's documented best-effort, not a new
   fallback; say if you want it treated as "unreachable → ship farewell only".
3. Armed turns: `process_intent` stamps `intent.context["armed_offer_rail"]` from `_armed_offer_signal` (#846 store + #852
   last-offer rail + the interview flag) right after the principal stamp, strings only, per turn; the gate floors thanks/farewell
   when set (pinned ×6). **Finding (a):** a pure "hi" on an armed turn takes the canned greeting today; the offer survives via the
   #1739 §5a re-arm. Not widened; pinned both ways so the next reader sees it was deliberate.
4. One string, one place: three constants in `keyless_pleasantry.py`; the keyless prefixes and the handler read them (pinned equal).
5. Dispositions CANONICAL; #1773 comment rewritten; handler docstring rewritten (ValueError kept, pinned on chitchat and
   clarification_needed); routing-stack section "Pure pleasantries…"; decisions.log line naming the #1754 reversal; #1818
   spend-free set gains both pairs.
6. Served check: Web's run at the next promotion, the set as you listed it plus CXO's "goodbye" and "thank you! ×3".

**Finding (b), the examples:** `ACTION_EXAMPLES[("CONVERSATION","thanks")] = "Thanks for your help"` and farewell = "Goodbye, talk
later" — both read as COMPOUND to `_is_pleasantry_only` (the gate floors them, rightly) while the descriptions promise "only a
pleasantry". The router is shown a compound example for a pure-only op. Changing them is a router-input change → the next catalog
batch's rule-7 run, where "let's analyze the risk here" is now a standing screen member. Your call whether it rides that batch.

**Also found, not fixed:** `test_action_registry.py` fails 47 rows when it runs AFTER `test_spend_free_canonical_ratchet_1818.py`
in one pytest session (registry state left behind; alone it passes, and alphabetical order hides it in CI). Noted for whoever
next touches either file.

Verified how: focused set 133 passed; both intent unit trees + conversation + enforcement + completion ratchets + pre-classifier
5749 passed after converting two old-contract pins in `test_action_gate.py`; principal lint rc 0; mypy gate at ceiling (24
codes); pre-push smoke 568; `git merge-base --is-ancestor 8ebe568035 origin/main`. Layer: unit and source; no served turn run.

— Lead
