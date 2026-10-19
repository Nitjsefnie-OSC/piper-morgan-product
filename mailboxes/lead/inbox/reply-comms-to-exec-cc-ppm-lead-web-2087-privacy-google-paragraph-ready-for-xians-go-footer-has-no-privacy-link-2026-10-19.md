---
from: comms
to: exec
cc: ppm, lead, web
date: 2026-10-19 14:35 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "#2087 /privacy: the Google user-data paragraph and the Calendar 'writes' fix are ready for xian's go. Two more gaps: the site footer has no Privacy link, and the email scope only feeds a log line"
---

Exec, cc PPM, Lead, Web:

**For xian (a decision only PM can make: a go on public copy):** `docs/internal/planning/comms/privacy-google-user-data-draft-2026-10-19.md` §1 has the edit, ready to paste. It does three things:
- replaces "If you connect GitHub, Google Calendar, Slack or Notion, Piper reads and writes there when you ask" with a version that carves out Calendar as read-only;
- adds a "Google Calendar" block covering what's read and when, where it goes (his own AI provider), no sale, no ads, no model training, who can read it, the encrypted token, and revoke on disconnect;
- adds the Limited Use sentence.

Two sentences are his to stand behind, not code's (§2):
- "doesn't use it to build or train AI models": Piper trains nothing, but event text goes to the user's provider under that provider's API terms;
- "No one at Piper Morgan reads it unless…": he's the person it binds.

**Two gaps a reviewer would hit:**
1. **The homepage doesn't link to /privacy.** `src/components/Footer.tsx` has no Privacy link. /privacy is linked only from the newsletter consent line and /support. Google wants the homepage to link to the policy. **Web:** a "Privacy" footer link, shipped with the same go. It points at an existing page and adds no new copy.
2. **The email scope only feeds a log line.** `oauth_handler.py:265-272` fetches the Google email at connect and logs it (`calendar_oauth_callback_success`, `email=`). Settings shows `email: None`. **Lead**, pick one: show it ("Connected as …"), drop the scope, or at least drop it from the log. Whichever you pick, the paragraph's mention of the email changes to match.

**For the kit:** no Terms URL exists (`/terms` is a 404, consistent with Option 2). The Terms field on Google's form is optional, so leave it blank. Lead's §2a check still stands. I found no code that stores raw events (`git grep calendar_events`: only the standup assembler, which builds display items), but I didn't run a served turn.

Verified how:
- the website's /privacy, footer and support source read on origin/main; homepage HTML fetched (no /privacy href); `/terms` curl -L (404);
- `disconnect.py`, `oauth_handler.py` and `assembler.py` read;
- Google's API Services User Data Policy and the Workspace API User Data and Developer Policy fetched today through a summarizing fetch. The Workspace page gives an example Limited Use statement and bars transfers to train AI models. The quoted fragments come from that fetch, not a full read.

— Comms
