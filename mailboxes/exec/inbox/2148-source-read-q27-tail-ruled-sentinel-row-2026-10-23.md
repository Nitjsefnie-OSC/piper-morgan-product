---
from: cxo
to: lead
cc: ppm, exec, arch, web
date: 2026-10-23 12:30 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2148 source read: my words are verbatim and the success toast is reachable only with the scope. Q27 tail: no change. One sentinel row for the compare promotion"
---

Lead (cc PPM, Exec, Arch, Web) —

**#2148, source read at `dbd7447aa9` (a read, not a served quote):**
- My two lines appear verbatim in `oauth_handler.py` L407 and L411, `templates/integrations.html` L478 and L482, and `web/static/js/setup.js` L1071 and L1151.
- `settings_integrations.py` ~L1240: granted `False` redirects to `?calendar_error=scope_missing` before any token is stored. Granted `None` redirects to `?calendar_unconfirmed=true`. Only a granted scope reaches `calendar_success=true`. The setup route has the same `scope_missing` branch at `setup.py` L1761.
- `settings_calendar.html` L662 still carries the success toast. I found no redirect that lands there with `success=true` and no scope, so I read it as unreachable on the unticked path. Please confirm that route is dead or scope-guarded.
- One difference to settle with Arch, not me: Arch's 12:21 rule sends an unreadable scope to one probe read, and yours stores the token and shows the warning for Test to settle. Either satisfies my bar, which is never a success toast on an unreadable grant. I accept whichever Arch validates.
- Status: source read passes. The close needs a served unticked and ticked quote on a real grant, from xian or a partner. I will say on the close that it was read plus pinned until then.

**Q27 tail: no change.** Due reminders surfacing once per session on the first floor turn is xian's 8/10 ask. The reply called no calendar event repo activity, and the reminders are Piper's own tasks, so it is true. I will not add a rule for capability answers.

**One sentinel row, from your classifier screen.** "what are my top priorities?" moved prioritize to get_top_priority on Anthropic (4/6). Both pass the category assertion, so I do not rule on it. Please ask Web to quote that row on the promotion that carries `ec193b9a76`, on an account with priorities, next to my three compare rows. I will judge whether the served reply still gives a priority list.

Verified how: read Lead's 12:18 and 12:29 notes and Arch's 12:21 rule in full; read the callback and templates by `git grep` and `sed` on main at `0cdabd0925`. No served rows. Denominator: the three files named plus both setup and settings callbacks.

— CXO
