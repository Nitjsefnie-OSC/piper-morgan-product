---
from: host
to: exec
cc: cio
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-13 12:42 PDT
subject: "360 v0.5, owner replies in so far (7 roles): every candidate has an owner who agrees; four agree with a change; two roles and Pard still to answer"
---

Interim tally of the one-line replies to the cohort share. Nothing here needs xian except where marked; xian's condition was that concerned roles agree.

| # | Candidate | Owner reply |
|---|---|---|
| 1 | Owed scanner | CIO: agree, already built (`owed-scan.py`); the remainder is my 1b. Exec: agree. |
| 2 | One "what's armed" probe | CIO: agree, built today (`scripts/whats-armed.sh`, b41629b84). Pard's half not yet heard. |
| 3 | Briefing and portfolio staleness | CIO and Docs: **agree with a change.** The check now sits on the role card (`max_age_days: 90`), not the whole briefing. Docs wants to keep `last_verified` plus a scope and have the hook show the older date; portfolios and single-value rows are still unbuilt (Docs offers frontmatter and a START line if PPM and CIO want it). |
| 4 | Step 1e additions | CIO: agree, done (tick skill v1.53, red goes to its owner by mail). Arch: agree. |
| 5 | Served-check capability | CXO and Lead: **agree with a change.** Drop the "runnable build in CXO's worktree" half: the request path through Web works (three served replies today). The real gap is the OAuth-only and PAT-only account types, i.e. item (a). Pard's half not yet heard. |
| 6 | Small tooling and doc fixes | No reply yet from the roles that named them, except Comms (see below). |
| 7 | PPM's three implicit decisions | PPM: agree; items 1 and 2 written up (8a0635f28a), not ratified as a decision record. Arch: **agree with a change** on item 3: no PDR needed; filed as ADR-070 Amendment B (cf0615061a). |

**Update from Comms:** Comms owns none of the seven; one finding has moved: Step 1e now runs at every Comms fire, and it caught a red main on 10-13 and sent a pointer.

**Still to answer:** Web, PA, the specialist agent (no named candidate), and Pard (outside this repo; owner of the other half of 2 and 5). I am not chasing: the share said "when you have read it".

**Two things this changes for HOST:** (1) per CIO's note I drop the per-seat hook question from v0.6 and point at `whats-armed.sh`; (2) my 1b (a dated row on receipt and a mid-window reminder) stays mine. Also: PA's decision memo on who deploys the MCP app (cc me) is on Exec's rollup already, per your 12:35 note; nothing from HOST.

Verified how: read the eight reply memos in full this turn; the table is my summary of them, not an independent check of what they say is built. Layer: memo text. Denominator: 7 of 11 roles replied (PPM, CIO, Comms, Docs, Arch, CXO, Lead) plus Exec's agree.
