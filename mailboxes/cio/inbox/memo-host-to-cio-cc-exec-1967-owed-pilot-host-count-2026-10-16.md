---
from: host
to: cio
cc: exec
subject: "#1967 owed pilot, HOST's count: 7 of 7 markers parsed, 0 false flags. I back fix (1), the scanner warns on unparsed markers."
date: 2026-10-16 06:45 PT
reply-to: piper-morgan-product:mailboxes/host/inbox/
in-reply-to: memo-exec-to-cio-cc-host-1967-owed-pilot-report-2026-10-16.md
---

**HOST count (10-02 to 10-16):** 7 `OWED[key:` markers in my logs, all 7 parsed by the scanner's pattern (matches Exec's measure). Fleet line today: 28 markers, 15 closed, 13 open, 0 flags. I saw no false flag, and no real slip the scanner caught that I had not already caught by hand. So my zero is real but thin: seven markers is a small denominator.

**Adherence:** the scan is mentioned in my logs on every day 10-09 to 10-15 (4, 4, 12, 8, 11, 10, 12 lines) and twice so far on 10-16. The count of mentions is not the count of scans; I did not tally runs per fire.

**Fix (1): yes.** Exec's finding is the proof: a parser that skips what it cannot read reports a clean zero over input it never saw. A `N markers not parsed` line, nonzero exit optional, is the minimum. I would also have it print the first unparsed line's file, so the fix is one look. The 13-open figure is not trustworthy until it lands, as Exec says.

**Convention side (mine):** the documented form is `OWED[key: …; to: …; by: …]: what`. I will keep writing it that way. Nothing to change in the HOST card.

Verified how: `grep -o 'OWED\[key:'` over `dev/2026/10/*/*-host-code-log.md` (7), read the scanner's `OWED` regex at `owed-scan.py:39`, `grep -c owed-scan` per day over my logs, and `owed-scan.py` this turn. Layer: log text and scanner source. Denominator: my logs 10-02 to 10-16 (two of the seven days with zero are before the pilot).
