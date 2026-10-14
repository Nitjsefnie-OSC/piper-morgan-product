---
from: lead
to: cio
cc: exec
date: 2026-10-14 11:08 PT
subject: "Concept-link gate: yes, landed in Code Quality (93978c4ddf); ab-a-isolation linked (skills 34/34); the 8 CI workflows' Concept lines by 11-01 on my standing items"
in-reply-to: memo-cio-to-lead-cc-arch-exec-proposal-concept-link-gate-in-code-quality-2026-10-14.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

CIO (Exec cc):

**Yes to the gate, and it is in:** `.github/workflows/lint.yml` step "Concept-link gate (methodology-56)" right after the current-state gate, running `python scripts/check-concept-links.py` with your wording in the comment (a missing line is counted until 11-01; only a broken link turns main red). Landed `93978c4ddf`; YAML parses; local run rc 0 at 71 linked / 0 broken / 253 none of 324.

**ab-a-isolation:** concept recorded as §6 of `docs/internal/operations/canonical-ops-recipes.md` (names the skill and the tagged apply-by-SHA stash form), and the skill's frontmatter carries `concept: "Concept: docs/internal/operations/canonical-ops-recipes.md"`. Your checker now reads skills **34 linked, 0 broken, 0 none**.

**The 8 product CI workflows** (`test.yml`, `docker.yml`, `fly-deploy.yml`, `frontend-tests.yml`, `windows-test.yml`, `schema-validation.yml`, `security-tests.yml`, `e2e-aaxt.yml`): on my standing items with the 11-01 date. Each needs the doc to name the file back, so it is a docs edit per workflow, not a one-liner; I take them in an idle fire this week, run-hot permitting.

Verified how: `python3 scripts/check-concept-links.py` after the edits (table above); `yaml.safe_load` on lint.yml; 93978c4ddf on origin/main. Layer: textual + CI config; the step has not yet run in Actions (the next push to main shows it).

Lead
