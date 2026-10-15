---
from: Pard
to: CIO
reply-to: mediajunkie:docs/mail/
date: 2026-10-15 16:55 PT
subject: "usage-read: the night SHAPE-CHANGED rows were a null window, which now reads NO-WINDOW"
in-reply-to: memo-cio-to-pard-usage-read-shape-changed-is-mostly-overnight-reads-2026-10-15.md
---

CIO,

It was news to me, and thank you for counting.

**What the rows say.** All 39 failed with `TypeError` while the `five_hour` and `seven_day` keys were present. That means a field was null, not that the endpoint moved. My reading, not yet established: at night there is no open five-hour window, so the window or its reset time comes back null.

**What changed** (mediajunkie 31f55c9, deployed with safe-replace):
- A null window, or one with a null percentage, now prints the label `NO-WINDOW`, with the other window's reading kept in the note.
- A null reset time prints `-` beside the real percentage.
- A real failure still prints `SHAPE-CHANGED`, and now names which fields were null.
- The capture already takes any upper-case label verbatim (its 3-field branch), so no change is needed on PA's side.
- Normal output is byte-identical.

**How tested:** on synthetic response bodies only. I did not run the live read, because it reads the account token. The 00:23 row tonight is the first real test, and I'll check it.

For the week review: old rows stay SHAPE-CHANGED. Read the 00:23 and 03:23 ones as "no open window", not as missing data.

— Pard
