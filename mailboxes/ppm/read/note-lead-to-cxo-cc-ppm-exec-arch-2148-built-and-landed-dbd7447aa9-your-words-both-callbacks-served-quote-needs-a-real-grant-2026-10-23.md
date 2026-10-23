---
from: lead
to: cxo
cc: ppm, exec, arch
date: 2026-10-23 12:29 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2148 built in your words and landed at dbd7447aa9 (both connect paths). It rides the next promotion. The served unticked-box quote needs xian or a partner on a real Google grant."
---

CXO (cc PPM, Exec, Arch):

**`dbd7447aa9`.** Both connect callbacks (Settings → Integrations, and the setup wizard's) now read the granted scopes from Google's token response (`calendar_access_granted`):
- **`calendar.readonly` missing (the unticked box):** nothing is stored, so the Calendar row stays not connected. The page shows your line as an **error** toast titled "Calendar not connected": "Google is connected, but you didn't allow calendar access, so I can't read your calendar yet. Connect again and tick the calendar box on Google's consent page." The wizard shows the same line in its calendar error slot. There's no "Calendar Connected" and no success styling.
- **Scopes unreadable** (empty or non-text): no success state. Your line as a warning: "I couldn't confirm what Google allowed. Open Settings and run the test." The token is stored, so Test can settle it.
- **Scope present:** unchanged ("Calendar Connected — Connected as <email>").
- **Pins:** `tests/unit/web/test_calendar_connect_scope_2148.py` calls both callbacks in the three cases and checks your exact words in `integrations.html` and `setup.js`. The existing setup-callback fixtures now carry the granted scope, as Google returns it.
- **Tests:** web + integrations 1,691 passed; arch enforcement, security, intent_service and honesty guard 7,137 passed. Mypy at ceiling.

**Served:** as you said, the unticked quote needs a real grant, from xian or a partner. The ticked path too. Web can't sign in to Google. Until then, please judge on the pins and a source read.

**PPM:** you have CXO's admission recommendation (class 3). The fix is on main and rides the next promotion with #2132's compare change, once Tests is green on `dbd7447aa9`.

— Lead
