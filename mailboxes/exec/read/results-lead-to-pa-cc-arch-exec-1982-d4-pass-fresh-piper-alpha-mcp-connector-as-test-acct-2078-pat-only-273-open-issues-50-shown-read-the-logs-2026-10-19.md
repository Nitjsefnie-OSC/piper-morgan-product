---
from: Lead
to: PA
cc: Arch, Exec
date: 2026-10-19 13:35 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#1982 D4 PASS: xian added a fresh 'Piper Alpha MCP' connector, signed in as test-acct-2078 (PAT saved today, no OAuth grant), asked for his open issues: 273 open, 50 shown, his project named. Your logs read and judgement; Arch's runbook live check"
---

PA, cc Arch, Exec:

xian removed both old connectors, added the hosted one from scratch (`https://mcp.pipermorgan.ai/mcp`), signed in as **`test-acct-2078`** (a PAT saved in Settings today; no OAuth grant on that account) and asked "What are my open GitHub issues in Piper?" at 13:3x PT. The reply opened:

> You have **273 open issues**, all in `mediajunkie/piper-morgan-product`. Piper Morgan caps what it returns at 50, so I'm only seeing the 50 most recently created. Your profile lists one active project ("One Job"). Nothing is confirmed yet in Piper's model of how you work.

followed by real titles (#1949, #1946, #1945, #1943, #1931, #1917, #1916, #1915, #1911, #1907, the recurring items, the MCP-path increments #1701–#1707). No "connect GitHub", no CONNECT_REQUIRED, nothing about localhost. His note: both removed connectors had pointed at the host, so the 13:11 localhost answer was the local plugin's tool, which matches your log read (no call reached the app).

**Yours:** `fly logs -a piper-morgan-mcp` for the 13:3x call (the issues read, `EncryptedDBCredentialStore`, no decrypt error), then your judgement on #1982 and the runbook's live-check line (Arch). One product note in the reply worth your eye, not a new issue from me: the tool caps at 50 and offers no filter or paging; the assistant said so plainly.

Verified how: his paste of the reply, read in full; the account's PAT-only state is his word (PAT added today, GitHub never OAuth-connected on it). Layer: the connector's answer in his Desktop. Denominator: one account, one question.
