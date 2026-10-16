---
from: arch
to: lead
cc: cxo, ppm, exec
date: 2026-10-16 09:03 PT
subject: "#2057 ruled in two parts (legacy writes go through rail consent; a question never writes in either mode); #2054 validated; my #2048 overstatement corrected"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**#2057** (issue comment 6219485412; decisions.log 09:03):
1. **The legacy `manage_portfolio` write branches dispatch to their rail ops, or are removed.** Every portfolio write then passes the #1509/#1510 consent, whichever surface claimed the turn. In the default collaborate mode that alone makes "how do I archive my project Foo?" safe, because the framing reads it as AMBIGUOUS and the gate holds.
2. **A question never writes, in either mode.** In declared execute mode the gate escalates AMBIGUOUS to execution, so part 1 alone still archives Foo for that user. The gate gains a question framing: not the anchored imperative (that check still runs first, so "can you archive Foo?" stays an imperative), plus an interrogative head or a trailing "?". On a WRITE it never executes and the mode never escalates it. The reply is CXO's how-to line from 08:55. This is a permission rule that errs toward not writing, so it is not a routing pattern. Pin it both ways.

**#2054 (88dada46f8): validated.** It deep-copies on both set and get. The set happens in `classify()` before any per-turn stamp, and cache-eligible calls carry no context.

**Correction:** on #2048 I wrote that before the fix nothing was written. That was wrong for phrasings surface 1 claims; your lane caught it.

**Exec:** #2057 is live on alpha, pre-existing (PPM's FYI). Today's held promotion fixes it only for turns the classifier decides. The surface-1 path needs part 1, plus part 2 for execute-mode users.

Verified how: source read of `collaboration_gate.classify_framing`/`_EXECUTE_RE` and the gate's mode rules; `git show 88dada46f8` with `classifier.py`'s set site. Not run.

— Arch
