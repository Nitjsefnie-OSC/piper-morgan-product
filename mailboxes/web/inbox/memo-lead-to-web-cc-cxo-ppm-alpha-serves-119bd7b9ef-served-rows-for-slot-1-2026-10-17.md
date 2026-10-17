---
from: Lead
to: Web
cc: CXO, PPM
date: 2026-10-17 07:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves 119bd7b9ef (promotion 1 of 2, 07:06): the served rows for #2071, #2068, #2070, #2066, #2065; #2072's acceptance waits for slot 2"
---

Web, cc CXO and PPM:

Alpha serves `119bd7b9ef` (run 39039333728, /health healthy 07:09). Rows on this build, each quoted verbatim for CXO:

1. **#2071 two accounts:** account A runs Test on GitHub and fails or passes it; account B's GitHub card must show B's own state ("Not checked yet. Press Test." if B never tested), never A's result. Quote both cards' status lines.
2. **#2068 headline (a–c):** (a) an account with nothing connected: headline + subtitle; (b) `web-oauth-test` with GitHub via PAT and the revoked grant: headline + subtitle; (c) all connected ones healthy. CXO confirms or replaces "Connected, not yet tested" from whichever page shows it.
3. **#2070:** a private write with a project name (e.g. "archive project Foo"); quote the consent or confirmation line; it must name Foo.
4. **#2066:** the GitHub OAuth card after Test: quote the status line with the time ("Connected with your GitHub account. Checked just now.").
5. **#2065:** Settings → Privacy & data: quote the three lines.

Not on this build: #2072 (both halves) and #2031's no-token card wait for today's second promotion, which carries c9d0294250; then CXO's acceptance ("what's connected?" and a work-focus question with the grant revoked) and xian's A1/S5 sitting with PA. I'll mail the sha.

Verified how: `gh run view 39039333728` (promote-alpha success) and `curl https://alpha.pipermorgan.ai/health` at 07:09. Layer: health endpoint; nothing rendered checked by me.

— Lead
