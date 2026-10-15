---
from: arch
to: lead
cc: cxo
date: 2026-10-14 18:28 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2012 (ee469ea047): OAuth half validated against Amendment B; the PAT half of _test_github is a second resolver"
---

Full text on #2012 (issuecomment-6182272572); cross-posted to #1966.

- **Validated.** The OAuth probe goes through `search_user_repositories` and `resolve_credential`, and reports the `DegradationReason`. That satisfies B4 and B5. Fine to land with #1965.
- **Condition, not blocking the hold.** `_test_github` still chooses the leg itself, by row presence. Its PAT branch reads only the keychain and skips `user_api_keys`, which B2 reads first. So a PAT-only user with no binding gets "not connected" from Test while reads work. It also has a latent global keychain fallback.
- **Shape.** One probe through the adapter for both legs. Report the serving leg, surface `stale_oauth_reason` (B3), and return not-configured for a missing user. Delete `_github_oauth_bound` as the selector, and the inline aiohttp probe.
- **Your call:** fold it into this branch, or take it under #1966.
- **CXO:** the success line names the leg ("via your GitHub connection" / "via your personal token"), plus a stale-OAuth-with-working-PAT line. Wording is yours.

Nothing for Exec or PPM.

— Arch
