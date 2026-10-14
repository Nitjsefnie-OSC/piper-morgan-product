# The five `piper-*` PM skills: what they are for and what each must do

**Status**: written 2026-10-14 by PPM at CIO's request (mechanism concept links, due 2026-11-01). **Owner**: PPM. This is practice, not a PDR. It records intent so the skills can be rebuilt or sunset against it.

**Mechanisms covered**: `piper-draft-issue`, `piper-draft-spec`, `piper-sprint-plan`, `piper-stakeholder-update`, `piper-synthesize-feedback` (each a `.claude/skills/<name>/SKILL.md` plus a README). They were renamed into the `piper-*` namespace on 2026-06-18 (commit 5c45a3fb56) as the product's PM skill set for alpha users, not as cohort process skills. Each skill file points back here with a `concept:` line.

## Why they exist

A product manager using Piper should get a thinking partner for the five documents a PM writes most: an issue, a spec, a sprint scope, an update to stakeholders, and a synthesis of feedback. The value is the discipline around the document, not the template. Each skill grounds its output in the user's own project context, works without a connector (asking the user for what a connector would have supplied) and is richer with one, and stops to let the user adjust before anything is sent or filed.

## What each must do

| Skill | Must do | Must not |
|---|---|---|
| `piper-draft-issue` | Produce a SLUG, a structured body (problem, goal, requirements, acceptance criteria) and correct metadata (priority, labels, milestone, epic) | File an issue without a milestone or epic home; skip the board step when used inside this repo |
| `piper-draft-spec` | Produce a spec whose non-goals and open questions are filled in, not only requirements | Ship a spec with empty non-goals or no open questions |
| `piper-sprint-plan` | Propose a sprint with explicit "not this sprint" reasoning, dependencies and risks, applying capacity below 100% | Present a full backlog fill as a plan; run the planning for the user rather than with them |
| `piper-stakeholder-update` | Match the user's voice and calibrate to the audience (exec, team, investors, board), then flag and confirm before sending | Produce one generic update for every audience |
| `piper-synthesize-feedback` | Read all source material before coding themes, then give prioritized themes with recommendations grounded in the product | Code themes from a first skim; hand back a summary with no recommendations |

## Shared rules

1. **Context first.** Load the user's project context (and the connector, if present) before drafting.
2. **Thinking partner, not autopilot.** Ask the questions the user would skip; offer the draft for adjustment.
3. **Degrade honestly.** Without a connector, say so and ask for the input rather than inventing it.
4. **Claims are the user's.** Figures and status in a drafted update come from the user's context; anything unverified is marked as such.

## How to evaluate against this page

Read a skill's `SKILL.md` against its row above: does the procedure produce the "must do", and does it avoid the "must not"? The textual link check (`scripts/check-concept-links.py`) only confirms this page names each skill; it does not measure behaviour. No served-model evaluation of these skills exists today (unverified by PPM: I read the skill headings and "why this exists" sections on 2026-10-14, not their full bodies or any output). Review date for this page: 2026-12-08, with the CIO checker's review.

## Known gap

Inside this repo, issues that arrive outside `piper-draft-issue` skip its board-add step, so PPM milestones and places them by precedent (see the PPM briefing). That is a PPM practice, not a property of the skill.
