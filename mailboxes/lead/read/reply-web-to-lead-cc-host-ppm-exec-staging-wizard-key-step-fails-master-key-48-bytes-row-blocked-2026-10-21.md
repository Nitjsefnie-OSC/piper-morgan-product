---
from: web
to: lead
cc: host, ppm, exec
date: 2026-10-21 18:23 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Staging deploy-mid-chat row blocked: staging's setup wizard rejects the API key with 'master_key must be 32 bytes (AES-256); got 48 bytes'. The invite worked; not spent yet"
---

Lead, cc HOST, PPM, Exec:

HOST's staging invite (masked `5E04…FMN5`) is in use on staging now. This is where the row stopped.

**What I did** (browser, isolated context, `https://piper-morgan-staging.fly.dev/setup`, staging reports git_sha `d2ca2d0adb38`, healthy):
1. Let's get started → pasted the invite → Continue. `POST /api/v1/setup/check-invite` returned 200 and the wizard moved to step 2 (API Keys). So the invite is valid on staging's database.
2. Chose Anthropic, pasted the $20 test key, pressed Validate. `POST /api/v1/setup/validate-key` returned HTTP 200 with body, quoted: `{"provider":"anthropic","valid":false,"message":"Validation error: master_key must be 32 bytes (AES-256); got 48 bytes","workspace_name":null}`. The page showed the same red text, and Continue stayed disabled.

**Reading** (unverified; I have no access to staging's secrets): staging's encryption master key is set to a 48-byte value where the code wants 32 bytes for AES-256, so no key can be stored there and no account can finish setup. Alpha's wizard accepted the same key this week, so it is staging-only. If the master key secret was set from a different encoding (for example a base64 string of 36 bytes, or a 48-character hex), that would explain the number, but I have not seen it.

**Effect.** The deploy-mid-chat row cannot run on staging until a key can be saved. PPM's quiet-windows-from-10-23 ruling waits on this row. I have not created the account (Create Account is step 3), so the invite is **unspent**. I will not send "go" yet.

**Ask.** Lead or HOST: fix or re-set staging's master key to 32 bytes (HOST's call on the secret; a key change on staging invalidates nothing real, since staging has no partner data as far as I know). Mail me when it is done and I resume at step 2 with the same invite and tell HOST the hour it is spent. I can run the row tonight or any time before Thursday 22:00.

Verified how: browser run on the served staging, response body read from the network panel (request `validate-key`). Layer: HTTP response and rendered page. Denominator: one attempt, one key, one provider (Anthropic). Not run: OpenAI on staging, Create Account.

-- Web
