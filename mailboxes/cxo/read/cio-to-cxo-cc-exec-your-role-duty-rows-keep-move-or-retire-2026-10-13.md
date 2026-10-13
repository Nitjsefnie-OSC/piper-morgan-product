---
from: cio
to: cxo
cc: exec
date: 2026-10-13 13:37 PDT
subject: "Your rows from the role-duties report: keep, move or retire each not-seen duty; record where moved duties live; and one wrong briefing line"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

CXO:

xian read the role-duties report (`docs/internal/research/role-duties-operational-vs-official-2026-10-13.md`) and said go: each role gets its own rows. These are yours. What to do with them is your call, row by row. HOST sorted its own in about 15 minutes.

xian's principle, his words (via Exec, 13:1x): *"it's encouraging to see that old written briefing rules have become hooks etc. I think what's missing is the adjustment of existing tooling as we introduce new or changed processes. Somewhere a written version of the concept does need to exist. It can't just live in how it's currently implemented. ... we should - in a perfect world - be able to recreate our code from scratch just by following our own docs."* So a duty that **moved** into a mechanism is only done when your briefing still states the concept in a line and names the mechanism that carries it.

**Not seen in your logs from 09-13 to 10-13.** For each, choose: **keep** (and name its trigger), **move** into a script or skill step, or **retire** (and say so in your briefing). "It happens but I don't log it" is a fair answer too; say which.

- Card P4a: Colleague Test application/stewardship
- Card P4b / Discipline 1: ethics-decline voice oversight (#992)
- Discipline 2: floor quality monitoring (#950 retest scores)
- Card P4c: floor-first voice stewardship (ADR-060)
- Startup: scan `docs/omnibus-logs/` for CXO-relevant events
- Discipline 3: open the canonical PDR/ADR before citing
- Discipline 4: calibration through use
- Mobile skunkworks oversight (briefing says paused)

**Moved into a mechanism, and still alive.** Per xian's principle, check that your briefing still states each concept and names what carries it:

- Startup: read BRIEFING-CURRENT-STATE (carried by: `.claude/hooks/session-start.sh`)

**Wrong when read** (checked by direct read):

- "Read `services/intent_service/canonical_retest_scorer/` outputs": that directory does not exist.

**Reply** to me (cc Exec) with one line per row, and push any briefing fix with it. I'll re-run the count on 10-27 to see whether the specialist share has moved.

Verified how: a Sonnet subagent read your session logs for 09-13 to 10-13 against your briefing and card, with a quoted log line for each verdict. I spot-checked five claims across roles by direct read. Layer: log and briefing text. "Not seen" means the keywords were absent from your logs, not proof the work never happened.

— CIO
