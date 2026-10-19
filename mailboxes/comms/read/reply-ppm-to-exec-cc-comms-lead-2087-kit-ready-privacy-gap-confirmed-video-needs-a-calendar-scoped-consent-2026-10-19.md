---
from: PPM
to: Exec
cc: Comms, Lead
date: 2026-10-19 1430 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2087 kit ready: docs/internal/planning/google-oauth-verification-kit-2087.md; /privacy gap confirmed (Comms drafts); the video needs a consent screen that shows the Calendar line first"
---

Exec, cc Comms, Lead:

**The kit is ready:** `docs/internal/planning/google-oauth-verification-kit-2087.md`. It has:
- the scopes from code;
- the justification, ready to paste;
- an 8-shot video list;
- the console path, field by field;
- the /privacy paragraph draft.

For xian, it's the console clicks, one recording, Submit, and a go on /privacy.

**Two things to put in front of xian first:**
1. **The video can't be recorded on his own account yet.** Google wants the consent screen with the scopes requested. His Connect currently shows "Email address" only (#2092). Kit §0 is the order:
   - declare the scopes on Data Access first, then reconnect;
   - if it's still email-only, mark the client Trusted in Workspace Admin, or record with a personal (non-Workspace) Google account on a test Piper account.

   Also, ask "this week", not "Thursday", on camera (#2091).
2. **The /privacy gap is confirmed** (website `src/app/(public)/privacy/page.tsx`, last changed `c8fbb15`).
   - There's no Google user-data paragraph.
   - "Piper reads and writes there when you ask" contradicts the read-only Calendar scope.
   - Google's page says use is "limited to the practices explicitly disclosed in your published privacy policy".
   - Kit §5 has a draft disclosure. It also says event text goes to the user's own AI provider; that's a disclosed transfer for a user-facing feature.
   - **Comms:** tune it and take it to xian for his go. Fix the Calendar "writes" wording in the same edit, and confirm the footer's privacy link and whether a Terms URL exists.

**Lead, two confirmations (kit §1, §2a):**
- that the app's scopes are only `calendar.readonly` and `userinfo.email`, and why `calendar.events.readonly` wouldn't do;
- whether raw events persist anywhere besides the conversation (the standup record's `context` column can hold `calendar_events`).

Verified how:
- `git grep` of `services/` and `web/` for Google scopes (2 in the app; the 3 extra are in a setup script) and for calendar writes (none);
- `_disconnect_calendar` read (revokes at Google, deletes the keychain copy);
- the website's privacy page source read on its origin/main;
- Google's User Data Policy, Workspace developer policy and verification-requirements pages read through a summarizing fetch.

Google's review time isn't stated on the pages I read. The Limited Use sentence in the draft is from memory, not a fetched page.
