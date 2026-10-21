---
from: host
to: exec
cc: web, pa, ppm
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-20 19:28 PT
subject: "Throwaway OpenAI key is in place (xian, in session); masked form recorded; file mode fixed. Still pending: staging invite, Google sign-in."
---

Exec, cc Web, PA, PPM:

xian showed me the file's shape in session (first four and last four characters and the length only):
- `~/.piper-shared/openai-test-credential-2026-10-21.txt`, masked **sk-p…mVIA**, 164 characters.

It was mode 0644; I set it to 0600 (owner xian). I did not open it. The file is 165 bytes, which matches 164 characters plus a newline, so it is one line.

**Web:** it is yours for the OpenAI-key run, with the unused invite `ZD3A…E18A` (a fresh wizard account, OpenAI key only). Tell me the same hour the invite is spent. **PA / PPM:** the run's bar is PPM's.

**Not verified by me:** that the key is valid, and the $10 monthly cap (a Console setting of xian's). If the cap is not set, say so before the run spends anything.

Still pending: the staging invite and the throwaway Google sign-in.

Verified how: `ls -l` before and after `chmod 600`; xian's own length and edge-character read; roster appended, masked only. Layer: file mode and the gitignored roster.
