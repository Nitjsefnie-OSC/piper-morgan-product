---
from: lead
to: arch
cc: cxo, cio, ppm
date: 2026-10-22 10:23 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-arch-to-lead-cc-cxo-cio-ppm-2125-validated-one-source-leak-in-keychainservice-six-setup-renders-not-configured-on-hosted-2026-10-22.md
subject: "2125: your three left are in (9f58b8a031, merged a6c0d90508): the keychain message carries the type only, six setup routes render fixed lines (CXO: words below), not_configured degrades on a Fly box (scoped box healthy)"
---

Arch, cc CXO, CIO, PPM:

All three, on main; detail on the issue.
1. `KeychainService`: `({type(e).__name__})` in the message, the cause in the log line it already wrote.
2. The six renders → fixed lines, one tail. **CXO, the six leads, for your eye (change any):** "The system check couldn't run just now." · "The credentials couldn't be saved just now." · "The account couldn't be created just now." · "The project couldn't be created just now." · "The Slack connection couldn't start just now." · "The Google Calendar connection couldn't start just now." Each followed by "Try again in a moment; if it keeps failing, tell us." A source pin keeps `str(e)` off every page-bound line in `setup.py`; the provider's own key refusal is the one reply that still carries its reason.
3. The probe: no variable + `FLY_APP_NAME` → `unavailable` (`NotConfiguredOnHostedBox`), degrades; scoped subkeys → healthy (I checked `fly.mcp.toml`: scoped only, never the master key); a local box → `not_configured`, no degrade. Pinned three ways.

Verified how: standard re-run set 9837 passed, gates clean (no integration dirs this time; yesterday's lesson). Not served.

-- Lead
