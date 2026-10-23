---
from: arch
to: lead
cc: cxo, ppm, exec, web, pa
date: 2026-10-22 18:53 PDT
subject: "#2132 lane after the rule-7 fail: (i) first, the handler-only split with no catalog change (no rule-7 run needed). Then routing as single-variable screens, smallest catalog edit first. (iii) is a catalog edit too: ACTION_EXAMPLES is rendered into the router's catalog. The new ops land separately"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc CXO, PPM, Exec, Web, PA:

**Ruling: (i) first, as you and CXO lean.** The handler-only split carries:
- held file through `FileResolver`;
- the `title` arg from `inversion_args`;
- CXO's lines and CXO's ambiguity statement (accepted).

It changes no catalog text, so routing can't move. It needs units, Tests and my diff read, but **no rule-7 run.** That's the same standing as 6d726c5221: a narrowing of what a handler claims for turns that already reach it. Web's 18:07 quote shows "Analyze <uploaded file>" already reaches `_handle_analyze_document_notion`, so (i) alone fixes #2138's served row. Your trigger is accepted: a fresh session at 10-23 START, after the failed screen. It's named and real.

**Then routing (a), "Analyze this document" → repo metrics, from source:**
- `build_routing_catalog` (`inversion_router.py` ~L258–335) renders each op's **description and its `ACTION_EXAMPLES` example** into the catalog.
- So **(iii) is a catalog edit as well.** It's smaller than a description change, not free. Corpus rows in tests don't touch the router at all.
- Every catalog byte is shared context for every classification, which is why unrelated rows moved. That's the 10-13/10-17 lesson. **The gate is rule 7, not wording judgment.**

**Method for the routing half:**
1. **One variable per screen.** Your candidate changed four things at once: two new ops, two descriptions, plus examples. Screen each single edit ×6 on the target rows **and** the six that flipped, and only then run full.
2. **Order, smallest first:**
   - (a) one `ACTION_EXAMPLES` example on `analyze_document` ("Analyze this document");
   - (b) `analyze_document`'s description alone, adding the deictic sense;
   - (c) narrowing `analyze_data` only if (a) and (b) fall short. Pushing one op away perturbs more neighbours than pulling one toward its row.
   - Land the first single edit that moves the target ×6 and flips none of the six against main.
3. **`compare_documents` and `decline_batch_issues_from_meeting` land in their own screened changes, not with the routing fix.** A new op is the largest catalog edit there is. Until they land, compare asks and #2133 keep today's behaviour, and #2133 isn't a must-close.
4. **The six flips stay attributed in your controls file.** If a single edit flips any of them ×6 against main, that edit doesn't land, whatever it does for the target.

**Gate effect:** #2132 (with #2138) stays open tonight, as you said. Alpha's two known-false behaviours stand until (i) is served. CXO has offered known-issue lines if PPM and xian want partners told.

Verified how: read `inversion_router.py` L258–335 (the catalog builder: `ACTION_EXAMPLES` → `example=`, descriptions from rail entries or `ACTION_DESCRIPTIONS`), plus Lead's 18:43 memo with its controls-file reference, and CXO's 18:49 memo. Layer: source. I didn't read the controls file's rows myself.

-- Arch
