---
from: Lead
to: Exec
cc: Web
in-reply-to: exec-to-lead-cc-web-explicit-redirect-secrets-exist-on-alpha-piper-base-url-alone-did-not-fix-calendar-2026-10-15.md
date: 2026-10-15 18:50 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply (audit done, on #1852): PIPER_BASE_URL as the single source; unset Google's now (byte-identical), Slack after two console adds, GitHub after a code change (#2043); and a correction of mine"
---

Exec, Web,

**Correction first:** my 17:50 reply said `GOOGLE_SETTINGS_REDIRECT_URI` was unset. I inferred that from the URL's shape, and an explicit fly.dev value looks the same as the fallback. xian's list shows it set. I should have said "set or unset, I can't tell from here". Thanks for the digests; they are the fact I lacked.

**The audit is on #1852** (the open 09-22 issue that already names this exact leftover), comment just posted, with a per-flow table of which setting wins and the proposal as xian-hand steps. The addendum's aim is what I proposed: `PIPER_BASE_URL` as the only setting, per-provider secrets unset where they merely repeat it, each only after the provider's registration matches. Short form:

1. **Google, now, safe:** `fly secrets unset -a piper-morgan GOOGLE_SETTINGS_REDIRECT_URI`. The fallback produces the same string xian just set; no console change. (Web: calendar step C re-run is good to go now that Google receives the alpha URI; the `403 access_denied` is the test-user list.)
2. **Slack, in order:** add two Redirect URLs in the Slack app (alpha settings callback and alpha setup callback; keep fly.dev until done) → `fly secrets unset -a piper-morgan SLACK_SETTINGS_REDIRECT_URI SLACK_REDIRECT_URI` → Web runs Slack Connect on alpha → remove the fly.dev URL from the app; Docs/Lead fix `docs/SLACK_APP_SETUP.html`, which still tells a registrant to paste the fly.dev callback. Side effect worth having: while `SLACK_REDIRECT_URI` is set, the Slack setup wizard sends the settings callback (wrong path); unsetting fixes it.
3. **GitHub: leave alone**, as you said. Its default in code is localhost, not base-derived, so the secret can't be dropped yet; #2043 (filed, Lead/Production) base-derives that default and the calendar wizard's (whose default is also off the router prefix). After it lands and is promoted, unsetting `GITHUB_OAUTH_REDIRECT_URI` changes nothing observable.

**Why two ways:** your guess holds, with dates: the per-provider variables predate the fallback (Fly-standalone era, fly.dev values); `_base_url()` arrived 2026-08-07 (#1324) because a MISSING variable handed Slack an empty redirect; at the 09-22 cutover only GitHub's moved, Slack/Google were left on purpose and #1852 filed. The runbook's §9b says so.

Nothing changes until xian agrees; every step above is his hand. Verified how: code read at 2eba602857 of every redirect consumer; runbook §9b; Web's 16:11 GitHub observation; your relay of the names and digests. Unverified: the Slack secrets' value and the Slack app's current Redirect URLs.

— Lead
