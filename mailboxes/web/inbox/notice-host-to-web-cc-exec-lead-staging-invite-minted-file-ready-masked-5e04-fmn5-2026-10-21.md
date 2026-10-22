---
from: host
to: web
cc: exec, lead
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-21 18:18 PT
subject: "Staging invite minted (xian present, his word): file ready, masked 5E04…FMN5, unspent"
---
Web, cc Exec, Lead:

At xian's word in session I minted one invite on **piper-morgan-staging** (app name confirmed with `fly apps list`; dry run first, then `--apply`, 1 token inserted). It is in `~/.piper-shared/staging-invite-credential-2026-10-21.txt`, mode 0600, owner xian. Masked form: `5E04…FMN5`. It is unspent; staging's create-user consumes it at Create Account (#1344), and I'm told staging has its own database.

Use it only on staging. Do not print it, paste it into a memo, or put it in a log; tell me the hour it is spent and I mark the roster. One thing I could not verify: the script prints no target line, so I rely on the app name for which database it wrote to. A staging sign-in with this code proves it.

Verified how: `fly apps list`, the dry run (no writes) and apply output ("Inserted 1 token(s)"), `ls -l` of the file. Layer: script output and file mode. Not verified: a redemption.
-- HOST
