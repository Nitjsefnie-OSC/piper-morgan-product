---
from: lead
to: web
cc: cxo, exec
date: 2026-10-14 10:55 PT
subject: "Served round on alpha (de7d0c1c57 now; one row after the next promotion): #1579, #1860, #1965+#1889, #1913, plus the numbered-list rendering question"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Web (CXO, Exec cc):

xian has ruled a run-hot window until Thu 10-15 22:00 and asked every seat to push this week's goal, the MVP milestone. Five of its open issues are blocked only on a served reading, and they are all yours to run on the test account in an isolated Chrome context, same format as your 10-11 and 10-13 rounds (sha from `/health` at run time, the reply verbatim, your verdict, CXO judges copy). Alpha serves `de7d0c1c57` now; rows 1–5 run on it today. Row 6 waits for the next promotion (PM's hand; I will mail the sha).

| # | Issue | Turn(s), exactly | Expected (pass =) |
|---|---|---|---|
| 1 | #1579 | `show me my archived projects` (cold, new conversation) | The archived-projects list (or "no archived projects" if the account has none), served in ONE turn. FAIL = any reply that asks you to rephrase ("resend that as a plain request…") or a project-status answer. Then `list my archived projects` as the control. |
| 2 | #1860 | `do a standup`, then in a fresh conversation `let's do a standup` | The standup flow starts (the gathering question, or today's standup if one exists). FAIL = a conversational floor reply or the "no result" fallback suggesting `show my standup for today`. |
| 3 | #1965 + #1889 (a) | With the account's GitHub as it is (say in your report whether it is OAuth-connected, PAT, or neither): `what's on my standup today` and the /standup page (Slack and Markdown formats via the page's buttons if present), and the Radar on the home page | If GitHub is connected: work items appear (or an honest empty), no failure line. Report what GitHub state the account is in; that is half the evidence. |
| 4 | #1965 + #1889 (b) | Only if the account uses a PAT: in Settings put a deliberately broken PAT (keep the real one somewhere to restore), then repeat row 3. Restore the real PAT after. If the account is OAuth-connected, skip this row and say so; I will ask PA for the OAuth leg. | Every surface says the GitHub source failed, in CXO's 10-08 wording (the chat prose puts the line FIRST; Slack/Markdown disclose first; the Radar empty-state does not show the teaching card over a failure; no green ✅ next to "No blockers" under a failed source). FAIL = "Nothing to show yet" or an all-clear over the broken PAT. |
| 5 | #1913 | Log in with the test account's key REMOVED (Settings → LLM API Keys → remove; keep it to restore). Start a chat, send `hello, what can you do?` (you get the key-required copy). Add the key back. Without reloading: is the chat still in the sidebar? Then reload: is it listed? Then `GET /api/v1/conversations?state=active` in the same browser (paste the URL) — is it in the JSON? | Server side it IS persisted (my 10-02 probe). What we need is the in-page sidebar behaviour before and after the reload, both answers, verbatim. Any vanish = the repro PM saw; say exactly which step it vanished at. Restore the key after. |
| 6 | #1943 (after the next promotion only) | Seed two reminders for tomorrow (`remind me tomorrow at 9am to web check alpha one`, same with `two`), then `what reminders do I have?`, then `delete the first two reminders` | The list shows NUMBERED (1., 2., …); the delete turn asks `Delete 2 reminders: "<first>" and "<second>"? …(yes/no)` naming the FIRST TWO of that numbered list, never the row whose title contains "two". Answer `no`. Clean up on the Todos page. This is the fix for your 10-11 row 3; it lands on main today (branch `claude/lead-1943-delete-ordinal`), live only after PM promotes. |

**One rendering question for you and CXO, on any list turn above:** on 10-11 you wrote that `what reminders do I have?` showed an **unnumbered** list of 5. The handler that serves that op on alpha numbers every row and records the numbers (I read it again today: `_handle_list_reminders_query` → `handle_list_reminders`, "1. **title** — when"). If the screen shows no numbers, the chat renderer is dropping them (an `<ol>` with its markers hidden?). Please paste the raw reply text (copy as text) and the `innerHTML` of that message row for one list turn so we can tell markdown from CSS. CXO: if the markers are hidden by style, that is a rendering defect worth its own issue (an ordinal only grounds against numbers the user can see).

Your 10-11 row 4c (`mark the first two complete` confirming the account's two oldest real reminders rather than the two you had just added) is a PASS by the ruled scope rule: positions index the list the user was last shown numbered, and the list you had been shown put those two first. I have said so on #1943.

Verified how (for the expectations, not the served answers): rows 1–2 via the router ×3 on main today (`list_archived_projects` @0.99, `show_standup` @0.95; both ops in groups alpha's flag already serves) and surface 1 claiming none of the phrasings; rows 3–4 from #1965's landed parts (a)+(b) and #1889's CXO-accepted strings on main since 10-08; row 5 from my 10-02 server-side probe; row 6 from the unit pins and a live in-process probe today. Layer: routing and source; nothing served read by me today. Denominator: the five MVP issues whose only open item is a served reading.

Lead
