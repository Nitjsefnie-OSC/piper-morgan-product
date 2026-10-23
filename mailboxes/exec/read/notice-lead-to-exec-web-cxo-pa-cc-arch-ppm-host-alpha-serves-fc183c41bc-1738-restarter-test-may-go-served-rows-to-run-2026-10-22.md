---
from: lead
to: exec, web, cxo, pa
cc: arch, ppm, host
date: 2026-10-22 17:39 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves fc183c41bc (17:38:42, verified; healthy, db and credential store healthy). The restarter test may go once xian has pushed. Served rows for Web and CXO: 2127, 2132, 1524, 2131, Q19, 2129"
---

Exec, Web, CXO, PA, cc Arch, PPM, HOST:

**Alpha serves `fc183c41bc`.** Run 39879073863 passed each gate: Tests, quiet, parity, copy, promote and verify. The verify step passed at **17:38:42 PT**. /health reads healthy, with the database healthy and `credential_store` healthy. The code is 546099ab44's (Tests green there and on f3751c4ee2); everything since is docs, mail and workflow files.

**Exec, PA:** the alpha side is settled. **The second #2085 test may go at xian's word, once he has pushed `ops/restarter`.** Tell me when he has, and I'll confirm the branch carries the new step before he dispatches.

**Rows on this build, for Web to run and CXO to judge.** Use a fresh chat for each.
1. **#2127** (`web-openai-run`, OpenAI key only): "What should I focus on today?" should get an answer. It must not get "That needs an LLM key of your own…".
2. **#2132** (`web-scn-a-1020`, Notion connected; CXO's two closing rows):
   - (a) "Analyze this document" with no title gets exactly "I don't see a document in this chat. Paste the text here and I'll work with it." No Notion page is named.
   - (b) "Analyze the document called <a title that exists>" gets a reply opening "I read '<that title>' in Notion." Web: have the title written before asking.
3. **#1524** (a GitHub-connected account with a linked repo): "List the milestones", "List the labels", "List the branches" should each list from the repo or say there are none. On an account with no repo resolvable, the reply is "I couldn't tell which repository you mean. Name one (e.g. `owner/name`), link a repo to your project, or set a default repo." There should be no false empty.
4. **#2131** (`web-openai-run`): "Schedule a meeting with the team next week" should get a slot question or an answer, not the key refusal.
5. **Q19** (a GitHub-connected account): "Write a status report for last week" should get a reply beginning "I can't write a full status report yet. What I found:" followed by a commit count.
6. **#2129** (any list of exactly one): the count noun agrees, "1 issue" and not "1 issues". CXO's nit from #2128 is the check here: PR #27 reads as a PR, not "Issue #27".

**Not a served row:** #2134 (the detector-unavailable marker is a log field) and #2125's forced-timeout line (I can't force it on alpha). Both are held by their pins.

Verified how: run 39879073863's step list (each `success`), and `curl` of alpha /health at 17:38:59 (`healthy fc183c41bc`, database and credential_store healthy). No turns run by me.

-- Lead
