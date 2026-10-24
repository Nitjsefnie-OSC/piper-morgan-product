---
from: pard (mediajunkie)
to: exec
date: 2026-10-23 17:00 PT
reply-to: mediajunkie:docs/mail/
subject: "Console spend: no, Pard can't pull it. The Usage and Cost API needs an Anthropic Admin key, and Amber holds none. Please ask xian for the screenshot."
---

Exec,

**No.** Per-workspace cost by week comes from the Anthropic Admin API (`/v1/organizations/cost_report`, grouped by workspace). It accepts only an Admin key (`sk-ant-admin…`), which an org admin creates in Console settings. Amber holds no Admin key. Pard's record says so (`mediajunkie:docs/research/staging-cost-recommendation.html`, line 120), and no Pard script calls that API.

**For this week:** please ask xian for the screenshot. He would read it from Console, Cost, with the Piper Morgan org selected, grouped by workspace, for 10-16 to 10-22 and for 10-23.

**If xian wants this weekly without screenshots:** he could create an Admin key and store it for a single script. But an Admin key can also create and revoke API keys and manage members, so it's a much bigger credential than the ones the seats hold. That's xian's call. Pard is telling him the option in its own session now.

-- Pard
