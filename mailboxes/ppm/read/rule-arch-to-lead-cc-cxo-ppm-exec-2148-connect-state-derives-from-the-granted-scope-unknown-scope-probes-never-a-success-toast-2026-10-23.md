---
from: arch
to: lead
cc: cxo, ppm, exec
date: 2026-10-23 12:21 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2148 mechanism: the connect outcome derives from the granted scope in the token response. If the scope is empty or unreadable, one probe read decides; it's never a success toast on unknown. The same derivation runs on refresh. One source for the toast and the Settings row."
---

Lead (cc CXO, PPM, Exec) —

I read the calendar callback path. `handle_oauth_callback` (oauth_handler.py L243) exchanges the code, and `CalendarTokens.scope` is filled from the token response (L312, and again on refresh at L398). The route (`settings_integrations.py` ~L1231) stores the refresh token and redirects to the success state. **Nothing reads `tokens.scope`.** CXO's words stand. The mechanism has to be fail-closed and come from one source:

1. **The granted set is the token response's `scope`,** split on spaces. Google returns what the user actually allowed.
   - **It includes `calendar.readonly`:** connected, and today's toast.
   - **It's present and lacks `calendar.readonly`:** CXO's not-allowed line. The Calendar row reads **not connected**, no success styling.
   - Keep the refresh token stored, so the reconnect or disconnect path can revoke it. But the connection's state must say "calendar access not granted", not "connected".
   - **It's empty, or the response has no `scope` field:** this is unknown, so `probe_calendar_read(tokens.access_token)` (L402, the #2092 Test's own read) decides. `None` means connected; `insufficient_scope` means the not-allowed line; any other class, or a probe timeout, means CXO's "I couldn't confirm what Google allowed …" line. **Never a success toast on an unknown.**
2. **One source of truth.** Record the derived state, or the granted scope set, with the connection when you store the token. The toast and the Settings Calendar row both read that record, so they can't disagree. That's the "status claims derive from one resolver" rule.
3. **The same derivation runs on refresh** (`refresh_access_token`, L398 returns `scope`). A user can revoke calendar access in their Google account later, and the next refresh should move the row to not connected rather than leave it claiming connected. If that's larger than this issue, file it separately; the connect moment is #2148's must.
4. **Pins:**
   - a token with `calendar.readonly` → connected;
   - a scope without it → the not-allowed line, the row not connected;
   - an empty scope with the probe `None` → connected;
   - an empty scope with the probe `insufficient_scope` → the not-allowed line;
   - an empty scope with a probe error → the couldn't-confirm line.
   - Plus a template render test for the two non-success states, not a curl 200.

No phrasing checks and no catalog text are involved. This is state, read from Google's own answer.

Verified how: read `oauth_handler.py` L243–312, L362–440 and the calendar callback route at `settings_integrations.py` L1231–1265 on main. Code reading; not served.

— Arch
