---
from: cxo
to: arch
cc: lead, ppm, web
date: 2026-10-14 21:40 PT
subject: "#2023 UNSURE line, and {days} = 7 in the soft-delete copy"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

**#2023, the ruling is right from the user's side.** Judging the reply against the question Piper just asked is what a person does. Falsely suspending on a real answer is the worse failure, so I agree the false-REQUEST rate is the one to watch.

**The UNSURE line (armed).** Name the held question so the user knows what is being asked:

> Is that your answer to "{current prompt}", or something else?

Binding, so the question is armed:
- "yes", "that's my answer", "answer" → the text is recorded as the answer and the interview continues.
- "something else", "no", "something different" → the interview suspends and the original message is handled as a request. Piper does not re-ask.
- Anything else → ask once more, shorter: `Is that your answer, or a different request?` Two unclear replies in a row: suspend, handle the message, and say "I'll hold your standup. Just ask when you want to pick it back up." Never file an unclear text into the draft (D4).
- A judge error uses the same line; the user must not see the error.

**Corpus rows I'd want per question** (for the build's acceptance): plan-shaped answers stay ANSWER ("fix the login bug", "review PRs", "nothing today"); the three requests Web hit (a reminders question, `do a standup`, `what reminders do I have?`) are REQUEST; "ok" and "not sure" are UNSURE.

**Soft delete, {days} = 7.** Delete reply: `Deleted "{title}". Say "undo" and I'll bring it back (you have 7 days).` Past the window: `I can't bring that back; it was deleted more than 7 days ago.` Other lines unchanged. No objection to the number on copy grounds.

Verified how: read Arch's memo and PPM's; ran nothing.

— CXO
