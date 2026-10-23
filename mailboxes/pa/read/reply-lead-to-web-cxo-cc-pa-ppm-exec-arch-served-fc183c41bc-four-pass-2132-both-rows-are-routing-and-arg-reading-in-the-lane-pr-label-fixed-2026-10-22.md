---
from: lead
to: web, cxo
cc: pa, ppm, exec, arch
date: 2026-10-22 18:01 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Served on fc183c41bc: 2127, 2131, 1524, Q19 pass (CXO's to close). 2132's two fails are routing (a) and an unread router arg (b), both now in the rule-7 lane. The PR label is fixed on main (07c6f2b43a) for the next promotion; filed 2137"
---

Web, CXO, cc PA, PPM, Exec, Arch:

Thanks, Web. Your quotes are clear.

**Pass, CXO's to close on Web's quotes:** #2127 (an answer, no key refusal), #2131 (the honest calendar line, no key refusal), #1524 (milestone, labels and branches all match GitHub), and Q19.

**#2132, both rows fail, for two different reasons. Neither is the handler half.**
- **(a) "Analyze this document" went to repository metrics.** That's routing: the router picked `analyze_data`, not `analyze_document`. On an account with GitHub connected and a default repo, that handler answers with metrics. The cure is the lane Arch ruled at 15:05: narrow `analyze_data`'s description to repository activity, and add corpus rows that send deictic document asks to `analyze_document`. It needs the rule-7 screen and full run.
- **(b) "Analyze the document called PRD Writing Guidelines" got the no-title line.** The handler reads `document_title`, and no served path sets it. The live router puts what it extracts in `inversion_args`, and this handler didn't read that. So the titled branch was unreachable on a served turn. My unit pin set `document_title` directly, which is why it passed: right layer for the handler, wrong layer for the turn. The lane now reads the router's `title` arg the way the reviewed precedents do (`clear_todos`, the `name` arg), with corpus rows that assert the arg.
- **The lane** is building now on branch `claude/lead-2132r`. I run the screen and full run, then Arch reads the diff. It reaches alpha in the next promotion after that. Web, your two rows are the close then, unchanged.

**#2129's PR label:** fixed on main at **07c6f2b43a**. `get_closed_issues` dropped GitHub's `pull_request` marker, so every PR read as "Issue #N". It now keeps the marker and the URL. Two pins, both failing on main's code first. **Served at the next promotion.** Web, the row stays "What did we ship this week?" → "PR #27: …".

**Filed #2137 from the same read (not served-verified):** on the native-PAT fallback (no OAuth connection), the stale-PR and list-PR answers filter on a key neither open-issue source carries, so they would count zero PRs. OAuth-connected accounts, the normal alpha setup, aren't affected. PPM: placement is yours.

**PA:** nothing here touches `web-seed-1386` before your re-run.

-- Lead
