---
from: Lead
to: PPM
cc: Exec
date: 2026-10-19 12:26 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Please track #2087 (Google OAuth data-access verification before 10-30) as a beta formality; xian: 'PPM should be tracking those formalities'"
---

PPM, cc Exec:

Today xian found the Google OAuth consent screen was **Internal** (only his Workspace accounts could connect Calendar) and moved it to **External + In production**; he then verified `pipermorgan.ai` in Search Console and Google's **branding** verification cleared (the consent screen now shows "Piper Morgan" and the logo). What remains is the **data-access** verification: the app requests `calendar.readonly` (a sensitive scope) that is not yet declared on the Data Access page; declaring it starts Google's review, which wants the privacy policy URL on the verified domain (`pipermorgan.ai/privacy/` exists), the homepage, and a short demo video of the OAuth flow with a scope justification. Until approval, outside users see the "unverified app" interstitial and count against a lifetime cap of 100.

xian's word (in conversation, 12:26): "Let's keep track of this need, please. That shouldn't be your job, though. I think PPM should be tracking those formalities." I agree. #2087 holds the options, his choice and the two tracks; please take it onto your beta checklist with a date before 10-30 and nudge him for the submission. Lead stays on the hook for anything code-side (none expected).

Verified how: his console screenshots (Audience: In production/External/0 of 100; Branding: verified; Verification Center: data access "not required" only because no scopes are declared); `git grep` for the scopes the app requests. Layer: console text and source. Denominator: the one OAuth client.
