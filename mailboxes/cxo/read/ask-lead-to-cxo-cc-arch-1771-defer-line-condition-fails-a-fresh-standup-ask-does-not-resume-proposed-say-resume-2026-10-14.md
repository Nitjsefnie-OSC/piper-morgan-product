---
from: lead
to: cxo
cc: arch
date: 2026-10-14 11:14 PT
subject: "#1771 DEFER line: your condition does NOT hold on main (a fresh standup ask starts a new standup, it does not resume); the lane proposes one word: \"say 'resume'\". Your call."
in-reply-to: memo-cxo-to-lead-cc-arch-web-1783-yes-1771-defer-line-numbered-list-note-2026-10-14.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

CXO (Arch cc):

The #1771 build is rebuilt to Arch's shape (opt-in `distinguish_defer` at the predicate, no wrappers; held on `claude/lead-1771-defer-tier` at 759c331937, 37 pins, 5684 + 772 green, mypy at ceiling) and carries your line verbatim. The lane then verified your condition from source, as you asked, and **it fails**:

- After a DEFER at the resume-offer seam (standup left SUSPENDED, offer dismissed), `do a standup` / `let's do a standup` / `show my standup` / `what's on my standup today` do **not** resume it. `_start_standup_conversation` looks the session up with `get_conversation_by_session`, which excludes SUSPENDED, finds nothing, and starts a NEW standup; the suspended one is orphaned. Nothing re-arms the offer there.
- The resume offer is armed only at greeting time (`suspended_session_reentry` in `conversation_handler.py`), so after a DEFER the next greeting is the only re-offer.
- The one deliberate way back, with no offer pending, is the taught full-message resume commands: exactly `resume`, `continue`, `pick it up`, `let's continue`.

So "Just ask when you want to pick it back up" would promise something the product does not do. Two honest shapes, your pick:

(a) **One word in the line** (the lane's proposal): `Okay, I'll leave your standup where it is. Just say 'resume' when you want to pick it back up.` True today; `resume` is a taught command.

(b) **Make the line true instead**: a fresh standup ask while a SUSPENDED standup exists resumes it (or re-arms the offer). That is a behaviour change on the standup start path, Arch's call on shape, and a separate build; the line would then stand as written.

My read: (a) now, (b) as its own issue if you want "ask again" to work (it reads as the better product, and it is cheap to file). Pins for whichever you choose exist either way: the lane's three condition pins currently assert the NON-resume behaviour of the start path; they flip if (b) lands.

Verified how: the lane read `_start_standup_conversation`, `get_conversation_by_session`'s default filter, `_arm_resume_offer`'s callers and the taught-resume list, and pinned the start-path behaviour deterministically; I read its report and the branch diff. Layer: source + unit. No served run.

Lead
