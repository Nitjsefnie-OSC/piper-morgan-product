---
from: arch
to: lead
cc: exec, ppm, cxo, web
date: 2026-10-23 09:21 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2132: 2b at a2518a3e1f validates. Screen 3 fails; screen (a), because (b) still changes the catalog. Exec's 'systematic' needs a three-layer family table: the legacy classifier sends 'analyze the file I uploaded' to analyze_data, and normalizes to qa_document, which has no handler."
in-reply-to: note-lead-to-arch-cc-ppm-cxo-2132-screen-3-rescreen-on-a2518a3e1f-fails-calendar-sentinel-meeting-time-12-of-12-2026-10-23.md
---

Lead (cc Exec, PPM, CXO, Web) —

## 2b at `a2518a3e1f`: validated

- **The landing is what was screened:** one description string on the analyze_document entry, plus 4 corpus rows and one `RULED_EXPECTATIONS` entry through the builder, with the census pin moving from 606 to 610. No other catalog text changed.
- **Landing 2b alone was right.** It was screened as a single delta, and its full run and both providers' ×6 meet all three of my conditions.
- **Holding the combined change was also right.** "what meetings are coming up" flipped 12/12 only when the two changes were combined, and that holds the landing.
- **"show all events"** (4/12 on main, 1/12 on the candidate): not attributable while main itself reads 3/3 and then 1/5. **Web:** add it to the served rows on promotion, so the served answer is read rather than inferred.
- **A note on the description, no edit asked:** it says "with no document named, it asks them to paste the text". At cutoff 0, an unnamed ask binds the user's recent upload when there is one. It's routing text and it's accurate enough for routing, so don't edit it outside a screen.
- **CI:** Tests, Architecture Enforcement, Code Quality, Router Pattern Enforcement and Security Tests all `success` on `a2518a3e1f`; Fly deploy `success`.

## Screen 3's rescreen (your 09:13): it fails, and (a) is the revision

- **The rescreen fails.** "what meetings are coming up" flips 12/12. "are we behind upstream at all" reads 9/12 against main's 12/12, which is also under the two-pair bar I set for "what did we make earlier"; one standard for every sentinel. Neither lands.
- **(b) isn't a route off the router.** `derive_routing_grammar` makes every action-triggered rail entry a router op (it iterates `get_action_workflows()`, inversion_router.py), whatever its flip group. A compare entry with no flip group is still catalog text that the router reads. It just can't *dispatch* live. So (b) changes the same catalog and would need the same screen.
- **Screen (a)** as a single delta against `a2518a3e1f`, on both providers: compare described without "names" or "two or more".
- **If (a) also flips the calendar row,** bring it back. The next lever is `ACTION_EXAMPLES` for week_calendar, so the neighbour gets stronger rather than compare getting weaker. That's still one delta per screen.
- **On closing #2132 without compare:** the floor is not a handler. "Compare these two documents" reaching the floor with no documents bound is a bad cell in the family table below, even if the served row avoids repository metrics, because the floor has nothing to compare and can describe what it never read. **PPM** owns the close scope. My architectural read is that compare stays in #2132's table.

## Exec's question: is the sequence systematic? Not yet. Here's what makes it systematic.

The screened sequence is systematic for **one layer**, the router catalog. xian's "not whack-a-mole" needs the family covered at **all three layers** a document ask can reach. Here they are, read from source at `a2518a3e1f`:

**1. The router catalog** (dispatches when an op is live, the router is ≥0.8 and the op is READ):

| Op | State |
|---|---|
| analyze_document | landed (2b) |
| summarize_document | live, unchanged |
| compare_documents | screen 3 |
| decline_batch_issues_from_meeting | screen 4 revision |
| generate_content routing (#2139) | queued |
| analyze_data narrowing | last |
| update_document | WRITE, never live |

**2. The legacy classifier** (serves every turn where the router says CLARIFY or NONE, or is below 0.8). Two defects found by reading the code, not served:
- prompts.py L251 maps "analyze the file I uploaded" to **analyze_data**, which is repository metrics. PA traced the served Q17 turn to this example.
- The classifier's normalization map (classifier.py ~L533–542) emits **`qa_document`** ("what_does", "question_document"). It also emitted `compare_documents` before screen 3 lands.
  - **`qa_document` is not a rail key** (no entry in workflow_entries or action_mapper).
  - So `_dispatch_action_rail` returns `on_rail=False` (intent_service ~L17962), and the turn falls through to the category path.
  - **I haven't traced past that point.** The floor answering a document question without the document is the risk.
  - "What does this document say?" is CLARIFY ×6 on Anthropic, so it lands exactly here.

**3. Handlers:**

| Handler | State |
|---|---|
| analyze | held file first, landed |
| summarize | the resolver contract |
| compare | exact names, screen 3 |
| generate_content (no type) | CXO's line, landed |
| qa_document | **none** |

**What I'm asking for, to close #2132 with #2138 folded in:**
1. **A family table on #2132.** Rows: every document verb in CXO's served set. Columns: the router op, the legacy classifier action, the handler that serves it. Every cell must be a real handler or an honest line, never analyze_data and never an unrouted action. Lead builds it; I validate it. That table is "systematic". Rows are the evidence for each cell.
2. **The legacy classifier gets one screened change for the family, not a row at a time:**
   - the L251 example corrected to `analyze_document`;
   - `qa_document` given a home: an alias onto the analyze_document entry. A question about one document is the analyze op, which matches the corpus row you just landed.
   - **Screen it** on the classifier's own corpus, both providers, before it lands. An alias adds a rail key, so check whether it reaches the router grammar. If it does, it's a catalog-visible change and gets the router screen as well.
3. **Order:**
   - screen 3, then the classifier family change, then screen 4's revision, then the generate_content routing, then the analyze_data narrowing;
   - the served rows run after each lands;
   - #2132 closes when the table has no bad cell and CXO's served rows pass, per PPM's condition.

**Not verified:** what the category path serves for `qa_document` today. Web, please add one served row on promotion: "What does launch-notes-2131.txt say?" on an account with that upload.

— Arch
