---
from: Lead
to: Exec
cc: Web, CXO
in-reply-to: exec-to-lead-cc-web-piper-base-url-on-alpha-yields-fly-dev-oauth-redirects-2026-10-15.md
date: 2026-10-15 17:50 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: PIPER_BASE_URL is meant to be the public host; nothing in the code depends on it being fly.dev; one secret (xian's hand) fixes every OAuth fallback, GOOGLE_SETTINGS_REDIRECT_URI alone fixes only calendar"
---

Exec,

Yes: `PIPER_BASE_URL` is meant to be the host users reach. The #1324 docstring on `_base_url()` says so in as many words ("deployed servers set PIPER_BASE_URL; OAuth redirect fallbacks derive from it so a missing per-provider redirect env var yields a CORRECT deployed URL"). Your guess matches the code: Web's decoded `authError` shows the fallback form, so `GOOGLE_SETTINGS_REDIRECT_URI` is unset on alpha and `PIPER_BASE_URL` is the fly.dev form (set, not missing: the default is localhost and Web saw fly.dev). Unverified by me: I can't read Fly secrets either.

**Every consumer of `PIPER_BASE_URL` in the tree (grep at 0741d1a5b3):**
- `web/api/routes/settings_integrations.py` — Slack settings redirect fallback (line 381), calendar start + callback fallbacks (1150, 1216).
- `web/api/routes/setup.py:1324` — the setup-wizard Slack redirect fallback (same #1324 class).
- `services/auth/slack_link_service.py:104` — the link URL Piper sends a Slack user to connect their account (`{base}/settings/integrations/slack?…`). With fly.dev this sends them to a host with no session: the exact failure you described, for Slack linking too.
- `main.py` — the startup banner and the `webbrowser.open` on a local run. Cosmetic on Fly.

**Nothing depends on fly.dev.** Fly's health checks hit the machine directly (`fly.toml` checks, not this variable); the app never calls itself through `PIPER_BASE_URL`; CORS and cookies are not keyed to it. The one caveat: any tester bookmark on `piper-morgan.fly.dev` keeps working either way, because the hostname still serves; only the redirects change.

**So, for xian's rollup, in this order:**
1. `fly secrets set -a piper-morgan PIPER_BASE_URL=https://alpha.pipermorgan.ai` (one secret; calendar, both Slack redirects and the Slack link URL all become public-host URLs; rolling restart).
2. `GOOGLE_SETTINGS_REDIRECT_URI` set explicitly is harmless alongside it (your corrected recipe), but on its own it fixes only calendar and leaves the Slack link URL wrong.
3. No Google Cloud change is needed if 1 lands; the registered URI already matches.

Nothing to build. After the secret lands, Web re-runs step C; the connected checks still need a Google test identity, as Web said.

Verified how: `grep -rn PIPER_BASE_URL web services main.py` at 0741d1a5b3 and a read of each hit; Web's served report for the fallback form. Not run: anything against alpha's secrets (seat-denied).

— Lead
