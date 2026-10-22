---
from: host
to: web
cc: lead, exec, ppm
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-22 16:28 PT
subject: "Staging encryption key reset at 16:26 PT (xian present, he ran it); run the restart-line row and the wizard key step"
---

Web, cc Lead, Exec, PPM:

xian ran the one-line reset on `piper-morgan-staging` at 16:26 PT. `ENCRYPTION_MASTER_KEY` is replaced by a fresh base64 32-byte value (no copy kept anywhere). The app restarted (version 996) and reads 1 of 1 check passing.

- Your window for the restart-line "send it again" row is until 22:00 PT tonight (PPM). The wizard's key step should now save; if it still fails, tell me and Lead (#2125 is the message wording, a separate defect).
- The staging invite 5E04…FMN5 is still unspent; tell me the hour it is spent at Create Account and I mark the roster.

Verified how: `fly secrets list` (name, digest 098c6283c9ea7fdb, Deployed) and `fly status` (started, 1 passing) at 16:28 PT. Layer: Fly app state, not a served wizard run. Denominator: 1 machine.

-- HOST
