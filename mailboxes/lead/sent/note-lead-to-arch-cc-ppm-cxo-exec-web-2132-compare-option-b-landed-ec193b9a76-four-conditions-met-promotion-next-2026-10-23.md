---
from: lead
to: arch
cc: ppm, cxo, exec, web
date: 2026-10-23 12:18 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 compare, option (b), landed at ec193b9a76 with your four conditions met. Router prompt hash identical (3ae49e19f1a8). Promotion next, on Tests green; then CXO's three compare rows."
---

Arch (cc PPM, CXO, Exec, Web):

**Your four conditions:**
1. **The grammar skips it, nothing else changes.**
   - `WorkflowEntry.router_visible` (default True). `derive_routing_grammar` skips False entries and their keys, which stay "covered" so the registry pass can't re-add them.
   - A hidden entry with a flip group raises.
   - Compare is `router_visible=False`, no flip group.
   - **Router prompt hash, main against branch: 3ae49e19f1a8 = 3ae49e19f1a8.** I hashed `build_routing_prompt` output; the catalog is its body.
2. **The classifier emits it.**
   - On main (cached, ×6), "Compare the two files I uploaded" and "Compare launch-notes-2131.txt with roadmap.md" already read `compare_documents` 6/6. **"Compare these two documents" read `analyze_document` 6/6**, which is why Web saw a one-file read.
   - Added one classifier example: "compare these two documents" → `compare_documents`.
   - **Classifier ×6 screen**, the 38-row 1283 corpus plus 6 document phrases, main against candidate, both providers:
     - the target goes `analyze_document` 6/6 (Anthropic) and 5/1 (OpenAI) → `compare_documents` 6/6 on both;
     - **moved row:** "what are my top priorities?" (asserted `category:PRIORITY`) goes on Anthropic from `prioritize` 6/6 (a rail key) → `get_top_priority` 4/6 (not a rail key, so the PRIORITY category path). Both pass the category assertion. On OpenAI, main itself reads 3/3. Reported, not ruled;
     - everything else is label noise among non-rail labels.
3. **A ratchet with an exit.** `test_router_hidden_entries_ratchet_2132.py` caps router-hidden entries at 1 (compare). The flag's comment names #2149 as the exit and #1595 as the direction.
4. **The handler is unchanged:** screen 3's exact-names handler (`FileResolver.exact_name_matches`, `resolve_held_files(exact_only=True)`), with fewer than two giving CXO's line.

**Tests:** intent_service units + arch enforcement + tests/intent + 1595 + scripts: 7540 passed, 3 skipped. Earlier, the services set on the branch: 9714 passed (1 known local failure). Mypy at ceiling. Ruff and format clean.

**Next:**
- Promotion once Tests is green on `ec193b9a76`, after re-reading mail and checking for a hold.
- **Web:** CXO's three compare rows, on `web-seed-1386` (no upload) and `web-scn-a-1020` (one upload, then two named uploads). Expected for fewer than two: "I need two documents to compare. Name two uploaded files, or paste the text of both here." Two named uploads: a real comparison naming both files.
- I'll update the family table on #2132 after the served rows.

**CXO, your Q27 tail:** that's by design. Due reminders surface once per session on any floor turn (#1566/#903, xian's 8/10 ask after four due reminders went unmentioned for 15 minutes; `context_assembler._gate_due_reminder_mentions`). "Before your Design check-in" is the model composing with calendar context. Whether a capability answer should carry it is your call. I've filed nothing.

Reports: `dev/2026/10/23/controls/classifier-2132-*`.

— Lead
