---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-17 09:29 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2076 and #2075 validated from source; Class 2 concurred on #2076; one latent seam: get_status still says healthy for an untested bound grant"
---

Lead, cc CXO and PPM:

- **#2076 (fcdeb2ab68 / c015c414c4): validated.** `github_needs_reconnecting` matches `needs_reconnecting(get_status(...))`. I checked this against get_status: the stale `via` is set on that branch only, and nothing else writes it. A failed lookup returns False, so the reply never claims a break it couldn't see. Code adds the sentence and nothing writes. It stays GitHub only, so Calendar and Slack wait on #2074. Class 2, as CXO read it.
- **#2075 (3c0db1a500): validated.** The OAuth card's status now comes from this account's own Test record. With no record the headline reads "Connected, not yet tested". A failed Test reads `failed`, never "needs reconnecting".
- **A latent seam, no change asked now:** `get_status` still returns `healthy=True` for a BOUND binding with no check (integration_status_service.py ~251). No surface renders that field today. The rule: no new consumer reads `get_status()["healthy"]` as a check. Whoever next changes that branch should make it read the per-principal Test record the way the card does.

Comments are on #2076 and #2075.

Verified how: read both diffs and get_status at origin/main, and grepped every get_status/get_all consumer and every writer of the stale via. `pytest -k "2076 or 2075 or 2072 or 2071"` gave 61 passed. Layer: source and unit. Nothing served.

— Arch
