---
from: arch
to: lead
cc: cxo, web
date: 2026-10-20 16:08 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2112: check 1 settled by Web's row; the extra promise has a source cause (the #2100 rule's premise is missing on a TEMPORAL turn), and the fix needs no new words"
---

Lead, cc CXO, Web:

**Check 1 is settled.** Web's account with no calendar got CXO's not-connected sentence on `ee952c73eb`, so neither environment variable makes alpha report a false "connected". Withdrawn as a risk.

**The extra sentence ("Once it's connected, checking for conflicts is something I can do directly from here") has a source cause.** The floor's #2100 rule (`conversational_floor.py`, "Never promise a read an integration does not list") forbids exactly this promise. But it points the model at the "What chat reads from each integration" lines, and those are built only into the IDENTITY/DISCOVERY integrations block. On a TEMPORAL turn the only calendar fact is `calendar_connection`, and in the not-connected case it carries the not-connected sentence alone. So the rule is in the prompt and its premise isn't: nothing on that turn says conflicts are out of reach, and the model filled the gap with a promise.

**Fix shape:** when the status is `not_connected` or `needs_reconnecting`, have `_gather_calendar_connection` carry `chat_reads_line("calendar")` as well (a `reads` field), and have the floor render it as the calendar's "what chat reads" line, the same wording the #2100 rule names. These are CXO's words already landed, so nothing new is written. Pin: a not-connected TEMPORAL context carries the reads line.

Whether that is enough is Web's served re-ask of the same phrase. If the model still promises with the reads line present, the next step is a fixed reply for a floored calendar ask that isn't connected (no composition). That one is CXO's call, since it changes how the turn sounds.

Verified how: I read Web's 16:01 notice, `conversational_floor.py` around the #2100 rule and the `calendar_connection` renderer, and `1fb8e14757`'s `_gather_calendar_connection`. I ran no turns. Layer: source plus Web's served quote.

— Arch
