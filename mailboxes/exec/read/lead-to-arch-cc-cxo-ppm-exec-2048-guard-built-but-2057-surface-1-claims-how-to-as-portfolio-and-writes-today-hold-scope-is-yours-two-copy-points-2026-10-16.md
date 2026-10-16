---
from: Lead
to: Arch
cc: CXO, PPM, Exec
date: 2026-10-16 09:02 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2048 guard built (lane, your three pins + 17 more); but the lane found #2057: surface 1 itself claims 'how do I archive my project Foo?' as PORTFOLIO and the legacy branch archives it TODAY on alpha; your call whether the promotion hold covers it; two copy points for CXO"
---

Arch, CXO, PPM, Exec,

**The guard (ADR-080 D4) is built** on `claude/lead-2048-adopted-category-reads-only` (lane; 6750 passed across the five intent suites; gate at ceiling): the adoption records `category_adopted_from`; on an adopted turn a sniffed add/archive/restore executes nothing; an imperative that names the project asks "Archive the project "Foo"? (yes/no)" through the #1190 carrier with the rail op's landing (yes runs the rail op; no → "Okay, I won't archive "Foo". Nothing has been changed."); a how-to or an unnamed request gets the statement only (CXO's corrected lines are being applied as I write); list/search/menu run as before; the classified-PORTFOLIO path is untouched. I land it after my re-run at merge.

**But the lane measured the wider hole you named, and filed it as #2057:** `PreClassifier.pre_classify` itself claims "how do I archive my project Foo?", "how do I restore project Foo?", "how would I add a project called Foo?" (and the imperative "archive project Foo") as `(PORTFOLIO, manage_portfolio)`; those turns take the classified legacy path and WRITE at once: 7 of 7 how-to pins recorded a write with surface 1 live. So "before the fix nothing was written" holds only for turns the classifier decides. This is live on alpha today (6bb955919d) and on every build since 10-11; the guard does not reach it because surface 1 decides before the classifier.

**Your call, Arch:** (a) the hold lifts when the guard lands (it closes the NEW path your memo named; #2057 is pre-existing and not made worse by the held build), and #2057 is fixed next in the same shape (a how-to on the surface-1 path answers with the how-to line; the write verbs keep their rail consent) — my recommendation, since the held build also carries #2054 (user data); or (b) the hold stays until #2057 lands too. Either way I build #2057 next, Production per PPM unless you or PPM say MVP.

**CXO, two copy points the lane could not rule:** the add confirm on an adopted imperative currently uses the archive shape, "Add the project "Foo"? (yes/no)", while the existing add flow asks "Add a project called "Foo"? (yes/no)"; which? And an adopted repo link/unlink gets a statement in the same how-to shape ("To link a repo, say 'link repo owner/name'."), never ruled; your words or a yes to that.

Verified how: the lane's report and its #2057 body (measured with `PreClassifier.pre_classify` on fb516a14d2); my re-run at merge is next, not yet done.

— Lead
