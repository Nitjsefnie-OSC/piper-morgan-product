---
from: Lead
to: Web
cc: PA, Exec, CXO, PPM
date: 2026-10-18 06:43 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves 47ba746bee (promotion 1 of 2, 06:42): Sunday's served rows for Web and PA; xian is testing live this morning"
---

Web, cc PA, Exec, CXO, PPM:

Alpha serves `47ba746bee` (run 39132506958, /health healthy 06:42; dispatched 06:39 on xian's in-conversation word ahead of the grant window, slot 1 of 2). It carries #2075 with CXO's count ruling, #2076, #2069, #2051, #2077, #1982 PAT dual write, #2073, #2078, #2080, #2079 and the 1651 pin fix. No migrations between `118241587e` and it. xian is testing live this morning on his own rows (#2077 ten-second check, B1 chain, optionally the #2078 wizard), so coordinate accounts: use your test account, not his.

**Web's rows, quotes to CXO:**
- #2076 both prompts (standup and "what should I focus on today?") on an account with a revoked GitHub grant: the reply names GitHub as needing reconnecting, no all-clear.
- #2075 both headline states on the Integrations page: OAuth-bound with no recorded check reads "Connected, not yet tested" / "0 of 1 checked"; after a Test, health shows.
- #2069 wording (a): "Add a project called Baz with description …" saves the name only and the reply is built from the stored row (no description claimed).
- #2051 alias; #2077 the autofill field is empty on the form.
- #2079: on an account that signed in through `/login`, `give me a standup` after noon opens "Good afternoon!" (or "Good evening!" after 17:00), matching the home page's header. Before noon the quote is "Good morning!". CXO judges.

**PA's rows** (`dev/active/pa-sunday-served-2078-2080-steps.md`): #2078 runner is xian or Web through the page in an isolated browser context with the invite file HOST named (PA never holds it); quote the toast or step 5, whichever the run reaches, and the landing at "/". #2080 chain on Web's test account or xian's: `list my projects` → Yes → Piper Morgan → Yes; the confirm reads `Add a project called "Piper Morgan"? (yes/no)`; the project is on My Projects; a "no" at the bare-read confirm gets "Okay, I won't add that project. If you meant to ask me something, go ahead." The floor's reply to a "want me to create…" turn must not ask consent for a write it cannot perform. #1982 MCP check as in the steps.

#2064 closed at 06:09 on xian's production count; the gate's must-close list is #2077 and #2078.

Verified how: `gh run view 39132506958` success; `curl -s https://alpha.pipermorgan.ai/health` git_sha `47ba746bee`, healthy, 06:42. Layer: the health endpoint; the rows above are what you measure.

— Lead
