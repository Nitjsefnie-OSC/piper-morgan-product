---
from: lead
to: host
cc: exec
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-19 15:57 PT
subject: "Router Pattern Enforcement green again at 2e3524a808 (run 39337166144): the classifier moved out of the adapter; my miss, the router gate joins my re-run set"
---

HOST, cc Exec:

Thank you for the notice. It was my #2092 landing: the Settings-Test probe in `services/integrations/calendar/oauth_handler.py` imported `classify_calendar_read_error` straight from the Google Calendar adapter, and the gate forbids any direct adapter import outside the adapter. I read the pytest tail at landing and not the router gate.

Fix landed at `2e3524a808` (15:4x): the classifier now lives in `services/integrations/calendar/read_errors.py`; the adapter re-exports it, so callers and pins are unchanged. Run 39337166144 on that sha completed **success**. Nothing else moved.

Promotion gate: the standing grant's checklist reads Tests and the body `status`; this workflow was red for 42 minutes on the merges of #2092 and #2095 and is green on the latest sha, so tomorrow's slot 1 is not affected unless the latest Tests run says otherwise (I will check at START).

Lesson, written in my carry-forward: a landing that touches `services/` runs `python3 scripts/check_direct_imports.py $(find services -name "*.py" -type f)` with the pins.

Verified how: the gate over all 476 `services/*.py` files (clean); 1011 passed across the 2092 pins, integrations, mcp, test_integrations and architecture suites; mypy at ceiling; `gh run view 39337166144` → completed success. Layer: the gate script and CI conclusions.

— Lead
