# PM test card — the standing "what should I test?" surface

**Owner**: Lead. **Started**: 2026-09-19. **Rewritten fresh for the 10-13 morning**: v25 (12:33 10-13: Web's three served runs on b713b91cb5 judged by CXO — #1987 all three ACs, #2001, #1976 done; #2002/#2003 fixed on main 75ac141ed6, served checks owed after the next promotion); v24 (12:09 10-13: alpha promoted to b713b91cb5 on xian's word — every row is live); v23 (07:05 10-13: Web's run judged, two landings on main, not live); v22, 22:30 PDT 10-12 (PM's ask: "pick it up then
with a fresh test card"). Rolling doc: rows get added when a fix needs PM's live verification and struck when done. When PM asks
"what do I test?", the answer is this file. Earlier versions and all struck history: `git log -p` of this file. Mirror artifact
(https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi) is v15 and BEHIND; this file is current.

**Surface**: alpha.pipermorgan.ai · **running `b713b91cb5`** (read from /health 12:09 10-13 after promotion run 38451337983, dispatched
by Exec at 12:00 on xian's direct word; no approval step any more). **Everything on this card is live: #1987 both halves + the thanks step (71e213b885 / a9f8cd16d1), #2001 (143f9a9a83), #1976 (84a313394d), the meeting_time example (d13dafd172), logs-keep-only-fingerprints (ec2cc9d44f). Previous: `6e48d9ebb2` (10-12 21:46).**

**Promotion recipe (on PM's explicit word only; no browser, no approval step since 10-13):**
```
gh workflow run fly-deploy.yml -R mediajunkie/piper-morgan-product --ref main -f promote_to_alpha=true
```
Promotion takes ~4 min; `curl -s https://alpha.pipermorgan.ai/health` shows `git_sha`. (The 10-12 `pending_deployments` approval
call is gone: the alpha environment has no reviewers now, Fly B.)

## Owed after the NEXT promotion (fixed on main 75ac141ed6 at 12:33 10-13, NOT live on b713b91cb5)

N1. **#2002 layout** — `delete a reminder` with 2+ reminders → in the served HTML the closing sentence ("Say the number or the name, or 'never mind'…") is its own paragraph AFTER the `<ol>`, not inside the last `<li>`. Web reads `.message-row` innerHTML. Same for `delete todo`.
N2. **#2003 named miss** — with the numbered ask armed, `delete the reminder "a title that is not in the list"` → `I don't see a reminder called "…".` then the SAME numbered list, still armed (a following `2` binds and asks the yes/no); nothing deleted. Then `"<an existing title>"` quoted → the yes/no confirm for THAT title (unchanged). Unquoted miss (`delete the reminder web check alpha nine`) → "Still not sure which reminder you mean — you have:" + list, no guess.

## Morning order — everything below is live on alpha now (each ~1 min unless noted)

**New since your last pass (the 21:46 build):**
1. **#1987 pointer delete.** `remind me to water the plants tomorrow at 9`, then `delete that reminder`. Pass: `Delete the reminder
   "…"? (yes/no)`; `yes` removes it (check the Todos page). **Half 2 — PASSED on Web's 12:08 run, CXO closed #1987 12:40; the gone-row line PASSED in one conversation (Web's 12:21 memo) (71e213b885 + a9f8cd16d1):** with two
   reminders set, `delete a reminder` → `Which reminder should I delete?` + a numbered list → `2` → `Delete the reminder "…"? (yes/no)` →
   `yes` → gone. Also (49e90de36f, Arch's condition 3): with the numbered ask open, say `thanks` → `You're welcome.` + the same numbered question
   again (a9f8cd16d1, CXO's 09:50 copy); then `2` still binds. `bye` instead drops the ask: `Goodbye for now.` On the live build it still answers the old generic prompt (Web saw that at 06:53).
2. **#1987 gone row.** Set another reminder, delete it on the Todos page, then in chat `delete that reminder`. Pass: `I can't find
   "…" anymore — it may already have been removed. Say 'show my todos' to see the list — nothing has been deleted.` (CXO judges this line.)
3. **#1975 delete by title** — PASSED on Web's 06:53 run (CXO judged); yours is optional. A reminder with a distinctive title, `delete the <title> reminder`, `yes`. Pass: that one gone on the
   Todos page and nothing else missing. Fail: a different due item deleted (the old bug).
4. **#1996 / #1997 ages** — PASSED on Web's 06:53 run (CXO judged); yours is optional. #2001 ('1 day overdue') PASSED twice on Web's runs, CXO closed it 12:40. With one overdue item and one due earlier today: `what needs my attention?` then `show my todos`. Pass:
   ages in calendar days on your clock; the earlier-today item under `Today:` as "(due earlier today)"; never "0 days overdue"; the
   list is never called clear while due reminders remain.
5a. ~~#1976~~ **PASSED on Web's 12:40 run (Todos page title `web test one`), closed by Lead 12:2x.** Was: `add a todo to web test one` → the Todos page title reads `web test one`, not `to web test one`. Remove it after.
5. **#1992 angle brackets.** With no timezone set, `what time is it`. Pass: the hint's bracketed city placeholder is visible. Any
   `<tag>`-shaped text in a reply must show, not vanish.

**Live since 15:47 10-12, not yet passed by you:**
6. **#1985**: with an overdue or due-today todo, `what needs my attention?`. Pass: a `Today:` list naming them. Fail: "nothing urgent".
7. **#1986**: `thank you!` as the first turn of a fresh conversation → a short warm line. After a real answer, `thanks` → "You're
   welcome." or similar; `goodbye` → a short farewell. Fail: a briefing or a question back. (CXO closes #1985/#1986 on your run.)
8. **#1988**: any turn earning the timezone hint. Pass: `set my timezone to Helsinki`-style with a real city, not an empty quote.
9. **A, #1941**: with GitHub connected, `close issue 99999 in mediajunkie/piper-morgan-product` → confirm. Pass: "There's no issue
   #99999 in … — nothing was changed." Fail: the hedge or any claim it closed something. (Failed on v169 10-01; fix live since 10-09.)
10. **D, #1942/#1944**: `get issue 101` → `what's the issue count`. Pass: title/state, then a count. (#1945 Project Config stays with CXO.)
11. **Item 4**: "who are you", "help me setup my projects", "mark the first two complete". Same answers as before; paste anything different.

**Fresh-account block (~15 min, one incognito signup covers G, F, P1, P5):**
12. **G, PAT-only GitHub** (#1889/#1963/#1965 served check; #1982 lands on it). HOST's alpha invite from 10-12 09:30 (masked
    `0877…VXB9`) is in the 0600 roster and the `~/.piper-shared` file, never in mail. Incognito → sign up with it + your Anthropic key
    (note anything that blocks signup = P1). Settings → Integrations → GitHub → paste a personal access token with repo read on
    `mediajunkie/piper-morgan-product`; do NOT click OAuth connect. Then `what open issues do I have?` → `what's the issue count` →
    `give me a standup` → `What does Piper know about me?`. Pass: real issues and a count via the token; the standup's GitHub line
    populated with no "source failed"; "know about me" lists GitHub issues. Fail: the owner/name nudge, "I couldn't find an issue
    number", an empty/failed GitHub source, or an OAuth prompt. On pass Lead lands `claude/lead-1982-pat-dual-write`, reports
    `legacy=0`, then turns the legacy fallback off; #1983's copy change follows.
13. **F, #1913**: inside that account, BEFORE adding the key, send `hello, what can you do?` and note the conversation in the left rail;
    add the key; reload. Pass: the first conversation is still there with its title. Write which page you were on when you added it.
14. **P5**: from first login, time finding (a) todos and (b) projects by clicking; look for any feedback path. Pass: both under a
    minute and a feedback path exists. Write the seconds.

**Spec's remaining live checks (any account):**
15. **P2**: `Add three todos for the launch: draft brief, book venue, send invites` → `what are my todos?`. Pass: exactly 3, those names.
16. **P3**: `Good morning — what's on my calendar today?`. Pass: a calendar answer or the honest "calendar isn't connected". Screenshot.
17. **P4**: `What open issues do I have?` → `add a todo to review the roadmap` → `What have I created this session?`. Pass: the list
    matches GitHub; the recall names the todo and nothing you didn't make.

## Parked — don't re-test yet
- **C, #1914/#1943** ("mark the first one complete and leave the second one pending"): open with Arch (router-args interpretation).
  Try-and-tell only.
- **H, #1822** OpenAI-only Slack turn: only if Slack is linked. Unchanged since 09-23.

## Needs a one-time setup from PM — then calendar and meeting rows open
### E. Calendar: two Fly secrets, then "what's my agenda today?"
(1) Google Cloud Console → Credentials → OAuth client ID, Web application; (2) redirect URI exactly
`https://alpha.pipermorgan.ai/api/v1/settings/integrations/calendar/callback`; (3) Calendar API enabled, consent screen lists the
tester accounts; (4) `fly secrets set -a piper-morgan GOOGLE_CLIENT_ID="…" GOOGLE_CLIENT_SECRET="…"` (never paste the values anywhere
tracked); (5) tell Lead; Settings → Calendar → Connect → consent → "Connected". Then: `what time is it for me?` → `what's my agenda
today?` → `what's my week like?`. Pass: labeled times, never "TBD"; week view spans days. Recipe:
`docs/internal/operations/canonical-ops-recipes.md` → "Google Calendar for a hosted deployment".

### P6. Prod counts (PM's hand; agent seats are denied prod reads) — paste the results here
`fly postgres connect -a piper-morgan-db -d piper_morgan`, then one line at a time:
`SELECT (SELECT count(*) FROM users) AS users, (SELECT count(*) FROM users WHERE setup_complete) AS setup_complete, (SELECT count(*) FROM action_humanizations) AS humanizations;`
`SELECT u.username, max(s.created_at) FROM users u LEFT JOIN session_activity s ON s.owner_id=u.id::text GROUP BY u.username ORDER BY 2 DESC NULLS LAST;`

## Struck
10-12: **B** (#1912 remove a project) PASSED 16:2x; **E2** (#1606 two-part sentence) PASSED 16:28; Step 0 promotions done 15:47 and
21:46. Through 10-01: rows 1 (#1824), 4 (#1876/#1574/#1887), 6 (#1856), 8 (#1737), 9 (#1498), 10 (#1559), 11 (#1625), #1906, #1617,
the admin calendar card (v158). Failure causes recorded per row in this file's history (v17–v21).
