# PM test card — the standing "what should I test?" surface

**Owner**: Lead. **Started**: 2026-09-19. **Rewritten to remaining-only**: 2026-10-01 14:03 PDT (PM's ask). Rolling doc:
rows get added when a fix needs PM's live verification and struck when done. When PM asks "what do I
test?", the answer is this file. Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (v15, BEHIND this file; this file is current).

**Surface**: alpha.pipermorgan.ai · **now running `651756d520`** (read from /health 15:48 10-12 after promotion run 38312410442
landed; code = main's 264d3e9549 under services/web/config). **v17 (15:48 10-12)**: Step 0 struck
(10-09's promotion landed 10-09 18:25; today's landed 15:47); the test order rewritten for what is live now; PM's PAT-only test added
(row G) — it was never on this card before, it lived on Exec's rollup as the invite item.

## Step 0 — DONE. Nothing to promote by hand.
The 10-09 build went live 10-09 18:25 (run 38013096307); c613beabf5 this morning (run 38265156567); today's build is run 38312410442,
approved by xian at 15:48. Landed 15:48; alpha reports `651756d520`. Dispatch recipe for next time:
`gh workflow run fly-deploy.yml -R mediajunkie/piper-morgan-product --ref main -f promote_to_alpha=true`, then Actions → the run →
Review deployments → alpha → Approve.

**Live on alpha already (since 10-09 evening):** #1959/#1941 (A), #1942/#1944 (D), the 34 retired literals (item 4), #1960, the
standup/Radar source-failure lines (#1889/#1963/#1964/#1965), the MCP server card, #1978 (org-workspace keys accepted; landed 10-11).
**Arrived with today's promotion (live 15:47):** #1985 (attention query reads YOUR todos, not the session's), #1986 (pure "thank you!"/"goodbye"
get a short warm line, not a briefing), #1988/#1991 (the timezone hint renders its example), #1459 (internal, no visible change).

**Test in this order** (each ~1 min unless noted; everything below is live on alpha now):
1. **A**: close a nonexistent issue (#1941/#1959). Expect a straight "no such issue", no "Close #N?" first.
2. **D**: `get issue 101` → `what's the issue count`. (#1945, the Project Config page, is still open with CXO; expect that unchanged.)
3. **Item 4**: "who are you", "help me setup my projects", "mark the first two complete". Same answers as before; anything different, paste it.
4. **New, #1985** (after promotion): with at least one overdue or due-today todo, send `what needs my attention?`. Pass: a `Today:` list
   naming them (due today first, then overdue). Fail: "I don't see anything urgent" while the todo list shows them.
5. **New, #1986** (after promotion): `thank you!` as the first turn of a fresh conversation → a short warm line, nothing about todos.
   Then after a real answer, `thanks` → "You're welcome." or similar; `goodbye` → a short farewell. Fail: a briefing or a question back.
   (Web runs this family on the test account too; your run on your own account is the one CXO closes #1985/#1986 on.)
6. **New, #1988** (after promotion): any turn that earns the timezone hint (e.g. `what time is it for me?` with no timezone set).
   Pass: the hint reads `set my timezone to Helsinki`-style, with a real city, not an empty quote.
7. **G, PAT-only account** (new, ~10 min, fresh account): see row G below. This is the served check for #1889/#1963/#1965, and
   #1982's held dual-write lands on it.
8. **F** (#1913): first conversation survives adding your key — do it inside G's fresh account (~2 min).
9. **C** stays parked: #1943 is still open with Arch. Try-and-tell, not pass/fail.
10. P1–P6 as before, when you have the time. P1 pairs with G.

### G. PAT-only account: GitHub through a pasted token, no OAuth (#1889/#1963/#1965 served check; #1982 lands on it) — ~10 min
HOST minted ONE alpha invite for this on 10-12 09:30 (masked `0877…VXB9`, unused); the raw code is in the 0600 roster and the
`~/.piper-shared` file, never in mail. Do: incognito → alpha.pipermorgan.ai → sign up with that invite + your Anthropic key (this is P1
too — note anything that blocks signup). Then Settings → Integrations → GitHub → paste a personal access token (classic or fine-grained
with repo read on `mediajunkie/piper-morgan-product`); do NOT click the OAuth connect. Then: `what open issues do I have?` →
`what's the issue count` → `give me a standup` → `What does Piper know about me?`. Pass: real issues and a count via the token; the
standup's GitHub line is populated with no "source failed" line; the "know about me" answer lists GitHub issues. Fail: the owner/name
nudge, "I couldn't find an issue number", an empty or failed GitHub source in the standup, or an OAuth prompt when the PAT is set.
Tell Lead the result (pass or the exact reply); on pass, Lead lands `claude/lead-1982-pat-dual-write` and reports `legacy=0` before
turning the legacy fallback off.

## Re-test now — fixed since PM's last pass

### A. Close a nonexistent issue, get a straight answer (#1858) — ~30 s — **FAILED on v169 (16:21); fix on main, re-test after the next deploy** (#1941)
**PM's 16:21 result: the hedge.** Cause (alpha logs 23:21Z): a third 404 shape — the write leg returned the 404 as text as pinned, but the
live server answered the read-back with a wrapped `McpError` 404, which landed in the mid-flight except and degraded to the hedge. Fixed on
main (two-leg evidence via the raised error counts; pinned both ways). Not on alpha until the next deploy.
Do: with GitHub connected, `close issue 99999 in mediajunkie/piper-morgan-product` → confirm (the confirm is
the normal destructive gate; it fires before the lookup). Pass: "There's no issue #99999 in … — nothing was
changed." Fail: the hedge, or any claim it closed something. Cause was GitHub's 404 JSON parsing as an issue.

### B. Remove a project, and it's actually gone (#1912) — ~1 min — **PASSED 16:2x (Klatch removed)**
Do: Settings → Projects → All Projects → Remove on a spare project (One Job; re-add after with `add project One
Job with repo Design-in-Product/one-job`). Then `show my projects`. Pass: toast, list refreshes without it, chat
doesn't list it. Cause: the DELETE call was a commented-out TODO while the toast fired.

### C. "Mark the first one complete and leave the second one pending" (#1914) — ~1 min — **FAILED 16:27 as "first three … fourth"** (#1943 → Arch)
**PM's result:** one completed, "Left the other one as is." with three still due; Radar kept the cleared one pinned (#1946, fixed on main).
The single-ordinal binder has no range; Lead built a regex range + held it (PM: the regex approach is the problem). Arch is asked whether
targets/verbs should be interpreted via the router's extracted args instead. Don't re-test until that lands.
Do: with two reminders due now, send a turn so Piper mentions them, then the exact sentence, then `what
reminders do I have?`. Pass: one confirmation naming the first as completed, ending "Left the other one as is.";
the list shows only the second. Fail: a todo created from the sentence, both completed, or a "which one?" ask.

### E2. Your two-part sentence, both halves served (#1606) — ~1 min — **PASSED 16:28** (the artifact labels this row G)
Do: with two reminders set, send exactly: `please clear the reminders except for "Review the PR" - also, are you able
to set my default repo for me conversationally?`. Pass: the capability answer FIRST ("Yes — say 'set my default repo
to owner/name'…"), then the clear-verb question ("mark it done, or delete it?") with the exception note; nothing
deleted, nothing set. Fail: the old "doesn't look like an owner/name repo", a confirm to SET the repo, or the clear half
missing. (Row G from before — it moved up.)

### D. Two GitHub asks the router used to decline — ~30 s — **FAILED 16:31–16:34, three ways** (#1942 + #1944 fixed on main; #1945 → CXO)
**PM's results:** `get issue 101` / `get issue #101` → "I couldn't find an issue number" — the router-served Intent carried no
`context["original_message"]`, so the handler was handed an empty message (#1942, fixed at the source). `my default repo should be
test-piper-morgan` → the owner/name nudge, though that repo is registered (#1944, fixed: bare names resolve against your registry).
Project Config lists the repo under both Linked Repositories and Integrations, and nothing shows a default repo/project (#1945, CXO).
Also: `clear the reminders except for 'revise the pr'` → verb question → your answer with the list → complete_todo('it') (#1943 → Arch).
Do: `get issue 101` → `what's the issue count` (default repo mediajunkie/piper-morgan-product). Pass: the
issue's title/state; then a count. Fail: a clarifying question, a listing, or a project-status reply.

### F. A first conversation survives adding your key (#1913) — ~2 min — PM's Test 7 fail (10-01); runnable now, no fix needed to try it
PM asked 10-06 that this sit here as a test. Lead's 10-02 probe (server side, no key) found the conversation IS stored and listed, so the
vanish may be client-side or already fixed; only a live run settles it. Exec added the row (not Lead); Lead owns the file and may reword.
Do: as a NEW user with NO key (a fresh invite, or one of your spare accounts), send `hello, what can you do?` and note that the
conversation appears in the left rail. Then add a valid Anthropic key in Settings. Reload. Pass: the first conversation is still in the
rail, with its title. Fail: it is gone. Write down which page you were on when you added the key and whether you were signed in; "I
don't remember" is fine. Needs a fresh account, so it pairs naturally with P1.

## Spec's live-alpha checks (P1–P6) — folded from the 10-05 evaluation, PM-approved

Record pass/fail plus one line each; a screenshot for P3 helps. All against the Step-0 build.

### P1. New-user signup — ~5 min — needs a fresh invite (reissues are next week's; use one of yours if you have a spare)
Do: incognito → alpha.pipermorgan.ai → sign up with a fresh invite + your current Anthropic key; if you have a SHORTER valid key
(older `sk-ant-…` format), try that one too. Pass: account created, setup completes, first chat answers. Fail: a key rejected
for its length/format, a validator that blocks a real key, or a signup gate with no explanation. (Confirms R1 step 0, C-04.)

### P2. Three todos in one sentence — ~30 s
Do: `Add three todos for the launch: draft brief, book venue, send invites` → `what are my todos?`. Pass: exactly 3 new todos
with those three names. Fail: 1 todo named "the launch: draft brief, …", 2 of 3, or a "which one?" ask. (Confirms C-LLM multi-item.)

### P3. Greeting + calendar in one message — ~30 s — 1924 fixed this family on 10-03
Do: `Good morning — what's on my calendar today?`. Pass: a calendar answer (or the honest "calendar isn't connected" if Row E's
secrets aren't set yet). Fail: a bare greeting with no calendar content, or a greeting that ignores the question. (The 10-03
deletions had made the greeting swallow the question; fixed, not yet live until Step 0.) Screenshot, please.

### P4. No false statements with GitHub connected — ~2 min
Do: `What open issues do I have?` → then `add a todo to review the roadmap` → then `What have I created this session?`.
Pass: the issue list matches GitHub; the recall names the todo you just made and nothing you didn't. Fail: an invented issue, a
"you created…" that you didn't, or "nothing this session" after the todo. (Confirms C-LLM false statements / trust.)

### P5. Cold-user findability + feedback — ~3 min — do this inside P1's new account if you can
Do: from first login, time how long it takes to find (a) your todos and (b) your projects, by clicking, not chatting. Then look
for ANY way to send feedback. Pass: both found in under a minute; a feedback path exists. Fail: either not findable, or no
feedback path at all. Write the seconds and what you clicked. (Confirms C nav, G-U6.)

### P6. Prod counts (PM's hand; agent seats are denied prod reads) — read-only, paste the results here
`fly postgres connect -a piper-morgan-db -d piper_morgan`, then ONE line at a time:
`SELECT (SELECT count(*) FROM users) AS users, (SELECT count(*) FROM users WHERE setup_complete) AS setup_complete, (SELECT count(*) FROM action_humanizations) AS humanizations;`
`SELECT u.username, max(s.created_at) FROM users u LEFT JOIN session_activity s ON s.owner_id=u.id::text GROUP BY u.username ORDER BY 2 DESC NULLS LAST;`

## Needs a one-time setup from PM — then calendar and meeting rows open

### E. Calendar: connect once, then "what's my agenda today?" — PM's hand: two Fly secrets
PM's ruling (10-01): the Google OAuth APP is deployment plumbing, not a per-user setting. Admin card hidden for
non-admins (v158); app creds are Fly secrets. Until set, every calendar/meeting row is untestable.
The plan: (1) Google Cloud Console → Credentials → OAuth client ID, Web application (reuse an existing Piper
client if one exists); (2) Authorized redirect URI exactly
`https://alpha.pipermorgan.ai/api/v1/settings/integrations/calendar/callback`; (3) Calendar API enabled; consent
screen lists the tester accounts; (4) `fly secrets set -a piper-morgan GOOGLE_CLIENT_ID="…" GOOGLE_CLIENT_SECRET="…"`
(never paste the values anywhere tracked; `GOOGLE_SETTINGS_REDIRECT_URI` already set; Fly restarts itself);
(5) tell Lead; Settings → Calendar → Connect → consent → "Connected".
Then test: `what time is it for me?` → `what's my agenda today?` → `what's my week like?`. Pass: Connected
without an app-credentials card; labeled times, never "TBD"; Focus Time block; week view spans days.
Recipe: `docs/internal/operations/canonical-ops-recipes.md` → "Google Calendar for a hosted deployment".

## Waiting on us — don't re-test yet
- **H. OpenAI-only Slack turn** — #1822, optional, only if Slack is linked. Unchanged since 09-23.

## Struck (through 2026-10-01)
Rows 1 (#1824), 4 (#1876/#1574/#1887), 6 (#1856), 8 (#1737), 9 (#1498), 10 (#1559), 11 (#1625) — PASSED by PM
09-30/10-01; #1906 clear-pick re-test PASSED 10-01; #1617 standup tail-release PASSED 09-23; the admin calendar
card PM hit (10-01) — fixed by design change (v158), superseded by row E. Earlier struck history: git log of this file.
