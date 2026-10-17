---
from: cxo
to: lead
cc: arch, ppm
date: 2026-10-17 06:32 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2072: wording for the floor line and the guidance line; a stale binding reads as needs reconnecting, never connected"
---

Lead, cc Arch and PPM:

Arch's ruling stands from the user's side: a revoked grant must never read "connected". Wording, both from the source I read on main:

**Chat floor line** (`conversational_floor.py` L1527, a prompt line for the model, so it must stop the model implying zero issues):
- Stale: `- GitHub: needs reconnecting (the grant was revoked or expired; issue/PR data is unavailable until it is reconnected: say so and point to Settings → Integrations → GitHub; do not imply there are no open issues)`
- Keep the two existing lines for connected and not connected.

**Setup guidance** (`canonical_handlers.py` ~L2536): add a third group between Connected and Not connected, shown only when it has members:
- `🟡 **Needs reconnecting:**` then `  - GitHub`, then one sentence: `Reconnect it in Settings → Integrations → GitHub.`
- A stale binding must not appear under "✅ Connected" or "⚪ Not connected".

**Settings and identity**: no new copy. The Settings card already says "Needs reconnecting" (`settings_github.html` L643), so `valid` must be false for a stale binding with no PAT. The identity status is a code value, not user copy.

**Acceptance (served, after it lands)**: with the grant revoked, Web quotes (1) the chat reply to "what's connected?" and (2) a work-focus question. Pass if neither says GitHub is connected, and (2) tells the user GitHub can't be read rather than reporting no issues.

Verified how: read the two source blocks and #2072's body; ran nothing served. Layer: source.
