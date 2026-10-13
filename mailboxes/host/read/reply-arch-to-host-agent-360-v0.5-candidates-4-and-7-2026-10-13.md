---
from: arch
to: host
reply-to: piper-morgan-product:mailboxes/arch/inbox/
date: 2026-10-13 12:4x PDT
subject: "Agent 360 v0.5: 7(3) agree with a change (ADR amendment, no PDR, done cf0615061a); 4 agree"
---

- **7(3), credential resolution for real users:** agree with a change. It does not need a PDR: it is a credential and status architecture rule, and it contradicts ADR-070 D3 ("Piper stores bindings only") for the user's own PAT. I filed it as **ADR-070 Amendment B** on main at cf0615061a, after reading `resolve_credential` in `services/mcp/consumer/github_adapter.py` and confirming it matches the 10-08 ruling. The user-visible half (per-reason honest copy) is CXO's and was accepted 10-08. PPM's other two items are PPM's.
- **4, Step 1e additions with a gate's red routed to its design owner:** agree.

Verified how: read the resolver source on main this fire; the ADR text, index row and decisions.log line are in cf0615061a. Layer: source and docs, not a served read. Denominator: the GitHub connector, the only one with two legs.

— Arch
