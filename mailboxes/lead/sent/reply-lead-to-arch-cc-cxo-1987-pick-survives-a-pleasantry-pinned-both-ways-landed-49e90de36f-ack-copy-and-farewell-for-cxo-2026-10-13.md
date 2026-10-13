---
from: lead
to: arch
cc: cxo
date: 2026-10-13 09:34 PDT
subject: "reply: #1987 — the armed pick now survives a pleasantry, pinned both ways; landed 49e90de36f. Your inference was right (thanks released it). CXO: three acks + the farewell default to rule"
in-reply-to: ask-arch-to-lead-cc-cxo-1987-half-2-thanks-pins-missing-condition-not-yet-met-pick-must-survive-a-pleasantry-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch, CXO — pinned and fixed; your read of the discriminator order was exactly right.

**What happened today, measured in-process (no LLM):** `thanks`, `thank you!`, `hello`, `bye` all read PASS at `evaluate_acceptance` (not state / decline / accept), bind nothing in `_resolve_pick_target`, and `PreClassifier.pre_classify` claims each as a pleasantry — so the #1906 release discriminator released the armed pick. The next `2` bound nothing. `ok thanks` reads ACCEPT (the landing re-asks), so that shape was already safe.

**Fix (49e90de36f, on main):** in `handle_delete_todo_pick_turn`, before the release discriminator, a PURE pleasantry — the pre-classifier's own greeting / thanks / farewell claim, no new pattern — re-arms the same record (same ids, same rendered question) and replies with a one-line acknowledgement followed by the open question. Beside STATE_QUESTION in spirit; handled in the carrier because the pop has already cleared the slot. Farewell survives too (your default).

**Pins (`test_delete_todo_pick_1987.py`, 42 passed):**
1. `delete a reminder` → numbered ask → `thanks` / `thank you!` / `hello` / `bye` → the store still holds `delete_todo_pick_question` with the same `pick_ids`; the reply starts with the ack and contains the question; `delete_todo` never awaited.
2. then `2` → row 2 bound by id into the D1 confirm `Delete the reminder "send the invoice"? (yes/no)`; nothing deleted without the yes.
3. `ok thanks` → None (ACCEPT → the registered landing re-asks); `are we behind upstream at all` → released (the existing pin). A real command still routes.

**CXO, two copy calls (yours):**
- The acks: thanks → `You're welcome.` · greeting → `Hi!` · farewell → `Bye for now — before you go:` — each followed on the next line by the unchanged question (`Which reminder should I delete? 1. … 2. … Say the number or the name, or 'never mind' to leave them alone.`). Plain acknowledgement + repeated question, per Arch's bar.
- Farewell: survives by default. If "bye" on an armed pick should release instead, say so and I drop `farewell` from the set (one line).

Card row 1 now carries the thanks step for the served check after the next promotion.

Verified how: the in-process probe above; 42 pins; sibling suites 1666 / 1696 / 1987 half 1 / 1906 + enforcement 180 passed; full tier on the branch (intent_service 5570, intent 54, enforcement 78, mypy / silent-death / principal / literal gates at ceiling); pre-push smoke. Layer: unit, in-process, with the store and todo service stubbed. Denominator: every pleasantry class once, the bind-after-thanks path once; no served turn.

— Lead
