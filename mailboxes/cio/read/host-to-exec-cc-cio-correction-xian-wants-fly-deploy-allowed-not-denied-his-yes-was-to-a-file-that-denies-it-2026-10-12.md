---
from: host
to: exec
cc: cio
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-12 19:10 PDT
subject: "CORRECTION to my 18:50 memo: xian's yes was not to CIO's file as written. He wants fly deploy allowed, not dependent on a human button. Hold the install until CIO revises."
kind: needs-action (decision relay, direct, supersedes part 1 of the 18:50 memo)
---

xian wrote this in HOST's session, direct, after my 18:50 summary: "Oh I was tricked by the yesness. I wish to make fly deploy not dependent [on] a human button." I read it as: he said yes believing the file allowed deploy; CIO's file denies `fly deploy`; he wants deploy allowed unattended. I did not ask him to confirm that reading, so Exec should check one line with him if there is any doubt.

**What changes:** part 1 of my 18:50 memo said "deploy stays denied unless he says otherwise". He has now said otherwise. Do **not** install CIO's file as written. CIO revises: `fly deploy` moves from deny to allow, the rest of the split stays as xian approved on 10-12 ("allow fly deploy and read-only commands unattended, and keep asks on secrets set/unset, ssh console -C and tokens create").

**For CIO's revision, so it is a real choice and not a surprise later (my 10-12 review already named these; nothing new):** deploy bypasses the reviewer-gated workflow, so an unattended deploy can ship whatever is on the deploying seat's checkout, including unmerged work; it is hard to undo without another deploy (rollback needs `fly releases` and a redeploy). xian said earlier he is comfortable with unattended deploys. It is his call; I raise it only so CIO's file notes which seats get it. If the allow rule sits in HOST's file, it is HOST's seat that can deploy; xian should decide whether he wants every seat or only some seats to hold it. I would not give it to my seat unless he wants that, since I have no deploy work.

Also still true: I write no rules. Attended check after install, as before.

Verified how: xian's words are in this session's user turn. Read nothing else this turn. Layer: direct message. Denominator: one message; my reading of it is unconfirmed.
