# Google OAuth verification kit (#2087)

**Assembled:** 2026-10-19 by PPM, on Exec's handoff (14:23). xian's part is only: the console clicks, one recording and its upload, Submit, and the go on the /privacy paragraph (§5).
**Row:** `beta-formalities-checklist.md`, "Google OAuth data-access verification". It must happen before the first partner's access (10-30, xian's target). Google's review time is not stated on the pages I read; Lead's "days to a few weeks" is unverified.
**Sources read for this kit (10-19, 14:3x):**
- Google's API Services User Data Policy;
- the Google Workspace API User Data and Developer Policy;
- Google Cloud Help "verification requirements" (13464321).

They were read through a summarizing fetch, so recheck any quoted line on the page before relying on it.

## 0. Before recording: the consent screen must show the Calendar line

Google requires the video to "show the complete OAuth consent screen, with the same scopes you are requesting". Today xian's own Connect shows **only "Email address"** (#2092). Lead's two candidates:
- the Workspace API controls, where the client isn't Trusted;
- the scopes not being declared on Data Access.

**Do step 1 of §4 (declare the scopes) first**, then Disconnect → Connect once.
- If the consent screen still shows email only on xian's Workspace account, either mark the client Trusted in Workspace Admin (Security → Access and data control → API controls → App access control), or record with a **personal Google account** (not on the Workspace domain) signed into a test Piper account.
- A personal account will also show Google's "unverified app" screen first. That's expected; click through it on camera.
- **10-21:** that click-through happens only while the app is **In production**. In Testing, Google refuses any account not on the test-user list ("The app is currently being tested…", seen on the throwaway account on 10-21). Check Audience before recording.

## 1. Scopes (from code)

| Scope | Sensitivity | Where requested |
|---|---|---|
| `https://www.googleapis.com/auth/calendar.readonly` | sensitive | `services/integrations/calendar/oauth_handler.py` (`self.scopes`), `services/integrations/calendar/config_service.py:30,175` |
| `https://www.googleapis.com/auth/userinfo.email` | non-sensitive | `oauth_handler.py` (`self.scopes`) |

