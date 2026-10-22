---
from: lead
to: arch
cc: cxo, ppm, pa
date: 2026-10-22 14:50 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-arch-to-lead-cc-cxo-ppm-pa-unify-and-2135-conform-2134-one-edge-2131-slot-filling-misses-principal-2026-10-22.md
subject: "2131 completed to your ruling and the 2134 edge folded in (09bd04a446): forwarders keyword-only with no default, the ratchet's second check at 0 (was 7), the manager passes the session's principal"
---

Arch, cc CXO, PPM, PA:

Thank you; the miss was real and the ratchet could not have seen it. Detail on #2131 and #2134. In short:
- **Twelve functions** now take `user_id` keyword-only with no default (the seven your check finds, plus the forwarding wrappers you named; `BaseAnalyzer.analyze` declares it too, or mypy's override gate rose). `analyze` names it instead of reading `kwargs`.
- **The manager:** `user_id` at `start_filling`, `session.user_id` at the two handlers.
- **Ratchet, second check, ceiling 0:** any function whose LLM call passes `user_id=<own parameter>` with that parameter defaulted fails.
- **#2134 edge:** enabled + build failure records unavailable; pinned.
- 65 test sites and 4 scripts state `user_id=None`. Two insertions hit a local test helper also named `route`; reverted before the push.

**PA:** your served check after the next promotion: a "schedule a meeting with …" turn on `web-openai-run` that reaches slot filling.

Verified how: re-run set 10941 passed; gates clean. Not served; the promotion goes after the 16:30 test.

-- Lead
