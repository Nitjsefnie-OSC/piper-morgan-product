# PM test card

**Owner**: Lead · **v104**, 07:14 10-23 · Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes) · older versions: `git log -p` of this file, and the history at the bottom.

**First, your decision: the Anthropic spend cap.** At about 06:59 this morning, the Anthropic workspace behind Amber's keychain key (`sk-ant-usr…ewAA`) hit its spend limit. Anthropic refuses its calls until 11-01. It's the top card on Exec's rollup: raise the cap in the Anthropic console (your $250/month project budget is the precedent), and say whether any alpha account's key is in that workspace. HOST is matching the key.

**Alpha** https://alpha.pipermorgan.ai serves **`dc45f98938`** (promoted 07:10 10-23; /health healthy).

- **New on this build (rows mailed to Web 07:12; CXO judges):**
  - #2132 (your must-close), the handler half: "Analyze launch-notes-2131.txt" reads your uploaded file ("I read '…' from your files.") instead of saying Notion isn't connected. "Analyze this document" with nothing named gets CXO's new lines. The routing half (which ask lands where) is still being screened.
  - #2139: "Create a doc from this conversation" on an OpenAI-only account no longer shows "Content type is required for content generation."
  - #2142: "Tell me more about the GitHub integration" no longer calls your calendar meetings repo activity.
- **Built, not yet live:** #2140 and #2143 ("what changed" says when a read failed, and names the window it read). It waits on CXO's words.
- **Staging:** an open chat kept its sign-in and history through a deploy (Web, 8 of 8 turns answered). That's PPM's condition for the quiet-windows ruling.
- **Google Calendar:** your "Piper Morgan (Alpha)" project is verified, and it's the one alpha uses, so nothing moves. The last proof is a connect from an account outside the Workspace domain, which needs you at a keyboard (Web can't sign in to Google).
- **Your account:** `mvp-tester` is the only admin.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## Your order (Thursday evening 10-22)

1. **The restarter (#2085, Class 4 must-close): push, then the second attended test.**
   - (a) **Push** Arch's approved fix (the restart without a lease) to `ops/restarter`, from your Mac's Terminal in any checkout:
     ```
     git fetch origin
     git checkout -B ops/restarter origin/ops/restarter
     git checkout origin/main -- .github/workflows/restart-alpha-postgres.yml
     git diff --cached --stat
     git commit -m "restarter: restart without a lease (2085 route 1)"
     git push origin ops/restarter
     ```
     The `--stat` line must show exactly one file; if it shows more, stop.
   - (b) **The second test,** after 17:41 and at your word: the same four steps as this afternoon (stop, dispatch, approve, undo only on a call). It passes if the restart step prints `restart accepted: HTTP 2xx`, alpha reads healthy within three minutes, and the alert comment posts. If Fly answers 401 or 403, the fallback is ruled and HOST-approved: re-mint the token with write rights on that one machine, by your hand.
   - (c) **Until #2085 closes,** HOST needs you to name who restarts the database by hand and how fast. That goes in the first partner's letter.
2. **The GitHub App (#2136, Exec owns):** CIO ruled to add Workflows write. Install on this repo only; the key goes to HOST's path, with no seat touching it.
3. **The held invitations:** confirmed inside the terms. HOST runs the send-morning checks; the sends are yours.
4. **The outside-account Calendar connect (#2087):** connect from an account outside the Workspace domain on alpha, then ask "What's on my calendar this week?"

## Version history

**v104 (07:14 10-23: alpha dc45f98938; 2132 handler half, 2139, 2142; the Anthropic cap decision)**, **v103 (19:21 10-22: alpha ac3c7581ff, the PR label; served results for 2127, 1524, 2131 and 2132)**, **v102 (17:45 10-22: alpha fc183c41bc, the Thursday update; 2127, 2132, 1524, 2131 live; the restarter push and second test)**,  **v101 (18:35 10-21: your evening order: the restarter setup, the staging key, the agents' GitHub identity, one Notion word)**, **v100 (15:05 10-21: alpha 76789a8988, the fifth update; 2108 hidden; the gate's first served quiet verdict)**, **v99 (14:27 10-21: alpha ae702f6a04, the fourth update; database back on 512 MB; hosted wizard for CXO's acceptance)**, **v98 (11:48 10-21: alpha's database unreachable since 10:55–11:21; #2124; updates held; the waiting build named)**, **v97 (10:05 10-21: alpha b28d46a97f; the quiet count's fail-open closed, Arch's read)**, **v96 (08:14 10-21: alpha 95dea16f50; the quiet gate's first served verdict, uptime served)**, **v95 (07:35 10-21: alpha 8e61423f1a, Wednesday's first update; the quiet count served)**, **v94 (19:22 10-20: alpha edf95b5c0c, the tenth update; the Notion lines, #2123)**, **v93 (17:38 10-20: alpha d1c64a92e3, the ninth update; the OAuth activity read, #2121)**, **v92 (16:46 10-20: alpha 71b4b15eed, the eighth update; the floor's reads line, #2120 and #2119 words)**, **v91 (15:59 10-20: alpha ee952c73eb, the seventh update; the #2112 floor fact and #2113's example)**, **v90 (15:07 10-20: alpha 86ee0bbfa1, the sixth update; CXO's words and #2118)**, **v89 (14:15 10-20: alpha 3b7fbb46fb, the fifth update; eight landings to Web)**, **v87 (11:01 10-20: alpha e729ba82d8, the third update; the #2101 fix live)**, **v86 (08:54 10-20: alpha 987dd10ed7, promotion 2 of 2; the thread surface, watchdog, #2098, #2097, #2106, #2102 Slack)**, **v85 (07:04 10-20: alpha ef907b2cd7, promotion 1 of 2; Monday's fixes live; Tuesday re-runs)**, **v84 (11:17 10-19, amended through 13:4x: alpha e801b1a309; every Monday card done; A2/A6/A7 findings filed)**, **v83 (11:39 10-18: #2080 and #2075 closed by CXO on Web's quotes; B1 re-run now optional; #2082/#2067/#2081 built for Monday)**, **v82 (09:54 10-18: D4 added, the #1982 MCP read on your A4 account, PA's ask)**, **v81 (08:40 10-18: alpha 83a2f4e40c, promotion 2 of 2; #2064/#2069/#2076/#2072/#2051 closed; D2 with your bank; reset script live)**, **v80 (06:45 10-18: alpha serves 47ba746bee; #2064 closed on your count; Sunday order + section D)**, **v79 (17:16 10-17: #2080 and #2078 landed for Sunday), v78 (16:39 10-17: A4 PASS, B1 create FAIL #2080), v77 (16:21 10-17: A5 PASS, #1913 closed), v76 (15:52 10-17: A4 invite pointer corrected), v75 (15:49 10-17: A5 path corrected), v74 (15:43 10-17: C1 done), v73 (15:28 10-17: C1 query corrected), v72 (15:24 10-17: C2 PASS; jump list links to the cards), v71 (15:21 10-17: A1 PASS), v70 (15:12 10-17, snippet added 15:15: your order at the top; A1 cut to what is left for your hand, read snippet inline), v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version.
