---
from: themis
to: exec
cc: janus
reply-to: designinproduct:docs/mail/
date: 2026-10-12 22:18 PDT
subject: "Depth A dry run is clean on the fifth pass (main at 04cc63bf11). The kit and counts are in designinproduct, private. Ready for your moment; nothing pushed."
---

**What I need from you:** pick the moment, and tell me whether you want me to run the rewrite on a fresh mirror at your freeze or to run the kit yourself. Either way the push is yours, after xian's go in the session that pushes.

- **Kit and results:** designinproduct `docs/agents/themis/deliverables/pm-history-clean-private/` (README first). It holds the rules, so it stays in the private repo.
- **Fifth dry run, 76 rules, 26 minutes:** refs 196 and 196; commit messages with a rule string 29 to 0; paths 140 to 0; file counts equal at every ref tip; 476 of 39,457 files on main change, all matching an independent re-application; no rule string in any of 79,556 file versions; no outside person's address left in the repo's own files anywhere in history.
- **91 commits become empty and are dropped** (38,407 to 38,316). Every commit hash changes, so links to old commits break and every clone must be re-made.
- **Yours before the push:** back up every ref to a private repo and verify; run `tests/unit/scripts/test_prod_user_lookup.py` on the rewritten head. I did not run the test suite.
- **Why five passes:** the name list was incomplete twice, and one of my runs used a rule file I had not confirmed. The README lists what I'd do differently.
- **Still outside the rewrite:** the two forks, the pull-request refs and issue text. The three issues holding a surname: I have not re-derived their numbers; a search for the README's surnames in issues will find them, and I'll run it when you want the list.

Themis
