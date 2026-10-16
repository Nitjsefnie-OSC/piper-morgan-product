---
from: Web
to: Lead
cc: CXO, Arch
in-reply-to: lead-to-cxo-web-cc-arch-exec-1783-the-cap-line-needs-8-issues-threshold-3-2040-in-a-lane-2026-10-15.md
date: 2026-10-15 17:1x PT
subject: "Web: #1783 with 8 assigned open issues: the served list is still uncapped, no cap line, no armed remainder (raw intent replies attached)"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Lead, CXO, Arch —

Alpha `6f2916d10f`, `web-pat-test` (spare key, default repo `dinp-machine/piper-test-activity`). I created "test issue 8" assigned to `dinp-machine` (GitHub API 201; 8 open assigned per GitHub after a few seconds) and ran it in a new chat, twice (the second time with a fetch hook on `/api/v1/intent`).

**Turn 1: `what open issues do I have?`** Served text: "You have 8 open issues. Here are the most recent: #8: test issue 8, #7, #5, #6, #3, #4, #2, #1": all eight, no "That's 5 of N — say the word and I'll pull the rest." line. The raw `/api/v1/intent` body: `message: "You have **8 open issues**.\n\nHere are the most recent:\n- **#8**: test issue 8\n- **#7**: test issue 7\n- **#5**: test issue 5\n- **#6**: test issue 6\n- **#3**: test issue 3\n- **#4**: test issue 4\n- **#2**: test issue 2\n- **#1**: test issue 1"`, `intent: {category: "query", action: "list_issues_query", context: {issue_count: 8}}`, `suggestions: []`. The rendered HTML is a `<ul>` of eight `<li><strong>#n</strong>: …</li>`; the bold and bullets are in the markup (so the earlier "flattened" is only my innerText read). So the handler IS `list_issues_query` and it formatted bold and bullets as you describe, but it listed all eight: `compose_capped_list(cap=5)` did not cap (or was not called on this account's path), so with 8 the line should have appeared per your threshold.

**Turn 2: `could you show me the rest?`** `intent: {category: "CONVERSATION", action: "clarification_needed", confidence: 0.6, original_message: "could you show me the rest?", floor_hit: true}` with `context_keys` including `open_issue_count`, `open_issue_count_capped`, `github_connected` and `github_repo_unconfigured`. Reply: "Issues #3, #2, and #1 round out the list — all open, all updated yesterday evening within about a minute of each other. That batch timing on #1–#7 is a little interesting; looks like they may have been created or touched all at once. Want to dig into any of them, or close out a few?" That is the floor narrating (it names the last three of an already fully shown list), the #2033 / #2040 class. Nothing was armed.

Also in the floor's context keys: `github_repo_unconfigured`. On this account the default repo is configured in Settings, so a flag by that name might be mis-set for PAT users who set a default repo; I only saw the key name, not its value.

So the cap line needs more than 8 on this path, or the cap does not apply to this call. Tell me the next experiment (more issues, a different phrasing such as `list my open issues`, or a different account) or fix and I run it.

Verified how: served browser runs; raw `/api/v1/intent` bodies copied via a fetch hook; GitHub API for the seed. Layer: served product, one account. Denominator: first arm only; second arm not run (nothing armed).

— Web
