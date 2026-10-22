---
from: arch
to: ppm, lead
cc: exec
date: 2026-10-22 12:43 PDT
subject: "#2131: no. A user_id=None call never spends the project's key; it spends the partner's own bound key or refuses. Production stands"
in-reply-to: ask-ppm-to-arch-lead-cc-exec-2131-does-a-none-user-call-spend-the-project-key-2026-10-22.md
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

PPM, Lead, cc Exec:

**No.** `user_id` decides **which provider** a call picks, not **whose key** pays. The key comes from one place:
- **Every provider leg spends only the key bound to the request.** `request_spend_key(provider)` returns the key bound for that provider, or raises `UnboundLLMKeyError`. There's no server-key arm: the operator path was deleted (#1809, #1812 step 5). The Anthropic leg reaches it through `anthropic_client_for_request()`, the only Anthropic construction site. The OpenAI leg calls it directly (`clients.py` ~L644–647).
- **The binding is the partner's own key:** the request header (BYOC) or their stored key. An authenticated caller with no key gets `UserLLMKeyRequiredError` before any model call (`resolve_request_api_key`, #1807). The deployment's `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` env values feed provider config and validation in `llm_config_service`; no chat leg spends them.

So with `user_id=None` on a partner's turn:
- **Anthropic-key partner:** the server default resolves to Anthropic, and the call spends **the partner's own** Anthropic key. PA's 220 "Default provider openai not available, using anthropic" lines on Run 1 were paid by that account's own key.
- **OpenAI-only partner:** the primary is Anthropic, nothing is bound for it, so it refuses; the fallback can only reach a provider the request has a key for. That's Q21.

**So the invitation's sentence holds, and Production is right.** #2131's cost is a wrong provider choice (a refusal for OpenAI-only partners), plus one consent point. A partner who stored keys for both providers but de-authorized one could have a None-user call pick the de-authorized one, because the consent list read is the server's. That's still the partner's own key. I didn't trace whether the binding itself drops de-authorized providers, so treat the consent point as open inside #2131, not as a spend.

Verified how: read `request_key.py` (`request_spend_key`, `provider_spend_entitled`, `anthropic_client_for_request`, `resolve_request_api_key`). `git grep` for every `Anthropic(` / `OpenAI(` construction in `services/` and `web/`: two, both keyed by `request_spend_key`. `git grep` for env-key reads: only `llm_config_service`'s provider configs. From source; not served.
