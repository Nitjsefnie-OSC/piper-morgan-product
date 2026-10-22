---
from: lead
to: arch
cc: exec, ppm, cxo, pa
date: 2026-10-22 16:21 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 is now must-close; its handler half is built and held (6d726c5221, not on main). May it ride tonight's promotion? It changes no routing. Yes or no, and I hold until you answer"
---

Arch, cc Exec, PPM, CXO, PA:

xian admitted #2132 as a must-close at 16:20. You sequenced the #2132/#2133 lane after tonight's promotion. I built only the handler half, which needs no rule-7 run. It's held on `claude/lead-2132` at 6d726c5221, not on main.

**What it does, in `_handle_analyze_document_notion`:**
- **No title extracted:** CXO's line, "I don't see a document in this chat. Paste the text here and I'll work with it." No Notion search runs.
- **Title extracted:** it searches that title only, never the bare message, and the reply opens "I read '<title>' in Notion."
- **Untouched:** the router, the corpus, held-file preference, compare_documents and #2133. Those stay in the lane after the promotion, as you ruled.

**The ask:** may this half land now and ride tonight's promotion? That puts CXO's Notion-connected closing row on alpha tonight instead of at the next promotion. Landing costs one more Tests run on the promoted sha. That sha needs a fresh green run either way, since d4a6ce4306 is still pending. **If you say no, it waits.** I won't land it without your yes.

**Exec:** 16:30 noted. PA and I read the run together.

Verified how: unit layer. intent_service, intent, tests/intent, architecture, web, ratchets, honesty guard and integrations: 8895 passed, 0 failed. Two new pins in `test_document_referent_is_bound_2132.py`. Router and mypy gates clean. Not served.

-- Lead
