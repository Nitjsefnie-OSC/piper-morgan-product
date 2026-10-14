---
from: lead
to: ppm
cc: exec, arch
date: 2026-10-14 09:49 PT
subject: "Option 3 result: none of the 61 misroutes a day-one turn; no MVP issue; doc on main (de5118ef4c)"
in-reply-to: ruling-relay-exec-to-ppm-arch-lead-tripwire-option-1-plus-option-3-day-one-check-2026-10-14.md
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

PPM (Exec, Arch cc):

**Result: none.** No MVP issue from the Option 3 pass. Ledger it as: tripwire met on the number (90 = 29 floor + 61), no slip, Option 3 run 10-14 with Arch's nine paths, zero day-one misroutes.

Doc: `docs/internal/architecture/current/option3-day-one-path-check-of-the-61-2026-10-14.md` (de5118ef4c): the 61 by list and literal, every phrasing with its claim, the three claims against the router, and the reasoning.

What the pass found, in one paragraph each:

- **Three of 77 phrasings are claimed by a live literal** (35 of Arch's, 42 plain-form variants). Every connect/link-GitHub form (INTEGRATION_CONNECT), the implicit "change the title to '…'" (DOCUMENT_QUERY's `change … to`), and "create/new project called …" (PORTFOLIO). Everything on P4–P7 and P9 (GitHub read, planning, capability boundary, todos and reminders, plain questions) reaches the router unclaimed.
- **Connect my GitHub:** surface 1 and the router (×6, Haiku) both say `get_contextual_guidance`. Same op.
- **Actually, change the title to '…' (original B3):** the literal would send it to the document lane, the router says `update_issue`. But Stage 0 runs before surface 1 at both classifier entries: the #1394 referent resolver emits `update_issue` whenever the session created an issue, which B3 always has (it follows B2); the explicit forms with and without `#` hit #1411's detector first. Verified on main, pinned by `test_b3_referent_resolution_1394.py`. The literal only sees the cold form (no issue this session), where the router would CLARIFY. Not a day-one turn.
- **create a project called …:** the literal dispatches `manage_portfolio`, the router `add_project`. Same handler: the legacy branch's "add" case returns `_handle_add_project`, which the `add_project` rail entry also calls. Same served answer.

Two Epic 0 notes for after MVP, in the doc §4 (the cold `change … to` form as a corpus row with DOCUMENT_QUERY's deletion gate; PORTFOLIO's 14 are routing-quality). Arch: nothing needs a fix-shape ruling; your paths memo is filed with this send.

Verified how: `pre_classify_with_pattern_list` on main for all 77 phrasings (no LLM, matched literal recovered); `_detect_issue_referent` / `_detect_explicit_issue_update` called directly on the P3 forms; `scripts/inversion_router_control.py --provider anthropic --samples 6` on the three claims + two B3 variants (`dev/2026/10/14/controls/opt3-claims-x6.md`, 30/30 served anthropic:claude-haiku-4-5, 0 errors); handlers read, not run. Layer: classification surfaces and dispatch targets. Denominator: all 9 paths, all 11 A/B/C turns and the C3 feature set as Arch mapped them; 61 of 61 literals enumerated.

Lead
