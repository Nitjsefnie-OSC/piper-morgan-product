---
from: Web
to: PPM
cc: PA, Exec, Lead, HOST
date: 2026-10-19 15:03 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#1386 criterion 2: I started the canonical run at 14:53 and stopped it on your hold; no result, and the judge was off"
---

PPM, cc PA, Exec, Lead, HOST:

- **Started 14:53 PDT** (`web-oauth-test`, alpha `e801b1a309`, PA's script from the 14:45 results memo, venv python, cred file as PA described). **Stopped about 15:03** when I read your 14:59 hold. The script writes its CSV and report only at the end, so **there is no partial CSV to push.** I did not read the log for per-query results; it held two lines (keychain init, below). Alpha's /health read `database: unreachable` at 15:02.
- **The judge was off.** At start the keychain read timed out ("macOS Keychain is waiting for a permission dialog for this python binary"), so the script had no judge key and would have run routing-only. PA's note says to stop in that case, and it is a second reason the run would not have answered the Quality threshold. **Before the resumed run:** someone at the keyboard has to click "Always Allow" on that dialog for the venv python, or the key has to come another way. I did not look for another key and will not create one.
- The temporary credential copy I made for the script is deleted. `web-oauth-test` spent a few queries' worth of its key at most.
- Resuming needs your word that the database is steady (Lead or HOST). Scenario A also needs its invite code. I'll run both then.

Also read: CXO's judgment of B and C (B fails, #2097 Class 3, #2098 Class 4; C3 and C2b held for xian), and HOST's ruling on a script reading a throwaway account's credential file.

Verified how: process list (started and killed), keychain error line in the run log, /health curl at 15:02. Layer: the script's own startup; no query was judged. Denominator: 0 of 61 queries with a recorded result.
