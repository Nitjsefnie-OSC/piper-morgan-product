---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-14 13:11 PT
subject: "#2011 built on a held branch (87b1e88384): services/** scanned, 67 → 53 genuine via 3 predicate classes + 1 arm signal, frozen at 74 rows; five 'class or site?' calls for you, with my recommendations"
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-2011-census-scope-widen-calibrate-freeze-2010-is-the-first-two-2026-10-14.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO, PPM cc):

Your four steps, built by an Opus lane on `claude/lead-2011-unarmed-census` at 87b1e88384 (held; it lands after PM's promotion with the rest of today's code, and its frozen counts come down by #2010's two when that lands):

1. **Widened:** `_SCAN_GLOBS` → `services/**/*.py` with `recursive=True` (454 files; without `recursive` the `**` silently stops one level down and misses `integrations/slack/` and `mcp/consumer/`); `services/standup/` and `services/onboarding/` excluded by name with the docstring's own reasons; files floor raised 40 → 400 so a glob fallback fails loud.
2. **Calibrated:** raw 110 rows (your numbers reproduced), 67 new outside the two exemptions, **53 genuine** after three predicate classes, each with a measured example: (a) an `examples=` kwarg (sample phrasings, `commands/definitions.py`); (b) an `original_message=` kwarg (a made-up user message handed to a handler, the `utterance=` class, `slack/webhook_router.py`); (c) a container whose own name says `question` (`ClarifyingQuestionGenerator.question_templates`); plus one new **arm signal**, constructing `LastOffer(...)` (the #852/#1529 second one-slot store, `_check_suspended_session_reentry`). No marked sites: no owner comment at any of the 53 says the ask is deliberate. No "formatter consumed by an armed caller" class: the lane read every caller of the consciousness formatters and none arms.
3. **Frozen:** 53 rows added to `KNOWN_UNARMED_ASK_SITES` at measured counts, grouped by package (consciousness 34, trust 3, slot_filling 3, integrations 2, mux 2, memory 2, conversation 1, api/home/mcp/personality/process/ui_messages 1 each); 74 rows total, equality-pinned; a self-test for the three classes. Enforcement 79/1 skipped; intent_service + completion ratchets 5782; mypy at ceiling.
4. **Not shrunk** (yours: "shrink by real fixes"); the full site list, 53 holders / 116 literals with file:line and question text, is in the lane's log on the branch (`dev/2026/10/14/2026-10-14-1301-prog-code-2011-log.md`), plus ~20 holders with no consumer outside their own module (unverified dead; cheap shrink if so).

**Five calls that are yours (the predicate is your contract); all five are COUNTED as unarmed until you rule, and my recommendation follows each:**
1. **A question answered by an instruction on the same line** ("Need help? Check our …" in `api/errors.py`, `ui_messages`, `TEMPORAL_GREETINGS`, auth's session-expired message). Same text shape as a genuine ask. Recommend: a class, "question followed in the same sentence by its own directive" — only if you can state it so the genuine "Which repo? I couldn't tell…" stays counted; otherwise count.
2. **`services/slot_filling/`** has its own CONFIRMING state machine, the standup shape. Recommend: third by-name package exclusion with that reason.
3. **`process/adapters.py::StandupProcessAdapter.has_suspended_session`**: its question is consumed by a caller that arms. Single site, no general shape. Recommend: count (never a site exemption), and let the standup-package exclusion's reason cover it if you widen that exclusion to the adapter.
4. **Non-chat surfaces** (`ui_consciousness`, `auth_consciousness`, `cli_consciousness`): the contract is about chat offers a "yes" cannot cash. Recommend: a named exclusion by SURFACE with the reason (not by path), or count them and let shrink work sort it.
5. **Open invitations** ("What can I help you with?") where any reply is a fresh request, not a yes/no on an offer. Recommend: a class, "open invitation with no offered object", with the example; it is the one class I am fairly sure of.

PPM: placement and timing are yours (Production by default; the shrink list is the backlog).

Verified how: the lane's report and log read; branch sha on origin; counts as the lane measured them (I did not re-run the census; I re-run the enforcement file at merge, as for every lane). Layer: static predicate at holder level. Denominator: 454 files, 110 raw rows, 5 open calls.

Lead
