---
from: exec
to: ppm, cxo, lead, host, web, pa, cio
date: 2026-10-20 17:42 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Relayed PM ruling (via Janus, ~17:3x): admit #2112 and #2117; partners bring their own keys; partners are worldwide, so the update window needs a new answer; xian supplies the invite and a throwaway Google account"
---
All, xian's answers to rollup v465, from Janus's 17:38 memo. They are recorded in decisions.log at 17:42, and his quotes are as Janus gave them.
**1. Admit #2112, #2117, #2120 as must-closes: yes.** #2120 closed on alpha first, so it drops off. **PPM:** please milestone #2112 and #2117 as must-close. That makes the gate 10 open, 7 must-close. **#2119** (CXO's 16:51 Class 3, the false "0 commits") was not in what he answered. It goes on his next rollup unless d1c64a92e3 closes it first.
**2. Keys:** partners bring their own, "Anthropic or OpenAI if we support the latter yet/still." **PPM**, for the invitation and budget lines: no project key is spent on partner chat. **Lead:** he asks whether OpenAI keys work on alpha today. From the code, an account with only an OpenAI key has been bound since #1823 (9ec028406, 09-21), and the refusal copy names both providers. Please confirm whether anything since then has narrowed that: the wizard's key step, the Settings key field, embeddings. Also say whether a served check is possible without an OpenAI key we can spend. I tell him "works in code, not checked on alpha" unless you correct me.
**3. Partner-day update window:** partners are "all over the world (one in Australia)," so no single hour is quiet. 07:00–08:30 PT is out. 20:00–21:00 PT is 14:00–15:00 in Sydney. He asked me to pick with PPM and CXO. **My proposal:**
(a) Lead builds the name-free "chat turns in the last 30 minutes" count on /health that Lead offered at 12:4x (about half a day). A promotion then waits for a quiet 30 minutes, whatever the hour.
(b) Until (a) is live, promote only 20:00–21:00 PT on partner days, and say so in the invitation ("Piper may restart briefly once a day around …"). CXO, the wording is yours.
(c) Must-closes can still go outside the window on xian's word, as before.
**PPM, CXO:** agree or counter by Wed 10-21 12:00. **CIO** writes the answer into the grant before Fri 10-23 07:00. **Lead:** say whether (a) fits before Friday next to the #1386 fixes. If it doesn't, (b) stands alone.
**4. Test invite (#2117 and the #1386 fresh account):** xian puts a code in "asap," before he heads out. **HOST** gets the masked form the same hour, and **Web** runs the wizard (#2117's "Key accepted.") and builds the seeded account.
**5. Test calendar:** a throwaway Google account is fine. **He creates it**, and **Web** seeds it with made-up events per PA's spec. No real names in event titles or attendees (Rule 8). Until it exists, PPM's 16:18 rule holds.
**6. Test-key rotation:** he will do it after he's back. HOST, no action until then.
**7. Medium crosspost of "The Phantom Feature":** he has already sent the URL to Docs.
His own test rows (A2 calendar, A6, #2100): probably not until tomorrow.
Verified how: I read Janus's 17:38 memo in full; `gh issue view` on 2112, 2117 (OPEN, Production), 2119 (OPEN, Production), 2121; MVP open 8 (`gh issue list`); `gh issue view 1823`, the closing comment,'s closing comment for the OpenAI line. I ran no turns.
-- Exec
