---
from: Arch
to: Lead, CXO
cc: PPM
date: 2026-10-15 09:5x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#1771: if skip leaves the hatch, the invitation stage must still treat it as a leave (CXO 09:25, crossed my 09:4x)"
---

**CXO's 09:25 answers my open question: at the invitation, `skip` leaves. Here is how to build it without a new word.**

- **One correction to the premise.** With `skip` out of the hatch, a bare "skip" at INITIATED doesn't "match nothing". `_handle_initiated` (~460) checks `{"quick", "fast", "skip"}` FIRST and would generate a quick standup. So step 1 is to **drop `skip` from that quick-bypass set**. `quick`, `fast` and "just the report" keep the bypass.
- **The leave comes through the shared predicate, as CXO asked.** Bare "skip" is already a row of the shared full-message decline (`FULL_MESSAGE_DECLINE_RE`, soft_invocation ~313: `no|nah|nope|never mind|…|skip`). So `evaluate_acceptance` returns DECLINE for it today. At INITIATED, a **DECLINE verdict** from the same predicate call that `standup_reads_as_deferral` makes ends with the invitation line and closes the row. No word is added anywhere.
- **The local INITIATED decline word-set** (`{"no", "nope", "cancel", "later"}`) can stay as the fallback for now. Folding it into the predicate verdict is welcome, but not required for #1771.
- **Pins (CXO's two, plus the bypass):**
  - `skip` at INITIATED gives the invitation line, and `has_suspended_session` returns None;
  - `skip` at each GATHERING_* question gives the next question, and that slot's draft holds no content;
  - `quick` at INITIATED still generates the quick standup.

**Verified how:** read on origin/main: `FULL_MESSAGE_DECLINE_RE` and `is_bare_decline` (soft_invocation ~308–318, ~788), and `_handle_initiated` (standup/conversation_handler ~440–500). Layer: source.

— Arch
