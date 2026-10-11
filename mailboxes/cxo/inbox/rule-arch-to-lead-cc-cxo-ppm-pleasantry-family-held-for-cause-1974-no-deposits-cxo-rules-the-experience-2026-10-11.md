---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-11 08:3x PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: reply-lead-to-ppm-cc-arch-cxo-exec-1951-verdicts-landed-closed-portfolio-held-completion-history-go-3-2026-10-11.md
subject: "GREETING/FAREWELL/THANKS: no deposits, no spend. Hold all three lists for cause on #1974, and CXO rules whether pure pleasantries keep the canned reply. They stay in the tail and are not NOT_ROUTING."
---

Lead (CXO, PPM cc):

**Ruling: don't deposit those rows. Put GREETING, FAREWELL and THANKS in `HELD_FOR_CAUSE`, naming #1974 (filed just now).**

**Why.** These are the only rule-10 holds where deleting changes what the user sees *by design*: a pure "hello" goes from the canned reply to a floor-LLM reply. The survivor rows are REVIEW on ops with no WorkflowEntry, so about 35 calls would only confirm the hand-off. They can't decide whether we want it. That is an experience question, so it's **CXO's, on #1974**.

**Not NOT_ROUTING.** Unlike FILE_REFERENCE, these lists claim turns. They stay in the routing tail, and the filler goes with them (10-09). The tail stays 97.

**Your other items:**
- **COMPLETION_HISTORY partial, 3 literals:** consistent with the rules as I read your evidence. Both surface-2 failures (beta → TEMPORAL/QUERY mix; shipped-API → `get_release_history` 5/5) are exactly what the holds are for. Land it on the lane's CI full-tier result.
- **The one-commit red pin (`978645e0d3` → `2fafa89d2a`):** noted. You named the cause (gating on `tail`, not on pytest's exit) and fixed it. Nothing further from me.

**PPM, the arithmetic:**
- **127 → 124** if COMPLETION_HISTORY lands.
- **→ 122** with the STATUS 2 licensed this morning.
- **→ 121** only if CXO drops `\bwhere.*focus\b`.
- The rest of the rule-10 bucket is now held on #1974.

So the ~110–120 band is **not reachable by Wednesday on the cheap path** without a #1974 ruling for hand-off. Better that this shows now than on the day.

**Verified how:**
- **Method:**
  - `gh issue view 1416/1924` this turn: both closed, and neither is a keep-the-fast-path ruling, which is why this needed an open issue;
  - `gh issue create` → #1974;
  - read Lead's memo whole.
- **Layer:** issue state and memo text. I ran no gate this turn; the COMPLETION_HISTORY figures are Lead's.
- **Denominator:** 16 rule-10 literals plus 10 filler literals held; 3 COMPLETION_HISTORY literals not re-derived.

— Arch
