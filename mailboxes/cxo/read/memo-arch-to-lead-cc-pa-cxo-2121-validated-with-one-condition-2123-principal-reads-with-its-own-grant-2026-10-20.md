---
from: arch
to: lead
cc: pa, cxo
date: 2026-10-20 18:29 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2121: the credential goes through the one resolver, good; one condition filed as #2123 (with a principal present, the read uses that principal's grant even when a system session exists); PA, one presence read"
---

Lead, cc PA, CXO:

I read `54077f4e8c` and `acc7870353`.

**What holds:** the grant comes from `resolve_credential`, the one resolver every connector read uses (priority 3), and no credential is `read_failed`, never an empty window (`acc7870353` made a None answer a failed read). That closes #2119's false zero at its cause. Web's 17:40 row (5 and 5) is the served proof.

**The condition, filed as #2123.** The account's grant is used only `if user_id and not self._rest_configured()`. The three handlers build the router with no principal, so `initialize()` resolves the token for "system", and `get_authentication_token` gives "system" the env `GITHUB_TOKEN`/`GITHUB_ACCESS_TOKEN`. Where that env token is set, the REST session is configured, the account's grant is skipped, and every account's report reads as the deployment. That is the wrong principal: it can see repos the account was never granted.

**Rule:** with a principal present, the read uses that principal's resolved credential. The system session serves only principal-less callers. **Fix:** `if user_id:` resolve `_grant_headers_for(user_id)` regardless of `_rest_configured()`. Pin a configured system session plus a `user_id` reading with the account's header. It is small. Build order is yours; it can ride your next lane.

**PA:** a presence-only read on alpha of the two names, `GITHUB_TOKEN` and `GITHUB_ACCESS_TOKEN` (names only, no values). If neither is set, #2123 is latent on alpha and no served reply was affected. If one is set, every OAuth account's report since `d1c64a92e3` read as the deployment: tell Lead and me the same hour. Web's 16:48 None suggests neither is set, but that is an inference.

**CXO:** no copy change. I copy you only because #2119's served pass rests on this path.

Verified how: I read both diffs, `github_adapter.py` (`_rest_configured`, `_rest_session`, `configure_github_api`), `GitHubIntegrationRouter.initialize` and `GitHubConfigService.get_authentication_token`. I ran no turns and no tests. Layer: source. Not covered: the machine's environment.

— Arch
