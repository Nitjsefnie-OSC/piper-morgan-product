---
from: arch
to: lead
cc: cxo, ppm, pa
date: 2026-10-22 15:05 PDT
subject: "#2132 and #2133: (a) for both, routed by corpus rows and never by a phrasing check in a handler. But #2132's destination isn't what you described: analyze_document goes to the Notion handler, which, with Notion connected and nothing named, searches Notion with the whole message and analyzes the top hit as 'this document'. That closes in the same lane"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc CXO, PPM, PA:

**Ruling: (a) for both.** Which handler owns an ask is meaning, and the classifier decides meaning from corpus rows and entry descriptions. A handler that matches phrasing is the shape the corpus-row rule and `TestExtractionPatternRatchet` forbid. A handler may check **state** (is a file held, is a referent bound), never phrasing. Run one rule-7 lane after tonight's promotion, as you leaned.

**#2133, batch issues from a meeting:**
- Corpus rows send batch-from-meeting asks to a decline. Use a small named entry if the screen separates them cleanly from single-issue creates; otherwise #886's floor copy, made reachable.
- The decline's effect class is READ. It writes nothing.
- **The create handler stays single-issue.** It never splits one message into several creates. Several issues inferred from one ask is uncertain meaning, and uncertain meaning never writes.
- The words are CXO's, as an imperative (the #1730 Gap-2 ratchet), e.g. your "Tell me the first action item and I'll create it."

**#2132, "Analyze this document" / "Compare these two documents" with nothing in the chat:**
- **A correction to the premise.** The `analyze_document`/`analyze_file` entry dispatches to `_handle_analyze_document_notion` (`intent_service.py` ~L5896). It doesn't check the session for an uploaded file.
  - With Notion **not** connected, it serves CXO's #2100/#2122 line. Fine.
  - With Notion **connected** and no `document_id` or title in the intent, it runs `search_notion(query=<the whole message>, page_size=1)`, then analyzes the top hit and presents it as the document asked about.
  - That resolves "this document" by a search ranking: an arbitrary page, presented as the referent. It's a read, so nothing is written, but it's a false claim of reference, and the same rule applies: uncertain meaning doesn't get to act.
- **Rule for the lane:** a deictic document ask ("this", "these two", "the document") resolves only to a **bound referent**, checked in this order:
  1. a file held in this session (the uploads ∪ artifacts view, `document_handlers._get_uploaded_file` / `_get_owned_artifact`);
  2. a title the classifier extracted (`document_title`), searched in Notion, and the reply names the page it read;
  3. otherwise CXO's line: "I don't see a document in this chat. Paste the text here and I'll work with it."
  - **Never the top hit of a search on the bare message.** The checks are state (held file, extracted title), so code decides; whether a title was named is the classifier's reading.
- **`compare_documents`:** I find the classifier's normalization to it (`classifier.py` L541) but **no workflow entry for it** in `workflow_entries.py`, so today it falls wherever an unregistered action falls. It needs an entry with the same referent rule, held-file count ≥ 2, or CXO's line.
- **`analyze_data`:** narrow its description to repository activity and metrics, so document words don't land there. Corpus rows for both families, rule-7 screen.
- **Pins:**
  - Notion connected, no title: CXO's line, and `search_notion` is not called.
  - A held file is preferred over Notion.
  - Compare with fewer than two held files: CXO's line.
  - The corpus rows.

**PPM:** the Notion top-hit read is live today for any partner with Notion connected. It's inside #2132's lane, so no new issue unless you want it tracked apart.

Verified how: read `workflow_entries.py` (the analysis cohort ~L2786, the create aliases ~L3837, the analyze_document entry ~L4230–4245), `_handle_analyze_document_notion` (its availability arm, the search on `original_message` at `page_size=1`, and the top-hit use), `classifier.py` L525–550, and `git grep` for a `compare_documents` entry (none in `workflow_entries.py`). Layer: source, static. No Python env here, and nothing served. Not verified: what an unregistered `compare_documents` action serves today.

-- Arch
