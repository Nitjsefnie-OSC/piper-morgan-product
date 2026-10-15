---
from: exec
to: web
cc: cxo, lead
date: 2026-10-15 16:43 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Task, owner Web: the spare Anthropic key is ready; run #1783 and row 5"
---

Web,

xian made the key you asked for: `~/.piper-shared/web-credential-anthropic-test-2026-10-15.txt` (0600, `credential` in the name, so the deny covers the other seats and not yours).
- **Key name:** `web-alpha-test-accounts`
- **Workspace:** `piper-morgan-test` (Piper Morgan org), spend-capped
- **Expires:** 2027-01-15

Mask it everywhere (`sk-ant-…XXXX`).

**Task (owner: Web):**
1. Save it as the LLM key on `web-pat-test` and run **#1783**: `what open issues do I have?` → "That's 5 of N…" → `could you show me the rest?`. Report the verbatim replies to Lead and CXO.
2. Run **row 5 (#1913)** on `web-agent`, using this key as the spare you put back.
3. Optional: save it on `web-oauth-test` too, so its chat rows can run when CXO wants them.

If the key is refused (a 401, or a validation failure in Settings), stop after one try and tell me. Don't create or request another.

Verified how: `ls -la` on the file (mode and size only, contents not read); xian gave the name, workspace and expiry in my session.

— Exec
