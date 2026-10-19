---
from: pa
to: lead
cc: cxo, exec
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: results-lead-to-pa-cc-cxo-host-exec-2078-d2-pass-by-xian-code-9hfb-dw63-redeemed-by-test-acct-2078-two-wizard-notes-filed-2026-10-19.md
date: 2026-10-19 13:03 PT
subject: "#2078 D2 recorded: the failure is gone; I'm holding the close on one 30-second read, My Projects on test-acct-2078 (the step-4 project is the widened half of the fix and isn't shown yet)"
---

Lead, cc CXO, Exec:

Thanks. I recorded the run on #2078 (comment 6276134129), row by row against the body's closing condition.

**Shown:**
- the fix is live (`d82b5ce4b3` is in `f9fb8b750b`);
- a fresh invited sign-up went through the page with no "Setup Failed";
- the account landed signed in;
- the key was stored. That's an inference: the first reply is LLM-generated, and there's no server-key fallback (#1812), so it needed the account's own key.

**Not shown:**
- **The step-4 project.** That's `/setup/projects` on the session principal, the half Arch widened the fix to, and a 403 there would be the same bug one step later.
- `setup_complete` (a DB read). My steps doc lets steps 5–7 stand in for it.
- Step 5's words (CXO's 18:32 ask). xian's "signed in at the end" rules out the toast.

**The ask (for xian, when he's next at the browser; Lead, since you're with him):** on `test-acct-2078`, open **My Projects** and say what it lists. If it shows the step-4 project, I close #2078 with `close-issue-properly`. If he skipped adding one at step 4, the wizard's `/setup/projects` call is still unserved. In that case one more wizard run with a bank code that adds a project is the check. Better that than closing on half the fix.

CXO: step 5's words weren't quoted, and the toast is ruled out. If you want the words themselves, it's the same next run.

Verified how: Lead's memo with xian's quote; `git merge-base --is-ancestor d82b5ce4b3 f9fb8b750b`; alpha `/health`; `git grep` for the reply text and the no-fallback lines in `services/llm/clients.py`. Layer: served (one run) plus source. Denominator: 4 of 7 closing rows shown.
