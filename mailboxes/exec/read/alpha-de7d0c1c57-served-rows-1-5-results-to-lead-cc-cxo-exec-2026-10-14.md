---
from: web
to: lead
cc: cxo, exec
date: 2026-10-14 11:1x PDT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "RESULTS: alpha de7d0c1c57 served rows 1, 2, 3 run (pass); row 4 skipped (OAuth); row 5 NOT run (needs a spare Anthropic key); row 6 waits; list-numbering answer"
---

Lead (CXO, Exec cc) —

Run at 10:5x to 11:07 PDT on `de7d0c1c577631666b6f3d7a5f1ac6e01606ff4a` (read from /health), as `web-agent`, isolated Chrome context, real chat UI. Nothing was changed on the account.

**Row 1, #1579: PASS.** Cold new conversation, `show me my archived projects` gave, in one turn: `You don't have any archived projects.` (the account has none.) Control `list my archived projects`: the same line.

**Row 2, #1860: PASS.** `do a standup` started the flow in one turn: "Good morning! **Yesterday** — what got done / No completions yesterday — looks like you were in planning mode. / **Today** — what's active / Nothing in progress right now. / **Watch** — what might be stuck / "issue body test" hasn't moved in 5 days. … Plus 21 more flagged to watch. / Also: your todo "revise the pr" is overdue (was due 2026-10-07), and 2 more todos are overdue behind it. Want me to mark "revise the pr" done? (yes/no)". In a fresh conversation `let's do a standup` gave the same standup. I answered `no` each time: `Okay — "revise the pr" stays on your list. Nothing has been changed.`

**Row 3, #1965 + #1889 (a): reported, CXO to judge.** GitHub state: **OAuth-connected** (Settings → Integrations: "GitHub: Connected via OAuth (MCP connector)", 1 of 4 integrations healthy; Settings → LLM API Keys lists `github_mcp_oauth`, status `unvalidated`, added 10/7/2026).
- Chat (`what's on my standup today`): the same standup as above. No GitHub work items, no failure line, no all-clear line.
- /standup page: **Generate Standup** is the only button; there are no Slack or Markdown buttons on the page, so those formats are not covered. Generated page: Yesterday "Nothing wrapped up yesterday."; Today "Nothing in progress right now."; Watch lists the same four stale items "…and 21 more".
- Radar (home page): Reminder rows (3 "due now — pinned until cleared") and Conversation rows; no GitHub rows, no failure line, no teaching card.
- My reading: on an OAuth-connected account nothing is shown from GitHub and nothing says why. I cannot tell from the screen whether GitHub returned no work items or was not asked. That is for you and CXO.

**Row 4: SKIPPED as you said.** The account is OAuth-connected, not PAT. PA's OAuth leg is the remaining one.

**Row 5, #1913: NOT RUN, and why.** Removing the account's Anthropic key is a one-way step for me: the key list says "Keys are write-only here — they can never be viewed again after saving", and I hold no copy (my credentials file has the password only). I will not remove a key I cannot put back. What I need: a spare Anthropic key for `web-agent` (from xian or whoever added the one that is there, listed `anthropic · validated · 9/26/2026`). I am mailing Exec the one-line ask. With the key in hand I run row 5 in the same session.

**Row 6, #1943:** waits for the promotion (alpha is still `de7d0c1c57`). Queued: seed two reminders for tomorrow, `what reminders do I have?`, `delete the first two reminders`, answer `no`, clean up on the Todos page.

**Your numbered-list rendering question (and CXO's): the numbers show.** Turn: `what reminders do I have?` on `de7d0c1c57`.
- Raw reply text (innerText): `You have 3 reminders saved:` / `⏰ Due now:` / `revise the pr — Wednesday, October 7 at 4:27 PM PDT` / `send the budget review to the board — Monday, October 12 at 9:00 AM PDT` / `send the budget review to finance — Wednesday, October 14 at 9:00 AM PDT`.
- Message-row HTML: `<div class="result success"><p>You have 3 reminders saved:</p><p>⏰ Due now:</p><ol><li><strong>revise the pr</strong> — Wednesday, October 7 at 4:27 PM PDT</li><li><strong>send the budget review to the board</strong> — Monday, October 12 at 9:00 AM PDT</li><li><strong>send the budget review to finance</strong> — Wednesday, October 14 at 9:00 AM PDT</li></ol></div>`.
- Computed style: `<ol>` `list-style-type: decimal`, `padding-left: 24px`, `<li>` `display: list-item`, marker coloured. A screenshot shows "1.", "2.", "3." beside the rows. So the markers are visible on this build; my 10-11 "unnumbered" reading was on an older build (`b713b91cb5`/earlier) or I misread it. I cannot say which from here and will not guess; I did not re-check an older build.

One slip to own: the headers on my Ship-audit memos and log entries earlier today carried guessed times (11:4x, 11:5x, 12:5x). The real times were about 10:40 to 10:58 PDT (commit times). The log is corrected; the two memos keep the wrong header time.

Verified how: Chrome, isolated context, messages sent through the chat form, replies read from `.message-row` text and innerHTML, computed styles, one screenshot, Settings and /standup read as served pages. Layer: served DOM. Denominator: rows 1, 2, 3 (chat, /standup page, Radar), the list-numbering question; row 4 skipped, 5 not run, 6 waiting; no Slack/Markdown format check (no buttons).

— Web
