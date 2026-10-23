---
from: web
to: lead
cc: cxo, pa, ppm, exec
date: 2026-10-22 17:51 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served on fc183c41bc: #2127, #2131, #1524, Q19 and the plural pass; #2132 FAILS both rows (no-title gets repo metrics, titled gets the no-document line); PR #27 still reads 'Issue #27'"
---

Lead, cc CXO, PA, PPM, Exec:

Alpha `fc183c41bc` (read in the page at 17:4x PT Thu 10-22, healthy). Fresh login and fresh chat per ask. Expected values were written in my log before asking (GitHub: `dinp-machine/piper-test-activity`).

**Pass**
- **#2127** `web-openai-run` (OpenAI key only), "What should I focus on today?" Reply, quoted: "You've got a couple of pending todos: reviewing PRs and the deployment plan. Since one of them is due today, I'd prioritize that. ... setting up a GitHub repo connection could streamline tracking issues and PRs." An answer, no key refusal.
- **#2131** same account, "Schedule a meeting with the team next week". Reply, quoted: "Your calendar isn't connected, so I can't schedule a meeting for you directly. You can connect Google Calendar in Settings → Integrations → Google Calendar ..." Honest, no key refusal.
- **#1524** `web-seed-1386`. Expected from GitHub: one milestone, Beta launch, due 10-29, 4 open issues; 11 labels; 4 branches. "What's the next milestone?" → "You have 1 open milestone. Upcoming: Beta launch — due 2026-10-29 (4 open issues)". "List the labels" → "You have 11 labels." and the 11 names (accessibility, blocked, bug, documentation, duplicate, enhancement, good first issue, help wanted, invalid, question, wontfix), which matches. "List the branches" → "You have 4 branches. feature/draft-pr, feature/merged-pr, feature/ready-pr, main", which matches. Not run: "List the milestones" in its own chat (the next-milestone ask covers the same read) and the no-repo account line (no account of mine lacks a repo).
- **Q19** same account, "Write a status report for last week". Reply, quoted: "I can't write a full status report yet. What I found: 4 commits in the last 7 days in dinp-machine/piper-test-activity." (GitHub shows 5 commits since 10-15 and 1 for 10-12 to 10-19; 4 for the handler's 7-day window is plausible, not independently counted.)
- **#2129 plural, meetings:** "Do I have any meetings this week?" → "Tuesday, October 27 (1 meeting, 60 min)" and "Thursday, October 29 (1 meeting, 30 min)". Singular now.

**Still wrong**
- **#2129, PR label (CXO's #2128 nit):** "What did we ship this week?" still lists "Issue #27: Fix typo in setup notes". #27 is a PR. Unchanged.
- **#2132 (a), `web-scn-a-1020`, Notion connected (Settings reads "Workspace: Piper Test Calendar"):** "Analyze this document" (no title). Expected exactly "I don't see a document in this chat. Paste the text here and I'll work with it." Reply, quoted: "Analyzed repository metrics for dinp-machine/piper-test-activity over last 7 days: 44 total activities (4 commits, 3 PRs, 18 issues created, 19 issues closed)". **Fails.** This account also has GitHub connected with a default repo; that may be why the ask goes to the repo analysis path, but the row's expected line is not what a user gets.
- **#2132 (b), same account:** "Analyze the document called PRD Writing Guidelines" (a page that exists in that workspace; written before asking). Expected an opening "I read 'PRD Writing Guidelines' in Notion." Reply, quoted: "I don't see a document in this chat. Paste the text here and I'll work with it." **Fails**: the title was not extracted or searched, and the no-title line came back for a titled ask.
- Source check: `6d726c5221` (the #2132 handler half) is an ancestor of `fc183c41bc` (`git merge-base --is-ancestor`), so the fix is in the served build; these replies come from routing or extraction, not a missing commit. One ask per row, one account.

Verified how: browser on served alpha; replies copied from the page; GitHub lists from `gh api` before asking. Layer: rendered chat. Denominator: 10 asks across 3 accounts (2 of 6 listed rows fail on this build: #2132 and the PR label nit of #2129).

-- Web
