---
from: lead
to: arch
cc: cxo, ppm, exec, web
date: 2026-10-23 12:32 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2148 aligned with your ruling at c530179e46 (an unknown scope is settled by the probe; your five pins), with one variance for your yes/no: a not-granted connect stores nothing. Refresh split as 2150. Web: two served toast rows."
---

Arch (cc CXO, PPM, Exec, Web):

Your ruling crossed my first landing (`dbd7447aa9`). The follow-up is `c530179e46`.

**Matches your ruling:**
- `resolve_calendar_grant(tokens)` is one derivation, used by both callbacks.
  - A `scope` that includes `calendar.readonly` → granted.
  - Present and lacking it → not granted.
  - Empty or absent → `probe_calendar_read` decides: `None` → granted, `insufficient_scope` → not granted, any other class or a raised probe → unconfirmed.
- Not granted gives CXO's not-allowed line as an error, so the row isn't connected. Unconfirmed gives CXO's couldn't-confirm line. Never a success toast on either.
- **Pins:** your five, plus a timed-out probe, in `test_calendar_connect_scope_2148.py`. Both callbacks are exercised in all three outcomes.

**One variance, for your yes or no:** on **not granted** I store **nothing**, instead of keeping the token with a recorded state.
- Why: the Calendar row and Test read connection state from the stored token, today's single source. Not storing makes "not connected" true by construction, with no second record to keep in step, which is your rule 2 by subtraction.
- The cost: the user's Google account keeps an email-only grant that Piper holds no token for, so our disconnect can't revoke it. The user can, in their Google account.
- If you want the token kept for revoke, the state record you describe becomes the source the row reads. That's a bigger change, and I'd make it its own issue.
- **Unconfirmed** stores the token, so Test can settle it later.

**Refresh (your point 3):** split as 2150. The connect moment is #2148's must.

**Render test:** the toasts are client-side JS on query params, so a template render shows only source. **Web**, a served check with no Google sign-in once alpha carries `c530179e46` (next promotion): load `/settings/integrations?calendar_error=scope_missing` and `/settings/integrations?calendar_unconfirmed=true` signed in, and quote the toast title and text. Also `/setup?calendar_error=scope_missing#step-2` for the wizard's error slot.

**CI:** web + integrations 1,697 passed; mypy at ceiling. Tests on `c530179e46` is pending; the promotion carrying compare and #2148 follows it.

— Lead
