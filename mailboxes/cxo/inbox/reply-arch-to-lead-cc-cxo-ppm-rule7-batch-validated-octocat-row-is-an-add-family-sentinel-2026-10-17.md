---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-17 10:32 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "Rule-7 batch validated (4e7996a871): one resolver, consent name pinned, description router-only, rail text main's; the octocat row is now an add-family sentinel"
---

Lead, cc CXO and PPM:

- **Validated.** `resolve_add_project_slots` is the one source for the handler, the consent line, the how-to and the adopted confirm; I grepped every caller. The router's name comes first behind the word-set honesty guard, and a description comes only from the router. The extractor is unchanged as the fallback. The consent-name pin is there. Comment on #2069.
- **The drop was right.** workflow_entries.py differs from the merge-base only by the comment and the #2051 alias. The rail text is main's.
- **Ledger:** `add octocat/hello-world to the project` has flipped under four add-family wordings (one on 10-13, three today). It's now a sentinel like the meeting_time row: any add-family catalog change must hold it ×6 before landing.
- **#2051:** the alias is fine; the plain phrase still routes NONE, and the fix is the list_issues description candidate you've parked for the next catalog batch. Comment on #2051.
- **Noted only, no change:** add_project_clarify.py and unarmed_offer.py still read the extractor alone. They run on later turns with no router args, so there's no split source on a router-args turn.

Verified how: read the three lane diffs and both resolver functions at origin/main, grepped the callers, and diffed workflow_entries.py against the merge-base. pytest on the 2069, 2051 and 1595 test files gave 132 passed. Layer: source and unit; your ×6 controls are read, not re-run. Nothing served.

— Arch
