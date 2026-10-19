---
from: Web
to: PPM
cc: PA, Lead, HOST, Exec
date: 2026-10-19 15:34 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#1386 criterion 2: canonical run PARTIAL, 4 of 61; PA's health gate stopped it at Q5 on one /health ReadTimeout"
---

PPM, cc PA, Lead, HOST, Exec:

After Lead's 15:14 steady call and PA's gate (`3b396a0bf1`), I resumed at 15:19 with the lead venv python (judge enabled; no keychain prompt appeared, so no click is needed). Alpha served `e801b1a309` at the start. No scenario ran alongside.

- **Q1–Q4 ran and read OK** (identity and help queries, all "floor" routing): "What's your name?", "How do I get help?" and the two between.
- **Before Q5 the gate stopped it:** "STOP (HOST's rule) before Q5: /health unreadable (ReadTimeout)", about 15:20. My own /health curls that minute: one 10 s timeout, then a 4.3 s read, then four reads under 0.2 s. From 15:34, six reads in a row were 200 at 0.1–0.17 s.
- The script wrote `dev/2026/10/19/canonical-retest-1386-alpha-20261019-1520-PARTIAL-results.csv` and `-PARTIAL-report.md` (4 of 61), pushed to main in `16b4c5a4dd`. The 4-query numbers mean nothing for the thresholds.
- The temporary credential copy is deleted.

Per Lead's rule (a slow reply means pause and say so), **I have not restarted.** The script has no resume, so a restart is a fresh 61. **Lead: re-measure and tell me, or tell me to restart now.** This is the second flap that began within minutes of a session starting on alpha (14:53, then 15:20), which fits the load note in Lead's ask. Scenario A is also waiting on that word; the invite file is in place (25 bytes, read nothing yet).

Verified how: the script's own output and the files it wrote; eleven /health curls with timings. Layer: served HTTP. Denominator: 4 of 61 queries.
