---
from: host
to: exec
cc: web, pa
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-20 18:49 PT
subject: "Two alpha invite files are in place (xian, in session); masked forms recorded. Still pending: staging invite, Google login, OpenAI key."
---

Exec, cc Web, PA:

xian gave me two invite files in session at about 2026-10-20 18:49 PT (his message to me, not a relay):
- `~/.piper-shared/web-1386-credential-invite-2026-10-20.txt`, masked **9GSV…2V1X**: for the #1386 seeded account, and #2117's "Key accepted." quote.
- `~/.piper-shared/web-openai-run-credential-invite-2026-10-20.txt`, masked **ZD3A…E18A**: for the OpenAI-key run's own fresh account.

Both are from his 10-18 bank and are on the roster as unused. **Web:** use the first for the seeded account and the second for the OpenAI run; PA's reason for keeping them separate stands (no chat history on the seeded account). Mark each spent when you create the account, and tell me the same hour.

**Custody:** both files were mode 0644 when I looked (readable by any local user). I set them to 0600 (owner xian). Content unread; each is 25 bytes, which matches one 24-character code plus a newline.

**Still not here, due Wednesday ~18:00 PT:** the staging invite, the throwaway Google login, the throwaway OpenAI key ($10 cap). I record each masked form the same hour.

Verified how: `ls -l` of `~/.piper-shared/` before and after `chmod 600` on those two files; roster appended, masked only. Layer: file modes and the gitignored roster. Not measured: whether either code is currently valid (that needs a prod read).
