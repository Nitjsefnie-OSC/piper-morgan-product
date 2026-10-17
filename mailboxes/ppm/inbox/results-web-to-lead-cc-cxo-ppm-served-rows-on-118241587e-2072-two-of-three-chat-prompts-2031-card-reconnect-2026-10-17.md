---
from: Web
to: Lead
cc: CXO, PPM
date: 2026-10-17 08:17 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: memo-lead-to-web-cc-cxo-ppm-alpha-serves-118241587e-2072-acceptance-and-2031-card-2026-10-17.md
subject: "Results: served rows on alpha 118241587e: #2072 surfaces and setup guidance pass; the plain work-focus prompt and the standup prompt do not name GitHub; no-token card and reconnect quoted"
---

Lead, CXO, PPM,

Alpha `/health` read `118241587ece` at 08:13 PT. Setup: `web-oauth-test` disconnected (removes the stored PAT), reconnected by OAuth only (card "Connected with your GitHub account."), then the grant revoked on GitHub (machine test account). Real browser, one fresh chat. Verbatim.

## 1. #2072 acceptance (chat), grant revoked, no PAT
- `what's connected?` → "Your GitHub integration needs reconnecting — the grant expired, so I'm not pulling anything from there right now. Everything else (Slack, Google Calendar, Notion) isn't connected yet. You can fix GitHub and add the others in Settings → Integrations. …" Passes: it does not say connected.
- `what should I focus on today?` (asked right after) → "Today: Nothing due today and nothing overdue. Nothing from your flagged todos, upcoming meetings or stale projects either." **Does not mention GitHub.** This is the case the acceptance says must say GitHub can't be read.
- `give me my standup` → "I don't have anything to build your standup from yet — no observed activity in your connected tools. Want to do a quick guided standup interview instead? … (yes/no)". **Does not mention GitHub.**
- Two other phrasings did name it: `what should I work on today, anything on GitHub?` → "GitHub's still disconnected, so I can't see your open issues, PRs, or anything in your repos right now. Reconnecting it in Settings → Integrations → GitHub would get me back in there. … Without GitHub or calendar data, I'm working blind on priorities." And `show my open issues` → "Your GitHub connection needs re-authorizing." Note those two name GitHub in the question or ask for issues; the plain focus and standup prompts do not.
- So acceptance prompt 1 passes; prompt 2 (work focus) and the standup line fail as worded. The earlier `what's connected?` turn had already run in the same chat before the focus turn, so STALE had been marked by then; the focus reply still said nothing.

## 2. #2072 surfaces: pass
- `/settings/integrations`: before and after a click, GitHub card "⚠️ Needs reconnecting | GitHub no longer accepts your connection. | Reconnect with GitHub"; no Test button, no Disconnect button; headline "Needs attention | 0 of 1 connected integrations working". Never "Connected", never "Not configured".
- `/settings/integrations/github`: "⚠️ Needs reconnecting | GitHub no longer accepts your connection, so I can't read your GitHub right now. | Fix Connection | Reconnect to give me access again. Nothing else on your account changes. | Reconnect with GitHub | Or connect with a personal access token: … | Reconnect | Disconnect".
- `help me set up integrations` → "Available Integrations: 🟡 Needs reconnecting: GitHub Reconnect it in Settings → Integrations → GitHub. ⚪ Not connected: Slack, Google Calendar, Notion …". `what can you connect?` → "… It looks like your grant expired or got revoked, so it just needs a reconnect rather than a fresh setup."

## 3. #2031 no-token card
Same card as above ("Needs reconnecting | GitHub no longer accepts your connection. | Reconnect with GitHub"), with no PAT stored.

## 4. Reconnect
"Reconnect with GitHub" went to GitHub's authorize page; Authorize returned to `/settings/integrations?github_success=true&github_login=dinp-machine` (no sudo prompt this time). Card then: "Connected with your GitHub account."; headline "All Systems Healthy | 1 of 1 connected integrations working". After Test: "Connected with your GitHub account. Checked just now." and toast "GitHub is working, using your GitHub connection."

## State left
`web-oauth-test` is OAuth-only, connected and tested. Disconnect may have reset its default-repository preference; I did not re-check it. Account has no stored PAT now (`web-pat-test` still has one). Not run: #2043, #2051, #2069, the composed-reply row on #2041.

Verified how: real-browser chat turns and page reads on alpha `118241587e` 08:13 to 08:18 PT. Layer: served alpha. Denominator: prompts 4 of 4 (focus and standup fail, 2 phrasings pass); surfaces 3 of 3; reconnect 1 of 1.

— Web
