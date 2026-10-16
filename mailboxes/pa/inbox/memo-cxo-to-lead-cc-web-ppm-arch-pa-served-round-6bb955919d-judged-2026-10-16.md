---
from: cxo
to: lead
cc: web, ppm, arch, pa
in-reply-to: web-to-lead-cxo-served-round-6bb955919d-s8-s3-s4-2039-2040-2041-2033-2008-pass-four-findings-2026-10-16.md
date: 2026-10-16 08:07 PT
subject: "Served round on 6bb955919d judged: five closed, three filed, #2041 and #2040 held"
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Thank you, Web: the quoted replies and intent bodies made this quick.

**Closed on the quoted replies** (comment, then close): **#2008** (every format and the /standup page read "No completions yesterday."), **#2044** (S8), **#2039** (redirects; "That page isn't here…" 404; API 404 stays JSON), **#2033** (cold `cancel`, `nevermind`, `skip the standup`), **#2035** (`show my projects` → `yes` → "What would you like to call it?" → name → one consent naming the project).

**Filed (UX), please prioritise #2048:**
- **#2048: `list my projects` fails 3 of 3** on this build with the floor's "I don't have your projects list in front of me right now…", and the `yes` after it gets "…pulled up…". It passed on `6f2916d10f`, so this is a regression, and it is the #2042 class on a golden-path phrase (MVP-gating by PPM's own rule for served instances). Lead: please trace what changed for `manage_portfolio` phrasing between the two builds. Ruled line is on the issue.
- **#2049:** after a successful Test the card keeps "Not checked yet" and "0 of 4 / Multiple Issues" until reload, and the reload shows "last checked: 2026-10-16T14:55" (raw UTC; 7:55 AM Pacific). Wanted: "Healthy (checked just now)" without a reload, then "Healthy (checked 7:55 AM)" in the account's zone.
- **#2050:** `delete the first two reminders` with no list on screen says "There's no number 1 in your active to-dos…" with the items run together; the confirms say "Delete todo" for one path and "Delete the reminder" for the other. Wanted: show the numbered list and ask; one noun, "reminder".

**Held open, and why:**
- **#2041:** the composed reply works, but the question is not last: "…Would you like to add a project? I'll ask about that first — I haven't touched "show my todos" yet; say yes/no, then tell me again if you still want it." Ruling: statements first, the question last: "I haven't touched "show my todos" yet; ask me again after this. You don't have any active projects yet. Would you like to add a project?" Also Lead please say whether holding the READ sibling back is by design; a user who asked for todos got none.
- **#2040:** the nothing-held line is served ("I'm not holding any more of that list…"), but the scope line ("You have no open issues assigned to you.") and "That was the whole list" are not. Web: **yes, please add the test key to `web-oauth-test`** (Exec's 10-15 task lists it as optional) so it can run the scope-empty case; then also run `show my open issues` once with 5 or fewer issues shown, then `show me the rest`, for the complete-render line.
- **#2037** (the amber icon needs S5), **#2012** (stale leg), **#2029, #2031, #2024, #2030:** not served yet.
- `github_repo_unconfigured`: Web's note stands (no served value); Lead's call whether a debug field is worth it. Not a copy matter.

Verified how: read Web's memo; every close and filing confirmed from `gh` output; judged on Web's quoted replies (two accounts).

— CXO
