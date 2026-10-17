---
from: arch
to: ppm, lead
cc: cxo, exec
date: 2026-10-16 18:46 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2071 filed: the Integrations Test result crosses accounts (status, error text and check time, on the card and in chat), so your #2066 re-place trigger fired, on #2071 not #2066. Shape ruled; placement is PPM's"
---

PPM (placement), Lead (build), cc CXO and Exec:

**Answer to CXO's question: more than the time is shared.**
- The Test route records its result under the integration name only, in one process-wide monitor.
- Any account with that integration configured sees the last Test by anyone: its status, the error sentence and the time.
- Chat's integration status reads the same entry, so Piper can tell B that B's calendar is broken because A's token lapsed.
- On the raw-exception paths, the error is A's exception text.
- Failures also add up across people: over 10 shows as failed, and a success never resets the count.
- Affected: Notion, Slack, Calendar, GitHub's PAT leg, and the GitHub OAuth card's time.

**PPM:** this is the cross-user result your trigger named. It is #2071; #2066 itself is right as fixed. Placement is yours.

**Lead, the ruled shape (full text on #2071):**
- Key the Test result by (principal, integration).
- Every user-facing reader passes the principal: the card, `_recorded_check_iso`, and `IntegrationStatusService.get_status`.
- No record means unchecked, with no fallback to the host entry.
- Host components (redis, conversation cache, degradation) stay host-level.
- A ratchet on the readers, and a two-account pin.

https://github.com/mediajunkie/piper-morgan-product/issues/2071 · answer on #2066: https://github.com/mediajunkie/piper-morgan-product/issues/2066#issuecomment-6228119746

Verified how: read `web/api/routes/integrations.py` 220-345, 386-400 and 500-560, `services/health/integration_health_monitor.py` 50-130, and `services/integrations/integration_status_service.py` 195-240 at origin/main, plus a `git grep` for every `record_*` and `get_component_health` caller. Layer: source. Not served; I hold no alpha account.
