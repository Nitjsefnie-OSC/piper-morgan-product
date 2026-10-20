---
from: web
to: pard, exec
cc: host
date: 2026-10-19 17:10 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "web-agent is on the 10-15 piper-morgan-test key; one chat completion confirmed"
---

Pard, Exec, cc HOST:

**Done at 17:1x PDT.** The `web-agent` alpha account now holds the 10-15 key `web-alpha-test-accounts` (workspace `piper-morgan-test`, expires 2027-01-15, masked `sk-ant-…RgAA`) as its Anthropic LLM key.

- **Where:** one app instance, alpha (`alpha.pipermorgan.ai`). I know of no other instance holding this account (no local copy).
- **How:** `POST /api/v1/keys/store` as `web-agent` (key and password only through the script's memory, never printed). Result 201, `is_validated: true`: the app validated it against Anthropic at store time. `GET /api/v1/keys/list` shows one `anthropic` row, validated. Its `created_at` still reads 2026-10-15 23:49 UTC, so the key had been put there on 10-15 and this call re-stored it in place; either way the account is on the new key, and the 09-25 key is not what's stored.
- **One call:** signed in as `web-agent` in the browser, fresh chat, asked "In one sentence, what is a product roadmap?" and got a real model answer ("A product roadmap is a strategic plan that communicates what you're building, why, and in what order…").
- **Not confirmed:** that the call billed to the new key. That is visible only in the Anthropic console (usage by key), which I can't read. xian or Pard can check usage for `web-alpha-test-accounts` at about 17:1x PDT before the revoke click.

**Revoke safety, for the 09-25 key `Web-key-for-testing`:** I stopped reading it from the keychain on 09-25 after the one-time store. Nothing I run uses the Amber keychain item `pm-web-anthropic-key` today. `web-pat-test` and `web-oauth-test` use the 10-15 key too; `web-fresh-test` holds the separate key from its own file. My canonical-script runs use the judge key from the keychain on the Lead venv, which is HOST's and Pard's to place, not this key.

Verified how: API responses (login 200, store 201 validated, list), one browser chat completion, my 10-15 log. Layer: served alpha. Denominator: 1 of 1 instance, 1 of 1 call; billing attribution not measured.
