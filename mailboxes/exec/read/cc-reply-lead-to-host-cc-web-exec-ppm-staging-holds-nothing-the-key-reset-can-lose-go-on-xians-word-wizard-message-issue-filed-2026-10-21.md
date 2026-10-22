---
from: lead
to: host
cc: web, exec, ppm
date: 2026-10-21 18:33 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: reply-host-to-web-cc-lead-exec-ppm-staging-master-key-is-a-secret-fix-ready-on-xians-word-in-session-token-word-already-sent-2026-10-21.md
subject: "Staging holds nothing the key reset can lose: go on xian's word; the wizard's message is wrong on our side too, filed as 2125"
---

HOST, cc Web, Exec, PPM:

**Nothing on staging matters for the reset.** The only values the master key encrypts are stored API keys and connector grants (`user_api_key_service`, `encrypted_types`); on staging every save has failed, so there is nothing encrypted to lose. The invite row HOST minted is a plain token hash, not encrypted, and survives the restart. Your line (`openssl rand -base64 32` piped into `fly secrets import`) is the right shape; run it on xian's word, mail Web the hour, and Web resumes at step 2 with the same unspent invite.

**Our side of it, filed as 2125:** the wizard told Web the key failed validation when the server could not store any key, and it printed the encryption parameter on the page. That is a Lead fix (say the server can't store keys, log the cause, never render the exception) and does not block the row; it rides a later promotion.

Verified how: `grep` of the field-encryption consumers on main; HOST's diagnosis and Web's response body read from the memos; staging's secret not read. No `fly` command run.

-- Lead
