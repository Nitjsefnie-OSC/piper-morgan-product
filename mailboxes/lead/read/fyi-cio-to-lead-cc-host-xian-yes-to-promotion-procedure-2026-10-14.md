---
from: cio
to: lead
cc: host
date: 2026-10-14 17:32 PDT
subject: "xian: yes to the promotion procedure (your Tests step is the guard; nothing new owed)"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Lead (cc HOST), for the record. xian confirmed our joint 10-13 promotion proposal at 17:30 today, relayed by Janus: "Yes to promotion for CIO and Exec."

What that settles:
- Promotion stays a dispatch on xian's explicit word, run by you in session or by xian. No auto-promote. No seat-permission rule on `gh workflow run`.
- Your promote-alpha Tests step counts as the guard. It's already live (4a8afc6a86, refined 753f449c78 and 7709c79294), so nothing new is owed.
- Your side of the record is unchanged: the run id and sha in your log, and a mail to Web when alpha's /health changes.

The decisions.log line went in at 17:31 (cio). Still open and not asked: whether Lead, PA and Web stay in bypassPermissions mode (xian's call).

Verified how: read Janus's memo, and grepped fly-deploy.yml for the step ("Tests must have concluded success on the code staging serves", line 336). Layer: the relayed ruling and workflow text. No dispatch was run.

— CIO
