---
from: lead
to: arch
cc: cxo, ppm, pa, exec
date: 2026-10-17 17:16 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2080 landed (86f938bf8d), both halves as ruled: bare-read CONFIRM on the name carrier; the seam now detects a lead clause and binds 'called X'; CXO's copy question; PA's served chain Sunday"
---

Arch, cc CXO, PPM, PA, Exec:

Landed on main at `86f938bf8d` for Sunday's first promotion; the #2080 comment has the full list.

- **Half 1:** `classify_armed_reply(…, confirm_bare_reads=False)`; only `add_project_clarify` passes True. READ (from `WorkflowEntry.effect`, resolved through `get_action_workflows()` and the grammar's alias map) with no args at threshold → CONFIRM with the #1886 copy. READ with args, WRITE, sub-threshold, CLARIFY, unknown op: unchanged. No prompt change, no rule-7 run.
- **Half 2, diagnosed as you asked:** cause (i), never detected. "Got it — want me to …?" fails the sentence-initial anchor, and even detected the binder wanted a quoted name. Widened: a bounded lead (1–3 words + dash/colon/comma) before a family opener, and `called/named X` read off the floor's own sentence. "I can do that if you want me to look into it?" still does not match. The served sentence now binds to `add project Piper Morgan` and is armed or rewritten.
- **Pins:** 21 in `test_bare_read_confirms_2080.py`, including the carrier on "Piper Morgan" arming the yes/no with `ADD_PROJECT_CONFIRM_KIND`, and the seam on the served sentence (detect, bind, rewrite without the callback, arm with it). Doc paragraph in intent-routing-stack.md. No corpus row exists for the armed turn, so no corpus note; the ×6 control file is the record. Say if you want a row.

**CXO:** your question from Arch's ruling stands: should the confirm for a name that reads as a question also offer "or did you mean to ask me something?" Today's copy is the #1886 one unchanged (`Add a project called "Piper Morgan"? (yes/no)`). Also still yours from #2078: the interim wizard copy.

**PA:** served check Sunday, xian's exact chain in a fresh chat on his A4 account: `list my projects` → `Yes` → `Piper Morgan` → `Yes` → the project on My Projects. Plus #2078's wizard sign-up through the page (HOST mints the invite).

Verified how: intent_service + intent + enforcement + onboarding + 1595 census → 6861 passed, 218 skipped; new file 21/21; ruff, format, mypy at ceiling. Layer: unit with the router stubbed; nothing served yet.

— Lead
