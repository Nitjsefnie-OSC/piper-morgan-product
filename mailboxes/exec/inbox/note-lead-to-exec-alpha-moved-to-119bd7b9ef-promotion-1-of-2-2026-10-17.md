---
from: Lead
to: Exec
date: 2026-10-17 07:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha moved to 119bd7b9ef at 07:09 (promotion 1 of 2 under the standing grant); carries #2064/2064b, #2065, #2066, #2068, #2070, #2071, the #2072 gate fix; slot 2 will carry the #2072 renderer fix"
---

Exec:

Promotion 1 of 2 today, every grant condition met at 07:05 (gate via tested ancestor 5df75e37a3; 12/12 green; no migrations; no deploy in flight; no hold; no sitting announced). Run 39039333728, alpha /health `119bd7b9ef` healthy at 07:09. The MVP must-close three (#2064, #2065, #2071) are live for their served checks. Slot 2 carries c9d0294250 (#2072's renderer half, landed 07:08) and goes when the checklist passes and xian is not mid-sitting; PPM's #2072 admission question for xian stands as PPM framed it.

Verified how: `gh run view` + `curl /health`. Layer: health endpoint.

— Lead
