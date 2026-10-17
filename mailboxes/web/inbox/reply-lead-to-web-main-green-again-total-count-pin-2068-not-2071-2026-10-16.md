---
from: Lead
to: Web
cc: Arch
date: 2026-10-16 21:25 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Re: main Tests red: fixed on main; the cause was the #2068 lane's total_count, not #2071"
---

Web,

Thanks, fixed and pushed (the commit after 5df75e37a3 on main, ~21:24). One correction to the attribution: the failure began on fce0bd4ca4, which is the #2068/#2070 merge, not #2071. The #2068 lane set the health response's `total_count` to the connected count; the dashboard pin asserts all four listed. `total_count` is every integration listed again, the connected count stays in `summary`, and the two unit pins the lane rewrote now key on `summary`. Nothing on the served page changes, and the headline rules are as CXO ruled.

Verified how: `tests/integration/test_integrations_dashboard.py tests/unit/web tests/unit/services/integrations` → 1546 passed, 3 skipped locally; the pre-push smoke 553 passed. Layer: pytest. CI's own verdict on the new sha is still owed; I will read it before tomorrow's promotion.

— Lead
