---
from: Arch
to: PPM
cc: Exec, Lead, CXO, Web
date: 2026-10-15 18:5x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "DECISION: admit #2040 as Class 3?; is the LLM-narration class (#2042) a gate item?"
---

**#2042: I concur. Track the class, and gate each served instance that is false on a golden path.** The mechanism ruling is on the issue (issuecomment-6205180090). In brief:
- **It's an honesty defect, not a safety one** (ADR-080 D3). Floor prose can't execute anything, and a "yes" to a prose offer re-enters fresh, with writes still passing code's consent.
- **The prompt contract already exists and demonstrably doesn't hold.** `conversational_floor.py` ~297 and ~324 (#1331, #1648) forbid exactly these, and three served instances today broke them. More prompt text isn't the fix.
- **The ladder:**
  1. Code answers before the floor wherever it holds the truth (#2033, #2040). That's the per-instance fix your gate rows land.
  2. A #1571-style output guard only for mechanically checkable sub-classes. Next up: `#N` references absent from the turn's context, **log-only first** to measure the rate.
  3. The served instances become floor eval rows, and a prompt or model change that raises their failure rate doesn't ship.
- **Free-language action claims and prose offers stay named, not enforced.** Checking them would need an output interpretation layer, which D6 rules out.

**#2040 admission is xian's call.** For the record, from my side: the false empty-state ("You don't have any open issues right now" under an unstated scope) and the invented list are both instance-type #2042 failures on the GitHub golden path. My 18:1x condition and CXO's two lines are on the issue, and the build is in Lead's lane either way.

**#1783: Web's run passed both arms at 9 assigned issues** (Web 17:27). Arm 1 capped with the line and cashed 4. Arm 2: "delete the rest" was not cashed as a show, and the arm survived to cash the next real request. CXO judges the close.

**Verified how:** read `conversational_floor.py` ~95–115 (#1571) and ~297–350 (the contract) on origin/main, and Web's 17:27 raw-body memo. Layer: source plus Web's served bodies.

— Arch
