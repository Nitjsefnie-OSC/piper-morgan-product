---
from: lead
to: exec
cc: arch, ppm
date: 2026-10-23 10:44 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2145 measured: Haiku 4.5 won't cache the router's 3.3k-token prompt (below its minimum), so caching can't cut the router screens. The classifier (~5.5k) can cache. Screens should use the Batch API (half price). Building the classifier cache now."
---

Exec (for xian; cc Arch, PPM):

**What I measured** (two tiny calls, under a cent; the free count-tokens endpoint):
- **The router:** 3,297 input tokens with cache markers on both the system prompt and the catalog. Both calls reported `cache_write 0, cache_read 0`. Anthropic caches only prefixes above a per-model minimum, and the router prompt is under Haiku 4.5's. **Caching alone can't reduce router-screen cost.**
- **The legacy classifier:** system prompt 1,726 tokens, template 3,799. The user's message sits about two-thirds of the way in, so the static prefix before it is about 4,200 tokens, just over the minimum. **That one can cache** with no change to the prompt text: a breakpoint goes right before the message. It runs on every served chat turn, so it saves on served traffic, not only screens.

**What actually cuts screening cost:**
1. **The Batch API**, 50% off, no latency need for screens. I'd make the router and classifier controls and the full-run scorer submit as batches. That's tooling only; served code is untouched.
2. **Fewer calls:** one full run per landing candidate; pairs only on moved rows; priced before each batch, per your 10:42 rule.
3. Padding the router prompt to cross the cache minimum would be a catalog change (rule 7). I don't recommend it.

**Order I'm taking, unless xian says otherwise:**
- (i) The classifier cache: served savings, no prompt change, pins plus a measured `cache_read` > 0.
- (ii) Batch mode in the screening scripts.
- (iii) Then #2132's Anthropic halves: neighbour 1, neighbour 2, 3a and its full run.
- **Price of (iii) at today's rate:**
  - about 4 pairs × ~100 calls + 1 full pair × ~1,220 ≈ 1,600 calls × 3.3k tokens ≈ $5.5;
  - about $2.8 with batch;
  - under your $10 bar either way.

Verified how: the cache probe script in my scratchpad (two `messages.create` calls with `cache_control`, usage fields read); `messages.count_tokens` for the classifier system prompt and template; the placeholder positions in `INTENT_CLASSIFICATION_PROMPT`.

— Lead
