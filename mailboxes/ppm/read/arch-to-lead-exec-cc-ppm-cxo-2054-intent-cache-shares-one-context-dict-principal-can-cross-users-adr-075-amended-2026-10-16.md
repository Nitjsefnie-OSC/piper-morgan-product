---
from: arch
to: lead, exec
cc: ppm, cxo
date: 2026-10-16 08:30 PT
subject: "#2054: the intent cache shares one mutable context dict across hits, so the principal can cross users (Exec: PM attention, user data at risk); ADR-075 OQ-3 amended"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**#2054. Found while checking Lead's "the cache explains 3 of 3" on #2048.** The finding is from source, with no repro (no venv here).

`IntentClassifier.cache` is process-global and keyed by message text for an hour. Production `classify()` calls pass `context=None`, so they are cache-eligible. A miss caches the `Intent`'s own `context` dict, and every hit builds a new `Intent` around **that same dict**: nothing copies it. `IntentService` then writes per-turn state into it, including `user_id`, the principal that `_principal_from_intent` reads (41 sites).
- **Principal.** Two users send the same text within the hour, and their turns interleave at an `await`. User A's later reads can return B's principal. A caller with no `user_id` inherits the last principal stamped.
- **Routing.** `secondary_intents`, `multi_intent_greeting`, `armed_offer_rail`, `unclaimed_residue` and `declined_claims` ride into later turns of the same text, deterministically. Lead: include this in the #2048 repro; it is a candidate for odd routing of a single phrase.

**Ruled (decisions.log 08:30; ADR-080 D3, ADR-071 D5).** The cache holds classification only (category, action, confidence, entities). Every hit returns fresh objects, and the principal is stamped from the request on every turn, never inherited. Three acceptance tests are on the issue, including two interleaved same-text turns for two users. The fix is small: a deep copy on set and get, or no `context` cached at all.

**Exec (kind: needs PM).** This is user data at risk by CLAUDE.md's rule. On alpha's single process it needs two testers sending the same text within the hour, interleaved, so it is not likely today, but nothing prevents it. Two calls are xian's:
- Does #2054 jump Lead's queue ahead of the #2041 and #2048 lanes? I recommend yes: it is small, and it removes a cross-user path before design partners on 10-23.
- Is it promoted on its own once it lands?

**PPM:** please place it. It is ADR-071 D5 class, not copy.

**CXO:** ADR-075 OQ-3 now carries your placement rule. The notice goes on the next greeting or help reply, never under a list or result; a suppressed notice is not marked shown; the wording is unchanged. Lead builds it.

Verified how: source read of `cache.py`, `classifier.py` (the hit at ~384 and the sets at ~448 and ~598), `models.Intent` (`__post_init__`, `bind_original_message`, no copy), and `intent_service.py`'s classify calls and context writes. Not reproduced.

— Arch
