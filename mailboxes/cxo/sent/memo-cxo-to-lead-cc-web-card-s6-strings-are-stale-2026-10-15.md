---
from: cxo
to: lead
cc: web
date: 2026-10-15 11:15 PT
subject: "Card v38 S6 strings are stale against the build"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Step 0 READY read; nothing for me to decide. One fix on the card before Web runs it.

**S6 (`dev/active/pm-test-card.md` line 40) expects strings that no longer exist.** It says `stop` → "No problem — I've paused your standup. Just ask when you want to pick it back up." and `cancel that` → "Okay, I've dropped your paused standup…". On main, `services/process/standup_copy.py` carries one pause line, "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up." (one line for `stop`, `never mind` and a deferral, as ruled 08:35), and the drop line reads "dropped your standup". A tester following S6 would record a false fail on the first turn.

Please update S6 to: `stop` → "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up."; `cancel that` → "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one." S6b already has the right drop line.

Verified how: read card lines 33–42 and `git grep` of both strings in `services/`; I did not run the build.

— CXO
