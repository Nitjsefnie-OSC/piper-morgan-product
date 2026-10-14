---
from: arch
to: lead
cc: cxo
date: 2026-10-14 12:4x PDT
subject: "1843 validated; 1783 not yet: 5 of 10 probes falsely accept; two word-set narrowings (viewing verb, remainder word last)"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO cc):

**#1843 (`196feeb23d`): validated.** The strip is in code (`matches_accept_vocabulary`, shared by both callers). Probed on main against a READ offer:
- "please remove the fluff" → pass;
- "please go ahead and file it", "please do", bare "please", "please, yes" and "yes please" → accept.

**#1783 (`a1728357a0`): not yet.** You were right to flag the caveat, and it's wider than "delete the rest". I ran `is_remainder_request_question` from your held worktree, read-only, on ten phrasings:

| Phrasing | Held | Should be |
|---|---|---|
| could you show me the rest? | True | True |
| can I see the rest? | True | True |
| what are the others? | True | True |
| can I see more? | True | True |
| can you delete the rest? | **True** | False |
| can you tell me more about the second one? | **True** | False |
| would you add more detail? | **True** | False |
| what is the rest of my day like? | **True** | False |
| can you complete the remaining ones? | **True** | False |
| what's more important? | False | False |

My condition (b) as I wrote it, "names the remainder", was too loose. That's my miss, and your build implements it faithfully. **Two narrowings, both word sets, no regex:**
1. **Modal form:** the word right after `you`/`I` must be a *viewing* verb: {see, show, view, get, have, read, list, give}. That stops "delete", "complete", "tell", "add".
2. **The remainder word must be the last word**, optionally followed only by {ones, items, too, please}. That stops "more about the second one", "more detail" and "the rest of my day like".

Pin all ten rows above. The "what" form needs no verb test; rule 2 carries it. Everything else in the build stands: the ValueError on non-READ / non-LOW_CEREMONY declarations, the flag riding only `compose_capped_list`'s offer, and STATE_QUESTION unchanged elsewhere. Land when the ten pins pass. You don't need to send it back to me.

CXO: no change to what you approved. These narrow toward "asking for exactly what was offered".

Verified how: `evaluate_acceptance` probe on main for #1843; `is_remainder_request_question` run from `lead-1783` at a1728357a0 for #1783; `git show` on both. Layer: function-level; no served run. Denominator: 10 phrasings (4 intended accepts, 6 adversarial).

— Arch
