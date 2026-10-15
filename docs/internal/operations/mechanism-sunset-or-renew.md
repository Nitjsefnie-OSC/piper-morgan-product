# Mechanism sunset-or-renew (R3 step 3)

**Status**: active from 2026-10-04 (PM approved R3; CIO drafts, Exec applies first). **Owner**: CIO.

## Before you build
`git grep` / `ls scripts/` for the problem's noun first. Twice in one week (10-01 ruff binary, 10-04 pre-push interpreter) the fix already existed in the tree and the finding was made again (Pard's observation). If the ask went to more than one role, read the others' replies first: on 10-15 CIO built a stuck-session check that Pard had put live 20 minutes earlier (methodology-43, instance 7).

## Before you remove
Find what reads or probes the mechanism: `git grep` its name, and check which copy each live probe hits (`whats-armed.md`, Pard's drumbeat). On 10-14, removing the user-level `check-branch.sh` turned the hook drumbeat red at 19:05, because the drumbeat had been testing that copy and no page said so (methodology-43, instance 6).

## The rule
Every **new** watcher, hook, gate, cron or recurring check carries five lines where it is defined (the
script header, or the registry/settings comment that installs it):

```
Cost:    <what it spends: commits/day, tokens/fire, seconds/commit, a seat's attention>
Benefit: <what it has caught, with counts, or "none yet: measuring">
Review:  <YYYY-MM-DD, at most 8 weeks out>
Owner:   <role>
Concept: <path of the doc that says why this exists and what it must do; the doc names this mechanism back>
```

The `Concept:` line (added 2026-10-14 from the methodology audit, xian's frame of 10-13: "a written version of the concept does need to exist ... we should be able to recreate our code from scratch just by following our own docs") points at a doc, not a commit or an issue. A design proposal counts only if it is updated to say what was built. If no doc exists, write one first; a header comment is not the concept. `scripts/check-concept-links.py` evaluates the pointers both ways: every declared `Concept:` path must resolve, and that doc must name the mechanism back. A broken link exits 1. A missing line is counted, not failed, until 11-01. xian on this direction, 10-14: "The reasons exist and point to mechanisms. The mechanisms point back to their reasons for existing and can be eval'd against them." Audit baseline 10-14: 39 of 152 process mechanisms linked both ways, 44 with no concept doc (`dev/2026/10/14/methodology-audit-2026-10-14.md`).

At the review date the owner writes one line, **renew** (with updated counts) or **sunset** (it gets
removed, with a pointer to what replaces it, if anything). A mechanism with no benefit recorded at its
first review is sunset by default, unless the owner says why the absence of catches is itself the
benefit (a guard that prevents rather than detects). That argument has to be made in writing, not
assumed.

## Existing mechanisms: one-time inventory
The existing mechanisms aren't grandfathered forever. Each gets the five lines at its next edit, or by
**2026-11-01**, whichever comes first. Watchers with a **false-clear history** get one consolidation
review first:

| Mechanism | Why it's reviewed first |
|---|---|
| freeze-check BELT-INVISIBLE/NO-SESSION-LOG paths | Pre-v0.16 they read "stopped" for busy seats; now corroborated. Keep, measure. |
| Step 0 DAY-CLOSED self-verification | HOST's 6-day prose-verified pass (09-23..28); the v0.17 detector now covers it externally. Consider retiring the self-check in favour of the external one. |
| post-commit heartbeat hook | 09-21 runaway; re-armed as a pilot 10-01. Record cost (commits/day) explicitly. |
| `mailbox_filename_lint` grandfathering | Archive moves passed while lengthening paths (fixed at the tool, 10-01). |

## Already compliant, as examples
- `scripts/ensure-ruff.sh` + `pre-commit-ruff-warn.sh` (10-01): cost ≈ 0.02 s per `.py` commit once the
  pinned ruff is cached; benefit being measured (Lead's one-week advisory window ends 10-08).
- `duty-cycle-freeze-check.sh` v0.17 NO-DAY-CLOSE (10-01): cost is one `git show` per logged day per role,
  about 1 s total; benefit replayed 6 real unmarked days (HOST).

## Measuring cost honestly
State **steady-state** cost, and report incident spikes separately. Example from 2026-10-04: CIO's
1,061 heartbeat-type commits over 09-05..10-03 were **968 from one runaway hour (09-21)** and **93 in
steady state (~3/day)**. Quoting the 1,061 as routine cost would have overstated it ~11×.
