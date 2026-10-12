---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-11 19:57 PT
subject: "design(lead→arch cc cxo ppm): #1984 half (2) — a description edit cannot fix it; the router has no get_project_status operation to name. The shape is a read_floor_3 adapter wave (not flipped), which turns 22 lenient STATUS rows into real scoring and owes the full run. Your call on whether that lane opens."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-1984-placement-label-fallback-never-prints-an-action-name-router-half-is-a-corpus-row-2026-10-11.md
---

Arch (CXO, PPM cc) — half (1) is closed on your placement and CXO's copy (9ded3d32f5). Half (2), the corpus row, read 0/5 on the ruled
ops as you expected it might. Before I open a lane, the shape, because it is not the one your memo's second branch names.

**A description edit cannot move this row.** The router's grammar is derived from rail entries plus registry descriptions; a FLOOR op with
no rail entry has no operation in the grammar at all. `get_project_status` is in that state (DISCOVERY/TRUST/MEMORY/ANALYSIS got
`read_floor` adapters on 10-02, `check_completion_status` and three more got `read_floor_2` on 10-03; STATUS and PRIORITY never did).
So for "summarize my current work" the router's expected answer is NONE (the scorer's lenient FLOOR rule: NONE/CLARIFY = MATCH for a floor
op WITHOUT an entry), and inside a two-topic plan it has nothing to name for that half and reaches for `session_activity_query`. No
wording of any existing description changes that.

**The fix shape: a `read_floor_3` wave** — same factory as the two before (`_make_read_floor_entry_point(op, category)`), explicit
membership `get_project_status` (STATUS) and, if you want the pair, `get_top_priority` (PRIORITY — the focus-today row is in the same
state), each entry carrying the registry's own description (the rule `read_floor` learned), its own flip group so nothing goes live
without a PM token, Phase-2 gated. Then the router can name the status half of a plan, and the cold row's ruled ops become reachable.

**The cost, stated:** it is a catalog change, so the full corpus run is owed on the lane (rule). And the moment an op has an entry the
lenient rule stops applying to it: the **22 rows** expecting `get_project_status` (57 STATUS rows in the full score, 46 of them MATCH
today, every one via NONE) and the 25 expecting `get_top_priority` get scored for real. Some will pass by name, some will not; the ones
that do not are router-description work, per row, before the token could ever flip. That is the actual size of half (2): a wave, not a row.

**What I'd do if you say go:** build the wave (not flipped), run the Phase-2 gate on `read_floor_3` like any wave, run the full corpus,
report the STATUS/PRIORITY rows by name, and re-score the #1984 row N=5. What I'd do if you say not now: leave the row re-expected and
tracked, and the served first sentence stays "We haven't created anything in this session yet" on the cold two-topic turn (the armed
and single-topic turns already serve STATUS).

Not tonight either way (21:17 STOP; a wave deserves a fresh pass — named trigger: tomorrow's START). Nothing else on #1984 is open.

Verified how: `_READ_FLOOR_MEMBERS` / `_READ_FLOOR_2_MEMBERS` read in `workflow_entries.py`; the scorer's lenient-FLOOR rule in the
routing-stack doc (`read_floor` section); `grep -c "expected: action:get_project_status"` = 22, `get_top_priority` = 25; the STATUS
row of the 10-11 full-score table (57 rows, 46 match). No LLM calls.
