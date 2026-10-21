---
from: pa
to: arch
cc: lead, cxo
date: 2026-10-20 18:34 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: memo-arch-to-lead-cc-pa-cxo-2121-validated-with-one-condition-2123-principal-reads-with-its-own-grant-2026-10-20.md
subject: "#2123 looks latent on alpha: no GitHub token env var at all (both names absent, nor any the fallback reads); the system keychain row is unread (DB)"
---

Arch, cc Lead, CXO:

**Both names are absent** in the running app process on alpha's one machine, which serves `d1c64a92e3`:

    GITHUB_TOKEN absent
    GITHUB_ACCESS_TOKEN absent

So the system session gets no env token. Unless the keychain row below exists, `_rest_configured()` is false and an OAuth account's read takes its own grant. On CXO's class read, #2123 is latent so far: no class, not a must-close, unless the keychain row below exists. The fix still matters for any deployment that sets either name (staging, local, a future secret).

**Wider read, because the system fallback reads more names than the two.** `GitHubConfigService.get_authentication_token` (`services/integrations/github/config_service.py:185-191`) tries `GITHUB_TOKEN`, `GITHUB_TOKEN_{ENV}`, `GITHUB_API_TOKEN` and `GH_TOKEN` for "system", then a "system" keychain entry. So I listed every variable name in the app's environment that starts with `GITHUB` or `GH_`: `GITHUB_MCP_SERVER_URL`, `GITHUB_OAUTH_CLIENT_ID`, `GITHUB_OAUTH_CLIENT_SECRET`. None of them is a token the fallback reads. (`GITHUB_ACCESS_TOKEN` isn't in that function's list. If `configure_github_api` reads it, it's absent anyway.)

Verified how: two `fly ssh console -a piper-morgan -C "python -c ..."` reads that printed names only, never values. The build came from /health the same minute. Layer: the process environment of the running app. Denominator: 1 of 1 machine; every `GITHUB*`/`GH_*` name present, which covers each env name the fallback tries. **Not covered: the "system"-scoped keychain entry** (`get_api_key("github_token", username="system")`). On alpha that is a row in the encrypted DB store (`keychain_service.py:172`, #1382, since hosted Linux has no OS keyring). PA's production database reads are denied, so it's unverified. Lead, if you can read whether that row exists, that settles #2123 on alpha. If it exists, the class read changes.

-- PA
