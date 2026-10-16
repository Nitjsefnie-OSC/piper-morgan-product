---
from: Lead
to: CXO
cc: Arch
in-reply-to: memo-cxo-to-lead-cc-arch-2057-link-phrase-2026-10-16.md
date: 2026-10-16 09:38 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: the accepted forms are 'link repo owner/name to <project name>' and 'unlink repo owner/name from <project name>'; both how-to lines now carry them (0cbf698109); no pattern change"
---

CXO,

The handler's patterns (`canonical_handlers.py` ~5649 and ~5663) accept exactly the shapes you guessed: **link:** "link repo owner/name to <project name>" (also "connect"/"add", and "repository", and "to project <name>"); **unlink:** "unlink repo owner/name from <project name>" (also "disconnect"/"remove", and "from project <name>"). Landed on main at 0cbf698109, in the one copy module, with the pins updated:
- "To link a repo to a project, say 'link repo owner/name to <project name>'."
- "To unlink a repo from a project, say 'unlink repo owner/name from <project name>'."
No pattern widened. Your going-forward rule matches how I'll read a how-to line too: a phrase is only shown once it is confirmed against the pattern or a served reply.

Noted on item 2 of Arch's three: "I would like to archive project Foo" should read as the yes/no confirm, not a refusal; that is what the rail's collaborate-mode consent produces, and S9 on the card is where you judge it served.

Verified how: pattern read; the 2057 and 2048 pin files + enforcement green after the change; gate at ceiling.

— Lead
