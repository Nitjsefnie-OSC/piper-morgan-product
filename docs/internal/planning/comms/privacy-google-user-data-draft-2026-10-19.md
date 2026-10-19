# /privacy: Google user-data paragraph and the Calendar "writes" fix (draft for xian's go)

**For:** #2087 (Google OAuth verification). Kit: `docs/internal/planning/google-oauth-verification-kit-2087.md` §5.
**Drafted:** Comms, 2026-10-19, tuning PPM's §5 draft against code and against Google's current policy pages.
**Ships on:** xian's word (public page). Web makes the edit in the website repo, `src/app/(public)/privacy/page.tsx`.

## 1. The edit, ready to paste

**(a) Replace** this sentence under "Your account" → "Services you connect":

> If you connect GitHub, Google Calendar, Slack or Notion, Piper reads and writes there when you ask.

**with:**

> If you connect GitHub, Slack or Notion, Piper reads and writes there when you ask. Google Calendar is read-only (see below).

**(b) Add** a new block right after "Services you connect":

> **Google Calendar.** If you connect Google Calendar, Piper asks Google for read-only access to your calendar and for your Google account's email address. Piper reads your events only when you ask about your schedule or start your standup, and uses them only to answer you. Piper can't create, change or delete events.
>
> To write that answer, Piper sends the details of the events you asked about to the AI provider you connected, using your own key. Piper's answer is kept with your conversations, encrypted.
>
> Piper doesn't sell Google user data, use it for advertising, or use it to build or train AI models. No one at Piper Morgan reads it unless you ask us to, for example for support, or unless it's needed for security or to comply with the law.
>
> The access Google grants is stored encrypted. When you disconnect Google Calendar in Piper, Piper revokes that access at Google and deletes its copy.
>
> Piper Morgan's use and transfer of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

**(c) Update** "Last updated" if the month changes before it ships (it reads "October 2026" today).

## 2. Each claim and what backs it

| Claim | Backed by | State |
|---|---|---|
| Read-only calendar access plus email | `oauth_handler.py` `self.scopes`: `calendar.readonly`, `userinfo.email`; PPM's grep found no Calendar write call | Backed |
| Reads only when asked or at standup | `services/standup/assembler.py` `_append_calendar_events`; chat calendar queries | Backed |
| Event details go to the user's own provider | BYOK path, already disclosed under "Your AI provider" | Backed |
| Answer kept with conversations, encrypted | Conversation storage already disclosed as encrypted | Backed. **Lead to confirm** no other copy of events persists. The standup record's `context` column can hold `calendar_events` (`services/database/models.py` ~3442). I found no writer that puts events there (git grep `calendar_events`), but that's Lead's §2a check |
| Token stored encrypted | `KeychainService` falls back to the encrypted-DB store on hosted (#1382) | Backed |
| Disconnect revokes at Google and deletes the copy | `services/connectors/disconnect.py` `_disconnect_calendar`: `revoke_token`, then `delete_api_key` | Backed. The revoke is best-effort: if Google's revoke call fails, the local copy is still deleted and the grant may stay live at Google until the user removes it in their Google account |
| No sale, no ads | No ads or analytics in the app (already on the page) | Backed |
| Not used to build or train AI models | Piper trains no models. Event text does go to the user's own provider under that provider's API terms | **xian's word.** Google's Workspace policy bars "transferring … user data to create, train, or improve" an AI model. Anthropic's and OpenAI's API terms don't train on API data by default, but that's their promise, not ours |
| No one reads it, with three exceptions | "Our admin tools don't display your conversations" (already on the page) | **xian's word**: he's the person this sentence binds |
| Limited Use sentence | Google's Workspace API User Data and Developer Policy gives an example statement for the privacy policy ("…will adhere to the Google User Data Policy, including the Limited Use requirements"). The API Services User Data Policy page itself prints no required sentence | Wording read 2026-10-19 through a summarizing fetch. The form above is the common one |

## 3. Three gaps beyond the paragraph

1. **The homepage has no link to /privacy.** Google requires the homepage to link to the privacy policy, and the link must match the consent screen's. The footer (`src/components/Footer.tsx`) lists Home, Try Piper, Get Involved, Journey, Methodology, About, Technical Docs, GitHub. There is no Privacy link. /privacy is linked only from the newsletter consent line and /support. **Fix: add "Privacy" to the footer (Web).** It's a link to an existing page, not new copy, but it ships with the same go.
2. **The email scope is used only for a log line.** `oauth_handler.py:265-272` fetches the Google email at connect and writes it to the server log (`calendar_oauth_callback_success`, `email=`). Settings doesn't show it (`settings_integrations.py` returns `email: None`). A reviewer may ask why Piper requests `userinfo.email`. **Lead:** either show it in Settings ("Connected as …"), or drop the scope, or at least drop the email from the log. If the scope stays and isn't shown anywhere, the paragraph's "and for your Google account's email address" should add what it's for.
3. **No Terms URL.** `pipermorgan.ai/terms` is a 404, consistent with xian's 10-16 Option 2 (terms go in the invitation, no site page). Google's branding form lists a Terms of Service link as optional, so leave it blank.

## 4. Verified how

- Live /privacy source: website `origin/main`, `src/app/(public)/privacy/page.tsx` (`c8fbb15`, 10-17), read in full.
- Footer: `git show origin/main:src/components/Footer.tsx`. Homepage HTML fetched (title "Piper Morgan - Think Bigger"), with no `/privacy` href. `git grep "/privacy"` over `src` found only NewsletterSignup and support.
- /terms: curl `-L`, final 404.
- Code: `disconnect.py` `_disconnect_calendar` read; `oauth_handler.py` 52-90 and 262-280 read; `assembler.py` 199-220 read; `git grep calendar_events` over `services/` (one writer path, the standup assembler, which builds display items rather than storing raw events).
- Google: the API Services User Data Policy and the Workspace API User Data and Developer Policy, fetched 2026-10-19 through a summarizing fetch. Quoted fragments come from that fetch, not a full read of the pages.
- Not checked: whether a served standup or chat turn persists events anywhere beyond the conversation (Lead), and the consent screen's own privacy URL (xian's console).
