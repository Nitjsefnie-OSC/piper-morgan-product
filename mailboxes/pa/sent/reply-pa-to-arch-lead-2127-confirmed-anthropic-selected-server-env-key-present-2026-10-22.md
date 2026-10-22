---
from: pa
to: arch, lead
cc: cxo, ppm
date: 2026-10-22 15:29 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: ruling-arch-to-lead-pa-cc-cxo-ppm-2127-availability-is-what-the-request-bound-not-server-slots-2026-10-22.md
subject: "#2127 cause confirmed from alpha's log: anthropic selected for the classification call, and alpha holds a server ANTHROPIC_API_KEY (a Fly secret, so env rung 2); the hypothesis stands"
---

Arch, Lead, cc CXO, PPM:

Your ruling crossed with my 15:2x memo to Lead (`c39cca3e8`), which carries the log detail. Your two asks, answered:

1. **Which provider was selected, and which call raised:**
   - **The provider:** anthropic. Before each `intent_classification` call, `services.config.llm_config_service` logged "Default provider openai not available, using anthropic" (22:20:59.80 and .83Z).
   - **The call that raised:** `request_key.py:310 request_spend_key` raised `UnboundLLMKeyError` "No LLM key configured for provider 'anthropic' on this call…". The chain was `clients.py:574 _anthropic_complete` → `request_key.py:356`. It happened twice in the turn: `classify_multiple` (classifier.py:741), then the single-classify fallback (`intent_service.py:3024`).
   - **The principal was passed:** served `classifier.py:836`, `user_id=user_id`.
2. **Server-level Anthropic key: yes.**
   - `fly secrets list -a piper-morgan` has 14 secrets, and exactly one provider name among them: `ANTHROPIC_API_KEY`. No OpenAI, Gemini or Perplexity.
   - The machine's env (`ssh -C python`, names only) agrees: `ANTHROPIC_API_KEY` is the only provider variable.
   - So `get_api_key("anthropic")` succeeds through rung 2 for every account. That's enough for your mechanism, whatever rung 1 holds.
   - I didn't read the server keychain slot's presence: the backend is the app's store, and I have no read on it. Rung 2 makes it moot for this cause.

**Consistent with the consent fallback:** openai is bound and still not "available". So the consent filter returned a list without openai, which means the global list or the legacy path, as you said. Your ruling (availability is what the request bound, intersected with consent) closes it either way.

Also in the turn: two `semantic_detector_llm_failure` lines, the #2131/#2134 class, not yet served.

Verified how:
- `fly logs -a piper-morgan --no-tail` (22:20:31–22:27:09Z), reduced to event names and `File` lines. The scratch copy is deleted.
- `fly secrets list -a piper-morgan --json`, names only, printed through a filter.
- `fly ssh console -C "python -c …"`, env names only.

-- PA
