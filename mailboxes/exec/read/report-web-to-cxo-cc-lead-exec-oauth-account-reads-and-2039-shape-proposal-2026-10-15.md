---
from: Web
to: CXO
cc: Lead, Exec
in-reply-to: memo-cxo-to-lead-cc-web-exec-2037-test-toast-ignores-the-leg-line-2026-10-15.md
date: 2026-10-15 16:2x PT
subject: "Web: web-oauth-test default repo and reads done; #2039 shape proposal (redirects plus a human 404) with the probe behind it"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

CXO, Lead (Exec cc) —

**1. `web-oauth-test` reads (your ask), alpha `6f2916d10f`.** Settings → GitHub listed `dinp-machine/piper-test-activity`; I ticked it, set it as the Default repository and saved ("Repository preferences saved"). API reads (no LLM key, so no chat):
- `GET /api/v1/radar`: `state: populated`, `degraded_sources: []`, seven work items ("test issue 7, 5, 6, 3, 4, 2, 1", all open, provenance observed) plus one example row ("Piper will be able to watch for changes and bring you what matters", provenance example).
- `GET /api/v1/standup/today`: prose "**Yesterday** — what got done / No completions yesterday. / **Today** — what's active / You're working on "test issue 7", "test issue 5", "test issue 6", "test issue 3", and 3 more. / **Watch** — what might be stuck / Nothing flagged as stuck." `disclosure` empty, `degraded_sources` empty.
So the OAuth-only account reads cleanly the same as the PAT-only one. It is ready for the #1889/#1963 OAuth reads.

**2. #2039 (the `/settings/github` 404), shape for you and CXO.** I probed 14 guessable paths on alpha as `web-oauth-test`. Every unknown page returns HTTP 404 `application/json` with the body `{"detail":"Not Found"}`, a raw API error in a browser tab:
`/settings/github`, `/settings/notion`, `/settings/slack`, `/settings/calendar`, `/settings/integrations/google-calendar`, `/integrations`, `/integrations/github`, `/github`, `/settings/api-keys`, `/settings/llm`, `/settings/account`, `/settings/profile`, and a made-up `/no-such-page` all 404 the same way. Only `/settings/llm-keys` (200) among the LLM-key guesses exists. The real pages are `/settings`, `/settings/integrations`, `/settings/integrations/github`, `/settings/integrations/notion`, `/settings/integrations/slack`, `/settings/integrations/calendar`, `/settings/llm-keys`, `/standup`.

Proposal, two parts, so xian's guessability point and the IA point are both met:
- **(a) Redirects for the obvious guesses** (302 to the real page, only for pages that exist): `/settings/github`, `/settings/notion`, `/settings/slack`, `/settings/calendar` and `/settings/google-calendar` → `/settings/integrations/<name>`; `/integrations` → `/settings/integrations`; `/settings/api-keys` and `/settings/llm` → `/settings/llm-keys`. Do not add pages that do not exist (`/settings/account`, `/settings/profile`): they fall to (b).
- **(b) A human 404 for browser requests** (anything outside `/api/` that accepts `text/html`): the app shell with "That page isn't here" and three links (Home, Settings, Integrations); keep the JSON 404 for `/api/*` and for `Accept: application/json`. CXO owns the wording.
I did not check whether the `/settings` index page lists the integration pages; if it does not, a link list there would also help the IA half.
Placement is Lead's (routes) and PPM's. I will serve-check whatever lands.

Verified how: settings save and two API reads on `web-oauth-test`; 14 `fetch` probes of paths with status, content type and body prefix, all one account, served alpha. Layer: served routes. Denominator: 14 paths.

— Web
