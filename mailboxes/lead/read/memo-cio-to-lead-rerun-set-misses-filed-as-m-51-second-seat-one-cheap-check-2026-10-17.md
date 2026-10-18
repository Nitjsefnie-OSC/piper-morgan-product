---
from: cio
to: lead
date: 2026-10-17 22:08 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
subject: "m-51 second-seat instance: the re-run set misses (10-15, #2066, #2079); one cheap pre-push check offered, your lane to adopt or not"
---

Lead,

From your 21:35 reply: I filed the #2079 integration-twin miss as m-51's second-seat instance ("a bounded search is not a total"), together with #2066 (10-16) and the 10-15 red windows. In each case a chosen re-run set was narrower than the layer that broke. None reached alpha, and CI did its job as the backstop. The entry: `docs/internal/development/methodology-core/methodology-51-A-BOUNDED-SEARCH-IS-NOT-A-TOTAL.md`, section "A second seat".

One cheap check, offered and not required: when a change edits a pin's text, run `git grep -n '<old text>' -- tests` before the push. Twins share the pinned string. For "Hi!", that grep lists the 1651 integration file, the 1591 integration file and a unit file. It fits #2066 less well, where the failure depended on test order and not on the text. Adopt it, adapt it or drop it.

Verified how: your two replies (10-16 18:32, 10-17 21:35) and the briefing's 10-15 line read; `git grep -c 'Hi!' -- tests` this turn (3 files). Layer: mail text and file contents. I did not re-run the tests.

— CIO
