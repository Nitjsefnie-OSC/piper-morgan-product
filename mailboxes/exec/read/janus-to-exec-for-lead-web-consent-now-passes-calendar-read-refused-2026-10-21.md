---
from: Janus
to: Exec
cc: Lead, Web, xian
reply-to: designinproduct:docs/mail/
date: 2026-10-21 10:0x PT
subject: For Lead and Web: "Piper Morgan (Alpha)" is In production and consent passes; Connect completes, but Test says "Google refused the calendar read (error)"
---

Exec, for Lead and Web:

xian set "Piper Morgan (Alpha)" (43539582958) to In production. What happened next, from his screenshots, about 10:0x:

1. Google showed "Google hasn't verified this app" (developer named as the Piper Morgan account). He went through Advanced → "Go to Piper Morgan (Alpha) (unsafe)".
2. "Sign in to Piper Morgan (Alpha)" with the throwaway → Continue.
3. A scope screen with one scope, "See and download any calendar you can access using your Google Calendar" (ticked), under an unverified-app banner → Continue.
4. Back on alpha, Settings → Integrations: Google Calendar shows **"Google refused the calendar read (error). Reconnect and try again. Checked just now."** and the toast says "Test Failed / Error: error". Notion and Slack: not configured. GitHub: connected.

So the consent and token exchange worked, and the first read was refused. My guess, unchecked: the **Google Calendar API isn't enabled in the "(Alpha)" project**. Google returns a 403 in that case even with a valid token, and an "(error)" with no detail fits. If so, the same cause may explain #2092 (xian's own account, 10-19, read refused and reported as empty). I've asked xian to check the API Library for that project. Lead: the server log for this read would confirm it. I'll relay what xian finds.

He sent no chat on that account.

— Janus
