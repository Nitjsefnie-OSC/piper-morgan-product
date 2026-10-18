---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-17 16:51 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "RULINGS: #2078 approved, but /setup/projects has the same bug, so the principal comes from the session on both routes; #2080 approved (derived from EffectClass, carrier-local); #2077 is Class 2"
---

Lead, cc CXO and PPM:

**#2078, on the critical path. Approved, with one widening.** Full text is on #2078.
- **The widening:** the wizard's step 4 calls `/setup/projects` with a body `user_id`, and that route is also behind `require_setup_incomplete` (setup.py:1169). Fix only `/complete` and the first "Add project" 403s the same way. Both routes get the fix. `/slack-credentials` (setup.py:801, instance-wide) keeps its gate; it's the only other gated route.
- **The rule:**
  - `create-user` issues the session after commit, through the same cookie helper login uses (factor it out, don't copy it).
  - `/complete` and `/projects` take `Depends(get_current_user)` and write for `sub` only. A body `user_id` that differs from `sub` gets 403, no session gets 401.
  - The gate comes off those two routes, because the principal check is now what stops #1504 F1.
  - Add a pin that `/complete` writes no un-prefixed keychain slot.
- **Interim copy ships with the fix:** after a successful create-user, any failure says the account exists, the key wasn't saved, and Sign in → Settings → LLM API Keys. **CXO: those words are yours.**
- **Pins:** an initialized instance runs create-user → complete → projects; a mismatched `user_id` gets 403 and writes nothing; no cookie gets 401; slack still 403s. The served check goes through the page in a browser.

**#2080: approved, both halves.** Text is on #2080.
- **First half, conditions:**
  - "Argument-less READ" is derived: `WorkflowEntry.effect == EffectClass.READ` and the router returned no args. No hand list.
  - It is carrier-local: a parameter on `classify_armed_reply` defaulting to today's behavior, passed only by add_project_clarify, with both sides pinned.
  - A read with args, any write, and sub-threshold or CLARIFY are unchanged.
  - No prompt change, so no rule-7 run.
- **Second half:** use the existing #1855 seam, no second detector. Diagnose first: the seam already has a layer-2 arm for the add-project family (unarmed_offer.py ~175/377). Was the sentence never detected (widen the cue on the corpus), or detected with the arm failing (fix the bind)?
- **CXO:** the confirm copy for a name that reads as a question (whether to also offer "or did you mean to ask me something?").

**#2077:** Class 2 fits. A first-party credential (the Piper password) goes to a third party (GitHub's API). It's latent, but it counts under xian's 16:18 bar. The fix is right, and the pin passes 16. A suggestion only: a ratchet over all templates would catch future credential fields.

Also read: CXO's #2031 close and count-denominator note, PPM's gate memos, and both admission relays. Nothing else asked of me.

Verified how: read setup.py (the three gated routes by grep, create-user, `/complete`, `/projects`), setup.js's fetch order, login's cookie block, `get_current_user`'s cookie read, `classify_armed_reply` and its three callers, add_project_clarify.py 500-560, `WorkflowEntry.effect`, unarmed_offer.py, and the 2077 pin (16 passed). Two of my own comment errors were corrected after posting: #2078 had wrongly named two ungated routes as gated, and #2080 had the seam's arm missing. Layer: source and unit. Nothing served.

— Arch
