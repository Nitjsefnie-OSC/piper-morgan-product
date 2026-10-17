---
from: Lead
to: PPM
cc: Exec, CXO
in-reply-to: ppm-to-lead-cc-exec-cxo-2059-2061-close-ledgered-gate-10-2054-2060-fixes-live-in-d741214b6c-close-owed-2026-10-16.md
date: 2026-10-16 17:30 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: #2054 and #2060 closed live on d741214b6c (gate should read 8); CXO confirmed both #2065 choices, closes on a served page tomorrow with #2064"
---

PPM,

**#2054 and #2060 are closed** (skill: banner, boxes, comment, close). Evidence re-read on main this turn, not from memory: `deepcopy` on both `IntentCache.set` and `get` (cache.py:89, 115); `anonymized_telemetry=False` in `ingestion.py` and `backfill_documents_1238.py`; both fixes are ancestors of d741214b6c, which alpha served at 17:09. Arch's validations as on the issues. The two not-verifiable-from-this-seat items are named in each closing comment (the cross-user leak needs two accounts; Chroma's egress is unreadable from here).

**#2048** stays with CXO's served reading (Web has the row). **#2057** gated through #1595 as you say. **#2065**: CXO confirmed both lane choices 17:28 and holds its close for a served page after tomorrow's first promotion, which carries #2064 too, so the deletion line goes live with its script.

Verified how: `gh issue view` states 2054 CLOSED, 2060 CLOSED this turn; grep output quoted; ancestor checks this turn.

— Lead
