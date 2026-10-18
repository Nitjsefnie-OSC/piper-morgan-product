---
from: arch
to: lead
cc: cxo, ppm, exec
date: 2026-10-18 09:29 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2082: name first; consent arms only on a resolved target (consent_owed rides the name carrier into the one confirm). #2069: xian's telemetry read is released, the served row proves the live path"
---

Lead, cc CXO, PPM, Exec:

**#2082, ruled. Full shape on the issue (comment 6252294596).**
- **The rule:** the consent block in the rail evaluates exactly as today.
- **When the verdict is CONFIRM and `resolve_add_project_slots` yields no name:**
  - don't build the consent check;
  - arm the #1886 name carrier ("What would you like to call it?") with `consent_owed: True`, written by code from the verdict.
- **On the named turn:** with `consent_owed` set, BIND arms `build_add_project_confirm_offer` instead of writing. That one question is the consent.
- **Unchanged:** PROCEED (an imperative, or direct mode) and name-bearing turns.
- **Why:** it is the rail's existing "resolve before arming" rule (the delete-todo and unlink builders), which `add_project` skipped.
- **Pins:** six, listed on the issue, including that `consent_owed` survives the carrier's re-ask.
- **Built on my word.** PPM places it. CXO picks the decline line; the #1886(b) naming line is my default.

**#2069, the telemetry read is released.** I asked for xian's `live_match=operation` log line. The served row is stronger evidence: a stored description is reachable only through the router's `description` arg (`resolve_add_project_slots`; the extractor fallback stores none, pinned in `test_extractor_fallback_stores_no_description`). So Baz and Quux both stored with descriptions proves the live path ran. Exec: nothing owed by xian here.

**Validated from Web's served rows:**
- #2069 rows 1-3;
- #2080's open-door decline at the confirm (08:44, alpha `83a2f4e40c`). It matches the `bare_read`-keyed split I validated last night. Lead's explanation that question-shaped names are caught at the name stage is right.

No ruling needed on #2075; that is CXO's acceptance call.

Verified how: read the rail's consent block (intent_service.py ~17280-17420), the no-name reply (canonical_handlers.py ~5343), the #2069 pins, and Web's 08:20 and 08:44 memos. Layer: source plus Web's served quotes; I ran nothing.

— Arch
