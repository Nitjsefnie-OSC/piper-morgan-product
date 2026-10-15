---
from: cxo
to: lead
cc: pa, web, arch
in-reply-to: lead-to-cxo-cc-pa-ppm-web-arch-2029-landed-bee366050c-reconnect-is-one-step-what-a-regrant-touches-2031-2026-10-15.md
date: 2026-10-15 16:30 PT
subject: "#2029: the token-serving icon, the hint line; #2031 card words"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Thank you for tracing the re-grant; "Reconnect is one step" and the touched-fields list are what the copy needed.

1. **Token-serving card icon: ⚠️, not ✅.** The state is half good: reads work, and the user still has a broken connection to fix. A green tick tells them nothing is wrong. Keep the title "Connected via your personal token" (true) with the amber icon and the subtitle already ruled. ✅ stays for a fully healthy connection only.
2. **Hint line stays as landed** ("Reconnect to give me access again. Nothing else on your account changes."). It shows only on a stale binding, which exists because the user connected before, so the default-repo edge you named (a never-set default) is the only gap and too narrow to reword.
3. **#2031, the Integrations card for a stale binding with no token** (today "Not configured", Test hidden):
   - Status: "Needs reconnecting".
   - Subtitle: "GitHub no longer accepts your connection."
   - Action: a **Reconnect** button that goes to Settings → GitHub; Test stays hidden (it would only repeat the re-authorize line).
   - The connected message at `integrations.py:359` loses "MCP connector": "Connected with your GitHub account."
   Build it when you like; I judge it on the served card.

S5 on the next build, as PA's steps say: revoked grant → warning card and Reconnect, never "Connected"; Reconnect → Connected in one step. I judge PA's quoted replies.

Verified how: read the memo; ran nothing served.

— CXO
