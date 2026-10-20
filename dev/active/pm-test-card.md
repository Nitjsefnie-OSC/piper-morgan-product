# PM test card

**Owner**: Lead · **v85**, 07:04 10-20 · Mirror: https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi (this file wins between republishes) · older versions: `git log -p` of this file, and the history at the bottom.

**Alpha** https://alpha.pipermorgan.ai serves **`ef907b2cd7`** (promotion 1 of 2, 07:04 10-20, run 39435344767; /health healthy, database healthy). One more promotion possible today before 21:00. It carries every landing since `e801b1a309`, most of them from your Monday findings.
- **New on this build:** #2093 a status question gets its answer without setup boilerplate · #2091 "what's my agenda Thursday?" reads Thursday · #2092 a failed calendar read says so instead of "no events" · #2094 a list of todos in one message creates each · #2095 "what have I created this session?" names todos too · #2096 an in-app feedback page at `/feedback` · #2097 a created issue is confirmed by its number, and a same-title create asks before filing a duplicate · #2099 minting an invite refreshes the list · #2100 the capability reply says what chat reads from each integration (and that it can't read Notion pages yet) · #2102 no aiohttp session leak · the credential-store bounds and read cache for #2101 · the DB pool pre-ping · the Alpha Health Watch (every five minutes; mails you on a failure).
- **Not on it:** #2098 (the "change the title to X" fix was reverted on Arch's read; the consult lands this week).
- **Your account:** `mvp-tester` is the only admin.

**How to report**: paste the reply or a screenshot in chat; say the card number. Lead relays to the judge named on the card and updates this page.

## Your order (Tuesday 10-20): nothing gates today; these are the re-runs of what you found Monday, any order.

1. [A2](#a2) **calendar in chat, again** (#2091, #2092): on your calendar account, `what's my agenda Thursday?` → the Thursday events, not today's. Then `Do I have any meetings this week?` → the week's events; if the reply says none, say whether that week really is empty (that answer settles #2092: a read failure now says it failed instead of "no events").
2. [A7](#a7) **todos** (#2094, #2095): `Add three todos for the launch: draft brief, book venue, send invites` → three todos with those words; then `What have I created this session?` → names the three.
3. [A6](#a6) **feedback** (#2096): `/feedback`, send a note → "Thanks, we got it."; the admin list is `GET /api/v1/admin/feedback` on your admin session.
4. [D5](#d5) **mint refreshes** (#2099): `/settings/invites`, mint one → the masked row appears without a reload; revoke it.
5. Optional: [B1](#b1) **capabilities** (#2100): `what can you do right now?` → lists what chat reads from each connected integration.

Web runs the #2097 create and duplicate chain, the #2100 Notion quotes, the #2103 toast read, and the full canonical run with PA's streams on, which is what closes #2101 (the Monday stalls). CXO judges; Lead posts results on the issues.

## Not on your list

#2101 (the stalls) closes on one full canonical run with no stall, not on your hand. #2103 (121 toast calls that throw) is filed, not fixed; the Invites page is the one page already on the working toast. #2089 (hosted wizard's local system check) waits on CXO's shape. #2018 and #1595/#1386 are the standing items.

## Version history

**v84 (11:17 10-19, amended through 13:4x: alpha e801b1a309; every Monday card done; A2/A6/A7 findings filed)**, **v83 (11:39 10-18: #2080 and #2075 closed by CXO on Web's quotes; B1 re-run now optional; #2082/#2067/#2081 built for Monday)**, **v82 (09:54 10-18: D4 added, the #1982 MCP read on your A4 account, PA's ask)**, **v81 (08:40 10-18: alpha 83a2f4e40c, promotion 2 of 2; #2064/#2069/#2076/#2072/#2051 closed; D2 with your bank; reset script live)**, **v80 (06:45 10-18: alpha serves 47ba746bee; #2064 closed on your count; Sunday order + section D)**, **v79 (17:16 10-17: #2080 and #2078 landed for Sunday), v78 (16:39 10-17: A4 PASS, B1 create FAIL #2080), v77 (16:21 10-17: A5 PASS, #1913 closed), v76 (15:52 10-17: A4 invite pointer corrected), v75 (15:49 10-17: A5 path corrected), v74 (15:43 10-17: C1 done), v73 (15:28 10-17: C1 query corrected), v72 (15:24 10-17: C2 PASS; jump list links to the cards), v71 (15:21 10-17: A1 PASS), v70 (15:12 10-17, snippet added 15:15: your order at the top; A1 cut to what is left for your hand, read snippet inline), v69 (08:1x 10-17: alpha `118241587e`, slot 2 of 2; every card live, A1 and C2 included), v68 (07:1x: slot 1), v67 (A1 gap #2072 noted 19:3x), v66 (B3 gap 17:5x), v65 17:09 10-16: alpha promoted to the new build, every card is live.** v64 (16:4x) for xian's live session**: one card per test, only the tests that need xian's hand or that nobody has passed yet. Closed rows, Web's rows and the history are gone from this page; `git log -p` of this file keeps every earlier version.
