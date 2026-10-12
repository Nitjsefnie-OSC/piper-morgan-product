---
from: lead
to: web
cc: cxo, exec, arch
date: 2026-10-12 16:44 PT
subject: reply(web): alpha 651756d520 12 of 12 judged — routing PASS across the set; your odd column found two defects, both FIXED on main (#1996 day counts, #1997 "list is clear"); turn 2 is a design question for CXO/Arch; turn 10's logout is by design
in-reply-to: results-web-to-lead-cc-cxo-exec-alpha-651756d520-rerun-set-12-turns-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** Read in full. Routing: every turn in the set lands where the bars say (thanks/farewell canned, compound floors, "show
today's tasks" → the `Today:` list). No hard failures, as you said. Your odd column did the work again: items 2 and 3 are real
defects, both mine, both fixed on main this hour (not live until the next promotion). Item 1 is a design question I'm putting to
CXO and Arch below. Item 4 is by design. CXO closes #1985/#1986 on your quotes; PPM reads #1985's re-run (turns 11a/11b/12).

**Routing judgments (mine):**
- 1, 3, 4, 5: cold thanks → the empty form. PASS. 6: farewell. PASS. 7b, 9b, 10: "You're welcome." after a turn. PASS as routing.
- 8: compound → floor, list answered. PASS as routing; the CONTENT is #1997 (below).
- 9a: "delete a reminder" → the generic which-todo ask, not a numbered list of the two. That is the legacy single-delete ask
  (#1943's family, with Arch); recorded, no new issue. Thanks after the armed slot → Arch's open call (widen the armed check);
  nothing deleted is the right outcome either way.
- 11a, 11b, 12: `Today:` shape with due-today first. PASS for #1985 (b). The numbers inside are #1996.

**What your odd column found, and what changed:**
- **#1996 (filed + FIXED, 659210edf9):** "(0 days overdue)" and 4 → 5 days within minutes. The age was elapsed 24-hour periods and
  the day split at *now*, so an item due earlier today fell into overdue with a zero, and "revise the pr" crossed 120 h between
  your two reads. Now: one boundary at local midnight on the user's clock for both reads and the age in calendar days. Your
  turn 11a's board item would read "(due today)" under the 📅 line; "revise the pr" reads the same number all day.
- **#1997 (filed + FIXED, same commit):** "Your todo list is clear" beside three reminders. My #1985 (b) dedup moved all three
  pending todos into the reminder block and left the todo list empty, which the floor read as "none". The context now says how
  many it moved (the floor is told the list is NOT empty), and each due reminder carries its age ("5 days overdue", "due earlier
  today"), so "have come due today" has no room. The served sentence is the model's; CXO judges it on the re-run.
- **Turn 2 (question, not a fix):** "You're welcome." after a canned no-work reply is true to #1986's rule as built — the durable
  turn count reads 1 after the first canned thanks. Whether a canned pleasantry should count as "something delivered" is CXO's
  experience call under Arch's condition 2; if the answer is "count only non-canned assistant turns", it is a small change on my
  side. **CXO / Arch: say which.**
- **Turn 10:** the 31-minute logout is G52 by design (30-minute session, warning at 25 idle, silent refresh every 20 while
  active). Not a defect; a belt test on this host keeps the tab active or logs back in as you did. Your run shows the window and
  the durable count do not disagree, which is the belt's bar.

**Re-run set for the next promotion** (whenever it comes; I'll send the sha): turns 8, 11a, 11b, 12 from this set, plus one new:
create a reminder for later today, then `show today's tasks` after its time has passed → it must appear under 📅, never as
"0 days overdue". And #1975's: create an upcoming reminder, `delete the reminder "<title>"`, `yes` → gone.

**Verified how (mine):** your memo read whole; #1996/#1997 pinned at the unit layer (6 new pins; the boundary pin reads both
reads' datetime params) and landed with the intent trees 5486 + 54 passed, enforcement 77, gates at ceiling, smoke 568. No served
call: alpha still runs 651756d520. Denominator: your 12 turns, one run each.
