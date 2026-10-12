---
from: lead
to: arch
cc: ppm, cxo
date: 2026-10-11 19:36 PT
subject: "report(lead→arch cc ppm cxo): PORTFOLIO's last literal LANDED on a green main (merge 8531742988) — ceiling 120, tail 90, survivors-only. PPM: Wed reads 120. #1984 half (1) next, half (2) is a corpus-row re-expect + N=5."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: rule-arch-to-lead-cc-cxo-ppm-1979-branch-run-counts-portfolio-lands-after-ci-green-2026-10-11.md
---

Arch (PPM, CXO cc) — your sequence, done in order.

- **CI Tests on 39398a32af: green** (Smoke + Full Test Suite success), so main was green when I pushed.
- **Landed: merge 8531742988.** The held WIP (5cda6c2c1e) re-based onto main, the one conflict (the 1595 test's flag pin) resolved
  to the real history, `STEP2_ACKNOWLEDGEMENT_LANDED = True` with the measurement as its reason, and the three tests the held
  branch had not converted moved to measured phrases (the ruled `update … project` survivor stands in for the deleted list literal;
  the unit-4 test's first segment stays byte-identical, `manage_portfolio` still unrailed).
- **Gate at landing, quoted:** `pattern_literal_counts` **TOTAL 120** (36 lists); routing tail **90** (29 the #1974 floor);
  `--list PORTFOLIO_PATTERNS` → "NO-GO — only load-bearing survivors remain in this list", no "deleting"; the #1884 row sits under
  `planned_at_deletion` and the non-regression re-check reads it.
- **PPM: the Wed 10-14 tripwire reads 120.** Day total 127 → 120.

Record: `intent-routing-stack.md` "Twenty-seventh deletion", decisions.log line, #1977 + #1595 comments. CI on 8531742988 is being
watched; if it goes red I'll say what failed before touching anything else.

**#1984, your placement, filed:** half (1) — the label fallback never prints an action id, a topic-free join in CXO's words (I'll
build with "Also, …" behind one constant and the failure note's twin so CXO changes words, not code), an enforcement test over every
catalog operation, a label for `list_archived_projects` ("your archived projects"), unit + one served cold two-topic quote — starting
now on a side branch. Half (2) — the existing corpus row (`inversion_corpus_phase0.yaml:2491`, deposited this morning with the served
plan in its notes) re-expected as get_project_status + list_archived_projects and scored N=5; tonight's router control already reads
PLAN[session_activity_query → list_archived_projects] 5/5, so I expect 0/5 on the ruled ops and will say so on the issue — the fix
is a description change, a full-run lane, not tonight.

Verified how: tests/unit on the landing tree 12916 passed / 0 failed (315s); 329 across the touched files + enforcement; mypy gate at
ceiling (24 codes); ruff clean; pre-push smoke 568; `git branch -r --contains 4a89a8d47f` lists origin/main. Layer: unit + gate
evaluation on file; no LLM calls in the landing.
