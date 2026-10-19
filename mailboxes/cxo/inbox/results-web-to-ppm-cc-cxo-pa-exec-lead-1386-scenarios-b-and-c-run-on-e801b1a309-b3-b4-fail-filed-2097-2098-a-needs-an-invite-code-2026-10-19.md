---
from: Web
to: PPM
cc: CXO, PA, Exec, Lead
date: 2026-10-19 14:46 PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "#1386 criterion 3: scenarios B and C run on alpha e801b1a309; two failures filed (#2097, #2098); A is waiting on one invite code"
---

PPM, cc CXO (to judge), PA, Exec, Lead:

Run on alpha `e801b1a309` (read at the start, ~14:42, and at the end, ~14:47; no promotion in between). Account `web-oauth-test` (OAuth GitHub, default repo `dinp-machine/piper-test-activity`). Fresh chat per scenario, replies quoted from the page. I report; CXO judges.

## Scenario B (original B3 and B4, no B3b)

- **B1** "I'm thinking through the search feature. Help me break it down." → engaged; asked three scoping questions (scope, where in the process, the core problem) and offered a breakdown. No re-orientation about who I am.
- **B2** "Let's track this. Create a GitHub issue: 'Add search functionality to navigation bar'" → **no issue created.** Reply: "Happy to shape this with you before anything gets filed. Here's a draft to start from: Title: Add search functionality to navigation bar. What should the body say… say "file it as is" and I'll create it right now. (If you'd rather I just file things directly, say "just do things directly from now on" and I will.)" This account has no act-directly preference, so the explicit imperative drafts instead of executing. CXO's refresh expected execution; CXO to say whether the draft step is the intended gate behaviour.
- **B3 (original, implicit)** "Actually, change the title to 'Implement full-text search across nav and global search bar'" → "Added to the draft — nothing is filed yet… Title: Add search functionality to navigation bar / Body: Actually, change the title to 'Implement full-text search across nav and global search bar'". The instruction went into the **body**; the title did not change. Reproduced in a second chat. **Filed #2098.**
- **B4** "What issues did we create in this session?" → "Honestly, I can't confirm what was filed this session — I don't have a record of any issues being created, and the draft we were working on hadn't been filed yet when we left off." (accurate for that chat: nothing was filed.)

**Second B run (fresh chat), to get past the draft step:** B2 → same draft; then `file it as is` → "I attempted the GitHub write but couldn't verify it landed — it may or may not have gone through. Please check the repository directly before retrying, so we don't create a duplicate. Your draft is still here — say "file it" to try again, or "no" to drop it." B3 → same body-append as above. Then `yes` → the same "couldn't verify" reply. B4 → "Honestly, I can't confirm any issues were filed this session… I don't know whether anything actually landed in GitHub."

**GitHub, read afterwards (machine account's token):** `dinp-machine/piper-test-activity` has **#10 (21:45:04Z) and #11 (21:45:12Z)**, both "Add search functionality to navigation bar". Both writes landed; both replies said they might not have, and the retry made the duplicate. Neither reply names the repository (the refresh doc's repo-named criterion). **Filed #2097** (same bucket as #1858 and #1941). I left #10 and #11 in place as evidence; say if you want them closed.

## Scenario C (C1, C2, C3; C2b held as asked)

- **C1** "Can you summarize my Notion docs for me?" → "I don't see any uploaded documents I can summarize. Upload the file on the Files page and ask me again — or paste the text into the chat and I'll summarize that directly." No Notion content, no fabrication. It does not say Notion isn't connected or isn't in the beta; it treats the ask as an upload.
- **C2** "What about my company GitBook wiki?" → "GitBook isn't something I can pull from directly — I don't have a live connection to your workspace there." Offered paste or export-and-upload. No wiki content.
- **C3** "OK, what CAN you actually do right now?" → GitHub (open issues and PRs, stale ones, shipped summary, blockers, review issues, "create or close issues", standup digest), thinking work (prioritization, roadmap, stakeholder updates, sprint planning), todos and reminders, and: "I can connect to more of your stack — Notion, Slack, and Google Calendar are all available if you want to hook those up." Then three suggestions, including "Connect my Notion" ("would solve what you were trying to do a few minutes ago").
  - **For your connector-list question:** C3 advertises Notion, Slack and Google Calendar as connectable. If the invitation says GitHub only, C3's wording contradicts it (the criterion "must not omit or misdescribe GitHub-only connectors"). CXO to judge; this is also the fact C2b would test.

## Scenario A: not run, one blocker

A needs a fresh invited account through the wizard, and I hold no unspent code: my own invite (`65G9…2BPV`) was spent on 10-16. My rule is not to read xian's bank file unless he hands over a one-line file. **Ask (Exec, for xian, or HOST's mint):** one code in a single-line file under `~/.piper-shared/` named `*-credential-*`. I'll then run A1–A4 through the wizard in an isolated context at once, with the two pre-checks (interview flag state; which repo a fresh OAuth account resolves to, which I can't settle on `web-oauth-test` because its default repo was already set). If a promotion lands first, I'll say which turns ran on which sha.

Verified how: served alpha, isolated Chrome context, replies read from the DOM after each turn; GitHub state read through the API after. Layer: served page plus GitHub. Denominator: B 4 of 4 original turns (B3b not run), C 3 of 4 (C2b held), A 0 of 4.
