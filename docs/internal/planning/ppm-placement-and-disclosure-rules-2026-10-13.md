---
type: working-rule
title: PPM placement and disclosure rules, written down (Agent 360 v0.5 candidate 7, items 1 and 2)
date: 2026-10-13
status: PPM practice, written down; not ratified as a PDR
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

# PPM placement and disclosure rules (as practised, written down 2026-10-13)

Two decisions I had been making without a written rule (Agent 360 v0.5, my §8.3 items 1 and 2). This records the rule **as I have applied it**, with the evidence, so a fresh PPM does not rebuild it from memory. It adds no gate class: the admission classes and the slip rule stay in `beta-gate-standard.md`, which governs. Nobody has ratified this note; the evidence below is mine and is quoted from issue and ledger state, not re-measured.

## 1. Production vs MVP for LLM-composed misbehavior

**Default: Production.** An issue where the model's composed wording is the problem (a wrong sentence, a bad format, a stray tool-shaped phrase) goes on Production, with a placement comment.

**It goes to MVP only if** it carries a `Gate class:` line, and for this family that means class 3: the product tells the user something false about **its own state, actions or capabilities**, and it reproduces. A single stochastic occurrence is not enough. A cosmetic or stylistic miss is never class 3.

**Triggers to move one up:** (a) it reproduces on a served re-run, or (b) CXO rules it gate-class. Neither moves it by itself into MVP: admitting still needs PM or Exec to say so, because the gate list is PM's.

**Admission, once PM or Exec says so:** add the `Gate class:` line and an Owner, ledger a slip entry (gate N to N+1, dates unmoved), and check the Wednesday tripwire clause.

**Evidence from practice:**
- #1772 went to MVP because it misstated system state (class 3).
- #1961 (strikethrough on an open todo) went to Production: one live occurrence, stochastic.
- #1985 ("nothing urgent" beside overdue items) was a class 3 candidate. I did not admit it. Its root-cause fix landed on main before any admission, xian's answer was "do whatever gives the team the least stress", and the post-promotion served re-run closed it. The re-run was the trigger, and it did not trip.
- #1998 was filed as a class 3 candidate from the same re-run. It duplicated an already-fixed defect (#1997), so Exec ruled not to admit it, applying xian's standing answer that a defect already fixed on main is not admitted and an in-and-out admission does not count against the 10-09 hold (the hold covers the dates).

**Limit:** this is my reading of five cases. Where a defect is both false-about-state and reproducing but already fixed on main, the practice above is to leave it on Production and let the served re-run decide; that is xian's instruction by relay, not a rule he has written.

## 2. What counts as a known issue disclosed to beta testers

**Bar:** an issue is listed under "Known issues in this beta" only if (a) the user can hit it on the golden path or a setting they are told about, and (b) it is established, either **"the setting does nothing"** shown by a check, or **"it reproduces"** on a served run. Anything that is only a suspicion, or a one-occurrence stochastic miss, is not listed.

**Who decides what:** PPM sets the bar and decides whether an item meets it; Comms owns the wording; CXO's source read can reinstate an item. The list lives in `docs/internal/planning/beta-invitation-copy-2026-10-07.md` §2.

**Evidence from practice (10-07):** the personality line was struck at 12:33 on the bar ("only if the check shows the setting does nothing") and reinstated at 15:33 after CXO's source read showed the setting does nothing. A workaround line was kept because the underlying problem reproduced even though the exact words differed. A known-issue bar written inside a planning doc moved twice in a day; this note is the first place it is stated apart from the copy.

**Not decided here:** whether this wants a PDR. If PM or Arch want the placement rule in section 1 or the bar in section 2 ratified, that is theirs to say.

Verified how: read my own 10-09 Agent 360 response (§8.3), HOST's v0.5 synthesis, `beta-gate-standard.md` (Class 3 text, the 10-12 ledger paragraphs), and the known-issues section of the invitation copy this wake; the case outcomes are quoted from my ledger and from `gh` issue state read in this session for #1985 (closed, Production) and #1998 (closed). Layer: documents and issue state, not a served run. I did not re-open #1772 or #1961 this wake, so those two are quoted from the response.
