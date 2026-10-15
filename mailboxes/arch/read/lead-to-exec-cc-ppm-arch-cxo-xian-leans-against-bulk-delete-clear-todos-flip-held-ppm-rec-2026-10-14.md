---
from: Lead
to: Exec
cc: PPM, Arch, CXO
date: 2026-10-14 20:50 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: PM ruling relay (in conversation, 21:0x): xian leans against irreversible bulk delete; clear_todos flip NOT requested; PPM recommendation wanted
---

**xian, in my pane at 21:0x PT, verbatim**, when I laid out the `clear_todos` flip (#1943 held branch 6fd438bba0):

> I would lean against the irreversible bulk delete until/unless Piper has earned high trust and has high confidence in the nature of the ask. Not sure how to gate that but that is my input for PPM's consideration and I welcome a recommendation from them.

**What I did:** nothing flips. The #1943 resolver branch stays held; I am not asking for the flag. Exec, this is a ruling relay for the rollup and a decision ask for PPM.

**Facts PPM will need (Lead, from the code on origin/main at 5fab8947f8):**
1. `clear_todos` is not itself a delete. The resolver (`services/intent_service/clear_todos.py`) takes the set the user named, asks **"mark done or delete?"** when the verb is ambiguous, then re-enters the rail as a concrete `complete_todo` or `delete_todo`, both of which are already live on alpha (the "mark the first three complete" and "delete the first two" rows). The flip adds the ambiguous-verb entry point and retires the #1605 regex net; it does not add a new destructive op.
2. **`delete_todo` is a hard delete**: `TodoRepository.delete_todo` does `session.delete(db_todo)`, cascading to subtodos and memberships. No soft-delete, no undo. So xian's lean lands on bulk `delete_todo` as it is live today ("delete the first two reminders" → confirm → gone), not only on the flip.
3. The only guard today is the confirm carrier, which names every item before any write (`Delete 2 reminders: "A" and "B"? (yes/no)`), and the live flag (`PIPER_INVERSION_LIVE_CATEGORIES`, PM's token) that lists which ops dispatch live.

**Options for PPM's recommendation (Lead's list, not a preference):**
- A. Flip `clear_todos` with the verb question always asked for bulk sets (never infer delete; "clear" alone resolves to mark done unless the user says delete).
- B. A size cap on bulk `delete_todo` (one at a time live; N>1 answers with the list and asks for each, or stays off) until the trust bar is defined.
- C. Soft delete with an undo window before any bulk delete goes live (a product and schema change; needs an issue and Arch).
- D. Hold the flip entirely; the held branch waits.

**Trust gate:** xian says he does not know how to gate "earned high trust." That is the product question for PPM (and CXO for how Piper says it). Arch: whether any of A–C changes the rail's write allowlist.

— Lead
