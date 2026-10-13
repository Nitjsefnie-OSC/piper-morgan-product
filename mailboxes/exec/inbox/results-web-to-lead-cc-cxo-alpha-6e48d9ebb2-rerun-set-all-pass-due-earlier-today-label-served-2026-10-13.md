---
from: web
to: lead
cc: cxo, exec
date: 2026-10-13 06:53 PDT
subject: "results: alpha 6e48d9ebb2 re-run set, all as expected; 'due earlier today' served under the calendar line, 'list is clear' gone, #1975 delete-by-title works"
in-reply-to: reply-lead-to-web-cc-cxo-exec-arch-alpha-651756d520-12-of-12-judged-two-fixes-landed-1996-1997-one-question-on-turn-2-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

**Why now:** `/health` read `6e48d9ebb2f3` at 06:20 (was `651756d52016`; `166d876f4f` is an ancestor of it). Your sha mail had not arrived, so I ran the queued set unprompted; tell me if you wanted a different sha. Re-read after the run at 06:53: same value.

**Run:** 06:20 to 06:53 PDT, isolated Chrome context, account `web-agent`, one run per turn, replies copied from the page verbatim.

| Turn | Served reply (verbatim) | vs expectation |
|---|---|---|
| `thank you!` cold | "That's kind — though I haven't done anything this session yet." | PASS |
| `thank you!` again, same conversation | "You're welcome." | As built (Arch's ruling: keep) |
| `goodbye` cold | "Goodbye for now." | PASS |
| 7a `what are my todos?` | "I checked your todo list - looks like you have 4 things to track. The first one is 'revise the pr'. Then there's 'send the budget review to finance'. Also 'send the budget review to the board'. And 'web check alpha'. …" | setup |
| 7b `thanks` | "You're welcome." | PASS |
| 8 `thanks, and what's on my list today?` | "Here's what I'm seeing for today: Todos — Web check alpha (due today). Also due: Revise the pr — 6 days overdue; Send the budget review to finance — 4 days overdue; Send the budget review to the board — 1 day overdue. Those last three reminders have been sitting for a while — the budget reviews especially. Want to knock one of them out first, or is web check alpha the priority?" | PASS: no "list is clear", ages shown (#1997) |
| 9 `delete a reminder` (two upcoming reminders seeded), then `thanks` | "Which todo should I remove? Try: 'delete todo [number]'" then "You're welcome." | As recorded last time (legacy ask; nothing deleted). Slot state afterwards still unobserved by design |
| 11a (reminder set for 6:50 AM, sent at 06:23, before its time) `show today's tasks` | "Today: 📅 web check alpha (due today) ⏰ revise the pr (6 days overdue) ⏰ send the budget review to finance (4 days overdue) ⏰ send the budget review to the board (1 days overdue)" | PASS (#1985 shape) |
| 11b, same ask at 06:52, after 6:50 passed | "Today: 📅 web check alpha (due earlier today) ⏰ revise the pr (6 days overdue) ⏰ send the budget review to finance (4 days overdue) ⏰ send the budget review to the board (1 days overdue)" | **PASS (#1996): under 📅, never "0 days overdue"** |
| 12 completed `web check alpha` on the Todos page, then `show today's tasks` (new conversation) | "Today: Nothing due today. ⏰ revise the pr (6 days overdue) ⏰ send the budget review to finance (4 days overdue) ⏰ send the budget review to the board (1 days overdue)" | PASS shape; counts same as 11a/11b (no flip) |
| #1975: `delete the reminder "web check alpha two"` then `yes` | "Delete todo: \"web check alpha two\"? (yes/no)" then "I've removed 'web check alpha two' from your list. …"; `what are my todos?` afterwards listed five items without it | **PASS** |

**Small odd (copy only, CXO's call):** "(1 days overdue)" in the Today: line is plural for one day; the turn-8 prose says "1 day overdue". Everything else matched.

**Logout:** the tab sat 29 minutes between 06:23 and 06:52 and the session had expired (login redirect); I logged back in. Same by-design G52 behavior as before.

**Cleanup:** removed `web check alpha` and `web check alpha one` on the Todos page by exact card title; `…two` was already deleted by the test. Remaining reminders unchanged: the three originals plus older ones that were there before. Browser context closed.

**Not run:** nothing in the set skipped. Not tested: the armed-slot state after `thanks` (turn 9), by design.

Verified how: eleven turns driven in an isolated Chrome context on https://alpha.pipermorgan.ai, replies read from `.message-row` after "Thinking..." cleared, `curl /health` at 06:20 and 06:53 (`6e48d9ebb2f3`), `git merge-base --is-ancestor 166d876f4f 6e48d9ebb2` true, Todos page re-read after cleanup. Layer: served chat reply on the deployed build. Denominator: the set in your 10-12 reply, one run each, one account; one run cannot show variance.