- Nothing in `services/` or `web/` requests a Calendar write scope, and nothing calls an events insert, update or delete (PPM's `git grep`, 14:3x).
- `scripts/setup_google_calendar_oauth.py` lists three more read-only scopes (`calendar.events.readonly`, `calendar.calendarlist.readonly`, `calendar.calendars.readonly`). It's a developer setup script, not the app's request; don't declare those.
- **Lead to confirm** the full list (Exec's ask). If narrower would do, a reviewer will ask why not `calendar.events.readonly`. The reason must come from code: does any path read calendar lists or settings, not just events?

## 2. Scope justification (paste into the form; Lead checks "stores")

> **calendar.readonly.** Piper Morgan is a product-management assistant. When the user asks about their schedule ("what's on my calendar today?", "do I have meetings this week?") or starts their daily standup, Piper reads that user's own calendar events for the period asked and answers in the chat. Piper only reads; it never creates, changes or deletes events, so it requests the read-only scope. Without it, Piper can't answer schedule questions or include meetings in the standup, which are the features the user turns on by connecting Google Calendar.
>
> **How the data is used.** Event details are used only to answer the user who connected the calendar. They go to the AI provider that user connected with their own key (Anthropic or OpenAI) to write that answer. Piper doesn't sell them, use them for advertising, or use them to train any AI model. The answer becomes part of the user's conversation history, which the user can see. The Google access token is stored encrypted. Disconnecting revokes it at Google and deletes Piper's copy (`services/connectors/disconnect.py`, `_disconnect_calendar`).

Checks before pasting:
- **(a) Lead:** does any path persist raw events outside the conversation? The standup record's `context` column can hold `calendar_events` (`services/database/models.py`, around 3442).
- **(b) xian:** sending event text to the user's own AI provider is a transfer "to provide … user-facing features … with the user's consent" under Limited Use. The policy page must say so (§5).

## 3. Demo video shot list (one take, about 2 minutes)

Record with the macOS screen recorder (Cmd-Shift-5) or QuickTime. Keep the **address bar visible** throughout, with the browser and the consent screen in **English**.

1. Open `https://pipermorgan.ai` and scroll to show what the app does and the **Privacy** link in the footer. Click it to show the privacy page (the reviewer matches this URL to the consent screen's).
2. Go to `https://alpha.pipermorgan.ai` and sign in to the test account.
3. Open Settings → Integrations, find Google Calendar (not connected), and press **Connect**.
4. Google's account chooser: pick the account. If the "unverified app" screen appears, show it and continue.
5. **The consent screen: hold it about 5 seconds.** It must show the app name ("Piper Morgan (Alpha)" in the Alpha project), the logo, and the line for **"See and download any calendar you can access using your Google Calendar"** (Google's wording for `calendar.readonly` as PPM recalls it; whatever calendar line appears is what matters). Press Continue or Allow.
6. Back in Piper: the Calendar card reads Connected. Press **Test** and show the result.
7. Open chat and ask "what's on my calendar today?". Show the reply naming the test events (10-23 update: "today", not "this week").
8. Optional, about 10 seconds: Settings → Integrations → Calendar → **Disconnect**, to show the user can revoke.

Upload to YouTube as **Unlisted** (Exec's instruction; the page I read doesn't name a host). Paste the link into the form.

**Blocked until #2091/#2092 are fixed?** Step 7 needs a real answer. Today, on xian's account, chat says "no events" (#2092's 403). With a correctly scoped grant the read should work, but a weekday question ("Thursday") still answers for today (#2091). Ask "this week" or "today", not a weekday.

## 4. Console path (xian's clicks)

1. **Google Auth Platform → Data Access → Add or remove scopes.** Tick `.../auth/calendar.readonly` and `.../auth/userinfo.email` (search "calendar.readonly" if it isn't listed), then **Update**, then **Save**. The sensitive scope appears under "Your sensitive scopes"; paste §2's justification in the box beside it if one is offered.
2. **Branding** (already verified; confirm these match):
   - App name: `Piper Morgan`
   - Homepage: `https://pipermorgan.ai`
   - Privacy policy: `https://pipermorgan.ai/privacy/`
   - Terms (if asked): **leave blank**. There's no Terms page (`/terms` is a 404, per Comms 14:35, consistent with xian's Option 2), and the field is optional.
   - Authorized domains: `pipermorgan.ai`
3. **Verification Center → Prepare for verification / Submit.** The form asks for:
   - the scope justification (§2);
   - the demo video link (§3);
   - a contact email: xian's choice, never pasted into this repo.

   Confirm the app is External + In production (already done).
4. Submit. Google mails the developer contact; answer its questions promptly, and paste any requested changes back to PPM so the row stays current.

## 5. Gap: /privacy has no Google user-data disclosure (for Comms to draft, xian to ship)

Google requires that the privacy policy "disclose how your app accesses, uses, stores, and/or shares Google user data". Use must be "limited to the practices explicitly disclosed in your published privacy policy".

Today `pipermorgan.ai/privacy/` (website repo `src/app/(public)/privacy/page.tsx`, last changed `c8fbb15` 10-17) says, under "Services you connect": "If you connect GitHub, Google Calendar, Slack or Notion, Piper reads and writes there when you ask." That is wrong for Calendar, whose scope is read-only. It has no Google user-data or Limited Use paragraph. The Analytics paragraphs are about the website, not the app.

**Draft paragraph for Comms to tune (xian's go ships it):**

> **Google user data.** If you connect Google Calendar, Piper reads your calendar events (read-only) to answer your questions about your schedule and to build your standup. Piper never creates, changes or deletes events. Event details are sent to the AI provider you connected, with your own key, to write Piper's answer to you, and the answer is kept in your conversation history. Piper doesn't sell Google user data, doesn't use it for advertising, doesn't let people read it except with your permission or for security or legal reasons, and doesn't use it to train AI models. The access Google grants is stored encrypted. When you disconnect Calendar, Piper revokes that access at Google and deletes its copy. Piper Morgan's use and transfer of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

Notes:
- The last sentence is the disclosure wording Google's reviewers commonly ask for. It's from Exec's and my knowledge; the policy page I fetched didn't print a required sentence.
- Fix "reads and writes" for Calendar in the same edit. "Reads, and writes when you ask" stays true for GitHub, Slack and Notion only if those write. Comms checks with Lead.
- The homepage must link to the privacy policy, and that link must match the consent screen's. Comms confirms that the site footer has it.

## Updates

- **Comms, 14:35:**
  - The draft paragraph is at `docs/internal/planning/comms/privacy-google-user-data-draft-2026-10-19.md`, waiting on xian's go. **Submit only after it's live.**
  - The site footer has no Privacy link, so Web adds one with the same go.
  - The email scope only feeds a log line (`oauth_handler.py` 265–272). Lead picks: show it, drop the scope, or drop it from the log. If the scope is dropped, §1 and §4 lose `userinfo.email`.
  - No code stores raw events: `git grep calendar_events` finds only the standup assembler, which builds display items. That's Comms' source read; Lead's §2a check stands.

- **Lead, 14:49 (§1 and §2a confirmed, source read):**
  - The app's scopes are exactly `calendar.readonly` and `userinfo.email`, with nothing that writes.
  - **Why not `calendar.events.readonly`** (paste this if the reviewer asks): the adapter also reads `calendarList`, for which calendar is primary and its time zone. `calendar.readonly` covers that; `events.readonly` doesn't. Both are sensitive in Google's table.
  - **No writer of raw events at rest:** the standup assembler builds display items in memory, and nothing assigns `context["calendar_events"]`. Event text reaches the user's own AI provider inside the turn, and the conversation keeps the rendered reply. So §2's "stores" sentences stand.
  - **The email scope stays** (to label the connection later). Lane 2092 stops logging the address (`has_email=True/False`). The privacy line: the address is "read to confirm which account connected" until Settings shows it.

- **15:43 (Exec's curl):** the /privacy Google paragraph is live. The homepage seemed to have no Privacy link. **Resolved 15:50 (Web, rendered browser): the footer shows Privacy → /privacy/.** The site renders client-side, so the link isn't in the raw HTML. **§5 is done; submit when ready** (§0 first). If Google's reviewer reports the homepage link missing, the cause is the client-side render, and Web has a sitewide fix ready (about 1 h).

- **10-23 (Exec, after xian's outside-account connect at 11:4x).** The step-by-step reading copy for recording is the artifact built from this kit (`google-oauth-verification-kit-2087.html`). What changed:
  - **Project:** submit in **"Piper Morgan (Alpha)"** (project number 43539582958), where alpha's Calendar client lives (Lead's 10-22 map). The kit was written before we knew there were two projects. The branding there reads "Piper Morgan (Alpha)", so leave it as is.
  - **§0 is answered.** A personal Gmail that had never touched alpha saw the full-page "Google hasn't verified this app", then a consent page with a yellow unverified box and the one calendar line ("See and download any calendar you can access…") as a **checkbox that starts unticked**. Tick it on camera. Settings → Test then passed.
  - **The 10-22 "verified" was branding only.** This submission (data access, sensitive scope) is what removes the warnings.
  - **Step 7: ask "what's on my calendar today?"** That shows only the account's own test events. "This week" would put real meetings with other people's names into a video Google's reviewers watch. #2091 and #2092 are closed, but "today" is still the safest ask.
  - **Server render is live** (website `a3cb49f`, 10-19), so the footer's Privacy link is in the raw HTML too.
  - **Before recording:** disconnect in Piper. Piper's Disconnect also revoked the grant at Google (xian's Linked apps reads empty). Hide the bookmarks bar and turn on Do Not Disturb.

## Whose part is whose

| Step | Owner |
|---|---|
| Confirm the scope list and the "stores" sentence (§1, §2 check a) | Lead |
| /privacy paragraph and the "reads and writes" fix (§5); Terms URL; footer link | Comms drafts, xian's go |
| Data Access clicks, recording, upload, Submit (§0, §3, §4) | xian |
| Keep the checklist row current; nudge through Exec | PPM |
