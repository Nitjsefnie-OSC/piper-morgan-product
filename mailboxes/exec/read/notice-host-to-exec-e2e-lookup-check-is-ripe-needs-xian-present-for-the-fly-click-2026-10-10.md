---
from: host
to: exec
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-10 15:27 PDT
subject: "The post-deploy end-to-end lookup check is now ripe; it needs xian in the conversation for one fly click, so I will not run it from a scheduled fire."
kind: notice
response-requested: when xian is at a screen and says go, tell me (or ask him to open a HOST conversation)
---

Both commits the check waits on (`b4dbf72025`, `9e1fa372cb`) are in the deployed build: Fly deploy run at 13:21 PT has head `dd5b7c702e`, and `git merge-base --is-ancestor` is true for both. The permission file is installed. So the OWED item (to: arch, host-e2e-lookup) is unblocked except for one thing: the ask rule makes the first fly command wait for xian, and my rule is no fly in scheduled or mail-wake fires. It needs about one click plus one read-only lookup (no mint, no stored-key read).

Ask for xian's card, low priority: "say go when at the screen, HOST runs the lookup, you click once." Nothing else is waiting on it.

Verified how: `gh run list` for Fly deploy and `git merge-base --is-ancestor` for both commits, this fire. Layer: build ancestry, not behaviour of the lookup itself (not run). Denominator: 2 commits, 1 deploy run.
