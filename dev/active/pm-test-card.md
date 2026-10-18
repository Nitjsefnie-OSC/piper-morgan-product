# PM test card

**Owner**: Lead. **v80 (06:45 10-18: alpha serves 47ba746bee; #2064 closed on your count; Sunday order + section D)**, **v79 (17:16 10-17: #2080 and #2078 landed for Sunday), v78 (16:39 10-17: A4 PASS, B1 create FAIL #2080), v77 (16:21 10-17: A5 PASS, #1913 closed), v76 (15:52 10-17: A4 invite pointer corrected), v75 (15:49 10-17: A5 path corrected), v74 (15:43 10-17: C1 done), v73 (15:28 10-17: C1 query corrected), v72 (15:24 10-17: C2 PASS; jump list links to the cards), v71 (15:21 10-17: A1 PASS), v70 (15:12 10-17, snippet added 15:15: your order at the top; A1 cut to what is left for your hand, read snippet inline), v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version. Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes).

**Alpha**: https://alpha.pipermorgan.ai serves **`47ba746bee`** (promotion 1 of 2, dispatched 06:39 10-18 on your word, run 39132506958; /health healthy at 06:42; `curl -s https://alpha.pipermorgan.ai/health` shows `git_sha`). One more promotion is possible today if something lands. This build carries everything since yesterday's: the #2077 token-field fix, the #2078 wizard fix with CXO's words, both halves of #2080 (your B1 chain) with the per-arm decline, the #2079 greeting by your clock, #2075 ("Connected, not yet tested" on an untested OAuth integration), #2076 (focus and standup say GitHub needs reconnecting), #2069 (project name saved as named, reply from the stored row), #2051, the #1982 PAT dual write, #2073. No migrations between `118241587e` and it.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## Your order (Sunday 06:45 10-18; each item links to its card)

1. ~~[C3](#c3) #2064 count line~~ **DONE 06:05, #2064 CLOSED 06:09.**
2. [D1](#d1): the #2077 ten-second check (must-close; your browser, your saved password).
3. [B1](#b1) again on a fresh chat: the full chain to a project on My Projects (#2080).
4. [D2](#d2): the #2078 wizard run, only if you want to see it yourself (Web runs it otherwise; must-close either way).
5. [A3](#a3), [A2](#a2), [A6](#a6), [A7](#a7), [B2](#b2), [B3](#b3): any order; none gates anything.

Yesterday's: ~~A1~~ PASS 15:19 · ~~C2~~ PASS 15:22 · ~~A5~~ PASS 16:18 · ~~A4~~ PASS 16:33 · ~~B1~~ offer PASS, create FAIL 16:31 → #2080 (fixed, re-run above) · ~~C1~~ DONE 15:40.

## A. Your cards (live since `118241587e`, still live on `47ba746bee`)

### A1. Broken GitHub grant: the card, the page, and one-step Reconnect (#2031, #1963)
- **PASS 15:19 10-17, your account, four of four steps** (readings: `dev/2026/10/17/controls/served-a1-xian-broken-grant-118241587e-2026-10-17.md`). PA writes the #2031/#2072 comments; CXO reads the words. Nothing left on this card.
- **Why your hand at all**: Web ran this whole scenario this morning on the cohort's test account on `118241587e`, and every surface passed (snippet discloses, card and Settings page say "Needs reconnecting", `what's connected?` honest, Reconnect one click). What Web cannot run is **your** account: it is the binding that failed on 10-16 (`degraded []` and an all-clear standup with the grant revoked), and the fix should be seen gone on the account that showed it. That is the whole remaining ask; CXO reads the words from your screenshots.
- **Already done (10-16, your run)**: steps 1 and 2 (snippet before, revoke) and the FAIL at 3.1. Nothing from that run needs repeating except the reads below.
- **What is left (about 5 minutes)**, on alpha signed in as yourself, from [pa-s5-broken-grant-steps.md](pa-s5-broken-grant-steps.md):
  1. Run the read snippet in the browser console. If `degraded` lists `github` with `stale_token`, your grant is still revoked from 10-16: go to step 3. If it shows `degraded []` and your issues, revoke the "Piper Morgan Alpha" app on GitHub (steps file, step 2) and run the snippet again. **Pass**: `degraded` names github `stale_token`; `today`, `slack`, `markdown` say GitHub couldn't be read. **Fail**: `degraded []` or "no open issues".
  2. Screenshot Settings → GitHub (`/settings/integrations/github`). **Pass**: ⚠️ "Needs reconnecting", a **Reconnect with GitHub** button, never "Connected" or "Not configured".
  3. Click **Reconnect with GitHub**. **Pass**: one step, back to ✅ Connected, no Disconnect hop. Reload `/settings/integrations` before judging the card.
  4. Run the snippet once more. **Pass**: `degraded []` and your issues are back.
- **The read snippet** (paste the whole block into the browser console on alpha, signed in, then Enter):
  ```js
  const show = (u, r) => r.text().then(t => console.log(u, t.slice(0, 1500)));
  fetch('/api/v1/radar', {credentials:'include'}).then(r=>r.json()).then(j=>console.log('degraded', JSON.stringify(j.degraded_sources)));
  fetch('/api/v1/standup/today', {credentials:'include'}).then(r=>show('today', r));
  for (const f of ['slack','markdown']) fetch('/api/v1/standup/generate', {method:'POST', credentials:'include', headers:{'Content-Type':'application/json'}, body: JSON.stringify({format:f})}).then(r=>show(f,r));
  ```
- **Skip today**: the Integrations **Test** button and the chat asks (`what's connected?`, a work-focus question with the grant revoked). Web served the first two; the focus and standup replies only say GitHub can't be read from tomorrow's build (#2076).
- **Judge**: PA relays, CXO reads the words. Paste the four outputs here, say "A1".

### A2. Calendar answers in chat (connected 10-15)
- **Where**: alpha chat, your account.
- **Steps**: `what time is it for me?` → `what's my agenda today?` → `what's my week like?`
- **Pass**: times labeled with your zone, never "TBD"; the agenda names today's events; the week view spans days.
- **Fail**: "calendar isn't connected", a TBD time, or a one-day answer for the week.
- **Judge**: Lead (CXO reads the copy if anything is off). Nobody has read these replies verbatim yet.

### A3. Disconnect dialog on the three pages Web could not cover (#2017)
- **Where**: `/settings/integrations/calendar`, `/settings/integrations/slack`, `/settings/integrations/notion`.
- **Steps**: on each page that shows a connected card, click **Disconnect**, then **Cancel** in the dialog.
- **Pass**: a confirm dialog appears on the click; Cancel leaves it connected. (Web passed GitHub and the Integrations page; these three had no connection on the test accounts.)
- **Fail**: the click does nothing, or Cancel disconnects.
- **Judge**: Lead closes #2017 on your pass.

### A4. Fresh account, PAT-only GitHub (#1982 dual write, #1983)
- **PASS 16:33 10-17, your fresh PAT-only account on `118241587e`, 4 of 4:** 274 open issues and the count through the token (capped list disclosed), standup's GitHub line populated with no failed source, "know about me" lists GitHub as linked and reads your work from the issues. No OAuth prompt. The held #1982 PAT dual write landed (`15dba249c8`) for Sunday's slot; #1983's hint copy follows. Side finding: the standup opens "Good morning!" at 4:29 PM → #2079.
- **Where**: an incognito window → https://alpha.pipermorgan.ai → sign up with a fresh alpha invite from HOST (the 10-12 one, `0877…VXB9`, was spent by Web on 10-15 for `web-pat-test`; HOST asked 15:52 to mint another; Lead relays the file name) and your Anthropic key.
- **Steps**: Settings → Integrations → GitHub → paste a personal access token with repo read on `mediajunkie/piper-morgan-product`; do NOT click OAuth connect. Then in chat: `what open issues do I have?` → `what's the issue count` → `give me a standup` → `What does Piper know about me?`
- **Pass**: real issues and a count via the token; the standup's GitHub line populated with no "source failed"; "know about me" lists GitHub issues.
- **Fail**: an owner/name nudge, "I couldn't find an issue number", an empty or failed GitHub source, or an OAuth prompt.
- **Judge**: Lead. On pass Lead lands the held PAT dual write (`claude/lead-1982-pat-dual-write`) and #1983's hint copy follows. Keep this account for A5–A7 and B1.

### A5. Keyless conversation survives adding a key (#1913, MVP)
- **PASS 16:18 10-17, your fresh account on `118241587e`:** keyless chat got the key-required reply, stayed in the rail after the key was added and the page reloaded (title and Radar card intact). #1913 closed on this run. Nothing left on this card.
- **Corrected 15:49 10-17:** the setup wizard's step 2 will not Continue without a validated LLM key, so "sign up and skip the key" is not a path. The equivalent, signed in the whole time, is to remove the key afterwards.
- **Where**: the A4 account, after sign-up (wizard: step 2 your Anthropic key, step 3 HOST's invite + account, step 4 skip projects).
- **Steps**: Settings → LLM API Keys → **Remove** the key (confirm the delete). Open a new chat and send `hello, what can you do?` (expect the key-required reply). Note the conversation title in the left rail. Settings → LLM API Keys → add the key back. Reload.
- **Pass**: the keyless conversation is still in the rail with its title.
- **Fail**: it is gone. Write which page you were on when you added the key back.
- **Judge**: Lead (the fix needs your repro path).

### A6. Find your way: todos, projects, feedback (P5)
- **Where**: the A4 account, from first login.
- **Steps**: time how long it takes to reach (a) the Todos page and (b) the Projects page by clicking only; look for any way to send feedback.
- **Pass**: both under a minute and a feedback path exists. Write the seconds and the path you used.
- **Judge**: CXO.

### A7. Three spec checks (P2, P3, P4), any account
- **P2**: `Add three todos for the launch: draft brief, book venue, send invites` → `what are my todos?` Pass: exactly 3, those names.
- **P3**: `Good morning — what's on my calendar today?` Pass: a calendar answer, or the honest "calendar isn't connected" on an account without one. Screenshot.
- **P4**: `What open issues do I have?` → `add a todo to review the roadmap` → `What have I created this session?` Pass: the list matches GitHub; the recall names the todo and nothing you didn't make.
- **Judge**: Lead; CXO reads any copy that surprises you.

## B. New on the 10-16 build (live since 17:09 10-16; still live)

### B1. `list my projects` with no projects (#2048, MVP)
- **16:31 10-17, your fresh account: steps 1–2 PASS (3 of 3 chats; #2048 closed by CXO on them), the rest of the chain FAIL:** `Piper Morgan` → "Got it — want me to create a project called Piper Morgan?" → `Yes` → "I don't have a confirmation that the project was created…"; My Projects empty. Filed **#2080**: the router read "Piper Morgan" as "who are you?" ×6, the name turn released it and the chain died; **fix landed 17:14 for Sunday** (a name that reads as a question now gets the yes/no confirm, `Add a project called "Piper Morgan"? (yes/no)`). Re-run this exact chain on Sunday's build.
- **Re-run on `47ba746bee` (Sunday):** fresh chat, `list my projects` → `yes` → `Piper Morgan` → expect `Add a project called "Piper Morgan"? (yes/no)` → `yes` → the project appears on My Projects. A `no` at that confirm should say "Okay, I won't add that project. If you meant to ask me something, go ahead." Paste the four replies. PA judges against CXO's acceptance; closes #2080.
- **Where**: the A4 account, or any account with no projects, three fresh chats.
- **Steps**: `list my projects` in each fresh chat, then `yes` to the offer once.
- **Pass**: 3 of 3 → "You don't have any active projects yet. Would you like to add a project?" → `yes` → "What would you like to call it?" (On `6bb955919d` this phrase fell to the floor 3 of 3.)
- **Fail**: "I don't have your projects list in front of me right now…".
- **Judge**: CXO closes #2048 on the served pass (Web also runs it).

### B2. A question about a project never changes it (#2057)
- **Where**: an account with a project (call it Foo).
- **Steps**: `how do I archive my project Foo?` then check the Projects page (`/projects`).
- **Pass**: "To archive a project, say 'archive project Foo'. You can restore it any time with 'restore project Foo'." and Foo is still active.
- **Fail**: Foo archived, or a consent question.
- **Judge**: CXO.

### B3. Integrations card after Test (#2053, #2045)
- **Where**: `/settings/integrations`, your account.
- **Steps**: press **Test** on the GitHub card; wait; then reload the page.
- **Pass**: without a reload the card drops "Not checked yet" and the summary count updates; the line reads "Healthy. Checked just now."; after the reload it reads "Last checked at H:MM AM" in your zone, never a raw UTC stamp.
- **Known gap (Web 17:33)**: on an account whose GitHub is connected by OAuth the time line never shows (the card arrives with no check time; #2066, fix on main, live with tomorrow's promotion). Run B3 only if your GitHub card says "Connected via your personal token"; otherwise skip it.
- **Judge**: CXO.

## C. Your hand only (agent seats are denied these)

### C1. Prod counts (P6)
- **DONE, reported 15:40 10-17 (your run on production):** users **10**, setup_complete **5**. The second line returned every username with an empty last-activity column: the `session_activity` ledger only records "created X" events from chat, so it is not a last-seen source; a corrected last-seen query (conversation turns) goes to Exec, not to you. Nothing left on this card.
- **Corrected 15:28 10-17:** the first line used to count `action_humanizations`, a table #1522 dropped on 10-07 (after your own count of 0 rows that day). The row was written on 10-06, before the drop; not a guess, stale. The line below is the two counts that still exist.
`fly postgres connect -a piper-morgan-db -d piper_morgan`, then one line at a time; paste the two results here or in chat:
```
SELECT (SELECT count(*) FROM users) AS users, (SELECT count(*) FROM users WHERE setup_complete) AS setup_complete;
SELECT u.username, max(s.created_at) FROM users u LEFT JOIN session_activity s ON s.owner_id=u.id::text GROUP BY u.username ORDER BY 2 DESC NULLS LAST;
```

### C2. Uploaded-file encryption census (#1306 backfill), live now
- **PASS, reported 15:22 10-17 (your run from your own machine):** `database: app config (services.database.connection)`; `uploaded files: 0 plaintext, 0 already encrypted, 0 missing-on-disk`. The script now reaches the production database (the 07:0x failure is gone); production has no uploaded files with a storage path, so nothing to encrypt. Recorded on #1306. Nothing left on this card.
- **Your 07:0x run failed before reading anything** (`ConnectionRefusedError … 127.0.0.1:5433`): the script ignored `DATABASE_URL`. Nothing was written. Fixed and live on this build; the lines now also print which database they resolved. Run them again.
Count first (writes nothing); run the second line only if the count shows plaintext files above 0:
```
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306 --count"
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306"
```

## D. New on the Sunday build (live on `47ba746bee` since 06:42)

### D1. Token field stays empty (#2077, must-close, your hand)
- **Why you:** Chrome fills a saved Piper password into password inputs; your browser has one, the test browsers do not. The fix is `autocomplete="new-password"` on ten credential inputs.
- **Steps**: sign in on alpha in your usual browser; open Settings → Integrations → GitHub; do not type in the token field; in the console run `document.getElementById('token').value.length`.
- **Pass**: `0`, and the field looks empty. **Fail**: any number above 0, or a masked value showing.
- **Judge**: Lead closes #2077 on your `0` (PPM gates it; Class 2).

### D2. Fresh invited sign-up through the wizard (#2078, must-close; you or Web)
- **Where**: a private window, signed out; the invite is the file HOST named in `~/.piper-shared/` (your mint of 10-17); PA's steps are `dev/active/pa-sunday-served-2078-2080-steps.md` §A.
- **Steps**: `/setup`, enter the invite code, a username, an email and a password, Create Account, then through to step 5.
- **Pass**: step 5 reads "Setup Complete", "You're all set. You're signed in, and Piper is ready to help." with an **Open Piper** button that lands on `/`, signed in. **Also acceptable**: a toast "Account created, setup did not finish" with the Settings → LLM API Keys pointer, signed in; quote it.
- **Fail**: "Setup Failed", a button stuck on "Creating…", or landing signed out.
- **Judge**: PA relays to CXO; closes #2078.

### D3. The greeting follows your clock (#2079, Production, anyone)
- On an account that signed in through `/login`, say `give me a standup` after noon: it opens **Good afternoon!** (after 17:00, **Good evening!**), matching the home page header. Before noon, **Good morning!**. A wizard-created account that never used `/login` opens **Hi!** (no zone known; CXO: fine). CXO judges the quote.

## Not on your list
Web runs S9–S13 (#2057 phrasings, #2053 card, #2055 notice placement, #2046 ordinals) on this build; CXO judges; Lead posts the results on the issues. Parked, try-and-tell only: #1943 ("mark the first one complete and leave the second one pending"). #2061, #2059, #2060 and #2054 have nothing observable to test by hand; they close on being live.
