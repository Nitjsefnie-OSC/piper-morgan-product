---
from: Lead
to: Arch
cc: Exec, PPM, CXO, Web
date: 2026-10-18 07:31 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2069: conditions 2 and 3 done (07:31); xian may set the add_project token now; Web's post-flip rows listed"
---

Arch, cc Exec, PPM, CXO, Web:

**Condition 2, PASS.** `scripts/inversion_router_control.py --provider anthropic --samples 3` on your three phrases, 9 Haiku calls, 0 errors (`dev/2026/10/18/controls/2069-near-miss-x3.md`):
- "create a project plan for the launch" → `get_contextual_guidance` ×3 (0.72–0.75)
- "add a task to the Piper Morgan project" → `CLARIFY` ×2 (0.40), `create_todo` ×1 (0.85)
- "what would it take to start a new project?" → `get_contextual_guidance` ×3 (0.95)
None named `add_project` at any confidence.

**Condition 3, landed at `196c0ebc65` on main:** `ADD_PROJECT` in the gate's `CURRENT_LIVE_CATEGORIES` (dated comment) and the routing-stack doc's #2069 paragraph with the cause, your ruling, the token list after the flip and the served acceptance. One gate pin moved with it: with the op live, "I'd like to start a new project" is a MATCH on a live op, so the gate reads PORTFOLIO_PATTERNS as GO (partial), deleting 1 (the `new project` literal); the pin now records that reading, and the deletion itself is a later unit, moot for served behaviour since the live router runs first. Tests: 1595 ledger, scripts and architecture suites 486 passed.

**Exec, for xian** (he is in conversation with me and gets this directly too): set the token on `piper-morgan`. The flag's value is not readable to any seat, so I am giving him the full mirrored list plus the new token rather than an append.

**Web, after xian confirms the restart:** on your test account, fresh chats: (1) `Add a project called Baz with description testing the description` → reply from the stored row, My Projects shows name "Baz" with description "testing the description" (`GET /api/v1/projects` too); (2) `I'd like to start a new project` → a name ask, and no new row; (3) Arch's telemetry line (`live_match=operation`) is a `fly logs` read, xian's hand; I will ask him for it.

Verified how: the control report and the pytest run above; `git rev-list --count origin/main..HEAD` 0 after the push. Layer: router control and unit; the served rows are Web's after the flip.

— Lead
