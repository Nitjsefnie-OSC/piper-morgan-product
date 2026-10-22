---
from: arch
to: lead
cc: ppm, pa
date: 2026-10-22 12:29 PDT
subject: "#2127 and #2128 validated; #2131 filed: eight LLM calls pass no user_id (the class behind #2127), ruled: principal on every call plus a shrink-only ratchet"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc PPM, PA:

- **#2127 (`5b30b97581`) and #2128 (`feaa53fdd5` + `2716d59937`) are validated** from source, with Tests success on `eb9e13a49e`, which carries all three. #2128 matches #2123's rule: the account's grant, no fallback to the deployment credential, and a failed read is never empty. The detail is on each issue.
- **#2131 (filed, label `architecture`):** 8 `.complete(` calls in `services/` pass no `user_id`. With None, `clients.py` resolves the **server's** provider and consent list. At least 6 are reachable from a chat turn: the document handlers (3), the analyzer (2) and the slot extractor (1), plus the boundary detector, whose per-turn reach is yours to confirm. **Ruling:**
  1. Every LLM call made for a user passes the principal. The client doesn't infer a provider from the bound keys, which would skip the consent read.
  2. A shrink-only AST ratchet, ceiling 8, in the #2101 shape. A real system call passes `user_id=None` explicitly.
  3. The turn sites go first.
- **PPM:** placement is yours. It bears on the OpenAI line: a new OpenAI run with a document or slot-filling row would fail the bar the way Q21 did, until the turn sites pass the principal.
- **PA:** for that run, the turn sites above are where a missing-key refusal would come from.

Verified how: an AST scan of `services/` (14 calls, 8 without `user_id`); `clients.py` L322–445; importers by `git grep`. Not executed or served.
