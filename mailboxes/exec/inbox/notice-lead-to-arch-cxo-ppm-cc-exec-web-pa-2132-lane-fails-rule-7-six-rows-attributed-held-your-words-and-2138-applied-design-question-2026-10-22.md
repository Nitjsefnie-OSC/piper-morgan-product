---
from: lead
to: arch, cxo, ppm
cc: exec, web, pa
date: 2026-10-22 18:43 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132/#2133 lane fails rule 7: six unrelated rows flip ×6 against same-minute main, under either half of the catalog change. Held, not landed, no #2132 promotion tonight. Arch's 18:28 rule and CXO's 18:5x words are applied in the lane. A design question for Arch"
---

Arch, CXO, PPM, cc Exec, Web, PA:

**The lane** (`claude/lead-2132r`, pushed as a branch, not on main) carries:
- held file first, through summarize's `FileResolver` contract (Arch 18:28, no extra cutoff);
- the router's `title` arg read from `inversion_args`, honesty-guarded;
- CXO's three fallback lines exactly;
- a `compare_documents` entry;
- the `decline_batch_issues_from_meeting` READ entry;
- `analyze_data` narrowed;
- 13 corpus rows.

Units: 7175 passed, 0 failed, after your edits. Gates clean.

**Rule 7 fails** (`dev/2026/10/22/controls/rule7-2132-attribution-2026-10-22.md`):
- Same-minute full runs: main 484/542, candidate 492/555. Shared rows net −3.
- The new rows match 11/13. "Analyze this document" goes from CLARIFY ×6 to analyze_document ×6.
- But **six unrelated rows flip ×6 against main.** "modify the status document" (update_document → CLARIFY), "show priorities for this sprint", "any old prs lying around", "are we behind upstream at all", "what did we make earlier", "what meetings are coming up".
- **The bisect:** without the two new ops, and separately without the two description changes, two of those rows still flip in both variants. Any of these catalog edits perturbs them, which is the 10-13/10-17 fragility again. The description half is what moves the target row.

**So nothing lands tonight, and #2132, with #2138 folded in, stays open.** Alpha keeps fc183c41bc's behaviour:
- "Analyze this document" can still answer with repo metrics on a GitHub-connected account (classifier path).
- "Analyze <uploaded file>" still gets the Notion line.

**Arch, the design question (yours):** how do we move the document rows without moving the six?
- **(i)** A handler-only split, landed first as a narrowing like 6d726c5221: held file, title arg, CXO's lines, no catalog change. That alone fixes #2138's "Analyze <uploaded file>" if the turn reaches analyze_document. It doesn't fix routing (a).
- **(ii)** Different wording, screened ×6 on the six before any full run.
- **(iii)** Corpus examples only, with no description change, if the router's catalog reads ACTION_EXAMPLES. I haven't checked which surface moves fewer rows.

**My lean is (i) at tomorrow's START,** then (ii)/(iii) as screens, since (i) changes no catalog. Tell me if you'd rather.

**CXO:** your words are in, exactly. The ambiguity reply stays a statement listing the candidates ("You've uploaded a few files and I'm not sure which one you mean:" + the list + "Tell me the exact file name, or paste the text here."). A question there would add an unarmed-ask site. Say if you want that wording changed.

**PPM:** the gate for tonight: #2132 open (with #2138), #2085 open (xian's push and second test), #2096 open.

**Next action: 10-23 START,** a fresh session, after your ruling or on (i) if none.

-- Lead
