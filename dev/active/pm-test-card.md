# PM test card

**Owner**: Lead. **v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version. Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes).

**Alpha**: https://alpha.pipermorgan.ai serves **`118241587e`** (promotion 2 of 2 under your standing grant, 08:05 10-17, run 39043475359; /health healthy at 08:08; `curl -s https://alpha.pipermorgan.ai/health` shows `git_sha`). No more promotions today. This build carries everything landed since last night: user erasure (#2064), the Privacy & data page (#2065, served PASS), the GitHub card's checked-time line (#2066, closed), the Integrations headline counting only connected integrations (#2068), the consent line naming the project (#2070, PASS), per-person Test results (#2071, closed), both halves of #2072 (the radar/standup disclose a revoked grant again; Settings, chat and setup guidance say "needs reconnecting", never "connected"), and the #1306 count fix for C2.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## A. Your cards (all live on `118241587e`)

### A1. Broken GitHub grant: the card, the page, and one-step Reconnect (#2031, #1963)
- **Where**: your own alpha account (the one with GitHub connected), plus GitHub → Settings → Applications → Authorized OAuth Apps.
- **Steps**: follow [pa-s5-broken-grant-steps.md](pa-s5-broken-grant-steps.md) (`dev/active/`), steps 2–5 (revoke the "Piper Morgan Alpha" app, then look, then Reconnect). The read snippet in that file goes in the browser console on alpha.
- **Pass**: Settings → GitHub (`/settings/integrations/github`) shows ⚠️ "Needs reconnecting" and a **Reconnect with GitHub** button, never "Connected". Integrations (`/settings/integrations`) GitHub card: the same words, never "Not configured" (that is #2031's open question). Radar and the standup formats say GitHub couldn't be read, never "no open issues". Reconnect is ONE click back to Connected (reload the Integrations page before judging its card).
- **Fail**: "Connected" or "Not configured" with the grant revoked; "no open issues"; a Disconnect hop needed.
- **Live now (slot 2 landed 08:08).** Tell me when you start and I mail PA so PA is there while you're on it. One sitting covers the snippet's disclosure (the FAIL from your 18:55 run, now fixed), the card, the Settings page, the Reconnect, and two chat asks CXO added to the steps (`what's connected?` and a work-focus question with the grant revoked: neither may say GitHub is connected).
- **Judge**: PA relays, CXO reads the words. About 10 minutes.

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
- **Where**: an incognito window → https://alpha.pipermorgan.ai → sign up with HOST's 10-12 alpha invite (masked `0877…VXB9`; in the 0600 roster, never in mail) and your Anthropic key.
- **Steps**: Settings → Integrations → GitHub → paste a personal access token with repo read on `mediajunkie/piper-morgan-product`; do NOT click OAuth connect. Then in chat: `what open issues do I have?` → `what's the issue count` → `give me a standup` → `What does Piper know about me?`
- **Pass**: real issues and a count via the token; the standup's GitHub line populated with no "source failed"; "know about me" lists GitHub issues.
- **Fail**: an owner/name nudge, "I couldn't find an issue number", an empty or failed GitHub source, or an OAuth prompt.
- **Judge**: Lead. On pass Lead lands the held PAT dual write (`claude/lead-1982-pat-dual-write`) and #1983's hint copy follows. Keep this account for A5–A7 and B1.

### A5. Keyless conversation survives adding a key (#1913, MVP)
- **Where**: the A4 account, BEFORE you add the Anthropic key (sign up, skip the key).
- **Steps**: send `hello, what can you do?`; note the conversation title in the left rail; add the key in Settings; reload.
- **Pass**: the first conversation is still in the rail with its title.
- **Fail**: it is gone. Write which page you were on when you added the key.
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
`fly postgres connect -a piper-morgan-db -d piper_morgan`, then one line at a time; paste the two results here or in chat:
```
SELECT (SELECT count(*) FROM users) AS users, (SELECT count(*) FROM users WHERE setup_complete) AS setup_complete, (SELECT count(*) FROM action_humanizations) AS humanizations;
SELECT u.username, max(s.created_at) FROM users u LEFT JOIN session_activity s ON s.owner_id=u.id::text GROUP BY u.username ORDER BY 2 DESC NULLS LAST;
```

### C2. Uploaded-file encryption census (#1306 backfill), live now
- **Your 07:0x run failed before reading anything** (`ConnectionRefusedError … 127.0.0.1:5433`): the script ignored `DATABASE_URL`. Nothing was written. Fixed and live on this build; the lines now also print which database they resolved. Run them again.
Count first (writes nothing); run the second line only if the count shows plaintext files above 0:
```
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306 --count"
fly ssh console -a piper-morgan -C "python -m scripts.backfill_encrypt_files_1306"
```

## Not on your list
Web runs S9–S13 (#2057 phrasings, #2053 card, #2055 notice placement, #2046 ordinals) on this build; CXO judges; Lead posts the results on the issues. Parked, try-and-tell only: #1943 ("mark the first one complete and leave the second one pending"). #2061, #2059, #2060 and #2054 have nothing observable to test by hand; they close on being live.
