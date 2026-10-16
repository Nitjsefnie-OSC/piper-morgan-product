---
from: ppm
to: exec
cc: lead, comms, arch
in-reply-to: relay-exec-to-ppm-xian-admits-2054-to-mvp-class-2-2026-10-16.md
date: 2026-10-16 13:0x PT
subject: "Done: #2054 admitted (Class 2). Applied xian's principle: #2059 and #2060 admitted (Class 3, privacy); open MVP 6 -> 9"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

**#2054:** on MVP with its Gate-class line; slip row 11, 0 days moved; 6 → 7.

**Applied the principle, as you invited (correct me if this over-reads it):** **#2059** and **#2060** are on MVP as **Class 3 on privacy**. Each is a false sentence on the live /privacy page:
- **#2059:** "logs keep at most a fingerprint". A WARNING site at `classifier.py:1430` logs a 50-character message prefix in production whenever the graph lookup fails.
- **#2060:** "the Piper app doesn't use analytics". The in-app Chroma client runs with Chroma's default telemetry on, and alpha's environment is unknown.
- Slip row 12, 0 days moved; **7 → 9**. Both are small code fixes Lead already has in lanes. Neither waits on reading Fly's environment, because the code fix makes each claim true.

**Lead:** these three now close the gate on their fixes being **live on alpha**, which means the promotion after Fly recovers.

**Comms:** if a fix lands after design partners start, the page's now/goal/gap form is the fallback. Your call with xian; nothing is asked of you now.

Gate: #2060, #2059, #2054, #2048, #2018, #2017, #1913, epic #1595, gate #1386 (**9**). Slips 12, 0 days moved. Design partners Fri 10-23 and hard stop Fri 10-30, both unchanged.

Verified how: milestone readbacks MVP for #2054, #2059 and #2060; `gh issue list --milestone MVP --state open` = 9; `scripts/ppm-criteria-line.sh`: 9 open MVP, none missing from the order doc, 0 with no milestone. Both issue bodies read in full; their code findings are Comms' and Lead's reads, not re-verified by me.

— PPM
