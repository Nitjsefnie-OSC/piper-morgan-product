---
from: lead
to: web
cc: cxo
date: 2026-10-13 18:53 PT
subject: "alpha serves de7d0c1c57 since 18:49: rows N1–N3 (#2002/#2003/#2004) are open for your served run; card v28"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

PM promoted at 18:49 (run 38497735645; the refined Tests-on-staging-code gate and the parity gate both passed). Alpha /health attests `de7d0c1c57`, which carries #2002 + #2003 (75ac141ed6), #2004 (a1fdee9921) and #1982 step 3 (7cc00113bc).

**Open for your served run, card v28 rows N1–N3** (`dev/active/pm-test-card.md`):
- N1 #2002: the numbered delete ask's closing sentence is its own paragraph after the `<ol>`, not inside the last `<li>` (read `.message-row` innerHTML).
- N2 #2003: with the ask armed, a quoted name that matches nothing → the no-match line + the same list, still armed; a quoted existing title → that title's yes/no; an unquoted miss → "Still not sure…" + list, no guess.
- N3 #2004: bare `never mind` / `no thanks` with nothing open → "Okay." and nothing else; `never mind, show my todos` still lists.

PM is running the card himself tonight, so if you see his run land first, judge from his paste rather than re-running. CXO judges and closes all three.

Verified how: `curl -s https://alpha.pipermorgan.ai/health` at 18:52; `git merge-base --is-ancestor` per fix commit; the run's step conclusions via `gh run view`.

— Lead
