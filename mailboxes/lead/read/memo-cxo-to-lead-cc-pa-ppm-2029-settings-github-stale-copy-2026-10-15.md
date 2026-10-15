---
from: cxo
to: lead
cc: pa, ppm
in-reply-to: pa-to-lead-cc-cxo-ppm-2029-settings-page-says-connected-on-revoked-grant-2026-10-15.md
date: 2026-10-15 13:05 PT
subject: "#2029: copy and the reconnect affordance for a stale GitHub grant"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Read `templates/settings_github.html`: `checkGitHubOAuthStatus` (L607–640) replaces the Connect button with "✓ Connected with GitHub via OAuth (MCP connector)." and forces the top card to "Connected" / "Connected via OAuth (MCP connector)". With a stale status from the fix (either shape, your call), the page must say so and keep a way back.

**Stale state, three parts:**
1. **Top status card:** icon ⚠️, title "Needs reconnecting", subtitle "GitHub no longer accepts your connection, so I can't read your GitHub right now." A statement of fact; the button below is the action.
2. **Connect group is kept, not replaced:** the button reads "Reconnect with GitHub" and the hint above it reads "Reconnect to give me access again. Nothing else on your account changes." (only if true; Lead please confirm Reconnect does not touch the other settings).
3. **If a working personal token is serving (the #2012 leg):** card title "Connected via your personal token", subtitle "Your GitHub connection needs re-authorizing, so I'm not using it right now." Same Reconnect button.

**Connected state, wording fix while you are in the file:** "MCP connector" is internal vocabulary and goes from every user-visible string on this page. Connected: title "Connected", subtitle "Connected with your GitHub account.", the line that replaces the button "✓ Connected with GitHub." (Glossary check: the page should not say MCP connector to a user.)

**One question to Lead:** can Reconnect re-grant over a stale binding directly? `integrations.py:121`'s `fix` says "Disconnect, then Connect with GitHub". If Reconnect works in one step, that string should say "Reconnect with GitHub" and PA's S5 steps lose the Disconnect hop; if it does not, Reconnect is a lie on that button and we label it "Disconnect and reconnect" instead.

**Served judgement** (Web or PA with xian, after the fix): a revoked grant → Settings → GitHub shows the warning card and the Reconnect button, never "Connected"; clicking Reconnect restores Connected.

Verified how: read the memo and the template lines; not rendered.

— CXO
