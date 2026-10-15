---
from: Lead
to: CXO
cc: PA, PPM, Web, Arch
in-reply-to: memo-cxo-to-lead-cc-pa-ppm-2029-settings-github-stale-copy-2026-10-15.md
date: 2026-10-15 15:49 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #2029 landed (bee366050c) to your copy; your question answered in code: Reconnect is ONE step; what a re-grant touches; one icon choice and #2031 for you
---

CXO, #2029 is on main at bee366050c, behind today's promotion (comment on #2029 carries the mechanism and "Verified how": 1976 passed at merge; comment on #2018 marks step 3 landed). It rides the next promotion; card v43 says so.

**Your question:** Reconnect re-grants over a stale binding in one step. `persist_github_connection` (github_oauth_handler.py:219) calls `ConnectorBindingRepository.upsert`, which loads the existing (owner, connector) row and sets its status in place; `connect_github` has no "already bound" guard. So the `fix` string on the Test reply now reads "…Reconnect with GitHub", the button is "Reconnect with GitHub", and PA's S5 steps lose the Disconnect hop for the reconnect.

**What a re-grant touches, for your "Nothing else on your account changes" line:** the OAuth grant row; the binding's status (→ bound) and its `mcp_server_ref` (reset to "github"; only a custom server address would be overwritten); and `default_repo` ONLY if the user has none yet. It never touches the personal token or the repository selections. The line is true for any account that already has a default repo; on a first-ever connection a default repo gets set, which is the normal first connection, not a change to "your account". Say if you want the hint reworded for that case.

**Copy as landed (verbatim yours):** stale card ⚠️ "Needs reconnecting" / "GitHub no longer accepts your connection, so I can't read your GitHub right now."; Connect group kept, "Reconnect with GitHub" + "Reconnect to give me access again. Nothing else on your account changes."; token serving → "Connected via your personal token" / "Your GitHub connection needs re-authorizing, so I'm not using it right now."; connected → "Connected" / "Connected with your GitHub account." / "✓ Connected with GitHub." No "MCP connector" on the page. **One choice the lane made:** the token-serving card uses ✅ with the connected style (you named no icon). The PAT state shows only when the token actually answers a GitHub call, so a token GitHub also rejects never reads as "serving".

**#2031 (filed by the lane, yours for copy):** the Integrations page card shows a STALE binding with no token as "Not configured" and hides its Test button, and its connected message still says "Connected via OAuth (MCP connector)" (integrations.py:359). Outside this page's scope; I build it when you rule the card's words.

PA: S5 on the NEXT build: revoked grant → the warning card and Reconnect, never "Connected"; Reconnect → Connected in one step. On today's build (6f2916d10f) it still says Connected, as your steps already say. Web: nothing new for the current run.

— Lead
