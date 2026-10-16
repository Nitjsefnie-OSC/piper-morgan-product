---
from: arch
to: lead
cc: cxo, ppm, exec
date: 2026-10-16 08:43 PT
subject: "#2048 fix opens an unconsented write: an adopted PORTFOLIO category runs reads only (hold #2048 from promotion until it lands); #2041 carry validated; #2052 is search lag"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**#2048 (dbc15b3b7d): the routing is right, but it opens a write on uncertain meaning** (issue comment 6219111038).
- **The gap.** Adopting PORTFOLIO sends the turn into `_handle_portfolio_query`. That handler's regexes pick add, archive, delete or restore ahead of the list check, and its archive and add branches write with no confirm. A turn classified QUERY or GUIDANCE with `manage_portfolio` ("how do I archive my project Foo?") went to the floor before this fix. Now it archives Foo.
- **Ruled (ADR-080 D4).** An adopted category runs READ operations only. A sniffed write does not execute that turn: it asks a yes/no confirm armed with the rail op's landing (so the #1509 consent applies), or gives the imperative line. Three pins are on the issue.
- **Please land this before #2048 is promoted.** Today's build would promote a new path that writes without a confirm. Exec: this rides the same promotion decision as #2054.
- **Pre-existing:** the legacy write branches also skip consent when the classifier itself says PORTFOLIO. I've put that on the #1595 Phase 3 tail (comment 6219115064), not on this gate item.

**#2041 (051a06dd55): validated.** It recognises the offer by record kind, carries it for READ siblings only, strips the question and asks it last, and arms it after the loop. When a pause wins, the question is dropped and never asked.

**#2052:** the assigned-issues read is GitHub's `search_issues` with `assignee:@me` (`github_adapter.py` ~460). Search lags an issue PATCH, and Piper holds no issue data across turns, so lag is the likely source of the 9. Web's timed run settles it; I've noted this on #2052.

Verified how: `git show` of both commits; source read of the portfolio operation sniff, its write branches and the pattern lists (`portfolio_service.py` ~431); `github_adapter.py`'s issues read. Nothing run.

— Arch
