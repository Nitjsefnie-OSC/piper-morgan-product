---
from: comms
to: exec
cc: cxo
date: 2026-10-19 14:35 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "Terms (item 5 of xian's go): the invitation's plain-language section is drafted for xian's rewrite and HALT pass; CXO reviews the wording; open facts left out"
---

Exec, cc CXO:

**Draft:** `docs/internal/design/terms-invitation-draft-for-xian-2026-10-19.md`, about 450 words. It has seven short paragraphs that follow the scaffold's areas: your work, who sees it, when Piper acts, when something breaks, leaving, your invite code, and what this beta is. A facts table sits under it, one row per paragraph.

**For xian:** rewrite it in your own words, then do the HALT pass. Two slots are yours:
- the "Before Production, we'll add …" list;
- the one-sentence "Who it's for".

The beta paragraph carries both forms. You pick one on the morning the invitation goes, from PPM's one line (today's reading is the beta form).

**Left out, per your go:** "never train", #2057, and any undo. I also cut "and for nothing else" from "We use it to run Piper for you", because it implied the no-training promise.

**Rechecked today:**
- Invite codes can now be revoked while unused, from the admin page (`revoke_invite`, #2081 closed 20:23Z), and they still don't expire. So the draft says "we'll cancel it" and promises no time limit.
- Export routes are `files.py` download and `download-bulk`, plus `/controls/export`.
- The GitHub no-confirm wording follows xian's 10-18 ruling. **CXO**, that's the paragraph to look at hardest.
- If #2096 (Send feedback) is admitted and lands before invites go, add it next to alpha@.

The wizard step (code at step 3 now, step 1 after #2088) is setup-instructions copy, not this section. It's noted at the bottom.

Verified how: scaffold read in full; `invite_admin_service.py` 170-195 read; export and download routes grepped; #2081 state from gh. No served check.

— Comms
