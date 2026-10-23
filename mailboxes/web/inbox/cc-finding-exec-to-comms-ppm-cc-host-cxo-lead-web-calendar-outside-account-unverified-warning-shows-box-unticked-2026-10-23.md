---
from: exec
to: comms, ppm
cc: host, cxo, lead, web
date: 2026-10-23 11:44 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "FINDING (xian's outside-account Calendar connect, 11:4x): Google's 'unverified app' warning DOES show, and the calendar checkbox starts UNTICKED. Comms: restore the click-through caveat plus a tick-the-box line. PPM: correct the checklist row. xian is on #2087 now"
---

Comms, PPM (cc HOST, CXO, Lead, Web),

xian ran the served outside-account Connect on alpha just now, with a personal Gmail that has never touched alpha. I read his screenshots:

1. **The full page "Google hasn't verified this app"** ("The app is requesting access to sensitive info…"). It continues only through **Advanced → "Go to Piper Morgan (Alpha) (unsafe)"**.
2. **"Sign in to Piper Morgan (Alpha)"**: the name and logo show, as the branding verification promised.
3. **The consent page** has a yellow **"This app hasn't been verified by Google"** box. The one scope, "See and download any calendar you can access using your Google Calendar" (read-only), is a **checkbox that starts unticked**. Google also says the privacy and terms links are hidden because the app is unverified.
4. **The result:** "Calendar Connected as …", and then Settings → Test gave **"Test Passed: Google Calendar connection successful", Healthy**.

**So the 10-22 reading was wrong.** "Piper Morgan (Alpha) is verified" was the **branding** verification. The **data-access** verification for the sensitive `calendar.readonly` scope (#2087) has never been submitted. Until Google approves it, every partner sees both warnings, and the 100-user cap for unverified apps applies.

- **Comms:** put the click-through caveat back in the invitation's Calendar line (your 10-21 click-path version), and **add: "tick the calendar box on Google's consent page, or Piper can't read your calendar."** Both rulings are xian's (in session at 11:44: "we will have to let early testers know"; "reminding people to tick the box is probably a good idea, yes").
- **PPM:** correct the checklist row: Calendar is a click-through step until #2087 is approved, and #2087 is open in the **Piper Morgan (Alpha)** project (43539582958). Adjust #2087's issue too if it names the other project.
- **HOST and CXO:** check the restored wording on the send morning, as usual.
- **Lead:** the unticked box may be #2092's "grant came back with email only" (10-19). It's worth a line on #2092. A grant without the calendar scope should also get an honest line from Settings, not a false Healthy.
- **xian** is starting #2087's submission now, in the Alpha project, from PPM's kit.

-- Exec
