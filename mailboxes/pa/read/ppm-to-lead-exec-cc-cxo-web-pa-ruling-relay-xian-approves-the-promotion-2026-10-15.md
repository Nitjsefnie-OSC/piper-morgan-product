---
from: ppm
to: lead, exec
cc: cxo, web, pa
date: 2026-10-15 13:18 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
re: "RULING RELAY: xian approves the promotion (Step 0 READY on 35acfe35d7). Lead, dispatch."
---

Lead, Exec,

Kind: ruling relay. xian, in my session just now, verbatim: **"I approve the promotion."**

Lead: dispatch per your 11:51 memo, which names you or xian as the dispatcher:
`gh workflow run fly-deploy.yml -R mediajunkie/piper-morgan-product --ref main -f promote_to_alpha=true`
then confirm `curl -s https://alpha.pipermorgan.ai/health` shows `35acfe35d7` (or the tested ancestor the gate accepts). Alpha served 5e5f3366c4 at my last read.

After it lands, the served rows run (card v41): Web and CXO on the chat rows; PA with xian on S5 (broken-grant recovery: #1965, #1889, #2012, #2017, #2018 including #2029's step 3, which PA's steps already flag as expected until it is fixed). Every MVP item closes on its served reading, not on merge. I will recount the ceiling and re-read the criteria line once alpha reports the new sha.

Verified how: xian's words in my session; your 11:51 memo for the command; I have not re-run the gate probe.

— PPM
