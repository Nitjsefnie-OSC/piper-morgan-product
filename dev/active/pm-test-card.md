# PM test card

**Owner**: Lead. **v77 (16:21 10-17: A5 PASS, #1913 closed), v76 (15:52 10-17: A4 invite pointer corrected), v75 (15:49 10-17: A5 path corrected), v74 (15:43 10-17: C1 done), v73 (15:28 10-17: C1 query corrected), v72 (15:24 10-17: C2 PASS; jump list links to the cards), v71 (15:21 10-17: A1 PASS), v70 (15:12 10-17, snippet added 15:15: your order at the top; A1 cut to what is left for your hand, read snippet inline), v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version. Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes).

**Alpha**: https://alpha.pipermorgan.ai serves **`118241587e`** (promotion 2 of 2 under your standing grant, 08:05 10-17, run 39043475359; /health healthy at 08:08; `curl -s https://alpha.pipermorgan.ai/health` shows `git_sha`). No more promotions today. This build carries everything landed since last night: user erasure (#2064), the Privacy & data page (#2065, served PASS), the GitHub card's checked-time line (#2066, closed), the Integrations headline counting only connected integrations (#2068), the consent line naming the project (#2070, PASS), per-person Test results (#2071, closed), both halves of #2072 (the radar/standup disclose a revoked grant again; Settings, chat and setup guidance say "needs reconnecting", never "connected"), and the #1306 count fix for C2.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## Your order (15:09 10-17; each item links to its card)

1. ~~[A1](#a1)~~ **PASS 15:19.**
2. ~~[C2](#c2)~~ **PASS, reported 15:22** (ran from your own machine; fine), then [C1](#c1): your hand only, one terminal command.
3. ~~[A5](#a5)~~ **PASS 16:18**, then [A4](#a4): the fresh-account PAT path behind the #1982 dual write you held. **Clear the token field before pasting** (this build still autofills it, #2077).
4. [B1](#b1): gates MVP (#2048), one short row.
5. [A3](#a3), [A2](#a2), [A6](#a6), [A7](#a7), [B2](#b2), [B3](#b3): any order; none gates anything.

## A. Your cards (all live on `118241587e`)

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

## Not on your list
Web runs S9–S13 (#2057 phrasings, #2053 card, #2055 notice placement, #2046 ordinals) on this build; CXO judges; Lead posts the results on the issues. Parked, try-and-tell only: #1943 ("mark the first one complete and leave the second one pending"). #2061, #2059, #2060 and #2054 have nothing observable to test by hand; they close on being live.
