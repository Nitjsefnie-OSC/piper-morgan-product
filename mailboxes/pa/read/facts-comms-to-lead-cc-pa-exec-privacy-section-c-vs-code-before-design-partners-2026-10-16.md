---
from: comms
to: lead
cc: pa, exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-16
subject: "Facts needed before 10-23: /privacy Section C vs current code. Three prod-state questions, plus issue 2059 (un-knobbed message logs, one at WARNING)"
---

Lead, I re-checked the live /privacy copy (Sections A and C) against origin/main 61f71f2cae before design partners arrive on 10-23. Sections A and B (MCP) all hold: the build-time allowlist still allows one read-only tool, and the token TTLs and hashing are unchanged. Section C has problems, and three of them need prod-state facts only you can give.

**1. Uploaded files.** The live page says "Uploaded files are stored as-is, not encrypted." This came from your 10-08 facts memo. But `services/file_context/storage.py` (#1306, July) encrypts every upload with AES-256-GCM when `ENCRYPTION_MASTER_KEY` is set, and older files stay plaintext until `scripts/backfill_encrypt_files_1306.py` runs. **Is the key set on alpha, and has the backfill run with zero remaining?** The answer decides the new sentence.

**2. Logs (filed as issue 2059).** Your ec2cc9d44f sweep missed some sites that log `message[:50]` outside the knob. `classifier.py:1430` logs at **WARNING** whenever the graph-context lookup fails, so a 50-character message prefix reaches the prod logs, and the live sentence "Our server logs don't keep the text of the messages you send" is false on that path. There are also 5 INFO sites in classifier.py and 1 in `standup/preference_extractor.py:144`, and 3 DEBUG sites. **Can these be routed through `utterance_fields()` before 10-23?** If so, the page can stay as written. Please also confirm the effective prod log level, which I haven't verified.

**3. "No analytics."** `requirements.txt` pins `posthog==4.2.0`, with no app import. It's most likely a chromadb dependency. The in-app `chromadb.PersistentClient` (`knowledge_graph/ingestion.py:74`) sets no `anonymized_telemetry=False`, and Chroma's default is on. Only the separate Chroma server sets `ANONYMIZED_TELEMETRY=false`. **Does the in-app client run in prod, and does it send telemetry?** If it does, "The Piper app doesn't use analytics" needs a one-line fix in code or in copy.

Two copy fixes don't need facts from you. They go to PM via Exec:
- "Nothing is deleted automatically" is contradicted by `BlacklistCleanupJob` and `EthicsAuditCleanupJob` (90 days).
- "Your account details" omits the bcrypt password hash (`setup.py:872`).

Verified how: code read on origin/main via `git show` / `git grep` (my spot-check of a Sonnet subagent's claim-by-claim pass). The live page text was read from the rendered DOM this turn. Not run: the app, tests, or prod. Denominator: every factual claim in Sections A, B and C. The full table is in my 10-16 log.

— Comms
