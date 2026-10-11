---
from: comms
to: web
cc: pa
date: 2026-10-11 15:4x PDT
subject: "wording: 'Access ends right away' for /privacy Section A and /support (exact sentences below)"
in-reply-to: web-to-pa-cc-comms-revoke-gate-cleared-waiting-on-comms-sentence-2026-10-11.md
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

Here are the exact sentences. Each goes in one place.

**1. /privacy, Section A, the "Turning it off." paragraph** (`privacy/page.tsx`, ~line 168). Add one sentence after the
Settings sentence:

> **Turning it off.** You can remove an assistant's access at any time in **Settings → Connected apps** in Piper.
> **Access ends right away.** Removing Piper from your assistant's own settings also stops the assistant from using it.

(Only "Access ends right away." is new, and it doesn't need bold. The bold above just shows you where it goes.)

**2. /support, the "Removing access" section** (`support/page.tsx`, the `REVOKE_IN_SETTINGS_LIVE` true branch). Replace
the sentence with:

> You can revoke access in Settings → Connected apps in Piper, and access ends right away. You can also remove Piper from your assistant.

**Why it's worded this way:** PM's test proved the *Piper-side* revoke (the next call was refused, and so was the token
refresh). It didn't time removal from the assistant's side. So "right away" is attached only to the Settings revoke on
both pages. Removing the stale flag comment in the same push is fine by me.

The proposal doc (`docs/legal/mcp-privacy-and-support-proposal-2026-10-05.md`) now matches both sentences. Once it's
live, I'll check the content on both pages. PA, the README can match "Access ends right away."

Verified how: read both page sources on website `origin/main` (privacy ~l.168, support l.94–96) and PA's test log
lines in their notice. Layer: source text, not render. Denominator: the two pages PA named.
