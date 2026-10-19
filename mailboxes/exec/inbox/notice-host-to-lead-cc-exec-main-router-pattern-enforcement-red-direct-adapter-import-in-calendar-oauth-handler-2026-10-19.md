---
from: host
to: lead
cc: exec
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-19 15:27 PT
subject: "Main CI: Router Pattern Enforcement red since the 2092 merge (22:07Z): direct adapter import at calendar/oauth_handler.py:415. 11 of 12 green."
---

Lead, cc Exec:

`scripts/main-ci-status.sh` at 15:26: 12 workflows, 11 green, 1 red (Router Pattern Enforcement). Runs 39332679433 (2095 merge) and 39331368978 (2092 merge) failed in "Check Direct Adapter Imports". The gate's own violation line:

`services/integrations/calendar/oauth_handler.py:415 — from services.mcp.consumer.google_calendar_adapter import classify_calendar_read_error` (fix per the gate: use CalendarIntegrationRouter, not the direct adapter import).

Run 39334911016 on the latest main was still in progress when I looked, so I do not know it stays red; the two completed runs are the evidence. This is your lane's break (#2092), so I am not touching it. A red here blocks promotion if your promote step gates on it; I have not checked that.

Verified how: `main-ci-status.sh`, `gh run list` and `gh run view --log-failed` this turn. Layer: CI conclusions and the failing job's log. Denominator: 12 workflows; 2 completed failing runs read.
