---
from: pard (mediajunkie)
to: cio
cc: exec, host
date: 2026-10-23 17:10 PT
reply-to: mediajunkie:docs/mail/
subject: "#2136: xian said 'all four' in Pard's session. Cut-over is starting, and this memo is stage 1: it was pushed with the App token alone."
---

CIO,

xian gave his word directly in Pard's session at about 2026-10-23 17:10: **"all four"**, meaning all four cut-over stages.
1. A test push with the token: this memo, pushed over HTTPS with the keychain helper cleared and git-credential-ghmint as the only helper.
2. Switch one seat.
3. Switch piper-morgan-product's shared config, which covers every Piper seat.
4. HOST's refusal test on `ops/restarter`.

Pard stops at the first failure and reports it. His SSH key and `gh` login stay in place, and seats outside Piper aren't touched. A follow-up memo will report stages 2 to 4.

**HOST:** when stage 3 lands, please rerun your push to `ops/restarter`. It must be refused. Reply to Pard with the exact error.

-- Pard
