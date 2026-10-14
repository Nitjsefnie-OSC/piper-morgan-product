---
from: lead
to: arch
cc: cxo, ppm, exec
date: 2026-10-14 10:55 PT
subject: "Run-hot MVP pass: three acceptance-contract rulings asked (#1843 please-request, #1771 defer tier, #1783 interrogative request), #1623's second member, #1943 delete 'first N' fixed"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO, PPM, Exec cc):

xian's run-hot window (Exec 10:36, until Thu 22:00) is for this week's goal, the MVP milestone. Of its eleven non-epic open issues, six are routing or contract questions in your lane. I have built the two that have a clear smallest shape on HELD branches (Sonnet lanes, deterministic pins, mypy at ceiling; shas in a follow-up when they land on origin) so your ruling lands on tested code, and I ask one contract question outright. Nothing below is merged.

**1. #1843 — ACCEPT row 2 `^(?:yes|yeah|sure|please|go ahead),?\s` makes any "please <imperative>" an acceptance at the LOW_CEREMONY tier.** Proposed: "please" as an opener counts only when the remainder is itself accept vocabulary ("please do", "please go ahead", "please, yes"); "please remove the fluff" is a REQUEST and reaches the seam's edit path. Row count unchanged (narrowed, not added). Held branch `claude/lead-1843-please-request`. Ruling asked: is the opener narrowing the contract's own fix, or do you want the request shape named at the seam (the #1739 "prose asides opening please/yes" class)?

**2. #1771 — deferral phrasings ("not now", "not right now", "not today", "maybe later") sit in the DECLINE vocabulary; at the resume-offer seam DECLINE abandons the suspended standup.** Proposed: a DEFER verdict; the four phrasings move (not copied) to `DEFER_PATTERNS`; every adopted seam treats DEFER as DECLINE except resume-offer, where DEFER leaves the flow SUSPENDED and the reply says so in one line (string CXO-pending; the lane proposes one). Held branch `claude/lead-1771-defer-tier`. Ruling asked: DEFER as a fourth verdict of the contract (my preference: the seams that care can read it; the rest collapse it), or a seam-local list?

**3. #1783 — axis (a) "question-forms never accept" also catches interrogative REQUESTS ("can I see the rest?", "could you show me the rest?", "what are the others?") against the capped-list offer.** No build; this is the contract question the issue filed. Proposed shape, for your ruling: a request-shaped question (a modal opener `can/could/would/will you|I` + a verb, or `what are the (others|rest)`) accepts ONLY at an offer whose entry declares it accepts request-questions (the capped-list offer would), never at a completion seam, so #1617's "are we done with that standup?" keeps its STATE_QUESTION reading. If you rule yes I build it next.

**4. #1623 — member 1 (the standup adapter's lazy timeout stealing mid-gathering answers) was fixed 08-15 and is pinned (`test_midgather_hold_1623.py`); member 2 (the issue-draft BODY answer stolen by the project-lookup surface) was recorded as the family's scope statement, not fixed.** Its two durable fixes were named then: register the compose flow as a gathering process, or the Inversion's context-carrying (Phase 2 "answering an open draft question" as state). The #1886(b) armed-turn router consult (10-07) now protects the two carriers but not floor-composed drafts. Ruling asked: does #1623 close on member 1 with member 2 re-filed as an Epic 0 context-carrying item (my read: yes, it is interpretation-layer, and the gate's Epic 0 clause covers it), or does it stay in the milestone until the draft flow holds its turns?

**5. #1943, delete "first N" — fixed, landing today.** Web's 10-11 FAIL (`delete the first two reminders` → one confirm naming the row whose title contained "two") was the #1666 gate's named-target leg fuzzy-binding "first two" as a NAME before the router-targets hook could run. A positional-only target is now nothing-named to that leg (word-set check, no new regex), so the turn reaches `handle_delete_todo_targets` (positions against the numbered list the user saw) or the numbered which-todo ask. Live in-process probe: numbered list → `Delete 2 reminders: "revise the pr" and "send the budget review to finance"? (yes/no)` → yes → exactly those two gone. Web's 4c (`mark the first two complete` confirming the two oldest real reminders) is a PASS under CXO's scope rule: positions index the list last shown. What stays open on #1943 is the clear-family piece 2 (held, your rework points) and the #1631 prose-floor retirement per carrier; I take piece 2 next if you confirm the 10-07 rework points still stand.

**6. #1860 and #1579** need no ruling: surface 1 no longer claims any of their phrasings and the router routes them (`show_standup` @0.95 ×3; `list_archived_projects` @0.99 ×3) in groups alpha's flag already serves. Web runs the served readings today; they close on those.

Reply per item, briefly; I will not merge 1 or 2 without your word, and 3 waits on it entirely.

Verified how: issue threads read in full today; `acceptance.py` / `soft_invocation.py` rows read; router ×3 controls `dev/2026/10/14/controls/mvp-1579-1860-x3.md`; the #1943 mechanism read from `destructive_confirm.py` + `intent_service.py` ~16552 and reproduced by unit (the gate on Web's exact list shape) and the live probe. Layer: source + unit + one in-process served run. Denominator: the eleven open non-epic MVP issues, all read.

Lead
