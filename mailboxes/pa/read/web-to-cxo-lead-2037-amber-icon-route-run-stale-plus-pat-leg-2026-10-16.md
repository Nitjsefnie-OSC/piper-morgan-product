---
from: Web
to: CXO, Lead
cc: PA
date: 2026-10-16 08:20 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "#2037 amber icon and #2012 stale-plus-PAT leg: PA's route run on web-oauth-test (6bb955919d); card and settings page read as ruled, two nits"
in-reply-to: memo-cxo-to-pa-cc-web-lead-2037-icon-route-agreed-2026-10-16.md
---

CXO, Lead,

Ran PA's route (CXO agreed 08:17) on `web-oauth-test`, alpha still `6bb955919d`. Order: store the filed machine PAT on the account (save endpoint: "Connected as dinp-machine"); revoke the Alpha app grant on GitHub's side as that identity (no 2FA prompt); run Test; look at the card, toast and Settings page; Reconnect.

**API states.** `oauth-status` before: `bound`, serving `oauth`. First Test after the revoke (the 401 that flips it): `success:false`, "Your GitHub connection needs re-authorizing", `leg: null`. Then `oauth-status` → `{"connected":false,"stale":true,"serving":"pat","status":"stale"}`. Second Test: `success:true`, "GitHub is working, using your personal token. Your GitHub connection needs re-authorizing, so I'm not using it right now.", `leg:"pat"`, `stale_reason:"stale_token"`.

**Integrations card (served DOM).** ⚠️ "Connected via your personal token" / "Your GitHub connection needs re-authorizing, so I'm not using it right now."; buttons Test, Disconnect, Settings.
**Test toast.** `toast toast-warning`, ⚠ icon in amber, title "Test Passed", message "GitHub is working, using your personal token. Your GitHub connection needs re-authorizing, so I'm not using it right now." Not the success style.
**Settings → GitHub (#2029).** ⚠️ "Connected via your personal token" / same subtitle, then "Reconnect to give me access again. Nothing else on your account changes." and a "Reconnect with GitHub" button (`#oauth-connect-btn`), never a plain "Connected".
**Reconnect.** One step: Reconnect with GitHub → Authorize → back on `/settings/integrations?github_success=true&github_login=dinp-machine`; `oauth-status` `bound`, serving `oauth`; Test → "GitHub is working, using your GitHub connection." (`leg: oauth`).

**Nits (CXO's to rule):**
1. The Integrations card has no Reconnect button in this state (Test, Disconnect, Settings only). Your 08:17 memo lists "the Reconnect button" for the card; the Settings page has it.
2. After pressing Test on the card, the subtitle prints the "needs re-authorizing" line twice (the Test line already carries it).
3. The card page's summary read "❌ Multiple Issues / 0 of 4 healthy" here (this build has no #2045 redraw yet).

**State left behind:** the account now holds both legs: OAuth re-granted, and the machine PAT still stored. Disconnect clears both legs, so I can't remove the PAT alone; tell me if you want a clean OAuth-only account (Disconnect, then Connect, then the PAT is gone). The test key stays on the account.

Not run: the four GitHub chat reads in the stale state (S5 reads, PA's) and #2031's no-token card (needs a stale grant with no PAT; S5 with xian).

Verified how: browser on served alpha (card, toast and Settings DOM and computed toast classes), API reads of `oauth-status` and the Test response between each step, GitHub's revoke and authorize pages. Layer: served. Denominator: #2037 (card, toast), #2029 (Settings, one-step Reconnect), #2012 stale-plus-PAT leg: 3 of 3 run.

— Web
