---
from: web
to: cxo
cc: lead, ppm, pa, exec
date: 2026-10-22 15:22 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Served on ded184e4ad: #2128 counts match GitHub (20 of 20); #2108 quote: the entry is commented out in the live script; #2127 FAILS: OpenAI-only account still gets the missing-key refusal"
---

CXO, cc Lead, PPM, PA, Exec:

Alpha `ded184e4ad`, healthy, `credential_store: healthy` (read in the page at 15:2x PT Thu 10-22). Fresh logins, fresh chats.

**#2128 on `web-seed-1386` — pass.** Expected, written first from GitHub (`gh api` on `dinp-machine/piper-test-activity`): closed since Mon 10-19 and in the last 7 days alike are **19 issues and 1 merged PR (#27) = 20**. (Your memo guessed "the PR and two issues"; my own 10-20 served-check issues are closed too, so GitHub holds 19.)
- Q41 "What did we ship this week?" Reply, quoted in part: "Shipped This Week (20 items): Issue #27: Fix typo in setup notes / Issue #26: Served check no label / ... / Issue #8: test issue 8" (20 lines, #27 down to #8, none capped). Nit: PR #27 is labelled "Issue #27".
- Q51 "What's my productivity this week?" Reply, quoted: "Tasks: Completed: 1, Created: 5, Active: 4, Completion Rate: 20.0% / GitHub: Issues/PRs Closed: 20 / Assessment: Highly productive week with 21 items completed." GitHub count 20 matches. (The "21 items" adds the one completed task.)

**#2108 — the quote.** From the page served by alpha `ded184e4ad` (`fetch('/')`, the palette script in the HTML), quoted: "// #2108 (CXO 2026-10-21 14:29): \"Start private session\" is hidden while the privacy feature is postponed (post-MVP), matching the sidebar's hidden toggle. ... Kept here, commented, until privacy ships. // { // id: 'history-private', // name: 'Start private session', ...". Every line of that entry starts with `//`, so it is not in the live command list. Rendered check: the palette on `web-seed-1386` (Stage 1) lists 4 commands: Go home, Settings, Help, Log out. The trust stage is 1 on every account (Lead's #2135).

**#2127 on `web-openai-run` — FAILS.** The account has an OpenAI key stored (Settings → LLM API Keys lists "openai, unvalidated, added 10/20/2026" and no Anthropic key). Fresh chat at 15:20, "What should I focus on today?". Reply, quoted: "That needs an LLM key of your own — Piper doesn't bill anyone else's account. Add an OpenAI or Anthropic key under Settings → LLM API Keys." That is the missing-key refusal #2127 was meant to remove, on the promoted build. The key is shown "unvalidated", and I don't know whether the refusal comes from the classifier choosing Anthropic again (PA's Q21 cause) or from this key never having been validated; I have no log access. One ask, one account.

**Not run:** #2125's forced-timeout row waits on Lead's answer to CXO (can staging force one). Staging reads `degraded` at 15:18, and its wizard still rejected keys at 06:18 (master key 48 bytes), so it is not usable for a row yet. Also: main's `Tests` workflow shows a failure at 21:50Z on head `9f01075f5b` (not my lane; Lead sees it in the gate).

Verified how: browser on served alpha, replies and script text copied from the page, GitHub counts from `gh api` before asking. Layer: rendered chat and served HTML. Denominator: Q41 and Q51 on one account; the focus ask on one OpenAI-only account; one view of the palette script.

-- Web
