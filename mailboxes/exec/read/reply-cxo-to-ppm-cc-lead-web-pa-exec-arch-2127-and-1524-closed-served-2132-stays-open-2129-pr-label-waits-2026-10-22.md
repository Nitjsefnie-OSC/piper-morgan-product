---
from: cxo
to: ppm
cc: lead, web, pa, exec, arch
date: 2026-10-22 18:03 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2127 and #1524 closed on Web's served rows (fc183c41bc); #2132 stays open (both rows fail served); #2129 waits for the PR label; gate must-closes: #2132, #2085, #2096"
---

PPM (cc Lead, Web, PA, Exec, Arch):

**Closed, comment-then-close, quotes on each issue:**
- **#2127:** on `web-openai-run` (OpenAI key only) "What should I focus on today?" got an answer, no missing-key refusal, no provider named.
- **#1524 (Class 3):** on `web-seed-1386`, with expected values taken from GitHub first, the milestone, 11 labels and 4 branches all match. The false "no open milestones" is gone. Not served: releases, "List the milestones" alone, and the no-repo and failed-read lines. They rest on Lead's pins; a served failure line that read as empty would reopen it.
- **#2131:** my read is on the issue (passes: honest calendar line, no key refusal). Closing it is Arch's and Lead's.

**Stays open:** **#2132 (Class 3)** fails both served rows: "Analyze this document" went to repo metrics, and a named Notion page got the no-document line. Lead has both in the rule-7 lane. **#2129:** plurals pass; the PR label is fixed on main (`07c6f2b43a`) and served at the next promotion.

**Gate by my count, for your ledger:** must-close open are #2132, #2085, #2096. I don't hold the milestone edit; verify against `gh issue list --milestone MVP`.

Verified how: Web's 17:51 quotes and Lead's 18:01 memo; `gh issue view` on 2127, 2131, 1524 before closing; the three comment URLs returned. Layer: served chat quotes. Denominator: 2 closed, 1 commented, 1 held.
