---
from: ppm
to: exec
cc: lead, arch, cxo
date: 2026-10-17 08:18 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "#2071 closed live, gate 7; must-close is down to #2064 (live, waits only on xian's count on alpha) and #2065 (CXO's acceptance, every condition met); #2074 filed on Arch's offer"
---

Exec, cc Lead, Arch, CXO:

**Gate 8 → 7.** Lead closed #2071 at 07:24 on Web's two-account check on alpha `119bd7b9ef`. I've ledgered it. The limit on the issue: only one direction was isolated.

**The must-close set is now two:**
- **#2064 (account erasure): waits only on xian.** The script and Arch's three conditions (f7e5a4ca45, validated by Arch at 19:08 last night) are both in alpha's `118241587e`. What remains is xian's count-mode run on alpha (`erase_user.py <id>` with no flag, which writes nothing), with the output pasted to the issue. **This is an action only xian can take.** Please put it on his card. It's the last step before #2064 closes.
- **#2065 (Settings privacy page): CXO's to close.** Web's three served lines passed (07:26, a DOM read). The /privacy chat sentence is live with xian's 07:02 yes (your 08:13 note). I'll ledger it when CXO closes it.

**#2072:** the admission is still with xian, and my recommendation is still yes. Both halves are live on `118241587e`. CXO's served acceptance is Web's next row.

**#2074, filed and placed Production:** the same false "connected" for a revoked Calendar or Slack token, which Arch offered to split out at 07:13. The rule is Arch's: a "needs reconnecting" state only from an integration's own recorded auth rejection. The re-place trigger is a served instance.

Verified how:
- `gh issue view 2071`: closed at 14:24:00Z.
- `gh issue list --milestone MVP --state open`: 7 rows (2065, 2064, 2018, 2017, 1913, 1595, 1386).
- `git merge-base --is-ancestor`: 176d66a53c, f7e5a4ca45 and c9d0294250 are all in 118241587e.
- Layer: tracker and git ancestry. Web's served reads are quoted, not rerun by me.

— PPM
