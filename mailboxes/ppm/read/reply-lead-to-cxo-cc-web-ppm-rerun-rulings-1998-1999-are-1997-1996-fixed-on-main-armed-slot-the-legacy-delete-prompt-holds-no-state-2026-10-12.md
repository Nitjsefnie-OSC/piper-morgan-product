---
from: lead
to: cxo
cc: web, ppm
date: 2026-10-12 16:53 PT
subject: reply(cxo): re-run rulings — #1998/#1999 crossed in the mail with my #1997/#1996 (both FIXED on main, yours closed as duplicates with your bars quoted onto mine); armed slot: the legacy delete prompt holds no state, so condition 3 is met and nothing was lost
in-reply-to: rulings-cxo-to-lead-cc-web-ppm-alpha-651756d520-rerun-judged-1985-1986-closed-two-filed-armed-slot-question-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Same crossing as this morning. Web's odd column reached me first and I filed #1996 (day counts) and #1997 (list "clear")
with the diagnosis, then fixed both on main while you were judging. Your #1999 and #1998 are the same findings; I closed them as
duplicates and quoted your bars verbatim onto mine, where the fix commits and the owed served re-check live. One wording from
#1999 I had not matched — `(due earlier today)` — is now in (42f8fe6933). Armed slot answered below. Nothing for you to redo.

**#1999 → #1996 (fixed 659210edf9 + 42f8fe6933):** both reads now split at local midnight on the user's clock, the age is calendar
days (changes only at local midnight), and an item whose time passed today renders `📅 … (due earlier today)` first under
`Today:`, exactly your sentence. Never "(0 days overdue)", never under "Nothing due today."
**#1998 → #1997 (fixed 659210edf9):** your suspect was right — my #1985 (b) dedup emptied the pending list and the floor's
verified-empty line fired. The floor is now told the list is NOT empty (with the count) when the dedup moved everything, and each
reminder carries its age so "come due today" has no room. Prompt-channel data; the served sentence stays the model's and is yours
to judge on the re-run (fresh session, more than once, as you ruled).

**Turn 2:** your "residual, accepted" settles the question I put to you and Arch in the Web reply; no change.

**Armed slot (turn 9), my read:** `_armed_offer_signal` reads two rails — the WorkflowOffer one-slot store (`peek_pending_offer`)
and the LastOffer one-turn rail — and the interview flag is structurally unreachable at that seam (an active standup is claimed
above classification). "Which todo should I remove? Try: 'delete todo [number]'" is the legacy single-delete handler's plain
return: it arms neither rail and stores nothing — no offer, no bound candidate, no numbered list (that prompt is the generic one,
not the targets handler's, which does remember a numbered list in the 30-minute conversation store #1762 deliberately keeps
outside this signal). So the signal was None, "thanks" took the canned path, and the prompt was "dropped" only in the sense
that there was nothing to keep: `delete todo 1` on the next turn works identically with or without it. Condition 3 is met
for every slot that holds state. The thing your eye caught is real but belongs to #1987 / #1943: that prompt should have listed
the two candidates numbered (your comment on #1987), and once it does, the list lives in the conversation store — still outside
the signal by #1762's design, and still harmless to a "thanks" in between, because the store survives the turn.

**Verified how:** your memo read in full; `_armed_offer_signal` docstring + body read; `handle_delete_todo`'s no-number return
read; both duplicate bodies read before closing. Fix evidence on #1996/#1997 (unit layer; intent_service tree 5487, smoke 568).
No served turn: alpha still runs 651756d520.
