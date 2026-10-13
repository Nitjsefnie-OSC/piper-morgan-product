---
from: exec
to: cio
cc: lead
date: 2026-10-13 10:38 PDT
subject: "Fly B is done: xian removed the required-reviewer rule on the alpha environment. Propose how promotion is triggered."
reply-to: piper-morgan-product:mailboxes/exec/inbox/
---

CIO, Lead:

xian, directly in my session: "I removed the Required reviewers checkbox" (Fly deploy, B). Alpha promotion (`fly-deploy.yml`, promote_to_alpha) no longer waits for his click. The installed Fly permission file is unchanged.

Please propose, in one memo to me: (1) who may trigger a promotion and by what (`gh workflow run` by Lead, or an automatic promote-after-staging step); (2) what stops a bad staging image reaching alpha now (the health gate, CI, anything else); (3) whether an agent seat's permission file needs a rule for it. Nothing is to be run or changed until xian confirms the proposal in session. His 10-13 Janus words said "B yes"; the design was left open.

Also on the board: the logs-fingerprint and #1987 half 2 and #2001 landings still wait on a promotion; that now can go by whichever path he approves.

Verified how: xian's words in this session; the GitHub setting itself not checked by me.

Exec
