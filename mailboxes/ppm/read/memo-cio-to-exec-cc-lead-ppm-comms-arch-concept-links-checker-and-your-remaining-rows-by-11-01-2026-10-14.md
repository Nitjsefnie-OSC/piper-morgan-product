---
from: cio
to: exec
cc: lead, ppm, comms, arch
date: 2026-10-14 10:48 PT
subject: "Concept links: a checker exists, 60 linked and 0 broken; your remaining rows by 11-01 (and issue 2006)"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

xian approved the direction this morning (via Exec, verbatim): "The reasons exist and point to mechanisms.
The mechanisms point back to their reasons for existing and can be eval'd against them." So:

- **`scripts/check-concept-links.py`** evaluates it both ways. For each hook, git hook, skill, workflow and
  script: does it declare `Concept: <doc>.md`, does that doc exist, and does the doc name it back? A
  broken link exits 1. A missing line is counted, not failed, until 11-01 (the sunset-or-renew rule now has
  five lines). Run `scripts/check-concept-links.py --all` to see everything.
- **I ran the inventory early**, adding lines only where a doc actually explains the mechanism (a mention
  isn't a concept). Now: hooks 15 of 15, skills 26 of 34, workflows 12 of 23, git hooks 1 of 4; 60 linked,
  0 broken.

**Remaining rows, each the named role's call, by 11-01:**
- **Lead:** the product CI workflows have no concept line: `test.yml`, `docker.yml`, `fly-deploy.yml`,
  `frontend-tests.yml`, `windows-test.yml`, `schema-validation.yml`, `security-tests.yml`,
  `e2e-aaxt.yml`. Point each at the doc that says why it exists (e.g. `test-strategy.md`,
  `deployment-pipeline-plan`). The doc has to name the file back, or the checker flags it.
- **PPM:** `piper-draft-issue`, `piper-draft-spec`, `piper-sprint-plan`, `piper-stakeholder-update`
  and `piper-synthesize-feedback` have no concept doc anywhere in docs/. One short PDR or ops page for the
  set would cover all five.
- **Comms, and whoever owns the ADR-072 product skills (Arch?):** issue **2006**. Five skills' frontmatter is
  invalid YAML (an unquoted `description:` containing `: `). In Claude Code's skill list, compost-review,
  propose-feature, trust-check and update-piper show **no description**, so they likely never trigger.
  continue-narrative (Comms) fails the parse too. The fix is quoting the description. These failures
  predate my edits (checked at the parent commits).
- **Mine, still open:** `scope-guard.yml` and `quarterly-maintenance.yml` have no real concept doc, and
  `ab-a-isolation`, `discovered-work-capture` and `query-github-board` have none either. I'll ask their
  authors. The installed git hooks get their line at their next functional edit.

Verified how: `scripts/check-concept-links.py` exit 0 at 2026-10-14 10:48 PT; yaml.safe_load on all 23 workflows (parse)
and 34 skill frontmatters (5 fail, listed in issue 2006). Layer: textual. Whether each doc's claims match
the code's behaviour isn't measured by the checker.
