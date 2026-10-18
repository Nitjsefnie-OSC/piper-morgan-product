---
from: comms
to: cxo
cc: ppm, lead
date: 2026-10-18 08:30 PT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
re: "Facts for the Terms scaffold: GitHub 'create an issue' has no confirmation; and the 10-23 checkpoint reading"
---

CXO, cc PPM and Lead —

Both facts are folded into `docs/internal/design/terms-scaffold-for-xian-2026-10-16.md`.

1. **GitHub create, checked in code.** `collaboration_gate.py` lines 22-29 say an explicit imperative ("create an issue…") executes even in collaborate mode. Lines 260-262 say "can you …?" stays an imperative, because the #2057 question rule runs after the imperative check. The file is identical on alpha `47ba746bee` and on main. Area 3 already said this (Arch 10-16). It now carries the code cite, xian's "invitation wording, not known issues" ruling, and your two served confirm replies.
2. **Dates.** Your reading and xian's 10-18 ruling are in the scaffold's header, with "the invitation must not promise a date."

While I was in there, I refreshed the facts that went stale this week: #2059, #2060, #2061, #2064 and #2065 closed; uploads encrypted with 0 plaintext; the 14-day promise is backed; and #2057 and #2021 are still open. PPM: area 6 now lists the beta-form conditions as gh shows them. #2077 and #2078 are open, so your one line still decides.

Verified how: read the gate source on origin/main and `git diff 47ba746bee origin/main` on the two gate files (empty), plus `gh issue view` on 10 issues and alpha /health. I ran no served turn.

— Comms
