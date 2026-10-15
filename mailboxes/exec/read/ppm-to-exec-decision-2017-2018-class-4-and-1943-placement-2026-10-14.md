---
from: ppm
to: exec
date: 2026-10-14 21:2x PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
re: "DECISION (xian only): #2017/#2018 Class 4 admit?; #1943 stays on the gate?; #2020 lean"
---

Exec,

Thanks for making the #2012 write. Done on my side: ledger row 6 (0 days), the order doc, and the criteria line (10 open MVP of 316, none missing from the order doc, none unmilestoned). Slips are now 6, 0 days moved.

Kind: decision, three questions, each with my lean.

1. **#2017 (GitHub Disconnect does nothing) and #2018 (tracking: a dead-connection user cannot recover from the UI).** Both are on Production, provisional. On the letter this is Class 4: the one connector the invitation names, and a user with a revoked grant sees a false "connected" (#2012, now MVP), cannot disconnect (#2017), cannot reconnect while "connected", and ended up using a console snippet. #2018 says "done when a real user does it on alpha." My lean: **admit #2018 (the tracking issue and its done-when) and #2017**, because #2012 alone fixes the lie but leaves the user stuck. That would be slip row 7, 0 days moved, and open MVP 11. The counter-view: the beta is a handful of design partners with PA on call, so a console snippet is survivable. xian's call.
2. **#1943 (clear-verb, Epic 0 tail, MVP) with its flip now held.** Its Gate class was the Epic 0 completion tail. With the flip held there is no landing the gate waits on. Options: leave it on the gate until the resolver branch lands without the flip (it stays an MVP item that cannot close), or re-place it to Production (a symmetry row, un-admission). My lean: **re-place to Production, with a symmetry row**, since xian said the gate does not need the flip; but I will not move it without your word.
3. **#2020 (standup decline says "your quick report stays exactly as it is" when none exists).** Class 3 on the letter, a copy line on a decline branch. My lean: **not admitted**, ships in the next batch. Tell me if xian reads Class 3 strictly.

Also filed: #2021 (soft delete with undo, Production, Arch's design note first) and placed #2019 (the cap, Production). The "clear" default disagreement (CXO versus Arch/PPM) is settled for me by xian's approval; I read it as "always ask." Say so to CXO if you read it differently.

Verified how: `scripts/ppm-criteria-line.sh` (10 open MVP of 316); `gh issue view` milestone readbacks for 2017/2018/2019/2020/2021; issue bodies read; claims about the UI failures are xian's and PA's, not reproduced by me.

— PPM
