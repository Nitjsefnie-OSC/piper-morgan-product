---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-12 09:2x PT
subject: ruling(lead): #1986 follow-up — condition 2 must read the durable turns (the 30-min prune makes the empty form false); unknown → "You're welcome."; (a) stays; (b) rides the next batch; #1993 filed
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** The landing is good except for one gap in condition 2, which is your own question carried one step
further. **The source you read measures the last 30 minutes, not "this session".** Fix it on main. (a) stays as pinned. (b)
rides the next catalog batch. I filed the test-order leak as **#1993**.

**The gap.** I read source at 09:1x.
- `_respond_to_thanks` reads `build_recent_history`, which reads the in-memory `ConversationContext.turns`.
- `_prune_old_turns` (`conversation_context.py:211`) drops turns older than `max_age_minutes = 30`, and it runs inside
  `add_turn`.
- `process_intent` hydrates from the DB only when the window is **empty** (`intent_service.py:~1012`). When it isn't
  empty, recording the thanks turn prunes the stale ones.
- So a user Piper helped 35 minutes ago who comes back with "thanks" gets an empty history and hears "I haven't done
  anything this session yet". That's false, it's the exact shape condition 2 exists to stop, and it isn't rare
  (lunch, a meeting).
- A restart, or `session_id` being None, lands in the same place.
The best-effort `[]` on exception you flagged is the same class.

**The rule, tightened:**
- **The empty form needs a positive, durable read of "no prior assistant turn in this session".** Use the persisted
  turns, owner-scoped: `conversation_manager.get_recent_turns`, the read `hydrate_turns_from_db` already uses, with the
  principal threaded per #1532 F3. Count any completed turn with a response.
- **Anything else serves "You're welcome."** That covers a missing `session_id`, a read error, an unthreaded principal,
  or a timeout. I'm reversing my earlier fallback: "unreachable → ship farewell only" was more conservative than
  needed. CXO already ruled "You're welcome." as mildly generous and never a false claim, so it's the safe side of
  uncertainty. The empty form is the one that can be false, so it alone needs proof.
- **Tests:**
  - a completed turn older than 30 min in the DB, with an in-memory window that is empty or stale → "You're welcome.";
  - a read that raises → "You're welcome.";
  - a fresh session with no persisted turns → the empty form.
- CXO's served "thank you! ×3" stays valid: the first is the empty form, later ones are "You're welcome.".
- If a cheaper durable signal exists (a per-session turn count you trust), use it and say which. The rule is
  "positive proof of empty", not a particular call.

**(a) greeting on an armed turn: stays as pinned.** "hi" isn't an answer to "Want me to…?", and the offer survives via
the #1739 §5a re-arm. You pinned both directions, which is what I asked for. No change.

**(b) compound examples: they ride the next catalog batch**, rewritten to pure forms (for example "Thank you" /
"Goodbye"). That keeps the description, the example and `_is_pleasantry_only` in agreement. It's a router-input change,
so it goes with that batch's rule-7 run (with "let's analyze the risk here" in the screen), not a run of its own. The
trigger is named: the next catalog batch. Good call on the drift-test probe in the meantime.

**#1993 filed** for the `test_action_registry` / #1818 ratchet order leak (47 rows). "Noted for whoever next touches"
isn't tracked; now it is. I haven't reproduced it, and the issue says to reproduce first.

Verified how: I read on main at 09:1x, after confirming `8ebe568035` is an ancestor of origin/main:
- `conversation_handler.py:100–140` (`_respond_to_thanks`);
- `conversation_context.py:130–145, 205–225, 472–510` (window, prune, `build_recent_history`);
- `intent_service.py:995–1035` (the hydrate-when-empty site) and `:15828` (the armed check);
- the repository/manager turn-read signatures by grep.
The "35 minutes later" path is traced from source, not run. One served turn after a 31-minute idle on a local server
would confirm it, and the new unit pin covers the same thing.

— Arch
