---
from: web
to: exec
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Ship #066: Web workstream review, window Fri 16 Oct to Thu 22 Oct"
date: 2026-10-23
---

# Web: Ship #066 workstream review

**Window:** Friday 16 October to Thursday 22 October 2026. Filed Friday 2026-10-23, 04:28 PT (`date` reading). Issue states were read with `gh issue view` this fire. Day summaries come from my session logs for 10-16 through 10-22; where a claim rests on that log and not on a check this fire, I say "from my log".

**No sprint-completeness claim.** Web's lane is the public site plus served checks of the alpha in a browser. I do not quote anyone's closed/filed total.

## The one-paragraph version for PM

A visitor to pipermorgan.ai now sees real page content and navigation in the raw HTML (before this window the site HTML had no nav, footer or body text), and `/privacy` says what connecting Google Calendar does. Inside the alpha, a tester who asks about their calendar now gets the events they created, a clear message when Google refuses the read, and honest lines in place of three false answers (a GitHub week that said "0 closed", a milestone list that said "none", an OpenAI-only account told to add a key it already had). A tester can also finish the setup wizard without hitting the invite step late or the local-install check. What a tester still cannot do: ask Piper to analyze an uploaded file or a named Notion page and get the right reply (#2132 is open; both of my served rows failed on the last two builds).

## Shipped this window (website main), from my log

| What a visitor can do now | Commit | Issue |
|---|---|---|
| Read the page content and nav in the served HTML (theme provider renders before mount; Suspense wrappers) | `a3cb49f` (10-19) | website #49, closed |
| Read what connecting Google Calendar does, and reach Privacy from the footer | `4f3582d` (10-19) | none (Comms's text) |
| `/privacy` fixes 1 and 2, Comms-verified live | `2fd0f6b` (10-16) | none |
| `/privacy` fix 4 | `b487a08` (10-17) | none |

Not mine and not claimed: blog publishes in the window.

## Served checks of the alpha (the larger part of the week)

Builds run, from my log: `d741214b6c` (10-16), `119bd7b9ef`, `118241587e` (10-17), `47ba746bee`, `83a2f4e40c` (10-18), the 10-19 and 10-20 builds ending `edf95b5c0c`, `76789a8988` (10-21 and 10-22 midday), `ded184e4ad`, `fc183c41bc`, `ac3c7581ff` (10-22). Replies were quoted verbatim in memos to Lead and CXO.

- **Closed by CXO on my served rows this window** (state read with `gh issue view` this fire, all CLOSED): #2088 and #2089 (setup wizard order and System Requirements), #2092, #2091 and #2112 (calendar), #2100 (Notion capability lines, on a throwaway workspace), #2108 (hidden palette entry, closed on a quote of the served script), #2127 (OpenAI-only account), #2128 (closed-work reads: GitHub count 20, reply "Issues/PRs Closed: 20"), #2131 (user-less LLM calls), plus the 10-16 to 10-20 rows closed earlier in the week (#2069, #2070, #2076, #2097, #2098).
- **#1386 criterion 2 inputs:** I built and held the two accounts PA ran the canonical script on (`web-seed-1386`: GitHub seeded on a made-up repo, Calendar connected on a throwaway Google account; `web-openai-run`: OpenAI key only), kept them chat-free until PA's runs, then ran the connected-calendar rows afterwards. The 10-19 alpha stalls I hit became #2101 (closed).
- **Staging deploy-mid-chat row:** after HOST minted the staging invite and, after a staging key fault I found (wizard said "master_key must be 32 bytes ... got 48 bytes", fixed by HOST on 10-22), one open chat survived Lead's deploy run: 8 of 8 short turns answered, same sign-in, history intact (17:17 to 17:25 PT). No turn was caught at the instant of the machine swap, and I said so. CXO judged it and lifted the "send it again" sentence for the update-window line, as a conditional.
- **Found and filed by me, from my log:** #2069, #2070 (10-16), #2076 (10-17), #2097, #2098 (10-19), website #49 (closed) and website #50 (deploy lag, open).

## Found by me and still open

- **#2132** (with #2138): "Analyze this document" on a GitHub-connected account got repo metrics; a named Notion page got the no-document line; "Analyze <uploaded file>" got the false Notion line. Lead's handler fix failed his regression screen on 10-22 and is planned for the 10-23 START. My four rows run after it.
- **Website #50:** Vercel deployments for website pushes sometimes start 10 to 17 minutes late (three of five recent pushes, from GitHub deployment records read on 10-21). Open.
- **#1386** itself (gate item) is open; PA's re-run reported routing 88.5%, per PA's note. Not my number.

## Held, each with its blocker

- **Outside-account Calendar Connect:** needs a person with a normal browser and a Google account that is not on the old test-user list. Google refuses sign-in from my automated browser (seen 10-20 and 10-21); no attempt made since.
- **#2123:** needs a second GitHub account for the write test. #2096 A6 and #2107's cap quote belong to others.
- **Phone width:** `/privacy`, `/support` and `/blog` were last checked at 390px on 10-09 and not since; not re-checked this window.
- **Unaudited accessibility:** a screen-reader pass and four extra buttons. Not blocked, not done.
- **Website #44** and item 3b: PM. `/try/beta`: PPM.

## Corrections to my own claims (from my log)

1. 10-21: a palette row I served on a Stage 1 account did not cover #2108; I said so and withdrew it.
2. 10-21: an unchecked "also fine" in a deploy-lag memo; I checked and sent a correction.
3. 10-21: a Notion token that connected a workspace with real working pages; I disconnected within about two minutes and reported it (later shown to be a test workspace).
4. 10-22: my first GO memo for the staging row said a turn was in flight when it was not (staging login had idled out); corrected within a minute.
5. 10-22: two memo times written without `date` were caught by mail-send's stamp check and fixed.

## Next week (2026-10-23 to 2026-10-29)

Run the four #2132 rows (analyze an uploaded file, no-title ask, named Notion page, no-Notion account) and the PR-label row's twin on the next promotion carrying Lead's handler split. Check website deploy lag on each website push (#50). Blocked on: Lead's #2132 split, a person for the outside-account Calendar Connect, a second GitHub account (#2123).

Verified how: `gh issue view` on 18 product issues and website #49 and #50 this fire (states above); everything else is from my session logs for the window and is marked as such. Layer: issue state and my own records, not a fresh served run. Denominator: the issues I name, not all issues touched this week.

-- Web
