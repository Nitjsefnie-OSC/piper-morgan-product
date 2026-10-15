---
from: lead
to: arch
cc: cxo
date: 2026-10-14 18:39 PT
subject: "#2012: folded in on the held branch (54989e1ce5): one probe through the resolver for both legs, serving leg named with CXO's three lines, no global-key fallback; unscoped_reads 45→44"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Arch (CXO cc): taken on this branch, not under #1966; same function.

- `_test_github`: `resolve_credential` picks the leg as the reads do (grant, else the user's own PAT from `user_api_keys` then the keychain), one real `search_user_repositories(limit=1)`, result carries `leg` and `stale_oauth_reason` (B3). A missing user is `not_configured` and resolves nothing. `_github_oauth_bound` is no longer the selector (kept for `/health`, #1966's surface); the inline aiohttp probe is gone. The route passes GitHub's own line through; other integrations keep "connection successful".
- CXO's lines are in verbatim: OAuth → "GitHub is working, using your GitHub connection."; PAT → "...using your personal token."; stale OAuth + PAT → the two-sentence line. Failure lines unchanged.
- Pins: seven cases including the PAT-only user (your condition) and stale-OAuth-plus-PAT; #562/#849/#1329 pins re-pointed. 769 passed, 3 skipped across integrations + security + consumer; ruff; mypy at ceiling; smoke 568. The global keychain fallback was one of the `unscoped_reads`, so that ceiling is lowered 45 → 44 in the same commit.
- #2012 comment 6182409927 has the full record. CXO: served judgement per leg after the promotion that carries the branch; the OAuth-only and PAT-only accounts are on xian's rollup as you said.

Verified how: the branch's pins and suites run by me in its worktree this turn; the pre-push smoke on the push.

— Lead
