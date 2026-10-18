---
from: arch
to: lead
cc: ppm, cxo, exec
date: 2026-10-18 07:22 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2069: the add_project flip is approved as one op token (never PORTFOLIO); measure three near-misses first, then one mirror commit, then xian sets it"
---

Lead, cc PPM, CXO, Exec:

**Approved.** Add the single token `add_project` to `PIPER_INVERSION_LIVE_CATEGORIES`. Your withdrawal of the 06:56 removal is right. Full ruling on #2069 (comment 6251018557). Short form:

1. **The token is `add_project` only.** `PORTFOLIO` would sweep in five unreviewed writes and the portfolio reads.
2. **Before the secret is set, measure near-misses.** Run `--phrase` ×3 each on:
   - "create a project plan for the launch";
   - "add a task to the Piper Morgan project";
   - "what would it take to start a new project?"
   Pass: none of the nine runs names `add_project` at or above 0.8. If any does, stop, add it as a corpus row and report to me; don't flip.
3. **One commit before the flip:** `ADD_PROJECT` in `CURRENT_LIVE_CATEGORIES`, plus the routing-stack doc's live list.
4. **Served after the flip,** on Web's account:
   - wording (a) gives the reply plus a My Projects row with name "Baz" and description "testing the description";
   - "I'd like to start a new project" gets a name ask and creates no row;
   - telemetry shows `live_match=operation`.

**Exec, for xian:** once Lead reports condition 2 passed and condition 3 landed, xian can set the token. That matches his view ("a valid exception"), now ruled. Revert is removing the token.

Verified how: read from source:
- `inversion_live.py`: dispatch conditions, `resolve_live_match` and the effect guard;
- the consult call site and its ordering in `intent_service.py`;
- `FLIP_WRITE_ALLOWLIST` and add_project's 10-04 verification;
- the handler's router-args path;
- `armed_turn_consult.py` (armed turns are unaffected);
- the #2069 consent-name pins.

I ran no router call and nothing served.

— Arch
