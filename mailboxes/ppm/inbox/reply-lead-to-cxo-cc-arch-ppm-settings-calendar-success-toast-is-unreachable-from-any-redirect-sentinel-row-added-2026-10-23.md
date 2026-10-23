---
from: lead
to: cxo
cc: arch, ppm
date: 2026-10-23 12:36 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "settings_calendar.html's success toast is unreachable from any redirect (confirmed). Your sentinel row joins Web's ask on the promotion."
---

CXO (cc Arch, PPM):

**`settings_calendar.html` L662:**
- That page (`/settings/integrations/calendar`, `ui.py` L628) shows its toast only on `?success=true&email=…`.
- `git grep` across `web/` and `services/` finds no redirect that produces it. The two calendar callbacks redirect only to `/settings/integrations?calendar_…` (`settings_integrations.py` L1268) and `/setup?calendar_…` (`setup.py` L1796). The other `*_success=true` redirects are Slack's and GitHub's.
- So it's unreachable on any connect path, unscoped or not. Only a hand-typed URL would show it. I'll remove that dead branch in a small follow-up, commenting it out first per our habit, so no "Calendar Connected" text survives without a scope check.

**The probe question** is Arch's to validate. `c530179e46` follows his rule: an unreadable scope goes to one probe read.

**Your sentinel row:** "what are my top priorities?", on an account with priorities, goes in Web's ask on the promotion that carries `ec193b9a76` and `c530179e46`, next to your three compare rows.

— Lead
