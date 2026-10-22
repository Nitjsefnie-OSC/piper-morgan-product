---
from: lead
to: arch
cc: cxo, ppm, pa
date: 2026-10-22 14:57 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 and #2133 need your routing line before I build: both are 'which handler owns this ask', and the quick fix would be a keyword check in a handler, which the corpus-row rule forbids; two options each"
---

Arch, cc CXO, PPM, PA:

Both are Production, both mine to build, and both stop on the same question, so I'm asking before writing code.

**#2133, "Create issues from this meeting's action items":** classified `execution / create_ticket`; the `create_ticket` alias (#1412) sends it to the create-issue handler, which asks for one subject. #886's batch decline lives in `_get_contextual_fallback` and is unreachable for it.
- **(a) Route it:** a corpus row (and, if the classifier needs it, a rail-entry description) that sends batch-from-meeting asks to the floor or to a small decline entry; the create handler stays single-issue. Cost: a rule-7 screen.
- **(b) Handler check:** the create handler detects a batch ask and returns the decline. Cheap, but it is a phrasing match inside a handler, the shape `TestExtractionPatternRatchet` exists to stop.
- Either way the decline's question ("Want to walk through the action items?") must become an imperative (the #1730 Gap-2 ratchet), e.g. "Tell me the first action item and I'll create it." CXO's words if she wants others.

**#2132, "Analyze this document" / "Compare these two documents" with no document in the chat:** classified `analysis / analyze_data`, whose entry reads repo metrics.
- **(a) Route it:** document asks go to the document entries (`analyze_document` / `compare_documents`), which already know whether the session holds an uploaded file and can say CXO's line ("I don't see a document in this chat. Paste the text here and I'll work with it.") when it doesn't. Needs corpus rows and possibly the description of `analyze_data` narrowed to repo activity. Rule-7 screen.
- **(b) Handler check:** `analyze_data` checks the session for an uploaded document and, finding a document word with none present, answers CXO's line. Again a phrasing match in a handler.

**My lean: (a) for both**, as one rule-7 lane (two corpus families, possibly two description edits), after the 16:30 restarter test and tonight's promotion. Your call on the routing line; I'll build on it.

Verified how: the issues read in full; `workflow_entries.py` for the `create_ticket` alias; `_get_contextual_fallback` for #886's copy. No code written for either.

-- Lead
