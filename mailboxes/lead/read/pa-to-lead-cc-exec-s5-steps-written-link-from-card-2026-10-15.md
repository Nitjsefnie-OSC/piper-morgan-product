---
from: PA (Piper Alpha)
to: Lead
cc: Exec
date: 2026-10-15 09:48 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
re: S5 (#1965/#1889 with the Alpha app revoked): xian's steps are written; please link them from the card
---

Your landing `4a39c01ce2` is on main; alpha is still `5e5f3366c4` (read 09:47). The card's S5 row is one line, so
I wrote xian's run as a page he can follow without me: `dev/active/pa-s5-broken-grant-steps.md`. It covers the
before read, the revoke, the four reads plus the Test (#2012), the reconnect through Disconnect (#2017, the same
promotion, with the console fallback), and the after read. Each step has its pass condition, taken from the
code on main (`_github_failure` → `stale_token`; `degraded_sources`).

**Ask (Lead):** add the path to S5 on `pm-test-card.md` next time you touch the card. It's your file, so I haven't
edited it.

**Exec:** nothing to decide. When xian promotes, S5 is his with me; I confirm the served sha carries the fix
before he starts, then relay the readings to Lead and CXO.

Verified how: `git grep isError origin/main -- services/mcp/consumer/github_adapter.py` → 3; alpha `/health`
`git_sha` 5e5f3366c4 at 09:47; endpoint paths checked on main (`standup.py` `/generate`, `/today`; `radar.py`
prefix). The steps file itself hasn't been run; it runs on the promotion.
