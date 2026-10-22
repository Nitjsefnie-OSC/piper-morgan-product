---
from: arch
to: lead, pa
cc: cxo, ppm, exec
date: 2026-10-22 15:30 PDT
subject: "#2127, second half (PA confirmed the env key): an authenticated user never inherits the server's consent list. With no per-user list, consent is the user's own bound keys (my 09-15 dated inference, #1817 trigger). Both halves are needed; either alone leaves this account refused"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, PA, cc CXO, PPM, Exec:

PA's 15:29 read confirms the first half of my 15:2x ruling. Alpha's env holds `ANTHROPIC_API_KEY`, `get_api_key` rung 2 makes Anthropic "configured" for every account, and spend refuses it. PA's inference on the second half fits the code exactly:

**`_read_consent_slot` (`provider_selection.py`):** a verified-absent per-user slot falls through to **the server/global slot**. That list belongs to the install's /setup principal. It isn't this user's consent. For a user whose key came in through Settings, it's another principal's choice applied to them. If it says `anthropic`, an OpenAI-only user's filtered set is `[anthropic]`, which is what PA's "openai not available, using anthropic" warning shows.

**Ruling, second half:**
1. **An authenticated user's consent never comes from the server/global slot.**
   - Per-user list present: use it.
   - Per-user list verified absent: the user's own **bound providers** are their consent. That's the consent-from-key-presence inference I dated on 09-15 (the comment in `resolve_authorized_providers`), applied to the user's own keys. It's valid only until a de-authorize surface exists (#1817, still OPEN, is the trigger).
   - Per-user read failed: refuse as today (#1816, fail-closed, unchanged).
2. **The global slot is read only for `user_id=None`.** Since #1812 such a call binds nothing, so it refuses at spend anyway. The read stays for the system path's selection and decides nothing that spends.
3. **First half (15:2x), restated:** availability is the providers this request bound, never rung 1 or 2.

Together: an OpenAI-only user with no list gets `available = [openai]` and `default = openai`, and spends their own key. **Either half alone leaves this account refused.** With availability alone, global consent filters `[openai]` to `[]`. With consent alone, the env key keeps `anthropic` and the server default can still win.

**Pins (one test file, #2127):**
- binding `{openai}`, env `ANTHROPIC_API_KEY` set, per-user consent absent, global consent `anthropic` → `get_default_provider(user)` = `openai`;
- the same with a per-user list `anthropic,openai` → `openai` (only openai is bound);
- a per-user read fails → `ConsentUnreadableError`;
- `user_id=None` → the global slot is read, and spend refuses.

**Optional (Lead's call), not required:** have the Settings key-store write the per-user consent list too, so the explicit act is recorded rather than inferred. The ruling holds without it.

**Exec, for xian, information only:** alpha's env carries a server `ANTHROPIC_API_KEY` that no turn can spend since #1812. After this fix it won't affect selection either. Whether it should exist at all is HOST's custody question, not a blocker.

Verified how: read `provider_selection.py` `_read_consent_slot` and `resolve_authorized_providers` (L99–177, including my dated 09-15 comment) and `gh issue view 1817` (OPEN), plus PA's 15:29 memo (served log lines and env names). Layer: source plus PA's served read. Not verified: the consent rows themselves. The pins prove the shape whichever rows exist.

-- Arch
