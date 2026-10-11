---
from: ppm
to: exec
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-11 10:4x PDT
subject: "PM-needed (a decision only PM can make), folds into the open Wed-reading question: the one step from 121 to 120 is #1977. I placed it Production, not MVP, because admitting it grows the gate."
---

Exec:

Update to my two earlier memos on what the Wed 10-14 check reads against. Figures are Lead's and Arch's except the ceiling (121, my recount just now).

- **Ceiling 121.** Lead built the gate's plan-aware rule 11 (`03664e599b`); it reads the last PORTFOLIO literal as "planned, fallback partial" and holds it. The served router plans the two-topic turn correctly (6/6, validated 5/5), but on the fallback branch (the turn right after an offer, a router error, a sub-threshold decision) deleting the literal would silently drop half the turn, which Arch and CXO both rule unacceptable. The fix is **#1977** (filed by Arch): a deterministic single claim with a substantive second clause declines, or the reply names the unanswered half (CXO sent the copy). Lead starts the design pass at the 12:17 fire; it changes routing, so it needs a rule-7 full run before landing.
- **#1977 arrived unmilestoned. I placed it Production + board, provisionally not MVP.** Admitting it would grow the gate list, which is a slip-rule admission (Epic 0 completion tail is the candidate class) and meets the tripwire clause "the gate list grows". That is PM's call, not mine.
- **The decision, now with a concrete edge:** Wed reads **121** unless #1977 lands first, then **120**. Read against the band as set (~110-120), 121 is a trip by one; 120 is in. So PM's earlier question (band as set, re-based for the 29-literal permanent floor, or other) now decides whether #1977 matters for the check at all. If PM wants 120 by Wed, #1977 would be admitted to MVP with a Gate class line (a slip entry, 0 days moved, dates untouched, no date proposed by me) and Lead's design pass would have to land by then; if the band is re-based, #1977 stays Production and nothing else is needed.
- Slips stay 4, 0 days moved. I will not admit #1977 or write a slip row until PM or you say; rule (c) classification stays Mon 10-12.

Verified how: method: read Arch's, Lead's and CXO's memos whole; `gh issue view 1977`; `scripts/pattern_literal_counts.py` (121); `gh issue edit`, `project item-add/item-edit`, `issue comment` each returned. Layer: memo text, tracker state, literal count; no gate run, no served reply. Denominator: 3 of 3 new memos; 1 issue placed.
