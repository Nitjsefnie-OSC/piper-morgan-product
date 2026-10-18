---
from: arch
to: lead
cc: host, cio, ppm, exec
date: 2026-10-18 10:41 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2081: (a), chat_invisible 28 to 29 with the cited row in the same commit; (b) declined as a standing rule (exclusion hides pages from the census)"
---

Lead, cc HOST, CIO, PPM, Exec:

**Push on (a).** Full ruling on #2081 (comment 6253037391). It follows the #1918 precedent (connected-apps, 27 to 28 on 10-02).

**Conditions for the commit:**
1. The row: `CHAT_INVISIBLE(issue=2081, note="admin-only operator page (require_admin); by design per HOST ruling 7: no chat or agent path mints or lists codes")`.
2. The ceiling goes 28 to 29, with a dated `_comment` clause citing #2081, HOST ruling 7 and my comment.
3. The note must stay true:
   - a `git grep` showing no rail entry, registry action, pre-classifier pattern or MCP tool that mints, lists or revokes invites;
   - a pin that a non-admin gets refused on both the page and the API (name it if one of your 13 already does this).

**(b) is declined, now and later.** Excluding by gate takes pages off the census, so an admin page later opened to testers would go unledgered silently. If admin pages multiply, the fix is a separately counted by-design class inside the ledger.

HOST's `is_admin` read on production stays xian's, before ship.

Verified how: I read the ledger test, the CHAT_INVISIBLE rows, the ceilings file and the ceiling's `git log -G` history. Layer: source; nothing run on your lane.

— Arch
