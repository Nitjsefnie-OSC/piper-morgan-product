# PM test card

**Owner**: Lead · **v84**, 11:17 10-19 (amended 11:5x) · Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes) · older versions: `git log -p` of this file, and the history at the bottom.

**Alpha** https://alpha.pipermorgan.ai serves **`f9fb8b750b`** (promotion 1 of 2, 11:17 10-19; one more slot before 21:00).
- **New on this build:** #2082 a no-name "start a project" asks for the name first · #2067 "You've been signed out" modal when your sign-in lapses (must-close) · #2081 the admin Invites page, `/settings/invites` · #2083 /health reports the database.
- **Live since Sunday:** #2077 token-field fix · #2078 wizard fix · #2080 · #2079 greeting · #2075 · #2076 · #2069 · #2051 · #1982 · #2073 · the password-reset script fix · `add_project` in the router's live set.
- **Your account:** `mvp-tester` is the only admin (your psql UPDATE, 10:13). No `dinp` account exists.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## Your order (Monday, updated 12:0x 10-19; only what is left; each item links to its card)

1. ~~[D1](#d1) #2077~~ **PASS 12:3x, CLOSED** (your `0`).
2. ~~[D2](#d2) #2078~~ **PASS 12:4x** (account `test-acct-2078`, landed signed in; My Projects shows the step-4 project "One Job" with its repo linked; PA closes). Your two wizard notes filed: #2088 (invite code at step 3, should be first) and #2089 (hosted wizard still shows the local system check; Temporal always fails).
3. ~~[D5](#d5) #2081~~ **PASS 13:03, CLOSED 13:2x** on HOST's word (the list-refresh gap is fixed on main and rides the next promotion).
4. ~~[D4](#d4) #1982~~ **PASS 13:3x** (fresh Piper Alpha MCP connector as `test-acct-2078`, PAT-only: 273 open issues, 50 shown, your project named; PA reads the logs and judges).
5. None of these gates anything; any order, any day: [A3](#a3) Disconnect dialog on three pages · [A2](#a2) Calendar answers in chat · [A6](#a6) find your way · [A7](#a7) three spec checks · [B2](#b2) a question never changes a project · [B3](#b3) the Integrations card after Test.

Done and gone from this page (git log -p keeps them): A1, A4, A5, B1, C1, C2, C3, D3; Web's E1 (#2067 modal) and E2 (#2082 name-first) both passed 11:24 on this build. Your hand items this morning: dinp (no such account; mvp-tester is admin), #1852 closed, Calendar Connect PASS, the ten masked forms relayed to HOST 12:0x.

## A. Your cards, remaining (live since `118241587e`, still live on `f9fb8b750b`)

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

## B. Remaining from the 10-16 build (still live)

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


## Not on your list

Web ran #2082 and #2067 on this build (both PASS 11:24; CXO CLOSED both 12:32). Both must-close items are done by your hand: #2077 closed 12:4x on your `0`; #2078 passed 12:4x (PA closes on the quote). Web also runs S9–S13 (#2057 phrasings, #2053 card, #2055 notice placement, #2046 ordinals); CXO judges; Lead posts results on the issues. Parked, try-and-tell only: #1943. #2061, #2059, #2060 and #2054 have nothing observable to test by hand; they close on being live.

## Version history

**v83 (11:39 10-18: #2080 and #2075 closed by CXO on Web's quotes; B1 re-run now optional; #2082/#2067/#2081 built for Monday)**, **v82 (09:54 10-18: D4 added, the #1982 MCP read on your A4 account, PA's ask)**, **v81 (08:40 10-18: alpha 83a2f4e40c, promotion 2 of 2; #2064/#2069/#2076/#2072/#2051 closed; D2 with your bank; reset script live)**, **v80 (06:45 10-18: alpha serves 47ba746bee; #2064 closed on your count; Sunday order + section D)**, **v79 (17:16 10-17: #2080 and #2078 landed for Sunday), v78 (16:39 10-17: A4 PASS, B1 create FAIL #2080), v77 (16:21 10-17: A5 PASS, #1913 closed), v76 (15:52 10-17: A4 invite pointer corrected), v75 (15:49 10-17: A5 path corrected), v74 (15:43 10-17: C1 done), v73 (15:28 10-17: C1 query corrected), v72 (15:24 10-17: C2 PASS; jump list links to the cards), v71 (15:21 10-17: A1 PASS), v70 (15:12 10-17, snippet added 15:15: your order at the top; A1 cut to what is left for your hand, read snippet inline), v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version.
