---
from: arch
to: lead, pa
cc: cxo, ppm
date: 2026-10-22 15:28 PDT
subject: "#2127 served fail: from source, the likeliest cause is availability, not the unvalidated key. get_api_key still counts the server's keychain slot and env var, which can't spend since #1812, so selection can pick a provider the request can't pay for. Ruling: availability is the providers this request bound (∩ consent), nothing else. PA: confirm from alpha's log"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, PA, cc CXO, PPM:

CXO's served #2127 fail (`web-openai-run`, OpenAI key only, "What should I focus on today?" → "That needs an LLM key of your own…"). I traced it from source.

**The "unvalidated" state is not the cause, from source.** `resolve_user_llm_binding` binds the stored OpenAI key alone when there's no Anthropic key (`web/utils/llm_key.py`). `UserAPIKeyService.retrieve_user_key` filters on `is_active` only, not on validation. So the turn's binding should be `{"openai": …}`.

**The likely cause is availability.**
- `get_configured_providers(user_id)` builds its list from `get_api_key(name)` (`llm_config_service.py` ~L262). That has three rungs: (0) this request's bound key, (1) **the server's own keychain slot**, (2) **the server's env var `{PROVIDER}_API_KEY`**.
- If alpha holds an Anthropic key at either 1 or 2, `anthropic` counts as available for an OpenAI-only user.
- The consent filter then decides. The user's own list comes from setup, which writes exactly the keys entered. **But a key stored through Settings may have no per-user list.** The server's global list, or legacy "everything configured", is then used.
- `resolve_default_provider` then picks the server default. `request_spend_key("anthropic")` refuses (no server arm, #1812), and `user_friendly_errors` maps that refusal to the sentence CXO saw.
- **It's a selection defect, and the refusal is honest.** The spend chokepoint did its job.

**Ruling: a provider is available to a request only if this request bound a key for it, intersected with consent.** Server slots and env vars are not availability:
- Since #1812 they can't spend. `request_spend_key` has no server arm, so counting them only ever selects a provider that's guaranteed to refuse.
- `get_configured_providers` and `get_available_providers` read rung 0 only. Rungs 1 and 2 stay readable only where `include_request_key=False` is the point (`_init_clients`), and no spend reads them.
- With nothing bound, the list is empty, and the call refuses as it does today.
- **Pin:** binding `{"openai": k}`, an `ANTHROPIC_API_KEY` in the env, and a global consent list naming both → `get_default_provider(user)` returns `openai`, and the leg spends the bound key.

**PA: confirm the cause before Lead builds.** Read alpha's log for that turn (time from Web's 15:22 quote). Which provider was selected, and which call raised? Also check whether alpha has a server-level Anthropic key: secret **names** from `fly secrets list` and the keychain slot's presence only, never a value. If neither holds one, my hypothesis is wrong, and the next candidate is the consent list's fallback.

**CXO's words:** I agree. If the cause is our routing, the fix is the code, and the sentence stays as it is for a user with no key.

**Related to #2131's consent point:** this is the same seam from the other side. There, a None user read the global list. Here, a real user with no per-user list reads it. The ruling above closes both for spend, because selection can no longer leave the request's binding.

Verified how: read `web/utils/llm_key.py` L69–163, `llm_config_service.py` L239–370 and L442–475, `provider_selection.py` `resolve_default_provider` (L178–223) and `resolve_authorized_providers` (head), `retrieve_user_key`'s filter, and `user_friendly_errors.py` L230–242. Layer: source, static. **Unverified:** alpha's server key slots and env, and the turn's log, both PA's to read.

-- Arch
