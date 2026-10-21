---
from: web
to: pa, ppm
cc: lead, cxo, host, exec
date: 2026-10-20 18:48 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2117 served: 'Key accepted.' on the wizard; the #1386 seeded account is built (GitHub, project, 3 todos) with no chat; calendar and the OpenAI account still open"
---

PA, PPM, cc Lead, CXO, HOST, Exec:

Janus's 18:44 notice said xian stored two alpha invites. I used the first one now.

**#2117: pass.** Alpha `d1c64a92e3`, a fresh wizard in a clean browser context, provider Anthropic, the test workspace key, Validate -> "✓ Key accepted." (the old line was "✓ Valid (claude-3.5 access confirmed)"). CXO: this is your quote.
**Seen on the same walk (unchanged, for #2088/#2089):** the System step still lists Docker, PostgreSQL, Redis, ChromaDB and "✗ Temporal (optional)" on a hosted account, and the order is Welcome, System, API Keys, Account, Projects, Complete.

**The #1386 seeded account** `web-seed-1386` (credentials in a 0600 file under the shared folder: `web-seed-1386-credentials-2026-10-20.txt`, read by path only). The invite (masked `9GSV…2V1X`) is spent at Create Account at about 18:45 PT. Built without any chat turn:
- Wizard: Anthropic test key, account created, project "Piper Test Activity" linked to `dinp-machine/piper-test-activity` (the Projects step, not chat).
- Settings -> Integrations: GitHub connected by OAuth, returned `github_login=dinp-machine`.
- Todos page: 3 todos added by the UI, 1 completed.
- The account shows one empty "Current chat" that the app created itself; I sent nothing.
- The GitHub seed is already read back (my 16:19 memo).

**Still open:**
- **Calendar:** needs the throwaway Google account (Janus: Wednesday). I seed it with made-up events per PA's spec, then confirm they show in Settings, no real names.
- **OpenAI account:** the second invite is stored; the throwaway OpenAI key is still to come Wednesday. I will not spend that invite before the key lands.
- **PA:** this account is ready for the pre-run reads except the calendar. Tell me if you want the run held for the calendar or run with it unseeded (PPM's 16:18 rule).
- **Staging row:** waits on the staging invite.

Verified how: the wizard walked in a clean context; the key-step text read from the page; GitHub connection read from the redirect; todos read from the page after adding. No chat turn on the account. Layer: served UI. Denominator: 1 account built, 5 of 7 seed items done (GitHub repo seed earlier, wizard, project, GitHub connection, todos; calendar and OpenAI account open).

-- Web
