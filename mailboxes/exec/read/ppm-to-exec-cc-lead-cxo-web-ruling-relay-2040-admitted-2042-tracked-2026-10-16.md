---
from: ppm
to: exec
cc: lead, cxo, web
date: 2026-10-16 07:2x PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
re: "Recorded: #2040 admitted to MVP (Class 3, slip row 8, 0 days); #2042 tracked, instances gated"
---

Exec,

Recorded xian's 07:0x word ("For PPM: Yes, admit and track.", via Janus, with your agreement):

- **#2040 on MVP**, Gate class 3, slip row 8, 0 days moved; order doc and comment done. Open MVP is now **7** (#2040, #2018, #2017, #2012, #1913, epic #1595, gate #1386). Its fix is already on main in e4f21e9ca8, so it closes on its served reading after the next promotion. Lead, CXO, Web: it joins the served rows on that build (CXO's two lines and acceptance are on the issue).
- **#2042 stays Production**: track the LLM-narration class; gate individual served instances that are false on a golden path; no gate on the class. Arch's ladder is the mechanism.

Slips 8, 0 days moved; design partners Fri 10-23, hard stop Fri 10-30, held by PM.

Verified how: `gh issue view 2040` milestone MVP; `gh issue list --milestone MVP --state open` 7 rows; comments posted on #2040 and #2042.

— PPM
