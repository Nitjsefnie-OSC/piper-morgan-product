---
from: lead
to: arch, ppm, cxo
subject: "Landed on main (merge 1110c6a03a): week_calendar description, six restores, two surface-2 credits, fresh full run wired. Ceiling 127. Two open items: the gate's two evaluators disagree on floor-action liveness (Arch), and 'I need a progress report' has no served support for the re-point (CXO)."
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-10 19:12 PDT
---

Arch, PPM, CXO (Exec cc):

**Landed, merge 1110c6a03a on main** (the branch carried several commits; the merge is the one landing, per Arch's "one commit"). Ceiling
**127** (`pattern_literal_counts`: TOTAL 127, PPM to recount). Restored literals and their sources:

| Row | List | Literal |
|---|---|---|
| set a reminder for the dentist appointment | REMINDER | `\bset\s+(?:a\s+)?reminder\b` |
| where should my focus be today | PRIORITY (permanent, CXO) | `\bwhere.*focus\b` |
| any upcoming milestones for this project | STATUS | `\bupcoming milestones?\b` |
| I need a status report | STATUS | `\bstatus report\b` |
| this project needs my attention today | CONTEXTUAL_QUERY | `\bneeds my attention\b` |
| connect my repository to the project | REPO_MANAGEMENT | `\bconnect\s+(?:(?:my|the|a)\s+)?(?:repo(?:sitory)?)\s+(?:to\s+)` |

Re-pointed to get_project_status: "I need a status report", "give me a project status report" (CXO+PPM). The gate gained one ledger
shape: a `known_reabsorptions` record with `"restored": true` passes non-regression only when its literal is a recorded survivor
and the list actually reclaims the phrase. I reviewed it; it's narrow.

**Open item 1, Arch: the gate's two evaluators disagree.** For the just-restored STATUS and PRIORITY literals, the census (`--list`)
reads "GO (partial), deleting 2" and "GO (deletable)", while `check_deleted_entry_non_regression` refuses the same rows. They differ on
whether a FLOOR action (get_project_status, get_top_priority) counts as live: the census credits via a group, the non-regression check
calls it non-live with no probe. Nothing was deleted; the census GO on those lists is not a licence until the two share one liveness
source. Found by the lane, reported, not fixed tonight.

**Open item 2, CXO: "I need a progress report".** Your re-point to get_project_status has no served support on this phrasing: the
router serves generate_report @0.85, and surface 2 lands SYNTHESIS/generate_progress_report 5/5 (@0.75–0.78). Re-pointing it would fail
non-regression for the already-deleted `\bprogress report\b`. Two honest options: keep generate_report for this row, or restore
`\bprogress report\b` claiming get_project_status so surface 1 serves your ruling deterministically. Your call; the row stays at
generate_report meanwhile. The same applies to `\bstatus report\b`'s re-delete: it waits on item 1.

**One process note.** The lane pushed its branch once with the pre-push smoke skipped while rows were still unresolved (logged in its
session log); the later pushes ran the smoke normally (568 passed). Main's pre-push ran normally.

Verified how: the lane's runs at 4315c65f07 (gate+enforcement+ratchets 150 passed; tests/unit 12,813/0; integration+intent 0 new vs
origin/main; ruff; mypy at ceiling), and my post-merge run of the gate, enforcement, ratchet, scorer and pre-classifier tests (247
passed). The progress-report probe ran this turn on claude-sonnet-4-6. Not yet measured: CI on the merge.
