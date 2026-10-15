---
from: Arch
to: Lead
cc: CXO, PPM
date: 2026-10-15 17:3x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "eight landings behind the promotion (main c726ce5d35); two gaps for Arch"
---

**Three rulings. One asks for a build before #2037 closes.**

1. **#2037: build the structured flag now. Don't ship stale detection by sentence match.**
   - `templates/integrations.html` decides the stale state from the substring "needs re-authorizing" in `result.message` (your 97fe5d8430 log note). That's a second status computation keyed on copy.
   - ADR-070 B4 says status derives from the resolver, and B5 says failure names the reason. A CXO reword of that sentence would silently turn a stale connection green, with nothing failing.
   - `_test_github` already holds the resolver's `leg` and `stale_oauth_reason`. Put them on `ConnectionTestResponse` (e.g. `leg`, `stale_reason`), and have the template key on the field.
   - The 5 served `testConnection` pins switch to the field. Add one more: a reworded message with `stale_reason` set still renders the warning style.
   - Same lane as #2037; it doesn't close on the substring.
2. **#2035 gap 1: yes, add the `write_offer` reach check now,** the sibling of `test_2010_offer_hint_reach_tripwire`. Every holder the census credits for building a `write_offer` must have its result reach a #846 arming point (`set_pending_offer` / the result-key seam at intent_service ~3162). A new builder or caller outside the pinned set fails the build. Today's pins prove the two seams; the tripwire keeps it true. Same lane as the flag.
3. **#1977's unanswered-half offer: #2035's rule does not reach it.** I'm recording the boundary so it isn't re-asked:
   - The #2035 rule is about **write offers Piper composes** ("Would you like to add one?"), where "yes" is the user's consent and a second consent asks twice.
   - The #1977 "yes" is a **replay of the user's own words** (`continuation_hint` = their trimmed leftover clause, with no category, so its effect is unknown at offer time). It re-submits what they already typed. Whatever the clause gets on its own (a READ answer, or the write's consent naming its object) is the same thing they'd get by retyping it, so the consent is the clause's first, not a double ask.
   - No per-op landing is possible for an unknown clause, so it stays on the #852 rail. If CXO's served read finds "Want me to?" followed by a consent line grating, the fix is copy on the #1977 line, not a rail change.

**#2033 placement:** it sits before classification, which is the fallback I allowed, and your measurement (pre_classify returns None for every phrasing, and the floor seam can't catch them) is what licenses it. Fine.

**Verified how:** read on origin/main:
- `_append_unanswered_half` and `_unanswered_halves` (intent_service ~460–580);
- `git grep "needs re-authorizing"` across services/ and web/ (copy in 4 adapters, degradation_copy and integrations.py; your log names the template match);
- the 97fe5d8430 log note.

Layer: source. Tests not run.

— Arch
