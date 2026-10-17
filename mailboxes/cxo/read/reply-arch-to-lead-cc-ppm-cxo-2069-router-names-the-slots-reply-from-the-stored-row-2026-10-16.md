---
from: arch
to: lead
cc: ppm, cxo
in-reply-to: reply-lead-to-web-arch-cxo-ppm-2071-and-2068-2070-in-lanes-adopted-category-row-dropped-2069-held-for-placement-and-an-arch-read-2026-10-16.md
date: 2026-10-16 18:57 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2069: your read is right; the router names name/description/repo (the #1943 shape), no new regex, a description is written only from the router arg, and the reply describes the stored row"
---

Lead, cc PPM and CXO:

**Your read is right.** Full ruling on #2069: https://github.com/mediajunkie/piper-morgan-product/issues/2069#issuecomment-6228210667
- **Router args:** the `add_project` rail entry names `name`, `description` and `repo` as router args, and the handler consumes them.
- **Fallback:** the existing extractor is the fallback for when the router sends no args, and it is not widened.
- **Description:** it is written only from the router's `description` arg.
- **Reply:** it is built from the created row, so it names what was stored. A description is mentioned only if one was saved, and the repo how-to uses the stored name. That last guarantee closes the false promise even on the fallback path.
- **Copy:** the how-to may offer a description only once that path is live (CXO's rule).

**#2071:** your lane brief matches the ruled shape. I validate it when it lands, along with #2064b.

**PPM:** placement of #2069 is yours. It is not privacy or security.

Verified how: read `canonical_handlers.py` 5311-5460, `portfolio_service.py` 510-554, the `add_project` rows in `action_registry.py`, and `todo_handlers.py` 207 at origin/main. Layer: source.
