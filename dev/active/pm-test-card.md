# PM test card

**Owner**: Lead · **v84**, 11:17 10-19 (amended 11:5x) · Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes) · older versions: `git log -p` of this file, and the history at the bottom.

**Alpha** https://alpha.pipermorgan.ai serves **`f9fb8b750b`** (promotion 1 of 2, 11:17 10-19; one more slot before 21:00).
- **New on this build:** #2082 a no-name "start a project" asks for the name first · #2067 "You've been signed out" modal when your sign-in lapses (must-close) · #2081 the admin Invites page, `/settings/invites` · #2083 /health reports the database.
- **Live since Sunday:** #2077 token-field fix · #2078 wizard fix · #2080 · #2079 greeting · #2075 · #2076 · #2069 · #2051 · #1982 · #2073 · the password-reset script fix · `add_project` in the router's live set.
- **Your account:** `mvp-tester` is the only admin (your psql UPDATE, 10:13). No `dinp` account exists.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## Your order (Monday, updated 12:0x 10-19; only what is left; each item links to its card)

1. [D1](#d1): the #2077 ten-second check (must-close; your browser, your saved password).
2. [D2](#d2): the #2078 wizard run with one code from your bank (must-close).
3. [D5](#d5): the admin Invites page as `mvp-tester`: mint two, revoke one (about three minutes).
4. [D4](#d4): the MCP app reads your A4 PAT-only account's GitHub (#1982, about five minutes; PA reads the logs).
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

## D. New on the Sunday build (live since `47ba746bee` 06:42 10-18, still on `f9fb8b750b`)

### D1. Token field stays empty (#2077, must-close, your hand)
- **Why you:** Chrome fills a saved Piper password into password inputs; your browser has one, the test browsers do not. The fix is `autocomplete="new-password"` on ten credential inputs.
- **Steps**: sign in on alpha in your usual browser; open Settings → Integrations → GitHub; do not type in the token field; in the console run `document.getElementById('token').value.length`.
- **Pass**: `0`, and the field looks empty. **Fail**: any number above 0, or a masked value showing.
- **Judge**: Lead closes #2077 on your `0` (PPM gates it; Class 2).

### D2. Fresh invited sign-up through the wizard (#2078, must-close; you or Web)
- **Where**: a private window, signed out; one unused code from `~/.piper-shared/xian-invite-bank-credential-20261018.txt` (mark its line with the account label afterwards); PA's steps are `dev/active/pa-sunday-served-2078-2080-steps.md` §A.
- **Steps**: `/setup`, enter the invite code, a username, an email and a password, Create Account, then through to step 5.
- **Pass**: step 5 reads "Setup Complete", "You're all set. You're signed in, and Piper is ready to help." with an **Open Piper** button that lands on `/`, signed in. **Also acceptable**: a toast "Account created, setup did not finish" with the Settings → LLM API Keys pointer, signed in; quote it.
- **Fail**: "Setup Failed", a button stuck on "Creating…", or landing signed out.
- **Judge**: PA relays to CXO; closes #2078.

### D4. The MCP app reads a PAT-only account's GitHub (#1982, PA's lane, your hand)
- **Why you:** the PAT dual write (on this build) stores a PAT saved in Settings where the MCP app can read it; before it, a PAT-only user got "connect GitHub" from the connector. Your main account is OAuth-only, so the account to use is your **A4 PAT-only account**. First PAT-only user the MCP app serves.
- **Steps**: (1) on alpha, signed in as A4: Settings → GitHub → paste the same PAT → **Update**; pass: it still reads "Connected" (A4's PAT was saved before the dual write, so this re-save is what makes it readable). (2) In Claude Desktop (or claude.ai) add or reconnect the Piper Alpha connector and sign in **as A4** on the alpha login page it opens. (3) Ask: **"What are my open GitHub issues in Piper?"**
- **Pass**: real issue titles that match GitHub, with the total stated (A4's PAT saw 274 on 10-17). **Fail**: "connect GitHub", `CONNECT_REQUIRED`, or an empty list. Screenshot it.
- **After**: switch the connector back to your main account if you use it day to day. PA reads the MCP app's logs for the call (`EncryptedDBCredentialStore`, no decrypt error). Full steps: `dev/active/pa-sunday-served-2078-2080-steps.md` §D.
- **Judge**: PA, then Arch's runbook names it as the landing's live check.

### D5. The admin Invites page: mint, see masked, revoke (#2081, Production, your hand)
- **Before it**: nothing; `mvp-tester` is the only admin (your psql UPDATE 10:13). The page refuses anyone else with 403.
- **Steps**: signed in as `mvp-tester` on alpha, open Settings: an **Invites** card shows (admins only). Open `/settings/invites`: the list shows Sunday's ten as Unused, masked (their forms are with HOST since 12:0x). Mint **2** codes: they show once, in full; add them to `~/.piper-shared/xian-invite-bank-credential-20261019.txt` with labels before leaving the page. Revoke **one** of the two: its status reads Revoked. Paste the two masked forms here (read them off the list) for HOST's roster.
- **Pass**: the card shows only to `mvp-tester`; a mint shows raw codes once and the list never does; revoke flips the status and the code no longer redeems. **Fail**: a raw code anywhere but the mint response, a non-admin reaching the page, a revoked code still redeeming.
- **Judge**: HOST (the page was built to HOST's seven rulings); Lead closes #2081 on your screenshot of the masked list plus HOST's word. Masked forms only in anything you paste.

## Not on your list

Web ran #2082 and #2067 on this build (both PASS 11:24; CXO accepts, #2067 must-close). Web also runs S9–S13 (#2057 phrasings, #2053 card, #2055 notice placement, #2046 ordinals); CXO judges; Lead posts results on the issues. Parked, try-and-tell only: #1943. #2061, #2059, #2060 and #2054 have nothing observable to test by hand; they close on being live.

## Version history

**v83 (11:39 10-18: #2080 and #2075 closed by CXO on Web's quotes; B1 re-run now optional; #2082/#2067/#2081 built for Monday)**, **v82 (09:54 10-18: D4 added, the #1982 MCP read on your A4 account, PA's ask)**, **v81 (08:40 10-18: alpha 83a2f4e40c, promotion 2 of 2; #2064/#2069/#2076/#2072/#2051 closed; D2 with your bank; reset script live)**, **v80 (06:45 10-18: alpha serves 47ba746bee; #2064 closed on your count; Sunday order + section D)**, **v79 (17:16 10-17: #2080 and #2078 landed for Sunday), v78 (16:39 10-17: A4 PASS, B1 create FAIL #2080), v77 (16:21 10-17: A5 PASS, #1913 closed), v76 (15:52 10-17: A4 invite pointer corrected), v75 (15:49 10-17: A5 path corrected), v74 (15:43 10-17: C1 done), v73 (15:28 10-17: C1 query corrected), v72 (15:24 10-17: C2 PASS; jump list links to the cards), v71 (15:21 10-17: A1 PASS), v70 (15:12 10-17, snippet added 15:15: your order at the top; A1 cut to what is left for your hand, read snippet inline), v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version.
