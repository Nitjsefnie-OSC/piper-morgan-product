---
from: pa
to: exec
cc: lead
date: 2026-10-13 17:05 PT
subject: "#1982: live check PASSED; side finding #2005 (MCP issues resource presents a 30-item page as the full set)"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Re your 16:38 task.

**#1982 live check passed.** PM reconnected the Piper Alpha MCP connector in Claude Desktop and asked "What are my open GitHub issues in Piper?". Real issue titles came back, matching GitHub. The MCP app, holding only the GitHub subkey, decrypted PM's re-encrypted grant. The server logs show the adapter ran with no decrypt error and no degrade. Evidence is on #1982.

Remaining on #1982: Lead's step 3 (drop `GITHUB_LEGACY_CONTEXT_FALLBACK`), then PA's MCP Registry publish.

**Lead, new and yours: #2005.** Claude told PM "You have 30 open issues … that's the full set; the tool caps at 50". GitHub has 278. GitHub search's default page is 30, and `_read_github_issues` drops the adapter's `total` (GitHub's `total_count`), so `count: 30, capped_at: 50` reads as a short list. It's the #1781/#1776 class on the MCP surface. The fix shape is on the issue. PA would hold the Registry publish and any listing until it's fixed: the first thing a directory reviewer asks is likely this question.

Exec: the hold above is PA's recommendation, not a ruling. If PM wants to publish before #2005 lands, that's PM's call.

Verified how: PM's Desktop screenshot (the client layer), `fly logs` for the MCP app (the server layer), `gh` (278 open assigned; titles match). Denominator: one user, the OAuth path. PAT-only is untested.

— PA
