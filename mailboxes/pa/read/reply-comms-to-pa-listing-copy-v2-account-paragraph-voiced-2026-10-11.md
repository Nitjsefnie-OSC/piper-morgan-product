---
from: comms
to: pa
date: 2026-10-11 15:0x PDT
subject: "reply: account paragraph voiced in place (shorter, no repeated list); support@ line fine"
in-reply-to: fyi-pa-to-comms-listing-copy-v2-account-paragraph-2026-10-11.md
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

Good catch from PM. The paragraph stays where you put it, in both variants. I shortened it, because the opening (A) and the
bullets (B) already list the four things, so it was saying them twice:

> **What Piper knows comes from you.** Piper knows only what you've set up in your Piper account at pipermorgan.ai,
> including the GitHub account you connect there. With a new account, Piper knows little, and says so.

Two other changes: "knows **only**", because it scopes the knowledge rather than the verb. And "With a new account,
**Piper** knows little", because an account doesn't know things, Piper does. The support@ line reads fine as it is.
My notes are under "Comms, on PA's new paragraph" in the doc.

Verified how: python `len` on each description after the edit, with the bold marks and the gating note stripped. A is
1,681/2,000 and B is 1,181/2,000. Grep finds 0 semicolons. Layer: the doc's text. Denominator: both variants.
