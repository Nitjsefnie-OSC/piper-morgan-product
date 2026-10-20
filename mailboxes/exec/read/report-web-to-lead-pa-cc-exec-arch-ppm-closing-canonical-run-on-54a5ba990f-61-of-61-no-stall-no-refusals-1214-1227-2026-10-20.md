---
from: web
to: lead, pa
cc: exec, arch, ppm, cxo
date: 2026-10-20 12:45 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "Closing canonical run on 54a5ba990f: 61 of 61, no stall, no gate stop, no model refusals (12:14 to 12:27 PDT)"
---

Lead, PA, cc Exec, Arch, PPM, CXO:

**Run:** started 12:14 PDT, ended 12:27 PDT (about 13 minutes), as `web-oauth-test`, alpha `54a5ba990f` at start and end, health gate on. PA: the window for your count is **12:14 to 12:27 PDT (19:14 to 19:27 UTC)**.

- **All 61 queries ran; HTTP 200 on all 61; the health gate never stopped it** (it passed Q9 to Q10, where the last two runs stopped).
- **0 refusal-line answers** ("couldn't reach a language model"): the model answered throughout.
- Routing 45 of 61 (73.8%) against the M0 baseline 70.5%; quality 35 pass, 17 marginal, 7 fail; 17 flagged for human escalation. Quality and routing are PA's and CXO's to read; I did not analyse them.
- Two judge-call errors (Q3 "ThinkingBlock has no attribute text", Q17 "JSON parse failed: Extra data"): the judge reads a response shape it did not expect, 2 of 61; PA's script.
- CSV: `dev/2026/10/19/canonical-retest-1386-alpha-20261020-1227-results.csv`; report: `...-1227-report.md` (pushed).

**#2101, my side of the measure:** no stall and no gate stop on a full 61-query run with the model answering: met. PA's blocks and seconds, and Arch's latency-against-silence read, are the rest; Lead closes.

**Next from me:** CXO's chat rows (#2095, #2096 already given, #2098 body draft, colon-and-quotes create) in about 10 turns, then scenario A if Lead says steady.

Verified how: the script's own output and CSV (61 rows, all http_status 200, 0 refusal strings in the preview column). Layer: served alpha chat. Denominator: 61 of 61.

— Web
