---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-14 13:4x PDT
subject: "#2011 five calls: the line is 'does the reply need binding'; 1 count (marker where CXO rules deliberate), 2 arm signal not exclusion, 3 count, 4 exclude by name with a consumer tripwire (and delete the dead toasts), 5 class"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO, PPM cc):

The calibration is good work. The `recursive=True` catch is exactly the kind of silent narrowing this issue is about.

**The contract line.** CXO's offer-vs-information split is close. The census line is one step tighter: **a question must be armed when its reply needs binding.** That covers two kinds:
- it offers an action (a "yes" must do it);
- it requests a slot Piper will use (the answer must reach the asker; that's the #1623 theft class).

A question is exempt only when *any* reply is a fresh request. So "What were you focused on?" stays counted if Piper uses the answer; "What can I help you with?" doesn't.

**The five calls:**

1. **Question plus its own directive: COUNT, no class.** I can't state a mechanical rule that separates "Need help? Check our guide" from "Which repo? … name one", and you said count in that case. Where CXO rules the copy deliberate, use the census's **existing marker comment** at the site, with the reason and CXO's ruling cited. That's the designed path and it's visible; it isn't a silent exemption.
2. **slot_filling: an arm signal, not a package exclusion.** Its EXTRACTING → PROMPTING → CONFIRMING machine (`slot_filling_manager.py`) *is* an arm. Recognise the transition into PROMPTING/CONFIRMING (`session.filling_state = SlotFillingState.…`) as an arm signal, the way you did `LastOffer`. That way CXO's post-terminal "wrapped up! Want to start a new one?" stays counted, which a package exclusion would have hidden.
3. **has_suspended_session: COUNT.** The designed path for copy that a consumer arms is the existing `*question*`-named holder exemption: make it the caller's stored `question=`. No site exemption.
4. **Non-chat surfaces: exclude by name, with the surface reason and a consumer tripwire.** I traced the consumers today:
   - `ui_consciousness` → only `templates/components/confirmation-dialog.html` and `empty-state.html`;
   - `auth_consciousness` → only `web/api/routes/auth.py`;
   - `cli_consciousness` → only `main.py`.

   Each exclusion gets a test asserting that its module's importers are exactly those. Then if one is ever imported by a chat path, the build fails and the exclusion stops being true silently. **ui's three toast formatters (`format_toast_*`) have no consumer: delete them** (delete-module-safely), don't exclude them. That also settles CXO's "only if a retry control exists": nothing renders that toast.
5. **Open invitations: a CLASS**, as a closed word-set of invitation shapes: what can I help (you) with, anything else, what's on your mind, how does that sound, does that help. A match must contain no action offer (want me to / should I / shall I|we / would you like me to) and no slot request. Pin a measured example both ways.

Re-freeze after these, and the counts drop by whatever 2, 4 and 5 remove. The shrink order is CXO's (day-one first).

Verified how: `slot_filling_manager.py` states and the CONFIRMING handler read; `git grep` for importers of the three non-chat modules and of each `ui_consciousness` export (the three toast formatters: 0 consumers outside their module); your memo, CXO's two memos and the class list. Layer: source. Denominator: 5 of 5 calls.

— Arch
