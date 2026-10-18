---
from: Web
to: Lead
cc: CXO, PPM, PA
date: 2026-10-18 06:51 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
re: "served rows on 47ba746bee"
---

Served rows on alpha `47ba746bee` (/health read 06:18 PT, same sha). One FAIL (#2069), the rest pass. #2078 is not run: it needs HOST's invite file name.

**#2069 wording (a): FAIL.** Account web-fresh-test, fresh chat.
- `Add a project called Baz with description Quarterly planning notes` → "Added Baz with description Quarterly planning notes to your portfolio. If you want a GitHub repo on it, say: link [owner/repo] to Baz with description Quarterly planning notes." `GET /api/v1/projects` → name `Baz with description Quarterly planning notes`, description `""`. Same as the 10-16 report; the description is still inside the name, and the reply still claims it.
- `Add a project called Quux, description: weekly status` → stored name `Quux, description: weekly status`, description `""`.
- `Add a project called Qux with description Sprint retro notes for the team` → "I can add a project — I just need its name in the same message. Say: add project [name] with repo [owner/repo] …" (no add).
- The fix commit `4e7996a871` is an ancestor of `47ba746bee`, so the build should carry it. I did not find why the served path skips it; the intent cache keys by message text and my texts were new, so a stale cache entry is unlikely.

**#2076: PASS (both prompts, then reconnect).** web-oauth-test (OAuth-only), grant revoked on the machine GitHub account.
- `what should I focus on today?` → "I can't read your GitHub right now (it needs reconnecting), so this leaves out your issues and pull requests. Today: Nothing due today and nothing overdue. …"
- `give me my standup` → "I can't read your GitHub right now (it needs reconnecting), so I have no activity from it. Want to do a quick guided standup interview instead? (yes/no)"
- After reconnecting through the page, `what should I focus on today?` → "Today: Nothing due today and nothing overdue. …" with no GitHub sentence.

**#2075: PASS.** web-oauth-test, Settings → Integrations, OAuth-bound. Before a Test: "Connected, not yet tested", "0 of 1 checked"; GitHub row "Connected with your GitHub account." After Test All Connections: "All Systems Healthy", "1 of 1 connected integrations working"; the row adds "Checked just now." After the revoke, the page read "Needs attention", "GitHub no longer accepts your connection.", "Reconnect with GitHub".

**#2080 chain: PASS.** web-fresh-test (no projects), fresh chat: `list my projects` → "You don't have any active projects yet. Would you like to add a project?"; `Yes` → "What would you like to call it?"; `Piper Morgan` → "Add a project called "Piper Morgan"? (yes/no)" (one question); `Yes` → "Added Piper Morgan to your portfolio. If you want a GitHub repo on it, say: link [owner/repo] to Piper Morgan." The projects API lists Piper Morgan. No "want me to create…" offer on any turn.
- **Decline: partly run.** `What's next` at the name prompt did not reach the confirm; Piper took it as not-a-name ("Picking up where we left off … What's the name?"). Then `no` → "Okay — I haven't added a project. Nothing was created." So that was the name-stage decline, not the confirm-arm line from PA's step 6. The confirm-arm decline ("Okay, I won't add that project. If you meant to ask me something, go ahead.") is not quoted. Still to run: a question-shaped name that does reach the confirm.

**#2051 alias: PASS.** web-pat-test: `what issues are assigned to me?` → "You have 9 open issues. … #9: test issue 9 … That's 5 of 9 — say the word and I'll pull the rest." (an answer, not an unknown-action error).

**#2079: PASS for the morning quote only.** web-pat-test (signed in through /login), 06:50 PT: `give me a standup` → "Good morning! Yesterday — what got done …". The afternoon and evening quotes come after noon. I did not read the page header text.

**#2077: attribute only.** Settings → GitHub token field: `autocomplete="new-password"`, value length 0. My isolated browser has no saved-password manager, so the actual autofill check is xian's.

Verified how: real browser (isolated contexts), verbatim reply quotes, `GET /api/v1/projects` reads, DOM reads of the Integrations page. Layer: served alpha `47ba746bee`. Denominator: 7 of Lead's 9 rows run to a verdict; #2069 FAIL, #2078 and the confirm-arm decline not run, #2077 attribute only.

— Web
