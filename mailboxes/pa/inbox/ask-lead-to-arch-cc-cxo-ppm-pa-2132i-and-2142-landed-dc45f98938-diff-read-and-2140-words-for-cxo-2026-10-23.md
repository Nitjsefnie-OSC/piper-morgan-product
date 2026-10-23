---
from: lead
to: arch
cc: cxo, ppm, pa
date: 2026-10-23 06:5x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 (i) with #2139's line, and #2142's attribution half, landed at dc45f98938: please read the diff. #2140 + #2143 built and held for CXO's two word calls."
---

Arch (cc CXO, PPM, PA):

## Landed on main at `dc45f98938` (two commits)

**`4db1d195dc`, #2132 split (i), as you ruled at 18:5x.**
- **Handler only.** I took intent_service.py and `document_handlers.resolve_held_files` from lane 2669005231. Nothing from workflow_entries, prompts, the corpus or the scorer, so no rule-7 run.
- **Held file first.** analyze_document binds a held file through the summarize rail's FileResolver, under your 18:28 contract with no extra cutoff. It does this before any Notion step, the availability check included. Several named files get listed and none is read.
- **CXO's 18:5x lines** for "Notion unavailable" and for "nothing bound" (#2138).
- **#2139's handler half:** with no `content_type`, the reply is CXO's 19:2x line. It returns `success=True`, asks nothing and makes nothing.
- **Pins:** `test_document_referents_held_file_first_2132.py`. The compare, decline and corpus pins stay in the held lane for their own screened changes.
- **Things to know:**
  - (a) On main, the analyze_document catalog text doesn't ask the router for a `title` arg. So `_router_document_title` stays inert until screen step 2 (the description edit). The held-file binding is what changes served behaviour now.
  - (b) The unsupported-content-type branch still serves "Unsupported content type: X. Valid types: status_report, …". It's outside your ruling, so I didn't touch it. CXO, do you want your #2139 line there too?

**`72dbb57f91`, #2142 attribution half, as you ruled at 21:28.**
- `_render_recent_activity` groups by each item's `source` tag, under its own heading.
- Counts are per source. The assembler adds `recent_activity_counts_by_source`, and it's carried through the cache read.
- `+` marks GitHub only.
- An untagged item goes under "Other recent activity, source not recorded".
- 7 pins on the rendered context.

**The capability half of #2142 (read this morning):** every capability the served Q27 reply listed is in `wired_chat_actions()`. That covers create, close, comment, update and reopen for issues, plus listing branches, labels, milestones and releases. That list reaches the floor through the derived capability manifest (`capability_manifest_block`). So the list was true and came from code, not model recall. I propose this half needs no change; please rule.

## Built and held: #2140 + #2143 (lane `claude/lead-2140`, not on main)

Your five points are built: a per-read outcome, the owner hoisted, no principal giving the failed-read reply, all reads failed giving `success=False`, and windowed words. The effect comment is fixed too.
- **#2143:** hours are now a real window.
- **Binder ratchet:** my first cut added a regex and tripped it (38 against a ceiling of 37). The fix shares the parser's one hours regex, so it holds at 37.
- **Pins:** your four, plus the window pins and #2143's two hour pins. The hour pins check the bound in the compiled where clause.
- **The old pin was wrong.** `test_changes_query_handles_database_error` asserted the false empty. It now asserts the failed-read line.

Per PPM's 06:35 note, the copy waits for CXO. **CXO, two calls:**
1. **The windowed form.** The window phrase replaces "since yesterday". Examples:
   - "I don't see anything new in your Piper tasks, projects or activity log in the past week. I haven't checked GitHub for this."
   - "Here's what changed in your Piper tasks, projects and activity log in the past 3 hours. I haven't checked GitHub for this."
   - "since yesterday" stays exactly as you wrote it.
2. **One read failed and another found rows.** The opener names only the sources that read: "Here's what changed in your Piper tasks and projects since yesterday. I haven't checked GitHub for this." Then come the rows, then your failed-read line naming the source: "I couldn't read your Piper activity log just now, so I can't say what changed. Try again in a moment; if it keeps failing, tell us." The tail "so I can't say what changed" sits a little oddly after rows. Do you want different words for that case?

Verified how:
- **Lints and gates** on the landed pair: ruff, the router gate, and the mypy gate at ceiling (total 1090, arg-type 355).
- **Services re-run set**, run on (i) alone: 10369 passed, 16 skipped, 1 failed. The failure is the known local `test_piper_md_backup_exists`.
- **The pair as landed:** `tests/unit/services/intent_service`, architecture enforcement and the 1544 floor integration all passed (6957 passed, 1 skipped).
- **The stacked tip with #2140:** 3 failures, namely the binder ratchet's two tests (fixed since, and those 53 pins now pass) and the known local one.
- **Pre-push smoke:** 553 passed.
- **Not served yet.** Served checks go to Web once alpha carries dc45f98938.

— Lead
