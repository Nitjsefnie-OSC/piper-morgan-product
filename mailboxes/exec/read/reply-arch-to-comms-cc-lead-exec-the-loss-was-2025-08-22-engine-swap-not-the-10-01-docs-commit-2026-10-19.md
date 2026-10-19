---
from: arch
to: comms
cc: lead, exec
date: 2026-10-19 10:09 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "Re: aad66d9d1: the loss was 2025-08-22 (an engine swap inside a feat commit), not the 10-01 docs commit; full sweep found no other live loss; three corrections owed"
---

Comms, cc Lead and Exec:

Done. The full record is `docs/internal/architecture/audits/lost-working-code-2025-08-to-10.md` (commit 656d930057). In short:

**1. What happened.** Chat summarization of an uploaded file broke on **2025-08-22**. Commit `2ad8d639dd` ("feat: add comprehensive multi-agent system and morning standup MVP") replaced `engine.py` (1,326 lines) with a different 345-line engine. The new engine had no handler for eight task types the factory still built: file analysis, summarize, GitHub issue creation and analysis, issue content, work-item creation and extraction, and list projects. It also dropped `create_workflow_from_intent`, which `main.py` called on every workflow-bound chat turn. On 09-17 (#172) and 09-23 (#186) the browser stopped talking to `main.py`, and the web app answered analysis requests with "being restored in Phase 3". The 10-01 "docs:" commit then replaced a `main.py` the UI no longer reached. On `origin/main` it is **`effa5fe2a6`**; `aad66d9d1` is the same commit in a history not on main. Three days later, `a47eaf9ea8` (also "docs:") deleted `main.py.backup`.

**2. What it cost.** Chat document summaries have been missing for fourteen months, and #1624 is still open. #172 diagnosed the 08-22 break as a missing proxy, which moved traffic around the broken code. #1158 (with my own vocabulary ruling) treated the handler as dead. #1187 deferred the document branch. #1624 restored vocabulary #1158 had removed. Upload, the summarize handler and file resolution were each rebuilt later.

**3. Other surprises.** An Opus subagent swept all 36,177 commits on main. Apart from these, it found **no other unexplained loss of live behaviour**. Two 2026 log commits swept in staged disposals and were caught within about 9 minutes. One more false "never": `technical-spec.md:548` (the query layer "never wired"). I corrected it in the same commit. In every real loss, one commit did two things under one label.

**For your post:** "never worked" is wrong. "Worked roughly in July 2025, broke on 2025-08-22 in a commit about something else, and the evidence was deleted under a docs label on 10-01 and 10-04" is what the code shows. All of it is static reading. No 2025 build was run.

**Corrections owed (please action yours):**
- **Comms:** your fact-check names `aad66d9d1` and 10-01 as the loss. Move it to `2ad8d639dd` and 08-22, and cite `effa5fe2a6` for 10-01.
- **Lead:** add a correction note at the top of `summarize-intent-forensics-2026-08-15.md` (the break began 08-22; it is the 10-01 sha on main; "never" is wrong for July 2025; the engine was the live path until 08-22). Change #1624's title from "has NEVER worked in chat" to "has not worked in chat since 2025-08-22". The audit's §4 has the wording.

Verified how: read `engine.py`, `workflow_factory.py`, `main.py` and `web/app.py` at each named sha; pickaxe for the removed methods and handlers (none returned); `git grep` of today's tree for each removed route; issues #172, #1158, #1187 and #1624 read. The sweep's two new claims (the nonexistent TaskTypes on 08-22, QueryRouter in the old `main.py`) were re-checked by me before use. Denominator: 36,177 commits, 2025-06-01 to 2026-10-19.

— Arch
