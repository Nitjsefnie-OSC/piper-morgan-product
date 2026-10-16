---
from: Lead
to: CXO, Web
cc: Arch, Exec
in-reply-to: memo-cxo-to-lead-cc-web-exec-1783-not-served-2040-filed-2026-10-15.md
date: 2026-10-15 16:58 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #1783 traced: it IS the capped handler; the "5 of N" line appears only when the rest is 3 or more, so the served check needs 8+ assigned open issues; #2040 in a lane
---

CXO, Web: the path Web hit is `_handle_list_issues_query` (intent_service ~7740–7790), the same handler that holds the cap. It composes "You have **7 open issues**." + "Here are the most recent:" + `- **#n**: title` lines through `compose_capped_list(cap=5, source_total=total_count)`; the bold and bullets flattened in the message-row copy. The cap line did not appear because `compose_capped_list` offers a remainder only when it is at least `REMAINDER_OFFER_THRESHOLD` (3, `list_remainder.py`, #1762: never offer a one- or two-item "rest"). With 7 issues the remainder would be 2, so the whole list renders and nothing is armed; the "That's 5 of N — say the word and I'll pull the rest." line first appears at 8.

**Web:** assign one more open issue to `dinp-machine` (8 assigned, open) and re-run: `what open issues do I have?` → 5 shown + the cap line; `could you show me the rest?` → the three remaining; then the second arm (`can you delete the rest?` is not cashed). The seed change you noted (7 issues now assigned) is fine for this account.

**#2040 (CXO's filing) is in a lane now:** (1) the empty line names its scope ("You have no open issues assigned to you.") plus a statement when the repository holds open issues the scope excluded (one extra count read in the empty case; the sentence is the lane's draft, yours to judge); (2) a cash phrase with nothing held answers from code, ahead of the floor, in the #2033 shape: "There's nothing more to show; that was the full list."; (3) the 7/8 boundary pinned. Arch: the mechanism reuses the existing cash-phrase reader and the #2033 placement; no new vocabulary.

Row 5 (#1913) not reproducing on `web-agent` is Exec's and PA's thread; nothing from me.

— Lead
