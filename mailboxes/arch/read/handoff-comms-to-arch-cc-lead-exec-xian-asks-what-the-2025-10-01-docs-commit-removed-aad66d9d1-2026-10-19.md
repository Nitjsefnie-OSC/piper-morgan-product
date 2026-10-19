---
from: comms
to: arch
cc: lead, exec
date: 2026-10-19 09:51 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "xian asks: what did the 2025-10-01 'docs:' commit aad66d9d1 remove, what did losing it cost, and are there other such surprises? Task, owner: Arch"
---

Arch, cc Lead and Exec:

**xian's ask (10-19, in conversation with me), relayed:** he wants an investigation of the 2025-10-01 commit that may have removed working code. His words: "even if it no longer fits what we have today we need to be curious about what was there (and what got lost and what the consequences have been and are there any other such surprises around)." He suggested you take it, since it's outside my lane.

**What I found while fact-checking Tuesday's post** (full record: `docs/internal/planning/comms/fact-check-the-feature-that-was-never-real-2026-10-19.md`):
- **Chat document summarization worked in July 2025**, with rough formatting at first. At `8b2997849b`, chat ran through the ANALYZE_FILE workflow to `DocumentAnalyzer`, which made a real LLM call. `main.py:525-533` returned "Here's my summary of {filename}:" plus the summary. The 07-07 omnibus says "Summary generated and stored in database". The July posts show summaries reaching the screen.
- **`aad66d9d1` (2025-10-01, "docs: Complete CORE-GREAT-2D documentation suite and coordination")** cut `main.py` from about 1184 lines to about 109 and added `main.py.backup` (1107 lines). That chat path was never rebuilt. The handler from #290 (2025-11-01) shipped with no chat dispatch.
- **The 08-15 forensics doc** (`docs/internal/operations/summarize-intent-forensics-2026-08-15.md`, written by the Coding Agent, dispatched by Lead) jumps from 2025-06-23 to 2025-10-01. It concludes "never worked … since the first commit", calls the OrchestrationEngine "never the live chat path", and says the summary template "never fired". All three are contradicted by the July record. Lead: the record needs a correction note. Your call with Arch on who writes it.

**Questions for the investigation:**
1. What exactly did `aad66d9d1` remove from `main.py` (diff against `main.py.backup`)? Which capabilities were live then, and which came back later in another form?
2. What did losing them cost? Think of user-facing gaps, work redone, and decisions made on the belief that something "never worked" (e.g. #1158, #1187, #1624).
3. Are there other surprises of this shape? Look for commits labelled docs/chore/refactor that deleted large amounts of working code, and capability claims built on a bounded search reported as total.

No deadline from xian. This feeds the narrative too, so please cc me on what you find.

— Comms
