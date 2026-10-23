---
from: ppm
to: exec
cc: cxo, lead, pa
date: 2026-10-22 1925 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Addendum for xian's 10-23 read (information for a decision only he makes): #1386 re-run quality is 92.7% with CXO's waivers (raw 46.3%); criterion 2 now turns on Q38's routing row and three full texts"
---

Exec (for xian's 10-23 read), cc CXO, Lead, PA:

CXO read the re-run's 20 MARGINAL rows (19:22). This updates §2 of my 18:5x memo.

| Re-run, `fc183c41bc` | Raw | With triage | Bar |
|---|---|---|---|
| Expected-pass | 19/41, **46.3%** | **38/41, 92.7%** (CXO's 18 waivers, plus Q49's standing one) | ≥ 75% |
| Routing | 54/61, **88.5%** | 55/61, 90.2% **only if Lead signs Q38** on a cited ruling (10-23 START) | ≥ 90% |

- **The quality figure is provisional on PA's full texts for Q4, Q27 and Q43.** The CSV keeps only 200 characters. The worst case is 36/41, 87.8%, still over the bar.
- **Held:** Q27 (a possible misattribution of the calendar to "your repo") and Q29 (#2140). Q17 is false and can't be waived; it's #2132.
- **What's left for criterion 2:** one routing row (Q38) and three full texts. If Lead can't cite a ruling for Q38, routing is one row short on this run.
- **For xian:** both boxes would be met only after triage. The raw figures (88.5% and 46.3%) are what the product scored before anyone's judgment. That's the honest frame for "close enough".

#2129's PR label is served on `ac3c7581ff` (Web 19:22), so CXO closes it. The gate is unchanged: 6 open, 3 must-close.

Verified how: CXO's 19:22 memo read in full; recounted the 41 judged expected-pass rows of the 1839 CSV (19 PASS, 20 MARGINAL, FAIL Q17 and Q49); read Web's 19:22 and Lead's 19:20 memos.

-- PPM
