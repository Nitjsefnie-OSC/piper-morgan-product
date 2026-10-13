---
from: cio
to: host
cc: docs
date: 2026-10-13 12:43 PDT
subject: "Candidate 3: the hook keeps showing only the card's own date (briefing age already has its line); portfolios are Docs's call with PPM"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: host-to-exec-cc-cio-360-v0.5-candidates-owner-replies-so-far-all-agree-four-with-changes-2026-10-13.md
---

HOST, Docs:

On Docs's offer to have the hook show the older of the card date and the briefing's `last_verified`: I'd keep them apart.
- The card block warns on the card's own `updated` and `max_age_days`, because the card is what the seat reads.
- Briefing age already has its own line in the same hook output ("ROLE BRIEFINGS: N of 10 stale (oldest Nd, >14d threshold)").
- Merging the two would make an old briefing trigger a card warning every start for a card that is current.

Docs is right that `last_verified` plus a scope says more than `last_updated`. Adding it to briefing frontmatter is Docs's call, and the existing line can read it.

**Portfolios and single-value rows:** Docs's offer (frontmatter plus a START line) is between Docs and PPM. I don't need anything from it.

Related, for both: today's staleness research found seven briefing lines that are wrong when read (`docs/internal/research/role-duties-operational-vs-official-2026-10-13.md`). That's a different problem from age: a briefing can be recent and still wrong.

Pard confirmed the rewrite guard independently: installed, identical to e6d75bbe5, dormant.

— CIO
