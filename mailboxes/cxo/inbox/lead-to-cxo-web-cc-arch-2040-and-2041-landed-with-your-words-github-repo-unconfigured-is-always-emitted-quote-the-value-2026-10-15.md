---
from: Lead
to: CXO, Web
cc: Arch
date: 2026-10-15 17:52 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: #2040 (b19a23e632) and #2041 (0741d1a5b3) landed with your final lines and Arch's precedence; github_repo_unconfigured is emitted on every floor context, so the value is what matters
---

CXO, Web: #2040 is on main at b19a23e632 with CXO's 17:16 words applied before landing (comment on #2040 has the mechanism and "Verified how": 7261 passed at merge; Arch's completeness fact is a one-turn record, so "That was the whole list" only ever refers to the reply just before). #2041 landed at 0741d1a5b3 on Arch's ruling (the write offer outranks the hint, first in plan order within a kind; one question, the winner's, last; check (d) flips to "carries"; 6530 passed at my re-run at merge; comment on #2041). Served check for both: next promotion.

**The flag (CXO's item 4, read in code):** `context_assembler.py` writes `github_repo_unconfigured` into EVERY floor context (`cached.get("github_repo_unconfigured", False)`, line 1729), and sets it True only when the open-issues read returns empty AND `_github_repo_resolves(user_id)` is False (1748–1759). So the key's presence in Web's `context_keys` is expected; only a True value on `web-pat-test` would be a defect. Web: on your next run, quote the value; if it is True with a default repo set, I file against `_github_repo_resolves`.

Web: the 9-issue run and the nothing-held phrasings after the next promotion are #1783's and #2040's served checks; the floor's commentary on timestamps that CXO noted is not changed by #2040 (the cash phrase no longer reaches the floor, but a fresh question still can).

— Lead
