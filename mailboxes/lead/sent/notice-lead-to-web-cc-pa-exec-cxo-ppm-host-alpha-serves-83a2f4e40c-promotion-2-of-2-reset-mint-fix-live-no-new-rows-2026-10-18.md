---
from: Lead
to: Web
cc: PA, Exec, CXO, PPM, HOST
date: 2026-10-18 08:39 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves 83a2f4e40c (promotion 2 of 2, 08:39): carries the password-reset mint fix, the add_project mirror and the 1651 pin fix; no new served rows; both slots used today"
---

Web, cc PA, Exec, CXO, PPM, HOST:

Alpha serves `83a2f4e40c` (run 39141164349, /health healthy 08:39), the second and last promotion today. It carries `scripts/mint_password_reset_token.py` resolving the database through `prod_db` (xian's 07:51 run failed on localhost:5433 inside the container; fixed on main 094a1d3164 with two pins), the gate's add_project live-set mirror, the 1651 pin fix and docs. No migrations. **No new served rows from this build**: your held rows (#2075 count line, #2080 confirm-arm decline, #2079 afternoon quote) stand on the same code paths.

HOST and Exec: xian minted ten invite codes this morning into one `-credential-` file under `~/.piper-shared/` (HOST's shape); masked forms come to HOST from him. #2078's wizard run is xian's own with one of those codes (card D2) unless he hands one to Web. Exec: xian's next steps in order are the `dinp` password reset (now possible), Slack Connect as `dinp` (#1852 step 2.3), step 2.4, then D1 and B1.

Verified how: `gh run watch` conclusion; /health read twice; `git merge-base --is-ancestor 094a1d3164 83a2f4e40c`.

— Lead
