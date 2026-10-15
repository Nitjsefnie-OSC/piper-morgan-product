# PM test card — the standing "what should I test?" surface

**Owner**: Lead. **Started**: 2026-09-19. **Rewritten fresh for the 10-13 morning**: v41 (11:51 10-15: Step 0 READY again on 35acfe35d7, staging serving it, gate probe accepting); v40 (11:29 10-15: Step 0 back to PENDING on the seventh #1771 landing 35acfe35d7 (politeness at the hatch, 'skip the standup'); S6b gains those phrases); v39 (11:15 10-15: Step 0 READY confirmed — staging f5c8e33c63 redeployed after the known-broken guard lifted, gate probe accepts via f76a307ecb; S6 strings corrected to the one pause line and the drop line (CXO 11:15)); v38 (11:06 10-15: **Step 0 READY** — Tests SUCCESS on `f76a307ecb` (run after the 2019 clock-fixture fix), staging lagging on 48b86d1d57 until the next push redeploys; 20 landings today incl. the whole #1771/#888 standup-word series; S6b lists the standup runs; #2017/#2018 admitted to MVP by xian 10:48 via PPM); v37 (08:25 10-15: 12 landings on main bf03ac3ab2 — the 7-branch batch minus #2010 then #2010 on Arch's census ruling, #2020, #2017, #1771 second seam, #2019 cap; main went red once on s2014items and is green again on bddb4a089c; Tests running on bf03ac3ab2; Step 0 READY when it concludes success; new served rows S1–S7 below; N5 superseded by S7); v36 (20:5x 10-14: Step 0 DONE, alpha 5e5f3366c4; N5 PASSED by Web 20:56, judged by Lead; clear_todos flip held on xian's lean, PPM recommends hold + soft delete); v35 (17:24 10-14: Step 0 READY, staging f8b2d15e52, Tests green on that exact sha); v34 (15:48 10-14: Step 0 RE-ARMING, gate walk widened after staging drifted past it); v33 (12:03 10-14: Step 0 READY, staging 1746f1ebec); v32 (10:58 10-14: new row N5 (#1943 delete the first two) needs the NEXT promotion; Step 0 is live again, wait for Lead's ready); v31 (09:13 10-14: post-history-rewrite note on Surface and Step 0, nothing new to test); v30 (19:16 10-13: CXO accepted N1–N3 and closed #2002/#2003/#2004 at 19:15; rows struck); v29 (19:06 10-13: Web's served run on de7d0c1c57 — N1, N2 (3 branches), N3 (4 branches) all PASS, CXO to judge and close; PM's run of those is optional); v28 (18:52 10-13: alpha promoted to de7d0c1c57 by PM at 18:49, run 38497735645, first pass of the refined gate; N1–N3 now live); v27 (17:18 10-13: row N4 #2005 after PA's MCP redeploy; #1982 fallback off 7cc00113bc rides the next promotion with nothing for PM to test); v26 (12:43 10-13: #2004 fixed on main a1fdee9921, row N3); v25 (12:33 10-13: Web's three served runs on b713b91cb5 judged by CXO — #1987 all three ACs, #2001, #1976 done; #2002/#2003 fixed on main 75ac141ed6, served checks owed after the next promotion); v24 (12:09 10-13: alpha promoted to b713b91cb5 on xian's word — every row is live); v23 (07:05 10-13: Web's run judged, two landings on main, not live); v22, 22:30 PDT 10-12 (PM's ask: "pick it up then
with a fresh test card"). Rolling doc: rows get added when a fix needs PM's live verification and struck when done. When PM asks
"what do I test?", the answer is this file. Earlier versions and all struck history: `git log -p` of this file. Mirror artifact
(https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi) was republished from v27 at 17:26 10-13; between republishes this file is current and wins.

**Surface**: alpha.pipermorgan.ai · **running `de7d0c1c57`** (read from /health 18:52 10-13 after promotion run 38497735645, dispatched
by PM at 18:49; the gate accepted staging's sha via its tested ancestor cd73af1b6e). **After the 10-14 history rewrite** (main now descends from `d217d8f1ca`): `de7d0c1c57` is a pre-rewrite id that /health will keep reporting until the next promotion; its code equals the rewritten main's on every served path (checked 09:13 10-14: `git diff` on services/web/scripts, one operator-script line). Staging already serves `d217d8f1ca` with Tests green, so a promotion needs no wait, and none is needed for the rows below. **Everything on this card is live, including #2002 / #2003 / #2004 (75ac141ed6, a1fdee9921) and #1982 step 3 (7cc00113bc). Previous: `b713b91cb5` (10-13 12:04), `6e48d9ebb2` (10-12 21:46).**

**Step 0 — promote the build (PM's hand, on PM's explicit word only; no browser, no approval step since 10-13). **READY (11:51 10-15): Tests concluded SUCCESS on `35acfe35d7` (main; 21 landings today incl. the three migrations, already on staging) and staging serves `35acfe35d7`; gate probe: "Tests concluded success on 35acfe35d75d0f2c6f810546f538f8c649a4d09f". Dispatch ONLY on xian's explicit word (Lead in session or xian). Earlier today: READY 11:2x on f76a307ecb, PENDING 11:3x on the seventh #1771 landing.** Two reds today, both test fixtures, both fixed; the 2019 clock pins are green on this run.** Previous: DONE 20:55 10-14 (5e5f3366c4, run 38678103509 dispatched 20:47 by Lead on xian's word in his pane); N5 PASSED on it. Previous: DONE 18:49 10-13 (de7d0c1c57); was READY 17:24 10-14: staging serves `f8b2d15e52`, Tests concluded success on that exact sha, the gate probe accepts. Two CI fixes landed this afternoon so this stays true while you are away: the gate now finds the tested ancestor however many docs commits land, and Tests on main no longer cancels when a newer push arrives. This promotion carries N5 (#1943 delete the first two) plus today's other landings (#1843 please-request, #1771+#2007 defer line, #1783 see-the-rest, #2008 copy); Web and CXO run those served rows after it. Dispatch the command below when you are back For the next one: wait for Lead's "ready" first, since the gate refuses until Tests is green on the staging code:**
```
gh workflow run fly-deploy.yml -R mediajunkie/piper-morgan-product --ref main -f promote_to_alpha=true
```
Promotion takes ~4 min; `curl -s https://alpha.pipermorgan.ai/health` shows `git_sha`. (The 10-12 `pending_deployments` approval
call is gone: the alpha environment has no reviewers now, Fly B.) **Since 5e42a37c3b (10-13): the promotion refuses unless Tests
concluded success on the exact sha staging serves, or (since the 17:21 10-13 refinement, 6164ab3ceb) on its nearest tested ancestor when only untested paths such as docs/ changed since — if it refuses, wait for Tests on that sha and dispatch again.**

## ~~N1–N3~~ CLOSED by CXO 19:15 10-13 on Web's served run (alpha de7d0c1c57). Not covered, not asked: the `yes` path, a bare `no` after an unarmed offer; CXO reads PM's paste if either lands.

Also live with nothing to test by hand: #1982 step 3 (7cc00113bc, the legacy GitHub-context fallback off; the MCP live read
already passed on PA's 17:05 memo). **N4 is on a different app** (piper-morgan-mcp, PA's v14), not alpha.

N1. ~~**#2002 layout**~~ **CLOSED 19:15 (CXO).** Was: `delete a reminder` with 2+ reminders → in the served HTML the closing sentence ("Say the number or the name, or 'never mind'…") is its own paragraph AFTER the `<ol>`, not inside the last `<li>`. Web reads `.message-row` innerHTML. Same for `delete todo`.
N2. ~~**#2003 named miss**~~ **CLOSED 19:15 (CXO), 3 branches.** Was: with the numbered ask armed, `delete the reminder "a title that is not in the list"` → `I don't see a reminder called "…".` then the SAME numbered list, still armed (a following `2` binds and asks the yes/no); nothing deleted. Then `"<an existing title>"` quoted → the yes/no confirm for THAT title (unchanged). Unquoted miss (`delete the reminder web check alpha nine`) → "Still not sure which reminder you mean — you have:" + list, no guess.
N3. ~~**#2004 bare never-mind**~~ **CLOSED 19:15 (CXO), 4 branches.** Was: with nothing open (e.g. right after the gone-row line, or cold in a new conversation): `never mind` → **"Okay."** and nothing else (no todo list). Also `no thanks` cold → "Okay.". Control: `never mind, show my todos` → the todo list as before (compound goes to the floor). CXO sets the word if "Okay." is not it.
N5. ~~**#1943 delete the first two**~~ **SUPERSEDED by S7 (#2019, xian's 10-14 ruling): on the next build `delete the first two reminders` is CAPPED by design (capped reply naming both, nothing armed), not a two-item confirm.** Was: LIVE on 5e5f3366c4; Web PASS 20:56 10-14 (confirm named the first two of the numbered list, `no` left everything intact); Lead judged PASS. PM's run optional:** `remind me tomorrow at 9am to web check alpha one`, then the same with `two`, then `what reminders do I have?` → the list is NUMBERED (1., 2., …); then `delete the first two reminders` → **`Delete 2 reminders: "<first>" and "<second>"? (yes/no)`** naming the FIRST TWO of that numbered list (never the row whose title says "two"). Answer `no`. Was (Web 10-11 on 4bd1a236e9): one confirm naming "web check alpha two". Clean up on the Todos page. Judged by Lead; CXO reads the copy.
N4. **#2005 MCP issue count** (MCP v14 live since 17:49 10-13, PA's deploy of c6c26a596f; PA runs this served check with PM and judges it): in Claude Desktop through the Piper
   Alpha MCP connector, `What are my open GitHub issues in Piper?` → the count Claude states is GitHub's total (278 at 17:5x 10-13, from
   `gh issue list --assignee mediajunkie --state open --limit 1000 | wc -l`), not 30, and it must not say "that's the full set" when the
   list shown is shorter than the total. Fail: 30, or "full set" with a 50-item list. PA judges (their surface); paste the answer here.

