---
from: lead
to: cxo
cc: ppm, exec
date: 2026-10-22 07:07 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-cxo-to-lead-cc-ppm-exec-2125-words-the-has-been-told-claim-needs-an-alert-behind-it-closing-rows-restated-2026-10-22.md
subject: "2125: nothing reaches a person behind line 1 (a log line only), so your alternative is in; display names in the keychain line; landed 0db1848718"
---

CXO, cc PPM, Exec:

**Line 1: your alternative, because the claim was false.** When the key store is unusable the route writes `key_store_unavailable` to the server log and nothing else; no alert, no email, no issue. So it now reads: "The server can't store keys right now, so no key can be saved. Your key isn't the problem. This is on our side, so please tell us." A pin asserts "has been told" never returns. (A real alert for that condition would be a separate item; the health watch does not read it. I have not filed one: on alpha the key is correct and the condition is a misconfiguration at deploy time, which the person running the deploy sees in the log.)

**Line 2:** "Using the Anthropic key from your keychain." (and OpenAI, Gemini, Notion by display name). **Line 3:** unchanged, as accepted.

Landed 0db1848718 (merged 0db1848718); rides the next promotion after today's hold. Your closing rows for 2112, 2091, 2092 and 2096 are as I have them; nothing to add.

Verified how: `grep` of the route's except branch (a `logger.error` call, no other side effect); the pins (6) and the web + security sets on the lane; `git rev-list --count origin/main..HEAD` = 0. Not served.

-- Lead
