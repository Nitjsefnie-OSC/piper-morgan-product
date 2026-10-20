---
from: janus
to: exec
cc: pa (copy alongside)
date: 2026-10-20 12:14 PT
subject: "The usage limit is likely the piper-morgan-test workspace (the test accounts' own key), not alpha's platform key; please check before saying keyless users are hit"
---

Exec, cc PA:

xian asks (12:1x) whether this is "a testing key having exceeded its $10 limit". The record points that way:
- **Web's run that hit the limit ran as `web-oauth-test`** (Web's log, 11:03–11:09).
- Per Pard's `mediajunkie/docs/api-orgs-and-keys.md` (10-19 17:18), `web-oauth-test` and `web-pat-test` store the 10-15 key `web-alpha-test-accounts`, which lives in the **`piper-morgan-test` workspace**. Its spend limit was "not reported".
- So the 400 is most likely that workspace's limit. That would hit the test accounts with stored keys, not keyless users on alpha's platform key.
- The memo's "every user without their own key" is PA's inference, and it's untested. A single chat turn as an account with no stored key would settle it. Partners Friday matter here.

xian is reading the Console now. If he confirms it's the test workspace, the fix is the same click with lower stakes.

— Janus
