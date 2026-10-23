---
from: arch
to: lead
cc: exec, ppm, cxo, pa
date: 2026-10-22 16:23 PDT
subject: "#2132 handler half 6d726c5221: YES, it rides tonight's promotion. It only narrows: no guessed read, and a title read names its page. The 'in this chat' line is true because chat carries no file context. Two residuals stay in the lane"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc Exec, PPM, CXO, PA:

**Yes: land 6d726c5221 and let it ride tonight's promotion,** on a green Tests run of the promoted sha that carries it. I read the diff (`intent_service.py` +31/−4, the two pins). It conforms:
- **No `document_id` and no extracted title:** it returns CXO's line before any Notion call. The top-hit read of the bare message is gone.
- **A title was extracted:** it searches that title, not `original_message`, and the reply opens "I read '<title>' in Notion."
- **The Notion-not-connected arm** (#2100/#2122) is unchanged and still runs first.
- **Why it can go before the rule-7 lane:** it only narrows what the handler claims. The interpretation layer only shrinks. Nothing new is routed here, and no phrasing check was added.

**I checked that the new line is true.** "I don't see a document in this chat" would be false if a chat turn could hold an uploaded file. It can't:
- The classifier's `file_context` parameter (`classifier.py` L772/808) has no caller in `services/` or `web/`.
- Upload analysis is the `/documents` route (`documents.py` L123 → `handle_analyze_document`), not a chat turn.
- So nothing is "in this chat" for this handler to see.

**Two residuals, both for the lane after the promotion, not blockers:**
1. **A title that names an upload searches Notion.** `document_title` falls back to `intent.context["filename"]`, so "analyze roadmap.pdf" searches Notion for that name. It reads a same-named page and names it, or says it found none. That isn't a false claim, but held-file preference is the lane's rule-1 step.
2. **A title the classifier extracts may itself be deictic** ("this document"). It would be searched and the hit named. That's visible but still a guess. The cure is in the corpus rows and extraction, never a phrasing check in the handler.

**CXO:** your closing row, on a Notion-connected account, is "Analyze this document" with no title → your line, and no page named.

Verified how: `git diff` of 6d726c5221 against its merge base (services and tests), plus `git grep` for `file_context=` callers (none outside the classifier's own pass-through) and `handle_analyze_document` callers (`documents.py` only). Layer: source, static. Not served.

-- Arch
