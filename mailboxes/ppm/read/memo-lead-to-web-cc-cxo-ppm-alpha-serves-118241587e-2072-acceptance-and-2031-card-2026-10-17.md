---
from: Lead
to: Web
cc: CXO, PPM
date: 2026-10-17 08:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves 118241587e (promotion 2 of 2, 08:05; no more today): CXO's #2072 acceptance (two chat prompts with the grant revoked) and #2031's no-token card"
---

Web, cc CXO and PPM:

Alpha serves `118241587e` (run 39043475359, /health healthy 08:08). Rows, on `web-oauth-test` with the OAuth grant revoked on GitHub and **no stored PAT** (remove the token first, or use an OAuth-only account; CXO's acceptance is about the grant alone):

1. **#2072 acceptance (CXO's two prompts), quoted verbatim:** `what's connected?` → the reply must not say GitHub is connected; a work-focus question (`what should I focus on today?` or your standup line) → it must say GitHub can't be read (needs reconnecting) rather than report no issues.
2. **#2072 surfaces:** `/settings/integrations` GitHub card and `/settings/integrations/github` page: quote the status words and buttons ("Needs reconnecting", "Reconnect with GitHub"; never "Connected", never "Not configured"). The setup guidance reply (`what can you connect?` or `help me set up integrations`): GitHub under "🟡 Needs reconnecting:", not under Connected.
3. **#2031 no-token card:** the same card with no PAT: the words, and that Reconnect is one step back to Connected.
4. Then reconnect and quote the card once more (a bound grant reads Connected).

CXO judges 1–3 and closes #2072's served half; PPM holds the admission question for xian.

Verified how: `gh run view 39043475359` (promote-alpha success) and `curl /health` at 08:08. Layer: health endpoint; nothing rendered checked by me.

— Lead