## S1–S7 — served checks owed on the NEXT promotion (main bf03ac3ab2; nothing below is live on alpha yet)

S1. **#2020 decline copy (Web/CXO):** on an account with no connected activity, `do a standup` → "I don't have anything to build your standup from yet… (yes/no)" → `not now` → **"No problem. I won't ask again in this chat. Say 'my standup interview' any time to try the guided version."** (no "quick report stays exactly as it is"). Fail: the old line, or "this session".
S2. **#2017 Disconnect (Web, 5 pages):** Settings → Integrations, click Disconnect on a connected card → the confirm dialog appears; `Cancel` leaves it connected; confirm disconnects. Same on the GitHub, Notion, Slack and Calendar settings pages. Fail: the click does nothing (the 10-14 finding).
S3. **#2010 empty projects (CXO):** account with no projects, `list my projects` → **"You don't have any active projects yet. Would you like to add one?"** → `yes` starts the add-project flow. With projects: the list ends on the last project line, no closing question.
S4. **#2012 Test line per leg (CXO; accounts on xian's rollup):** Integrations → GitHub → Test: the reply names the serving leg (OAuth-only / PAT-only / stale-OAuth-plus-PAT) with CXO's three lines; never a bare success on a stale leg.
S5. **#1965/#1889 reads with the Alpha app revoked (PA with xian):** the four GitHub reads disclose STALE_TOKEN, never an empty list. **xian's step-by-step (PA, 09:48): `dev/active/pa-s5-broken-grant-steps.md`** (before read, revoke, the four reads + the Test line (#2012), reconnect through Disconnect (#2017), after read; each step with its pass condition).
S6. **#1771 (Web, three runs again):** mid-standup `stop` → "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up." (the ONE pause line, CXO 08:35; `never mind` and `not now` mid-interview give the same); `do a standup` → the continue/restart offer (even with no source connected); `not now` at that offer → the ruled defer line and the standup STAYS paused; `continue` resumes. Also `cancel that` (or bare `cancel`) → "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one." Fail: "has been cleared", "I've paused your standup", or no offer.
S6b. **#1771/#888 standup words (Web runs, CXO judges; landed 635f6f9878 → 022dc3074c):** mid-interview `cancel` → "Okay, I've dropped your standup. Say 'do a standup' whenever you want a fresh one." then `do a standup` starts fresh; `stop` or `never mind` → "Okay, I'll leave your standup where it is. Just ask when you want to pick it back up." then `do a standup` → continue/restart offer; typed `skip` at "Any blockers…?" → the draft/next step, NOT a pause (on 5e5f3366c4 it paused: Web 09:3x); at "ready to start?" `stop`, `cancel`, `skip` or `no thanks` → "Okay, no standup for now. Say 'do a standup' whenever you want one." and a fresh `do a standup` with no continue offer; `quick` → the quick standup; **(35acfe35d7)** `please cancel` mid-interview → the drop line, `please stop` → the pause line (answers kept), `skip the standup` → the drop line mid-interview and the invitation line at "ready to start?", `please cancel my 3pm meeting` → a normal answer, not an escape.
S7. **#2019 interim cap (CXO judges):** with two or more reminders, `delete the first two reminders` → **"I can delete one reminder at a time for now. You asked about these: 1. "…" 2. "…" Tell me which one to delete first. Nothing has been changed."** then `what reminders do I have?` shows both still present. `delete reminder 1` alone still gets the named confirm.

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
    number", an empty/failed GitHub source, or an OAuth prompt. On pass Lead lands `claude/lead-1982-pat-dual-write`; the legacy
    fallback is already off (7cc00113bc, 10-13 on PM's `legacy=0`); #1983's copy change follows.
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
