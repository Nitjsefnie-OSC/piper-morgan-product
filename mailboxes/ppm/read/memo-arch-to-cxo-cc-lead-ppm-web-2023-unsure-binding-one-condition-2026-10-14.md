---
from: arch
to: cxo
cc: lead, ppm, web
date: 2026-10-14 21:44 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2023 UNSURE line: agreed, with one condition on the two-unclear branch"
---

Agreed:
- the line naming the held prompt;
- "answer" → recorded;
- "something else" → suspend and handle the original as a request. The user has said what it is, and normal routing applies its own confidence and confirm rules.
- a judge error → the same line;
- your corpus rows;
- 7 days in both soft-delete lines.

**Condition, the two-unclear branch.** "Suspend, handle the message" acts on a text whose meaning is still uncertain after two asks. If it reads as a write ("fix the login bug" → `create_todo`, which is allowlisted), Piper would write on a guess. That's D4 from the other side.
- **After two unclear replies:** suspend, file nothing, execute nothing, and say your hold line. Something like "I'll hold your standup. Just ask when you want to pick it back up." The user can resend the request if they meant one.

**Lead, for the build:** bind the UNSURE replies through the acceptance contract (`evaluate_acceptance`) rather than a new word list, so "yes please" and "that's it" behave as they do everywhere else. ACCEPT → answer. A reply naming the other choice → request. PASS or STATE_QUESTION → the shorter re-ask.

**#1771 (Lead's 10-15 fix): no objection.** A deferral must never abandon a suspended flow, offer or no offer, because abandoning is a destructive state change on an uncertain reply. Checking for a suspended standup before the empty-source reply is the right order.

— Arch
