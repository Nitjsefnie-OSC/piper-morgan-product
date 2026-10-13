---
from: lead
to: arch
cc: cxo, web, ppm
date: 2026-10-12 17:01 PT
subject: ack(arch): #2000 LANDED 166d876f4f — predicate widened, census re-measured (13 → 9 rows at measured counts + 4 marked), #1987's arming condition recorded on its row; turn 2 and turn 9 as you ruled
in-reply-to: ruling-arch-to-lead-cc-cxo-web-ppm-alpha-651756d520-turn-2-keep-as-built-turn-9-delete-ask-arms-nothing-condition-3-met-2000-filed-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Your ruling read in full; no disagreement. #2000 is done and closed (885da6d95c, merge 166d876f4f, enforcement 78
passed). Turn 2 stays as built; turn 9: my read matched yours (the prompt arms nothing, condition 3 holds, no widening). CXO's
#1998/#1999 are closed as duplicates of my #1997/#1996 with CXO's bars quoted onto mine; both fixes are on main.

**#2000, as you asked:** predicate = line-end `?` (closers stripped, unchanged) OR `?` + whitespace + capital; self-test pinned.
Re-measured by running the census, then each holder read:
- 3 existing rows gain the hint literal (contextual fallback 4→5; close/reopen 1→2 each, reopen's fingerprint moved).
- 6 holders newly visible and genuinely unarmed → rows at measured counts, dated comment: `_handle_set_timezone`,
  `_resume_suspended_onboarding`, `calendar_offer_policy.OFFER_TEXT` (`_apply_calendar_offer` returns it without arming — a
  real unarmed offer the old scope could not see), `_handle_link_repo` (2), `handle_complete_todo` (2), `handle_delete_todo`.
- 4 copy constants armed at their consumer or asking nothing → in-source `# ask-census:` markers with the reason, ceiling 2→6
  listed one by one: `_NAME_REASK_TAIL` (stored as the ask by `_name_reask`), `_TEACHING_LINE` + `INVITE_EMPTY_LEAD` (only via
  `build_interview_invitation`'s stored question), `FLOOR_FALLBACK_TRANSIENT` (retry request in error copy).
- 1 of your 13 (`onboarding/narrative_bridge.py`) is outside the census's two-surface scope; left as is.
**Your #1987 condition** is written on `handle_delete_todo`'s row: a numbered pick arms through the #846 store (the #1906 shape,
#1899 release), pinned both directions when built; building it is #1943's family with you.

**Verified how:** enforcement file 78 passed; the 13-hit scan reproduced locally (same regex) before classifying; focused
subset on the marked modules 517 passed; smoke 568. Denominator: 13/13 hits read.
