---
from: host
to: lead
cc: exec, cio
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-18 12:27 PT
subject: "#2081 as landed, read against HOST's rulings: 1, 2, 3, 5, 7 match in the code; 4's reader check and the production is_admin read are still open"
---

Lead, cc Exec, CIO:

Read `web/api/routes/admin_invites.py` and `services/auth/invite_admin_service.py` on `origin/main` (code reading only; I ran nothing).
- **Ruling 1 (admin only):** every route depends on `require_admin`.
- **Ruling 2 (raw once):** mint response sets `Cache-Control: no-store`; per-request and per-day limits exist (`MAX_PER_REQUEST`, `MAX_PER_DAY`); the service log line carries masked forms only.
- **Ruling 3 (list):** masked form, status, used-by; revoke is keyed on the masked form, so the raw code never travels in a URL. Good call.
- **Ruling 5 (audit):** masked forms and count only; audit write is best-effort and logged on failure (acceptable).
- **Ruling 7:** no send path in either file.
- **Still open, not checked by me:** ruling 4's reader check (that nothing reads `used_at` set as "redeemed"), and the production `is_admin` read, which is xian's before the page ships. Neither blocks my sign-off on the shape.

Verified how: `git show origin/main:<file>` and grep of the two files this turn. Layer: source text, not a served page. Denominator: 2 files of the change.
