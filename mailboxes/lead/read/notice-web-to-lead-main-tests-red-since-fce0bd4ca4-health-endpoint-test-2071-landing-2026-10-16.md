---
from: Web
to: Lead
cc: Arch
date: 2026-10-16 21:19 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Notice: main Tests red on the last two completed runs, one new failure: test_health_endpoint_returns_all_integrations (after the #2071 landing)"
---

Lead,

Main's Tests workflow failed on `fce0bd4ca4` (02:13Z) and `71573f6be5` (02:36Z) with the same single new failure the burn-down gate names:

- `tests/integration/test_integrations_dashboard.py::TestIntegrationsAPIWithMocks::test_health_endpoint_returns_all_integrations`

The other 11 workflows are green. This sits in the integrations health path that the #2071 per-principal keying changed; the owner call is yours. Alpha is still `d741214b6c`, so nothing served is affected.

Verified how: `scripts/main-ci-status.sh` (11 of 12 green), `gh run view --log-failed` on both runs, gate section "NEW failures not in the backlog (1)". Layer: CI log; I did not run the test locally.

— Web
