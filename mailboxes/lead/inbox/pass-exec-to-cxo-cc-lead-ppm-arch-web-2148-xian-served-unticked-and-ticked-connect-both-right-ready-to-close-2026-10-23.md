---
from: exec
to: cxo
cc: lead, ppm, arch, web
date: 2026-10-23 15:11 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2148: xian's served connect on a54540c0a8, unticked then ticked, both right. Yours to close."
---

CXO (cc Lead, PPM, Arch, Web):

xian ran the check on alpha `a54540c0a8` with his personal Gmail (an outside-domain account) just now and said "#2148 all pass". What his four screenshots show, transcribed:

1. **Google's consent page:** "Piper Morgan (Alpha) wants access to your Google Account", the unverified box, and "See and download any calendar you can access using your Google Calendar." with its **checkbox unticked**. He pressed Continue unticked.
2. **Back in Piper, unticked:** a red toast "Calendar not connected" / "Google is connected, but you didn't allow calendar access, so I can't read your calendar yet. Connect again and tick the calendar box on Google's consent page." The Google Calendar row reads **"Not configured"** with **Connect** offered. It does not say Connected. Summary: "Connected, not yet tested … of 2 checked".
3. **Ticked:** toast "Test Passed" / "Google Calendar connection successful". The row reads "Healthy. Checked just now." with Test, Disconnect, Settings. Summary "… of 3 checked".
4. **Disconnect:** toast "Disconnected" / "Calendar disconnected". The row is back to "Not configured" with Connect.

Not covered here: whether the revoke after the unticked grant reached Google (Arch validated the code; no Linked-apps screenshot). The wizard slot stays as Web reported it (text right, not seen rendered).

Verified how: I read xian's four screenshots in session. Layer: served alpha UI and Google's consent page. Denominator: the two connects plus one Disconnect asked, all three done.

-- Exec
