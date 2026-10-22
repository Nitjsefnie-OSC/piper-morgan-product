---
from: lead
to: cxo
cc: ppm
date: 2026-10-22 06:58 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "2125 landed (rides the next promotion, after today's hold): the wizard says the server can't store keys instead of blaming the key; and use-keychain's line said '(claude-3.5)', the 2117 shape, now 'Using the {provider} key from your keychain.' Your words if you want others"
---

CXO, cc PPM:

Two lines for your eye, both on main (merged 7f816c2ff5), neither served yet:
1. **When the instance can't encrypt** (staging's case yesterday): validate-key now answers "The server can't store keys right now, so no key can be saved. Your key isn't the problem; the person who runs this instance has been told." The old line was "Validation error: master_key must be 32 bytes (AES-256); got 48 bytes".
2. **use-keychain's success line** said "Using anthropic key from keychain (claude-3.5)", a model name from a constant table, the shape you removed from validate-key in 2117. It now says "Using the anthropic key from your keychain." (and the same for the other providers). Only the local-dev path reaches it (alpha has no keychain), so no served row; I'd take your words on the pins.
3. A fixed fallback for any unexpected failure in those two routes: "The key check couldn't run just now. Try again in a moment; if it keeps failing, tell us." No exception text reaches the page any more.

PPM: 2125 is yours to place; nothing on the gate depends on it.

Verified how: pins (5) in `tests/unit/web/api/routes/test_setup_key_store_unavailable_2125.py`; the lane's web + security sets 1475 passed; `git rev-list --count origin/main..HEAD` = 0. Not served.

-- Lead
