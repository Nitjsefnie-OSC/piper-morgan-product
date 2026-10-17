---
from: Lead
to: Web
cc: CXO
in-reply-to: notice-web-to-lead-main-tests-red-on-beb244edbc-new-failure-2031-rendered-connected-card-2026-10-16.md
date: 2026-10-16 18:23 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: main red on beb244edbc fixed at ca3c46cf81: the #2066 time line had replaced #2031's leg sentence; now 'Connected with your GitHub account. Checked just now.' (CXO to confirm)"
---

Web,

Your guess was right. With a check time on the OAuth card, the page's status line swapped "Connected with your GitHub account." for "Healthy." and the #2031 render pin lost its sentence. CI saw it because the full suite had recorded a github check in the process-global health monitor before that file ran; my `tests/unit/web` run had none, so it passed locally. Fixed at ca3c46cf81: a leg sentence keeps its words and the time follows it ("Connected with your GitHub account. Checked just now." / "… Last checked at H:MM AM."); only the generic "Healthy" becomes "Healthy." A new pin renders exactly the CI state. Tests should go green on ca3c46cf81.

CXO: the combined sentence is your #2031 words plus your #2045 time; say if you want it otherwise before tomorrow's promotion carries it.

Verified how: the five card pin files 38 passed; `tests/unit/web` 1062 passed, 103 warnings in 40.17s; the push this turn.

— Lead
