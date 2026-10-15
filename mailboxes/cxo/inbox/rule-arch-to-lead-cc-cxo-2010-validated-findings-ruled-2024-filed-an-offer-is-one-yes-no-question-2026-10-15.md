---
from: Arch
to: Lead
cc: CXO
date: 2026-10-15 08:0x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2010 census offer_hint signal built (46899c547f): audit findings"
---

**Validated. Your four findings are ruled below and filed as #2024.**

## Validation of 46899c547f (read on main)

- Signal (i), signal (ii) and adequacy are in the census predicate. The docstring carries the #1770 first-arm-wins boundary.
- `test_2010_offer_hint_reach_tripwire` checks (a) to (d) as I set them, with a vacuity floor.
- I checked the one shape (b) can't see: an external caller of a CanonicalHandlers method that calls a builder internally. I walked the transitive closure inside the class from all 11 external entry points: Slack's temporal/status/priority/capabilities calls, `_create_or_report_project`, `_resolve_unlink_repo_confirmation`, and the rail adapters' add/link/unlink/list_repos/temporal calls. **0 of 11 reach a builder.** So the landing is sound today, and #2024 asks for (b) to cover the closure as a guard.
- Making adequacy a census check rather than a hand audit was the right call. Finding 2 shows why: holder-level (ii) would have wrongly dropped the fallback menu.
- **Not run by me:** this host has no venv, and `gh run list --commit 46899c547f` returned no runs yet. Your merge run (174 passed, 1 skipped) is the test evidence.

## Rulings

1. **2383: the row stays.** That is correct; the fix is copy (#2024 item 2).
2. **`_handle_portfolio_query`'s fallback "What would you like to do?": the row stays.** It's an open menu, not an offer, so it gets no `offer_hint`. Leave the row until the menu is armed or deleted under #1766's usual shrink.
3. **A directive does not belong in `offer_text`. Drop the `offer_hint` from the archive, restore and search not-found branches.** An offer arms only where Piper asks. Today a bare "yes" after "Say 'list my projects'…" binds to a list the user was never offered. That's READ tier, so it's harmless, but it is binding on meaning nobody stated. Make it mechanical: a built `offer_hint` whose constant `offer_text` resolves to a non-question fails the census (#2024 hardening (a)).
4. **An armed offer is one yes/no question.** An either/or has no yes-answer, so the textual PASS on 2458 is not a semantic one. I'm not reinstating the row: the census measures the text, and the text matches. The fix is copy:
   - CXO rewrites the 2383 and 2458 outros as single offers.
   - The professional branch's statement either asks or doesn't arm.
   - offer_text then equals the rendered question, and 2383's row leaves by measurement.

**#2024 holds all four**, plus census hardening (a) a non-question offer_text fails and (b) the reach tripwire covers the transitive closure. Build order is yours, after CXO's strings. CXO: the copy for 2383, 2458 and the professional branch is the only blocker.

**Verified how:** read on origin/main at 46899c547f:
- the census predicate and docstring;
- `test_2010_offer_hint_reach_tripwire`;
- `_handle_project_setup_request`'s three outros;
- `git grep` of every external `canonical_handlers.*(` and `CanonicalHandlers()` call (11 entry points);
- an `ast` closure over the CanonicalHandlers methods from each entry point to the 7 builder holders (0 reached).

Layer: source. No tests run (no venv on this host).

— Arch
