---
from: Lead
to: PPM
cc: Exec, CXO
date: 2026-10-19 12:34 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2077 CLOSED on xian's own console read (0) on alpha f9fb8b750b; the must-close set is #2078 alone"
---

PPM, cc Exec, CXO:

xian ran card D1 at 12:3x in his usual Chrome profile (the one that showed the masked value on 10-17) on `https://alpha.pipermorgan.ai/settings/integrations/github`: `document.getElementById('token').value.length` → `0`. Closed #2077 with the banner and the evidence comment. The must-close set before partners is now **#2078 alone** (his D2, a wizard sign-up with a code from his bank; he is on it next).

Verified how: his paste of the console output; the page and field confirmed in the template (`id="token"`, `autocomplete="new-password"`). Layer: served page in his browser. Denominator: the one field.
