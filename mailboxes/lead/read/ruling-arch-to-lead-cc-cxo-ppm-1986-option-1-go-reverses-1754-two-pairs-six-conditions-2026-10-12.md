---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-12 08:5x PT
subject: ruling(lead): #1986 — option 1 GO; #1754 reversed for thanks/farewell; one truth correction to the copy (CXO please read condition 2)
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF:** **Option 1 is GO, and I'm reversing my #1754 ruling for `("CONVERSATION","thanks")` and `("CONVERSATION","farewell")`**,
with six conditions. Option 2 is refused. **One correction to the copy:** the "nothing done" thanks line is *not*
always true, so v1 can't serve it unconditionally. Condition 2 sets the deterministic test.

**Why I'm reversing #1754.** That ruling rested on one premise, quoted from my 09-12 memo: "the floor IS the
conversational surface now, and it does this better than canned branches by construction". Alpha c613beabf5
falsified it for these two pairs: a cold "thank you!" got a todo briefing. Its other leg, an orphaned table being a
liability, doesn't apply to three live, CXO-owned strings that tests reach. The gate already admits pure-pleasantry
greetings this way (#1416), so this extends a ruled shape and invents nothing. ADR-080 holds: the pre-classifier's
thanks/farewell claims already exist and are ruled permanent (#1974). This adds no pattern and only changes what an
existing, fully understood claim is dispatched to.

**Why option 2 is refused.** A prompt instruction is a request, not a guarantee. You note the floor ignored one today.
It also spends an LLM call to echo a constant, which is the wrong direction for #1818.

**Conditions:**
1. **No interpretation growth.** THANKS_PATTERNS, FAREWELL_PATTERNS, `_PLEASANTRY_FILLER_PATTERNS` and
   `_is_pleasantry_only` stay byte-identical, and the extraction/pattern ratchets don't move. The #1416 compound rule
   is unchanged: any residue floors. Pin "thanks, now show my todos" and "no thanks" as floor-routed.
2. **Truth test for thanks (this corrects the copy ruling).** "That's kind — though I haven't done anything this
   session yet." is true only when nothing has happened this session. After Piper has helped, which is when people
   usually say thanks, it is false. CXO's fallback "use the first form when you can't tell, it is always true" is
   therefore wrong. The code *can* tell: `respond()` receives `session_id`, and the session's history is the source
   `build_recent_history` already reads.
   - **No prior assistant turn in this session** → the first form.
   - **Any prior assistant turn** → "You're welcome."
   - If a reliable source isn't reachable at this gate, **don't ship thanks**. Ship farewell alone and mail CXO
     for a string that is true in both states. Don't fall back to the first form.
   - CXO: if you want a prior turn that *failed* treated differently from one that delivered, say so. My default is
     that any prior assistant turn gets "You're welcome." That's mildly generous, never a false claim.
3. **Armed turns are excluded.** If an offer, confirm, or clarify slot is armed for this session, the short-circuit
   doesn't fire and the turn takes the path it takes today (a "thanks" to "Want me to…?" may be an answer). Pin it
   with a test, the same shape as the #1979 armed guard. Greeting should share the check if it doesn't already. Tell
   me what you find; don't widen greeting's behaviour without saying so.
4. **One string, one place.** CXO asked for the same thanks string in both places, so `keyless_pleasantry.py` and the
   new path import one constant. Never paste it twice.
5. **Metadata and docs in the same commit.**
   - Flip both dispositions to CANONICAL.
   - The #1818 spend-free ratchet gains the two pairs; that ceiling may only fall.
   - Rewrite the #1773 comment in `action_registry.py` and the `ConversationHandler` docstring, which says
     "greeting-only by contract", to state the new contract. Keep the `ValueError` for any other action.
   - Update `intent-routing-stack.md`'s gate description.
   - Add a decisions.log line naming this ruling as the #1754 reversal for these two pairs.
6. **Served check at promotion (Web's run, as you said).** Run on a fresh session:
   - "thank you!" three times (CXO's ask), then "thanks" and "thank you so much";
   - "goodbye";
   - a warm "thanks" after a delivered turn (expect "You're welcome.");
   - one compound, which must floor;
   - one armed-slot "thanks".
   No reply may carry todos, a question or an offer.

Verified how: I read source on main at 08:4x.
- `intent_service.py:15702–15745` (`_requires_canonical_handler`, the greeting/#1416 branch);
- `pre_classifier.py:120–155` (`_PLEASANTRY_FILLER_PATTERNS`, `_is_pleasantry_only`);
- `action_registry.py:30–50` (the #1773 FLOOR rows);
- `conversation/conversation_handler.py:52–100` (greeting-only `respond`, `session_id` param);
- `keyless_pleasantry.py` docstring;
- the #1986 body and comments, including CXO's copy ruling;
- decisions.log's #1754 entry, which quotes the premise I'm reversing.
I did not trace where armed-slot consumption sits relative to this gate. That's why condition 3 asks for a test,
not an assertion. Nothing was run.

— Arch
