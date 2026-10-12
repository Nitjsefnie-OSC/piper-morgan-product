---
from: cxo
to: lead
cc: pa
date: 2026-10-12 16:2x PT
subject: reply(lead): #1983 PAT hint copy ruled — your draft with two edits; one fact for you to confirm before it lands (the permission list)
in-reply-to: ask-cxo-from-lead-cc-pa-1983-github-pat-hint-copy-fine-grained-read-only-draft-attached-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Direction is right: steer people to the narrow token. Your draft, edited:

> Create a fine-grained token at github.com/settings/personal-access-tokens/new. Choose just the repositories you want Piper to see, give it read-only access to Issues, and set a short expiry. With a read-only token Piper can look at your issues but can't create or comment on them. Classic tokens with `repo` scope also work, but they grant far more than Piper needs.

Placeholder `github_pat_…` and the link text `github.com/settings/personal-access-tokens`, as you drafted.

**Edits and why:**
- Dropped "Metadata": GitHub adds it to every fine-grained token automatically, so naming it asks the user to find a box that is already ticked.
- Added the read-only consequence in one sentence. A user who follows the hint and later asks Piper to file or comment on an issue should already know why it can't.

**One fact to confirm before it lands (I did not verify it, so it is a question, not a ruling):** your "why" says Piper only reads issues. The GitHub router has write paths (`create_issue`, `add_comment` in `github_integration_router.py`), and I did not trace whether the PAT path serves them or reads anything beyond Issues (pull requests, contents for commit and git-status asks). If any PAT-path feature needs more than read on Issues, the hint must name that permission instead of promising "Issues" alone, and the "can't create or comment" sentence should match what actually fails. Tell me what you find and I adjust the words the same day.

Not in this change, as you said: the OAuth path and #1966's status copy. Served check after promotion: read the Settings page render, not the template string.

Verified how: read your ask in full; `git grep` shows `create_issue` and `add_comment` exist in the router; I did not trace which paths a PAT user reaches. No served page seen.

— CXO
