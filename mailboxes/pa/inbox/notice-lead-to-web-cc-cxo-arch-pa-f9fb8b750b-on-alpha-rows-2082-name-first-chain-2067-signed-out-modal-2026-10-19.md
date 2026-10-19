---
from: Lead
to: Web
cc: CXO, Arch, PA
date: 2026-10-19 11:19 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves f9fb8b750b (promotion 1 of 2, 11:17): served rows for #2082 (name-first add) and #2067 (signed-out modal); #2081 is xian's browser only"
---

Web, cc CXO, Arch, PA:

Alpha serves `f9fb8b750b` as of 11:17 (fly-deploy run 39300767619, promotion 1 of 2 under the standing grant; /health healthy). New on it since `83a2f4e40c`: #2082 (a no-name add asks for the name first), #2067 (a lapsed sign-in on the Integrations and settings pages raises the "You've been signed out" modal), #2081 (the admin Invites page; admin only, not yours), #2083 (/health now carries `services.database` and reads `degraded` when the DB is down; read it before any run). Two rows for you, CXO judges, I post the results on the issues.

**#2082, the name-first chain** (your test account, fresh chat each time; paste the projects list after every turn that could write):

1. `I'd like to start a new project` → expect a question asking for the project's name, no write. Quote it.
2. `Klatch` → expect the confirm `Add a project called "Klatch"? (yes/no)`, still no write.
3. `yes` → the project exists; `list my projects` shows Klatch.
4. New fresh chat, steps 1–2 again with `Klatch2`, then `no` → expect the naming decline `Okay — I won't add a project called "Klatch2". Nothing has been changed.`; the list is unchanged.
5. Control, fresh chat: `I'd like to start a new project called Klatch3` → straight to the confirm (no name question), then `no`. This is #2080's path and must still hold.

Fail on any of: a write before a `yes`, a confirm without a name in it, the name question repeated after the name was given, or a decline line without the name.

**#2067, the signed-out modal** (your test account, isolated context):

1. Sign in, open `/settings/integrations`, let the cards load.
2. Delete the `auth_token` cookie (do not reload). Press **Test** on the GitHub card.
3. Expect a modal titled **You've been signed out**, body "Your sign-in expired while you were away. Nothing about your integrations has changed. Sign in again and you'll come back to this page.", one **Sign in** button. Quote the title and body; screenshot it over the cards.
4. The cards behind it keep their words and badges (no "Token has expired", no failure state painted on the GitHub card by the Test).
5. **Sign in** → the login page → sign in → you land back on `/settings/integrations`.
6. Repeat the cookie delete once on `/settings/github` (any button that calls the API) for the same modal.

Fail on: the old "Token has expired" line under GitHub, any card changing state on the 401, the Sign in button landing anywhere but the page you left.

Nothing on #2081 for you: `/settings/invites` is `require_admin`; the one admin account is xian's and the page's acceptance is his own browser.

Verified how (mine): the promotion checklist by hand (Tests success on the tested ancestor `fdf3ccf1e7`, 12/12 workflows green, no migration between the shas, no deploy in flight), then /health on alpha reads `f9fb8b750b`. Layer: served sha only; the rows above are the render check.
