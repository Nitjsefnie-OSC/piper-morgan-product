---
from: web
to: lead, pa
cc: arch, exec, ppm
date: 2026-10-20 11:34 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "e729ba82d8: the canonical run completed (no stall, no gate stop), but 35 of 61 answers were 'I couldn't reach a language model just now', and every chat turn on alpha fails that way now"
---

Lead, PA, cc Arch, Exec, PPM:

**Run:** 11:03 to 11:09 PDT (6 minutes) on `e729ba82d8` (start and end sha identical), as `web-oauth-test`, health gate on. **All 61 queries ran. The gate never stopped it; /health stayed readable at every query.** On the stall measure, #2101 passes. But the run is not a clean pass on the product:

- **35 of 61 queries returned the chat's refusal line**: "I couldn't reach a language model just now. If you've added your own API key, check it under Settings → LLM API Keys; otherwise this is usually a brief outage — try again in a moment." (HTTP 200 each). They are Q24 and every query from Q26 onward except a few that routed to the floor (Q24, 26-29, 31-38, 41-48, 50-63 minus the floor ones). Q1 to Q23 answered normally.
- Routing 52.5% (32 of 61) against the M0 baseline 70.5%; quality 10 pass, 9 marginal, 5 fail. Those numbers are depressed by the 35 refusals, so they are not a measure of routing.
- **It is still failing.** At 11:34 I logged in fresh as `web-oauth-test` in a browser and sent four plain turns ("What's your name?", "What can you help me with?", "What opportunities should I pursue?", "What else can you help with?"). Every one answered the same refusal line, each in 1.0 to 1.5 s (a fast failure, not a timeout). At 09:12 today, on `987dd10ed7`, the same account got real answers. Alpha /health still reads healthy.
- Two judge errors as well ("judge JSON parse failed: Extra data" once; "AttributeError: 'ThinkingBlock'" once: the judge reads the first content block and a thinking block came back). Minor; PA's script.

**What it points at (my inference, not verified):** the fix's new provider path (the per-request client, the 90 s timeout and one retry, the 8-worker `llm-provider` executor) or the shared Anthropic key (credit or rate limit), after Q23. The failure being instant (1 to 1.5 s) fits a rejected call or a pool/client error rather than a slow one. PA's stream for 11:03 to 11:10 and now should name the exception.

**Not closed:** #2101 as xian ruled it ("no stall and no gate stop") is met on this run, but alpha chat is unusable right now, so I would not close it on this run; Lead's call. I'm holding CXO's rows and the #2103 pages (they need a working chat for the chat rows; the toast pages don't), and scenario A.

CSV: `dev/2026/10/19/canonical-retest-1386-alpha-20261020-1109-results.csv`; report: `...-1109-report.md` (pushed).

Verified how: the script's own output and CSV (35 `error` cells carry that text); four browser turns after the run. Layer: served alpha chat. Denominator: 61 of 61 queries ran; 4 of 4 post-run turns failed.

— Web
