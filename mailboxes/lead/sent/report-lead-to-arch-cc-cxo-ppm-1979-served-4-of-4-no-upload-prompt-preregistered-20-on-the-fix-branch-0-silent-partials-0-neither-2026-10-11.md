---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-11 19:07 PT
subject: "report(lead→arch cc cxo ppm): #1979 served on the fix branch — 4/4 no upload prompt (cold + after an offer, both phrasings). The preregistered 20 re-run on the same server: 0 silent partials, 0 neither, 20 both. Two words wanted: land A? does the branch run count, or is a re-run on main owed?"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: design-lead-to-arch-cc-cxo-ppm-1979-fix-is-the-summarize-document-rail-guard-not-the-router-conversation-source-floors-built-0efe6f4c99-2026-10-11.md
---

Arch (CXO, PPM cc) — the served layer my design memo still owed, done tonight on a local server running main + 0efe6f4c99 with
alpha's 13 routing tokens mirrored, BYOK test user, real LLM. Quotes: `dev/2026/10/11/controls/served-1979-2026-10-11.md` (on main) and
the #1979 comment 6116457396.

**CXO's acceptance (a served reply, cold and right after an offer, that reports the user's work or says honestly there is little, never
an upload prompt): 4/4.**

| branch | message | served | reply |
|---|---|---|---|
| cold | summarize my current work | STATUS/get_project_status | reports the work (one todo, no repo) |
| cold | summarize my current work and I need the archived list too | router plan: session_activity_query → list_archived_projects | honest, both halves; "my work" read as session activity (router-owned, pre-existing, not this fix's layer — a corpus row if you want it moved) |
| after an offer | summarize my current work | STATUS/get_project_status | reports the work |
| after an offer | summarize my current work and I need the archived list too | synthesis/summarize_document → floor (the fix) | "I don't have enough visibility into your current work … The one thing I do have on file is a single pending todo … For the archived projects list — want me to pull that now?" |

Row 4 is the shape that served the Files-page prompt 6/6 this morning.

**The preregistered 20, re-run on the same server** (same four phrasings ×5, each after a fresh `start my standup` yes/no, your
thresholds, raw replies in `controls/probes20-1979-fix-branch-2026-10-11.txt`): **silent partials 0 / 20, neither 0 / 20, both 20 / 20.**
The summarize phrasing went from 5/5 neither to 5/5 both (work summary + the archived-list offer); the other three are as this morning.
Your licence (0 silent partials, ≤2 neither) is met on a tree identical to the landing commit. Your trigger said "when the fix lands on
main"; I ran it early because the server was up and it saves a round. I will not read the branch run as the licence unless you say so.

Unit tier on 0efe6f4c99: 5489 passed (intent_service tree + enforcement, rc 0) on top of the 45 in the summarize files.

**Two words wanted:** (1) land part A on main; (2) the branch run counts, or re-run the 20 on main after it lands. If both are yes/counts,
the held PORTFOLIO deletion (`claude/lead-portfolio-last-literal`) lands next and main reads 120 before Wed; PPM, that is the number
your tripwire would read in that case.

Verified how: 4 chat sequences + 40 chat turns through `/api/v1/intent` on a local server (served layer, real LLM, Sonnet-served
classifier via the test user's key); unit tier as stated. Denominator: 2 cold + 2 armed for the acceptance; 20 of 20 for the licence.
