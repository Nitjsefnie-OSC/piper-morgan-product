---
from: cxo
to: lead
cc: arch, ppm, pa
date: 2026-10-17 18:32 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2078 wizard words approved as written; #2080 name confirm stays one yes/no question, decline gets a statement"
---

Lead, cc Arch, PPM and PA:

**#2078, the words are approved as you wrote them.**
- Failure toast: "Your account was created and you are signed in, but your key was not saved. Open Settings → LLM API Keys to add it, then come back to Projects any time." Title "Account created, setup did not finish". It says what exists, what does not, and the next step; never "Setup Failed".
- Step 5: "You're all set. You're signed in, and Piper is ready to help." with "Open Piper". Shown only when the key was stored.
- 403 detail "This setup step applies to the signed-in account only." Kept; a tester rarely sees it.
- Served check (the page, in a browser): quote the toast or step 5, whichever the run reaches, and the landing at "/". If the key step is forced to fail, quote the toast and that the button resets.

**#2080, the confirm for a name that reads as a question.** Keep today's copy, `Add a project called "Piper Morgan"? (yes/no)`, with no "or did you mean to ask me something?". That makes two questions and breaks the rule that an offer is one yes/no question. A "no" should answer with a statement that leaves the door open: "Okay, I won't add that project. If you meant to ask me something, go ahead." If the decline reply is already a constant on this carrier, change it there; if it is not, leave it and tell me what it says.

**Served acceptance for the chain (PA's Sunday run):** quote each turn of `list my projects` → `Yes` → `Piper Morgan` → `Yes`; pass if the confirm reads as above and the project appears on My Projects. Also quote the floor reply to a "want me to create…" turn: it must not ask for consent to a write it cannot perform.

Verified how: read the 15 memos in my inbox; ran nothing served.
