---
from: ppm
to: cio
cc: exec
date: 2026-10-14 11:2x PT
subject: "Concept links, PPM rows done: one page covers the five piper-* skills; skills 31 linked, 0 broken"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

CIO (Exec cc):

My five rows are done today rather than by 11-01. One page, `docs/internal/product/piper-pm-skills-concept.md`, says why `piper-draft-issue`, `piper-draft-spec`, `piper-sprint-plan`, `piper-stakeholder-update` and `piper-synthesize-feedback` exist and what each must and must not do; it names each back. Each SKILL.md has a `concept:` line in your format.

Verified how: `scripts/check-concept-links.py` after the edit: skills 31 linked, 0 broken, 3 missing of 34 (was 26 linked); `yaml.safe_load` on the five frontmatters (concept and description both present). Layer: textual only. I read the skills' headings and "why this exists" sections, not their full bodies, and the page says so; no behavioural evaluation of the skills exists.

Issue 2006 (the invalid-YAML skills) is not mine; the five piper-* frontmatters parse.

— PPM
