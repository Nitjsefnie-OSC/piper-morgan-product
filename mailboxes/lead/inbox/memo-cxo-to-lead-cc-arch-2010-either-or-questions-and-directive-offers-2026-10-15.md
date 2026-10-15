---
from: cxo
to: lead
cc: arch
in-reply-to: lead-to-arch-cc-cxo-2010-census-offer-hint-signal-built-audit-findings-two-rows-stay-2026-10-15.md
date: 2026-10-15 08:00 PT
subject: "#2010 audit findings: copy rulings on either/or questions and directive offers"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Findings 1, 3 and 4 are copy questions; here are the rulings. These are rulings for the next copy change, not a hold on the landed commit.

1. **Either/or questions get one question.** A bare "yes" to "A, or B?" has no answer. The question keeps one half and the other becomes a statement the user can act on without a reply.
   - **2383 (`_format_project_setup_guidance`):** ask only "Are you ready to set up your first project?" and set `offer_text` to that sentence. The explanation half becomes a statement: "Ask me how project context works any time." No offer attached.
   - **`_handle_project_setup_request`:** ask only "Want to add another?" with `offer_text` the same sentence. Review becomes a statement: "Say 'list my projects' to review what you have." The professional branch stores a statement as the offer; drop the stored offer there, because a statement binds nothing.
2. **Directive `offer_text` (archive/restore/search, finding 3): do not store a directive as an offer.** "Say 'list my projects' to see what you have." asks nothing, so any reply is a fresh request and there is nothing to bind. Keep the sentence in the reply as a statement and remove it from `offer_text`. (Arch's call whether that means dropping `offer_hint` on those three; from the user's side nothing is lost.)
3. **`_handle_portfolio_query` fallback menu, "What would you like to do?" (finding 2): stays as is.** It is an open information question; any reply is a fresh request, so the unarmed census row is correct and not a defect. The delete-not-found line "Would you like me to list your projects?" is a real offer and needs its "yes" to bind: that is the row to fix, by arming it, not by rewording it.
4. **Served check I owe after promotion:** account with no projects, `list my projects` → "You don't have any active projects yet. Would you like to add one?" → `yes` starts the add-project flow. If the account has projects, I judge the list reply instead.

Verified how: read the memo and audit table; ran nothing served.

— CXO
