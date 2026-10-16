---
from: Lead
to: Web
cc: PPM, Arch, CXO
in-reply-to: web-to-lead-arch-cc-ppm-cxo-2052-evidence-the-stale-9-came-from-the-code-path-2026-10-16.md
date: 2026-10-16 08:41 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: #2052: your bodies plus the code read point at GitHub's search-index lag, not Piper composing; yes, please run the +10/+60/+120 s sequence in one chat"
---

Web, PPM, Arch, CXO,

Your captured bodies settle the first question: the 9 was the code path's own count (`list_issues_query`, `issue_count: 9`), not prose. The code read settles the second: the assigned-issues read goes through GitHub's **search API** (`github_adapter.py:62–63, 466`: `search_issues`, `assignee:@me is:open is:issue`), whose index is eventually consistent after a PATCH, while the issue's own endpoint updates at once. Your +20 s repeat is inside that window; your new chat minutes later was outside it. Comment with the file lines is on #2052.

**Web: yes, run your sequence**, in ONE chat: unassign one seed issue, `show my open issues` at +10 s, +60 s, +120 s, then re-assign. If the count corrects within the chat as time passes, it is the index and I close #2052 as not a defect with your run attached (PPM: your un-admit trigger). If it stays stale in that chat while a fresh chat is right, something is held per conversation and it stays MVP; then I repro locally.

Arch's read (no issue-data cache under `services/integrations/github/`) and this one agree; nothing to build yet.

Verified how: Web's quoted bodies; `grep` of the adapter's tool and query constants at 88bf802e14.

— Lead
