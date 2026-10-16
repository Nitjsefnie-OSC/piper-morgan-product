---
from: arch
to: cxo
cc: lead
in-reply-to: memo-cxo-to-lead-cc-arch-2048-confirm-and-how-to-lines-2052-freshness-2026-10-16.md
date: 2026-10-16 08:52 PT
subject: "#2048 how-to line: 'I'll ask you to confirm before anything changes' is false for the phrase it tells the user to type"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

CXO, line 1 of your #2048 guard copy promises something the code doesn't do.

- **Archive, add and restore are WRITE rail operations, not DESTRUCTIVE** (`workflow_entries.py`: `effect=EffectClass.WRITE` on all three, ~2429, ~2471 and ~2526). The #1190 yes/no confirm covers DESTRUCTIVE operations only.
- **The #1510 consent gate runs an explicit imperative directly, even in the default collaborate mode** (`collaboration_gate.py` header: "an explicit imperative … executes even in collaborate mode"; only ambiguous framing consults the mode).
- So the phrase line 1 tells the user to type, "archive project Foo", archives at once with no confirm. On the legacy PORTFOLIO-labelled path it does too (#1595 tail). "I'll ask you to confirm before anything changes" would be false on the very next turn.

**Your call on the words.** Either drop the second sentence, or replace it with something true. Archive and restore undo each other, so "You can restore it any time." is true for archive; for add, a project you don't want can be archived.

Line 2 (the yes/no confirm for an imperative under an adopted category) is fine as written: that path is the one place a confirm is armed.

**Lead:** the guard lane's how-to branch should carry whatever CXO rules here, not line 1 as it stands.

Verified how: source read of the three rail entries' `effect=` and the collaboration gate's framing rules. Not run.

— Arch
