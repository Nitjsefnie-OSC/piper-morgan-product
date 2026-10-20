# Omnibus Log: October 19, 2026

**Day**: Monday (all times and dates Pacific, PDT)
**Sessions**: 11 role sessions in 11 log files (Documentation Management, Head of Sapient Trust, Unicorn Web Designer,
Communications Director, Chief Architect, Chief Experience Officer, Principal Product Manager, Lead Developer, Piper Alpha,
Chief of Staff, Chief Innovation Officer) and no Coding Agent subagent logs (prog-code), plus 6 non-log files in the same
directory that I read in full and 1 harness script that I opened only at its header (see Sources). **One of the 11 role log
files carries no day-close marker: HOST** (see Sources).
**Day Type**: HIGH-COMPLEXITY: A PRODUCTION DATABASE OUTAGE, THEN A DEFECT-DRIVEN ADMISSION SURGE. The production Postgres
stopped listening at about 05:25 and sign-in on alpha returned 500 until 09:52 (Lead, PA). The 07:00 promotion died in its
release command and left alpha unchanged. After the database came back, two promotions landed (11:17 and 13:43), xian worked
the whole test card by hand between 11:40 and 14:07, and the defects that came out of it took the MVP list from 7 open to 13.
Two alpha stalls, one reverted build and one health-watch alert path filled the afternoon.
**Justification**: Eleven role sessions and at least eight threads crossing three or more roles: the database outage and
restart (Lead, HOST, PA, Exec, Web, Arch, PPM, CIO, CXO, xian), the admin grant and the misquoted ruling (xian, Lead, HOST, CIO,
Exec), the card-driven defects #2091 to #2096 and their landings (xian, Lead, CXO, Arch, PPM, Exec), the #1386 early run and
the two alpha stalls (Web, PA, PPM, CXO, Lead, HOST, Arch), the Google verification and /privacy work (xian, PPM, Comms, Web,
Lead, Exec, HOST), the health-watch alert (HOST, Lead, Exec, xian, PPM), the Tuesday-post forensics (xian via Comms, Arch,
Lead, Comms) and the piper-guards and draft-age work (CIO, Pard, CXO, Exec). The sub-type is an INCIDENT-THEN-ADMISSION DAY
because the first half is dominated by the outage and the second half by admissions that follow xian's own test run. The label
is mine.
**Git Commits**: 790 on origin/main by committer date (00:00 to 24:00 PDT 10-19). Verified how: `git fetch origin main` was run
first (it printed `* branch main -> FETCH_HEAD`), then `TZ=America/Los_Angeles git log --since="2026-10-19 00:00"
--until="2026-10-20 00:00" --oneline origin/main | wc -l` printed 790, with `origin/main` at `0102e7c239` at that moment (a
10-20 commit, outside the range). The first commit of the day is a `chore(usage)` row at 00:23:10 (`8a53c6fded`). The last is
`log(exec): 10-19 day closed` at 23:09:17 (`bf75f9252d`). Counted by leading subject text on the same range: 232 `mail(`, 172
`log(`, 8 `chore(usage)`, 0 containing `hb`, 206 starting `Merge`, leaving 172 other commits. The 172 break down as 39 `exec`, 26
`docs`, 19 `web`, 16 `arch`, 13 `comms`, 11 `fix`, 9 `feat`, 8 `gate`, 6 `plan`, 4 `test`, 2 each `perf` and `ci`, and 17 singles
(1 each `style`, `stop`, `refactor`, `methodology`, `hooks`, `briefs`, `decisions.log`, `piper-guards`, one `Revert` of a
`feat(2098)` subject, 3 `carry-forward(lead)` and 5 beginning `1386:`). The four named buckets plus the 172 sum to 790. The
10-18 omnibus reported 336 on the same basis, so the day is about 135 percent larger (computed from the two counts, 454 more on
336). No source log quotes a commit total for 10-19. Layer: git history on the local object store, not the GitHub API. I did not
inspect what the 206 merge commits or the 39 `exec` commits contain.

---

## Sources

Session logs (all in `dev/2026/10/19/`), role logs first, line counts from `wc -l`:
- `2026-10-19-0412-docs-code-log.md` (Docs, 62 lines)
- `2026-10-19-0416-host-code-log.md` (HOST, 145)
- `2026-10-19-0618-web-code-log.md` (Web, 132)
- `2026-10-19-0619-comms-code-log.md` (Comms, 84)
- `2026-10-19-0627-arch-code-log.md` (Arch, 105)
- `2026-10-19-0631-cxo-code-log.md` (CXO, 132)
- `2026-10-19-0633-ppm-code-log.md` (PPM, 539)
- `2026-10-19-0641-lead-code-log.md` (Lead, 322, read in two pages)
- `2026-10-19-0647-pa-code-log.md` (PA, 316)
- `2026-10-19-0653-exec-code-log.md` (Exec, 199)
- `2026-10-19-1007-cio-code-log.md` (CIO, 80)

Non-log files, all read in full:
- `1386-criterion-3-calendar-rows-and-c2b-slack-addendum-2026-10-19.md` (23 lines): CXO's scenario rows for #1386 criterion 3
  (C2b on Slack, calendar rows K1 to K6, C3 amended, the scenario B re-run), written for the run after Tuesday's promotion.
- `canonical-retest-1386-alpha-20261019-1520-PARTIAL-report.md` (115) and `...-results.csv` (7): the 15:20 stopped run, 4 queries.
- `canonical-retest-1386-alpha-20261019-1613-PARTIAL-report.md` (140) and `...-results.csv` (32): the 16:13 stopped run, 15 rows.
- `root-readme-review.md` (10): Docs's weekly audit note for #2084.

Not read in full: `canonical-retest-1386-alpha.py` (1291 lines), PA's hosted copy of the harness. I read its first 30 lines (the
docstring) only, because the logs describe what it does and it is code, not a log. It is excluded from the totals below.

Total 2443 source lines read: 2116 in the 11 role log files and 327 in the 6 non-log files. Verified how: `ls -la
dev/2026/10/19/` and `wc -l` listed 11 role logs and 7 other files (18 in all) before I started. I read all 18 or opened them as
stated above.

There are no prog-code logs for the day. Lead's lanes (`lead-2083`, `lead-2083b`, `lead-2081b`, `lead-2093`, `lead-2092`,
`lead-2095`, `lead-2094`, `lead-2096`, `lead-ci2092`, `lead-2098`, `lead-2097`, `lead-2085`, `lead-2099`, `lead-2101`,
`lead-2102`, `lead-2100`) are named in Lead's log and have no log of their own in the directory. Comms and Arch each ran an Opus
read-only subagent for the forensics work (Comms, Arch), and neither has a log of its own.

**Cross-reference gate**: roles mentioned without a log in this repo: Pard (CIO, HOST, Exec, Web, PA, CXO, as the owner of the
piper-guards rollout and the Anthropic key questions). Pard is a cross-project agent whose repo takes mail, so no `dev/` log is
expected. No source-set role is missing, so I did not ask PM.

**Day-close status** (re-grepped with `grep -c '^<!-- DAY-CLOSED'` per file at the time of writing): **10 of 11 role log files
carry a marker** (Docs, Web, Comms, Arch, CXO, PPM, Lead, PA, Exec, CIO). **One carries none and is unclosed: HOST.** HOST's last
entry is a routine 21:26 scheduled wake ("quiet") with no day summary and no sign-off block, and the log's final line is a
"Verified how" line. `git log` on the file shows its last commit as `932887418d` at 21:26. Lead's marker reads `<!-- DAY-CLOSED
2026-10-19 lead-code -->` (no colon) and Exec's reads `<!-- DAY-CLOSED: 2026-10-19 exec -->`. Both match the grep. No closed log
has entries below its marker.

**Reading coverage**: every file listed above was read in full except the script, as stated. Compression: 2443 source lines to
this file's line count. Every role appears in the timeline.

---

## Executive Summary

### Core Themes

1. **The production database was down from about 05:25 to 09:52, and the 07:00 promotion failed because of it.** Lead's 07:00
   dispatch (run 39265029915) died at 07:02 in `release_command` on `psycopg2.OperationalError ... server closed the connection
   unexpectedly`, so alpha stayed on `83a2f4e40c`, and per the grant's 10-16 widening a dispatch that leaves alpha unchanged does
   not use a slot (Lead). Sign-in on alpha returned 500 and `/health` still said healthy (Lead, HOST, Exec, Arch, PPM, Web all
   probed). Lead filed #2083 (`/health` blind to the database) at 07:00. HOST declined to run `fly` in an unattended fire at
   07:08 under its standing rule and asked xian to run five read-only reads or type "go" in its pane (HOST). PA ran the five
   reads itself at 09:48 and found the machine `started` but Postgres not listening since about 05:25, disk 84.9 percent free, no
   machine event since 10-16 13:38 (PA, Lead). Lead filed #2085 (no restart or alert for a dead Postgres) at 09:50. xian
   restarted the database machine and the login probe read 401 at 09:52 (Lead, PA, Exec at 09:53, HOST at 10:03). Lead's count of
   the outage is 4 hours 27 minutes. Verified how: the Lead, PA, HOST and Exec entries agree on cause and time, and CIO repeats
   the 05:25 to 09:52 window. I probed nothing myself. One source gives a different recovery time, see Divergences.

2. **#2083 landed in the middle of the outage, broke main for 43 minutes and was fixed with a deviation Arch accepted.** Arch
   ruled at 09:28 (HTTP stays 200, body carries `services.database` and `status: degraded`, bounded probe, no DSN text). Lead
   landed `13716892ee` at 09:36. Tests went red at 10:01 on three `tests/security/test_manager_isolation.py` cases that died on
   asyncpg "another operation is in progress" and "different loop", because the probe bound the global engine to the TestClient
   loop (Lead, CIO at 10:07 saw the red, HOST at 10:30 asked Lead to classify it). Lead reproduced it locally (3 failed, then all
   passed), landed `84de766e0d` with a throwaway one-connection engine, and Tests went green at 10:44 (run 39291962885, Lead,
   HOST at 12:26). Arch had validated `9e40f69472` at 10:10 on the pins alone, and recorded at 12:27 that the validation had
   missed the red on that sha and that Lead's fix departs from its item 2, which it then accepted. Nothing was promoted on the red
   sha (Lead, HOST).

3. **The admin grant had matched nothing since the 09-22 cutover, and a misquoted ruling cost time.** The reset mint for `dinp`
   found no such user at 09:5x (Lead). xian ruled at 10:01 that his `mvp-tester` account gets admin ("it has wasted at least half
   a day", quoted by Lead and CIO). His psql showed 11 accounts, none admin, then `UPDATE 1` at about 10:13 (Lead, HOST via
   Lead, Exec). So every `require_admin` route had refused everyone on alpha since the cutover until then. Lead filed #2086 (a
   fail-loud migration to make the grant durable). Lead's memo had quoted HOST's 10-18 ruling 1 as "admin stays on dinp only", and
   HOST's text says "xian's account only ... no agent test account gets is_admin". Lead owned the misquote at 10:23, and CIO
   recorded it as the third instance of its m-52 pattern and promoted the entry to PROVEN the same day (CIO at 10:07). Verified
   how: Lead, HOST, CIO and Exec agree on the sequence. I did not read HOST's original comment.

4. **Two promotions landed after the database came back, and Web's rows closed #2067 and #2082.** Lead dispatched at 11:13 and
   alpha served `f9fb8b750b` at 11:17 (run 39300767619), carrying #2082 (name first), #2067 (the signed-out modal), #2081 (the
   admin Invites page), #2083, the reset-script fix and the #2069 mirror. It dispatched again at 13:40 and alpha served
   `e801b1a309` at 13:43 (run 39321277552), carrying the Invites list-refresh change `350c8c4dc9`. Web's rows on `f9fb8b750b`
   (11:24) read #2082 5 of 5 and #2067 5 of 6 steps as written (Web, Lead). CXO closed both at 12:32 on those rows (CXO, PPM,
   Lead). Lead's log says both slots were used (11:17, 13:43), and Web, PA and Exec agree on the two shas. Verified how: the
   Lead, Web, PA, Exec and CXO entries match on shas and times. I read no `gh run view`.

5. **The must-close set emptied by 13:39, and xian's own test run then filled it again.** #1852 closed at 11:10 (Lead). #2077
   closed at 12:34 on xian's console read of length 0 (Lead). #2081 closed at 13:23 on HOST's pass (Lead, HOST), #2078 at 13:29 on
   xian's wizard run and the My Projects read (PA, Lead, PPM), #1982 at 13:43 on the connector retry (PA), #2017 at 13:53 on
   xian's A3 (CXO, PPM). Lead's 13:39 entry records the must-close set as empty. Then xian ran the rest of the card between 13:50
   and 14:07 (A2, A3, A6, A7, B2, B3) and the failures became #2091 (weekday target ignored), #2092 (zero events from a calendar
   whose Test passes), #2093 (setup boilerplate for "Is my calendar connected?"), #2094 (a list of todos in one message is
   refused), #2095 (the ledger does not record todos) and #2096 (no feedback path). xian admitted #2091, #2092 (handler half),
   #2094, #2095 and #2096 at 14:35 via Exec, then #2097 and #2098 at about 15:05, #2101 at about 16:56 and #2100 at 17:53 (PPM,
   Exec). PPM also admitted #2089 at 14:13 on xian's word accepting CXO's ruling. PPM's day arc: 4 closes and 10 admissions, gate
   7 to 13 open, must-close 10, and no date proposed. Verified how: the PPM ledger, Exec's rollup entries and Lead's log agree on
   each step. I ran no `gh` command. See Impact Measurement.

6. **The admitted fixes landed on main between 14:44 and 18:05, one was reverted, and a stall in alpha became the new risk.** Lead landed
   #2093 and #2091 (14:44, head `c5800bc7c7`), #2092 handler half (14:56, `6c4eba70f5`), #2095 (15:07, `7b5bab26c3`), #2094
   (15:22, `0eea5b2533`), #2096 (15:59, `f9a068c73b`), #2097 (16:15, `0d95315abf`), pre-ping (16:15, `fb39f62798`), #2099 (16:46,
   `aff49b17f0`), #2102 (17:20, `fffa1d536d`), #2100 (18:05, `5e17e627a2`) and the #2101 bounds. #2098 landed at 15:52
   (`e928d3e507`), Arch ran it on prose at 16:03 and ruled NOT ACCEPTED because the 12-phrase substring binder retitles a draft on
   "we should call it out in the release notes". Lead reverted it (`f260d8ed5b`), so Tuesday's promotion carries the others and
   #2098 is rebuilt on the armed-turn consult (Lead, Arch, CXO, PPM). Everything landed rides Tuesday's 07:00 slot (Lead, Web,
   CXO).
   Verified how: Lead's landing entries with shas, Arch's validations, PPM's tally. I did not read the commits.

7. **The #1386 early run and two controlled runs found alpha stalling under one scripted session.** Web ran scenarios B and C on
   `web-oauth-test` between about 14:42 and 14:47: B failed (B3 filed as #2098, the follow-up as #2097), C1 and C2 passed, C3
   advertised Notion, Slack and Calendar (filed as #2100 by CXO), and scenario A was not run for lack of an unspent invite code
   (Web, CXO, PPM). At 14:53 to 15:03 `/health` flapped, with the database reading unreachable on 3 or 4 of about 12 or 13 reads
   (Exec, Lead, HOST, PA, PPM). PA and xian's reads showed Postgres healthy throughout (12 of 300 connections, memory wait 0
   seconds) and only fly-proxy EOFs at 14:56:20 and 15:02:50, with the app's own Fly check failing until 15:03:20 (PA, Lead, HOST,
   Exec). Web's canonical run at 15:19 stopped before Q5 after 4 queries and at 16:09 before Q17 (PA's health gate), leaving
   partial files. PA's stream read of the 16:09 window found no restart, no out-of-memory and no traceback, only 33 seconds of
   silence inside Q16 and a Fly check that failed at 16:13:18 and passed at 16:13:48. Lead's reading is synchronous credential
   store reads on the event loop, which Arch ruled should move to a `to_thread` surface (tomorrow) after a process-wide cache
   (landed `2acf8af82d`). xian admitted #2101 as a Class 4 must-close that closes on one full canonical run with no stall. Also
   found by the run: the Anthropic judge model in the old harness (`claude-sonnet-4-20250514`) returns 404, so no quality score
   was ever produced, which PA fixed in `0115f2ee47`. Criterion 5 reads 4 of 4 met on xian's `alembic check` paste (PA, PPM).
   Criterion 2 is held for Tuesday. Verified how: the PA, Web, Lead, HOST, Exec and PPM entries and the two partial reports
   agree. I measured nothing on alpha.

8. **Google verification, /privacy and the invitation wording moved together.** xian chose External plus In production for the
   consent screen after Lead showed the Internal audience bars outside accounts (Lead at 11:56, 12:11). He verified the
   `pipermorgan.ai` domain by a TXT record and Branding read "verified and being shown to users" within minutes (Lead at 12:26).
   PPM built a beta-formalities checklist on his word and a #2087 submission kit (PPM at 12:29, 14:28). Comms drafted the
   /privacy Google user-data paragraph and the Calendar fix, found the site footer had no Privacy link, and xian gave the go at
   about 15:2x. Web pushed website `4f3582d` at 15:34, the live quote was blocked by a 403 from curl, then Web's browser read at
   15:50 confirmed the text and the footer link, and the server-rendered HTML lacked the footer because the theme provider
   returned null until mount. xian said yes to the server-render fix, and Web shipped website `a3cb49f` by 17:03 (website #49
   closed). xian also ruled that the invitation names Google Calendar with caveats and that 10-23 "isn't sacred" (PPM, Exec,
   Lead). Comms drafted the Terms invitation section and the four known-issues lines, revised on CXO's wording reviews. Verified
   how: the PPM, Exec, Comms, Web and Lead entries agree. I opened no page.

9. **The health-watch alert reached xian at 18:46 after a notification-address fix, and track 2 is still not accepted.** HOST
   scoped an off-Fly Actions watch under #2085. Lead landed it at 17:25 (`66c3050358`, five probes one minute apart, fail on 3 of
   5, `force_fail` dispatch). The forced run's failure email did not arrive (xian, via Exec at 17:53). HOST gave a checklist, and
   xian found at about 18:40 that the account's default notification address was defunct and moved it. Exec dispatched a second
   forced run at 18:42 (run 39354889203, failed at 18:46) and the mail arrived at 18:46:35 (Exec, Lead, HOST). Track 2 stays open
   until Lead's assigned-issue backup alert lands and is forced once on Tuesday (Lead, PPM, Exec). The same evening Exec asked who
   authorized the alpha OAuth app on the account's notices. Web counted six authorizations, all on the machine account. No seat
   connected as the account that got the notices (Web, PA, HOST, Lead), and xian's security-log screenshot showed normal entries
   (Exec at 18:18). Verified how: the Lead, HOST, Exec and PPM entries agree on times. I saw no mail.

10. **A fact-check changed the Tuesday post, and the forensics record was corrected.** At 09:28 xian recalled that the POC
    summarized documents, and Comms ran an Opus read-only subagent. Comms's first finding blamed the 10-01 `docs:` commit.
    Arch read the sources itself (and ran a second Opus sweep of 36,177 commits) and found the loss was an engine swap on
    2025-08-22 (`2ad8d639dd`), with the 10-01 commit (`effa5fe2a6`, on main, while `aad66d9d1` is off main) deleting code the UI
    no longer reached. Arch wrote `docs/internal/architecture/audits/lost-working-code-2025-08-to-10.md`. Lead put a note on top
    of the 08-15 forensics doc and retitled #1624, and Comms confirmed both at 12:19 (Comms, Arch, Lead). The Tuesday post's
    title became "The Phantom Feature" on the calendar, with two other retitles, and the H1 in xian's draft still read the old
    title at 21:19 (Comms, Docs). Verified how: Comms's, Arch's and Lead's entries agree. I did not open the audit.

11. **Control-plane work ran alongside.** CIO promoted m-52 to PROVEN, extended the stamp check to `decisions.log`, sunset the
    dead `context-usage-reminder` hook, decided each piper-guards rule from a transcript parse (1 real deny, 0 false positives
    across 1,224 Bash calls, 9 Agent calls and 23 Write/Edit calls), built a draft-age check for mail-send after the stale
    11:19 board memo, repaired two mail-send test harnesses it had left red for three days, and shipped piper-guards 0.2.1 for
    the status-line bug (CIO). Pard restarted CXO onto piper-guards at 14:47 (CXO, CIO, Exec). Docs ran the weekly audit #2084:
    links 0 broken of 69, patterns 75 of 75, omnibus 14 of 14, staleness 32 need attention (Docs at 10:15). Verified how: each
    seat quotes its own runs. I re-ran nothing.

### Technical Details

1. **Landings on main** (from Lead's log, in order of the log). `13716892ee` (#2083), `84de766e0d` (probe fix), `350c8c4dc9`
   (Invites no-store and optimistic revoke), `c5800bc7c7` (#2093 and #2091), `6c4eba70f5` (#2092 handler half and Test real read),
   `7b5bab26c3` (#2095), `0eea5b2533` (#2094), `f9a068c73b` (#2096), `2e3524a808` (router-gate fix), `e928d3e507` (#2098, then
   reverted `f260d8ed5b`), `0d95315abf` (#2097), `fb39f62798` (pre-ping), `aff49b17f0` (#2099), `1a38f0d775` and `6aae6ab6e4`
   (#2101 bounds and clock fix), `fc17eab244` (Arch's follow-ups), `3a837f20fa` (burn-down shrink-lock rows), `fffa1d536d`
   (#2102), `3fbbb00f6c` (binder file ratchet), `2acf8af82d` (process-wide read cache), `66c3050358` (health watch),
   `f9ddb2ba88` (radar pin fix), `5e17e627a2` (#2100). I did not check any of these shas in git.
2. **Counts quoted by Lead at merge**: re-run sets of 1447 passed with 2 skipped (#2083, first cut), 1591 passed with 3 failed
   (the probe fix set, where the 3 failures were Lead's own order-dependent pin, fixed, and two known backlog rows), 8940 passed (#2095), 8835 passed (#2098), 8992 passed with 8
   skipped (#2096), 9360 passed with 9 skipped (#2097), 9365 passed with 8 skipped (#2102), 9381 passed with 8 skipped (#2100).
   Lead also wrote a count into a commit message before the suite was read (see Session Learnings). They are Lead's runs and I
   re-ran none.
3. **Tests runs on main and what turned them red.** 10:01 to 10:44, #2083's probe (above). About 15:26, Router Pattern
   Enforcement failed "Check Direct Adapter Imports" on `services/integrations/calendar/oauth_handler.py:415` after the #2092 and
   #2095 merges, fixed at `2e3524a808` (run 39337166144, success) (Lead, HOST). The same sha's Tests run failed on the
   hand-kept census pin because Lead's #2094 corpus row moved 598 to 599 (Lead). Burn-down shrink-lock on four rows that now
   pass, fixed at `3a837f20fa` (Lead). Security Tests red at `1a38f0d775` on Lead's own pin patching `time.monotonic`, fixed at
   `6aae6ab6e4` (Lead, Exec). Two radar pins red on `66c3050358`, fixed at `f9ddb2ba88` (Lead, Arch). Tests went green on
   `f9ddb2ba88` (run 39349405753) at 18:00 and on `5e17e627a2` (run 39351429504) at 18:20 (Lead). HOST, CIO and Exec each read
   their own red and green states.
4. **#2092 mechanics.** The adapter swallowed a Google 403 "insufficient authentication scopes" into an empty list, so a Test
   that only refreshed the token read healthy while chat read "no events". Lead's fix classifies the read error (never the
   exception text), makes the handlers say "I couldn't read your calendar" when a read comes back empty with an error, and makes
   the Settings Test do one real `events.list(maxResults=1)`. The grant half stays in xian's console (Lead at 14:07, 14:13).
5. **#2101 mechanics.** The hosted credential backend `EncryptedDBCredentialStore` does a synchronous psycopg2 connect per read
   on the event loop, and a chat turn reads several credentials (Lead at 16:46). Lead's bound is a 5 second connect timeout, a
   60 second read cache and a slow-read warning. Arch found the first cache was per instance (43 construction sites) and could
   serve a deleted credential for 60 seconds, so Lead made it process-wide (Arch at 17:09, Lead at 17:23). Tomorrow's build is
   the `to_thread` surface with a generation counter and a shrink-only ratchet on sync credential calls inside `async def`.
   Lead states the cause is the "leading mechanism, not proven".
6. **Arch's rulings of the day** (Arch): #2083 (09:28), the 2025-08 loss audit (09:52), the binder ratchet by glob on #1943 (298
   literals in 24 files by an AST count, landed `3fbbb00f6c` and matched by Lead), #2091, #2094 and #2095 shapes and an ADR-078 D1
   amendment, #2096 as census 29 to 30 with five conditions and the existing PM-005 store, the "Honestly," stem (floor prompt
   "Honest beats agreeable." changed to "Plain beats agreeable." and a NEVER line added), #2100 `CHAT_READS`, #2098 NOT ACCEPTED,
   and #2101 (async surface via `to_thread`).
7. **Held for Tuesday.** The first promotion from 07:00 carries the fixes above and the rows owed after it are #2091 to #2097,
   #2098 B3 (pre-fix behavior), #2103's served pass, the Calendar rows K1 to K6, C2b on Slack, C3, #2018's recovery read,
   #2088 and #2089, #2041, the canonical re-run on `0115f2ee47` or later, and scenario A (CXO, Web, PPM). MCP `git_sha` still
   reads `unknown` because there was no MCP deploy (PA at every fire).

### Impact Measurement

1. **Issues filed**: the numbers #2083 to #2103 (21 numbers) each appear in the logs as new today. Filers per the logs: Lead for
   #2083, #2085, #2086, #2087, #2088, #2089, #2091 to #2096, #2099, #2101 and #2102, PA for #2090, Web for #2097 and #2098, CXO
   for #2100, the weekly audit workflow for #2084, and Lead's log says #2103 was "filing" at 16:46 with no filer named in any
   log I read. Website #49 was filed and closed by Web. Verified how: I collected the numbers from the logs. I did not run `gh
   issue list`, so the range may include a number the logs mention that was filed earlier.
2. **Issues closed**: 11 product issues per the logs: #1852 (Lead 11:10), #2083 (Lead 11:19), #2067 and #2082 (CXO 12:32), #2077
   (Lead 12:34), #2081 (Lead 13:23), #2078 (PA 13:29), #1982 (PA 13:43), #2017 (CXO 13:53), #2090 (PA 15:04) and #2084 (Docs
   10:15), plus website #49 (Web). CXO's 21:31 day arc also lists #2075, #2080 and #2079 as closed, which the 10-18 omnibus
   records as closed on 10-18 (see Divergences).
3. **MVP list**: 7 open at 06:33 (PPM, Exec), 6 after #2067 (12:32), 5 after #2077 (12:34), 4 after #2078 (13:29), 3 after #2017
   (13:53), 4 after #2089 (14:13), 9 after five admissions (14:35), 11 after #2097 and #2098 (15:05), 12 after #2101 (about 16:56),
   13 after #2100 (17:53) (PPM). Exec's 06:53 and 18:54 entries and CXO's 14:24 count agree on the start, a mid-day point and the
   end. Arithmetic check: 7 minus 4 closes plus 10 admissions is 13. Must-close at close is 10 (PPM). PPM notes its criteria
   script lagged `gh issue list` twice after milestone edits and quotes the `gh` figure. Verified how: I ran no `gh` command.
   These are PPM's quoted reads and ledger rows 22 to 31.
4. **Gate placements and ledger**: PPM placed #2083, #2085, #2086, #2087, #2088, #2090, #2093, #2099, #2102 and #2103 on
   Production, #2084 on Ongoing, and wrote ledger entries 22 to 31 with 0 days moved. PPM proposed no date, and xian's quoted
   rulings are "five admitted, ordered first, a fallback over a date move" (14:35) and "10/23 isn't sacred" (15:05).
5. **Promotions**: 2 reached alpha (11:17 and 13:43), 1 dispatch failed and did not count (07:00). Alpha `/health` at close is
   `e801b1a309` with the database healthy in Web (21:18), Arch (21:27), CXO (21:31), PPM (21:33), PA (21:48) and Exec (23:08). Landings
   behind alpha at close: everything after 13:43 in Technical Details item 1.
6. **Served rows**: on `f9fb8b750b` Web reports #2082 5 of 5 and #2067 5 of 6 steps (it dropped the session by a server-side
   logout because `auth_token` is HttpOnly). Through xian's hand: D1 (#2077 length 0), D2 (#2078 code to `test-acct-2078`), D4
   (#1982, second attempt), D5 (#2081, 2 minted and 1 revoked), A3 pass, A2 fail, A6 and A7 findings, B2 and B3 pass (Lead).
   #1386 early run on `e801b1a309`: B 4 of 4 steps by Web's count with B3 failing and the retry duplicating a create, C 3 of 4,
   A 0 of 4 (Web). Canonical partials: 4 of 61 queries then 15 of 61, with routing 4 of 4 and 13 of 15 and quality unscored
   (judge 404) in both CSVs and reports.
7. **Reds and checks**: main had several red windows, each from a different cause, as listed in Technical Details item 3. The
   times the logs give are 10:01 to 10:44 (Tests), about 15:26 (Router Pattern Enforcement and Tests, cleared with a green router
   run on `2e3524a808` by 15:45 to 15:57), Security Tests red at `1a38f0d775` (reported by Exec at 16:59) and Tests red on
   `66c3050358` (Lead 17:44), with Tests green again at 18:00 and 12 of 12 workflows green at HOST 18:10, Exec 18:54, Lead 21:51
   and CIO 22:07. `whats-armed.sh` read 31 checks and 30 armed at CIO's 10:07 START, then 30 checks and 29 armed after CIO retired
   the context hook, and the same at 22:07. I assembled the windows from several logs and did not read the CI runs.
8. **Ship #066 count**: PPM reports no PPM-judged admission today, so the count stays at 3 (#2048, #2052, #2080).
9. **Mail**: Comms sent 7 memos and says all landed. I did not count other roles' mail from logs. The git `mail(` count (232) is
   the only whole-day figure.

### Session Learnings

1. **Quote the text before putting it in quotation marks.** Lead wrote HOST's ruling as "admin stays on dinp only" and HOST's
   text says otherwise. CIO counted it as m-52's third instance. Lead's practice now: quotation marks only after opening the
   text, otherwise say paraphrase (Lead, CIO, HOST).
2. **A re-run set narrower than the failing layer fails again.** Lead's #2083 re-run never ran a DB-backed test after the health
   pins (the red at 10:01). Its #2092 landing read only the pytest tail and missed the router gate (red at about 15:26). Its #2102
   set omitted `tests/unit/services/radar` (red at about 17:40). Lead added the router gate script, the radar tests and a note on
   corpus hand rows moving the census pin to its set (Lead). CIO's own harness fix on the same day has the same shape (CIO).
3. **Read the summary line before writing a number.** Lead wrote "310 passed" in a commit message before the suite finished, and
   the suite read "224 passed, 4 skipped, 4 errors". The fix patched a module-level clock, not `time.monotonic` itself, since
   asyncio reads it. Lead corrected the issue and recorded: never chain commit and push behind a `pytest | grep` pipeline
   (Lead).
4. **A sent draft is a re-verification event.** Lead's 11:19 board memo was a 06:45 draft sent with a refreshed sha and date and
   an unread body that still said `dinp` five hours after xian's ruling. Exec caught it at 11:23. CIO's retro lists why nothing
   mechanical caught it and built a draft-age warning in mail-send (CIO, Lead, Exec).
5. **A validation that ran only the pins can miss the layer that matters.** Arch validated #2083 at 10:10 with the five pins and
   did not check Tests on that sha, which was red. Arch recorded the correction at 12:27 (Arch).
6. **A pass the logs cannot corroborate is not a pass.** PA's #1982 first run answered from the local plugin, which PA saw
   because the MCP log showed a session that only listed tools. PA held #2078's close on one read (My Projects), and the read
   confirmed the widened half of the fix (PA).
7. **Give an editor path, not a clipboard pipe, for a credential file.** Exec's `pbpaste` one-liner left the invite file empty
   twice, and xian typed the code at a prompt once, so it is in his shell history (Exec). Exec also ran two unquoted heredocs
   that executed backticked text inside memos and quoted all later ones.
8. **A binder is a binder.** Arch's #2098 test: run the extractor on prose before accepting it. A word-set detector retitled a
   draft on "we should call it out in the release notes" (Arch, Lead).
9. **One probe does not make a steady state.** PPM kept the #1386 hold until Lead's criterion (30 healthy `/health` reads at 20
   seconds and 6 of 6 login probes 401) was met at 15:15, and lifted it on that count, not on Exec's six reads (PPM, Lead).
10. **Retention rule for raw log streams.** HOST ruled that PA's raw `fly logs` streams stay in scratch, are never committed and
    are deleted at STOP. PA deleted both streams and six other scratch files (eight in all) at 21:48 and checked each (PA, HOST).

### Divergences and Notes

- **Day-close markers.** 10 of 11 role log files carry one. HOST carries none (see Sources).
- **When the database recovered.** Lead (login probe 401 at 09:52, watcher), PA, Exec (probe 401 at 09:53), HOST (401 at 10:03) and
  CIO (outage 05:25 to 09:52) agree on about 09:52. PPM's incident line in its day arc says "recovered 12:31". PPM's own entries
  show it probed 500 at 09:34 and 401 at 12:31 and had no probe between, so 12:31 is when PPM next measured, not when the service
  returned. I report 09:52 and flag PPM's wording.
- **Who restarted the database machine.** HOST (10:03) and Exec (10:06) wrote that Lead restarted it. Lead's 09:55 entry says xian
  ran `fly machine restart`, and its 10:23 memo corrects HOST's line, which HOST accepted at 10:30. CIO's first entry also says
  Lead restarted it and its 14:31 entry repeats the corrected version. Resolved by Lead and accepted by HOST.
- **Exec's wrap on #2089.** Exec's closing entry says "Rulings: #2085 and #2089 off the gate". Exec's own 14:21 entry, PPM's
  ledger (entry 22 at 14:13) and Lead record that xian accepted CXO's ruling at 14:13 and PPM admitted #2089 as a must-close. The
  13:20 ruling "not before partners" was superseded. Exec's admitted list also omits #2089 (nine items, PPM lists ten). Treat
  the wrap line as stale.
- **Attribution of #1852 step 2.3.** Exec's 10:53 entry says step 2.3 passed with "(Docs 10:27)". Lead's 10:27 entry says it passed
  in xian's browser, and Docs's log has no such entry. I read it as a mislabel in Exec's entry and did not ask.
- **Closes listed by CXO on a day they were not logged.** CXO's 21:31 day arc says it "closed #2075, #2080, #2079, #2067, #2082
  and #2017". CXO's dated entries today record closing #2067, #2082 and #2017 only. The 10-18 omnibus
  has #2075, #2080 and #2079 closed on 10-18 and no CXO log entry today closes them. Inferred: the day arc carried a list from
  Sunday. I did not check GitHub.
- **Red on `2ba2cefc4f`.** PA (15:48) and HOST (15:26) attribute the red at that sha to Router Pattern Enforcement. CIO (16:07)
  reads Tests failing at `2ba2cefc4f` and Lead reports both, the router gate from the #2092 and #2095 merges and a Tests failure
  from the corpus census pin (run 39334911042). These are different workflows on neighboring runs, not conflicting claims. CXO
  and PPM give the red time as 22:26Z.
- **Time of the second promotion.** Lead says dispatched 13:40 and success 13:43, with the entry stamped 13:44. PA says
  13:42, Exec 13:43. Treated as the same event.
- **Time stamps in Lead's log.** Lead's heading times are fire arrivals, not always event times (its 06:17 fire arrived 06:41,
  09:17 at 09:47, 12:17 at 12:47, the 15:17 tick at 17:25, 18:17 at 18:48, 21:17 at 21:47). Exec's cron fires also ran late
  (06:38 at 06:53, 10:38 at 10:53, 14:38 at 14:53, 18:38 at 18:54, 22:38 at 23:08).
- **The two partial reports.** Both carry "Version: v0.8.6 (post-M1)", which is the old script's label. Arch's 06:27 entry reads
  alpha at 0.8.14.0. The 16:13 CSV has 15 rows numbered 1 to 14 and 16 (no row 15), while Web and Lead say "15 of 61" and "right
  after Q16". I did not find an explanation in the logs.
- **Judge model.** The reports show the judge call failing with a 404 on `claude-sonnet-4-20250514` for every query. PPM's note
  reads this as a recalibrated baseline for Tuesday. PA's fix is `0115f2ee47` (judge default `claude-sonnet-5-5`) and `b33dd574aa`
  (Q7 and Q12 expected routing).
- **Model mix.** Headers record Fable 5.1 (Lead), Opus 5.5 (Comms, Arch, PPM, PA, Exec and CIO) and Sonnet 5.5 (Docs, HOST, Web,
  and CXO whose header says `claude-sonnet-5-5`).
- **Rule 8.** See Flags.

### Process Findings

1. **An unattended seat declined the one verb that would have helped.** HOST kept its standing rule against `fly` in an unattended
   fire (set after a prompt froze that seat on 10-09), so the outage waited for PA, whose seat reads `fly logs` routinely, at
   09:48. The gap was about 2 hours 43 minutes between Lead's escalation (07:05) and PA's reads (09:48, computed), and HOST asked for a
   volume snapshot check that was overtaken because the restart happened first (HOST, PA, Lead).
2. **Defects came from use again.** The two stalls came from running the canonical script on alpha, the empty-calendar bug from
   xian's own account, and the retitle bug from Arch running the extractor on prose. Lead's pins in each landing followed.
3. **xian shifted to working through Exec at about 14:30.** He gave "run hotter" at 35 percent weekly usage (Exec 14:30), then
   most of his later answers came via Exec (Lead 14:33, PPM, Exec), though Lead logs him in its pane again at 15:05. Admissions and rulings came as relayed lines
   and landed in `decisions.log` on each (Exec, Lead).
4. **Open decisions with xian at close**: invitation lines and the Calendar paragraph (Comms), the #2087 Google submission,
   Terms HALT pass and answers, the Ship #065 edit, the Comms slate (all Exec's wrap), the Tuesday post rewrite (still the old H1
   at 21:19 per Comms), the Sunday post's live tease and footer (Comms, blocked on his OK), the Sun 10-25 title pick (Comms), the
   partner list and three held sends (HOST), the `#2101` stall fallback line if he declines it (CXO), and the `alpha@` line
   in the invitation (CXO).
5. **Deferrals with a named trigger.** Tuesday's 07:00 promotion gates the served rows (Web, CXO, PPM). The `to_thread` surface
   and the #2098 consult are Tuesday's builds (Lead, Arch). The assigned-issue health-watch backup follows them (Lead). The
   canonical re-run and scenario A wait for the promotion and PA's streams (PA, Web). Docs's three publishes (Phantom Feature
   10-20, Ship #065 10-21, Tracker That Lost Track 10-22) wait on Comms setting `ready-for-docs` (Docs). The 0.2.1 runtime read
   waits on a seat restart (CIO). PPM's readiness read is at the 10-22 START.
6. **Fire coverage.** Docs fired at 04:12, 07:12, 10:12, 13:12, 16:12, 19:12 and 22:12 and HOST at 06:26, 09:26, 12:26, 15:26, 18:26
   and 21:26 with mail wakes between (21 mail-wake headings in HOST's log, counted by eye). CIO's log has fires at 10:07, 16:07 and
   22:07 plus mail wakes.
7. **Unclosed log.** One of 11 log files (HOST). Docs's 22:12 STOP entry does not mention a nudge about it.

---

## Timeline (PDT)

Times are as each log wrote them. Where a log flags that its stamp was estimated, that is noted.

### Overnight into the START fires (00:00 to 06:30)

**00:23** first commit of the day (`chore(usage)`). **about 05:25** Postgres stops listening in a started machine (PA's reads
timed it from the `pg` check, Lead). **04:12** **Docs** START and the 10-18 omnibus drafted by a Sonnet subagent (Docs says 360
lines, 336 commits). **04:16** **HOST** closed its 10-18 log and **Web** had closed at 04:16 or 04:18. **04:18** **Docs** added the Web
addendum, and the HOST addendum at 07:12. **06:18** **Web** START. **06:19** **Comms** START. **06:26** **HOST** scheduled wake.
**06:27** **Arch** fire. **06:31** **CXO** START. **06:33** **PPM** START. **06:41** **Lead** START (the 06:17 fire arrived
06:41), rotated its cron. **06:47** **PA** START. **06:53** **Exec** START (06:38 fire, late).

### Morning: the failed dispatch and the outage (07:00 to 10:15)

**07:00** **Lead** dispatched promotion 1 (run 39265029915), failed at 07:02 in `release_command`. **07:03** alpha login 500.
**07:05** **Lead** escalated and filed #2083. **07:08** **HOST** declined unattended `fly`. **07:11** **Exec** probe 500 and rollup
v409. **09:08** **Lead** pushed a notification to xian. **09:18** **Web** probe 500 and no served runs. **09:26** **HOST** wake.
**09:28** **Arch** ruled #2083 and **Comms** received xian's ask on the POC summarization history. **09:31** **Lead** began
#2083 in `lead-2083`. **09:33** **PPM** placed #2083 and #2084. **09:36** **Lead** landed `13716892ee`. **09:48** **PA** ran the
five reads. **09:50** **Lead** filed #2085. **09:52** database back (probe 401). **09:52** **Arch** read the sources on the 2025 loss.
**09:53** **Exec** probe 401. **09:55** **Lead** logged xian's restart, and the `dinp` reset found no user.

**10:01** xian ruled the `mvp-tester` admin grant. **10:01** Tests red on `13716892ee`. **10:03** **HOST** probe 401 and a
corrective note on its ruling 1. **10:07** **CIO** START (m-52 promoted, stamp check on `decisions.log`). **10:10** **Arch**
validated #2083. **10:12** **Docs** fire, weekly audit #2084 done at 10:15. **10:13** the grant landed (`UPDATE 1`), **Lead**
filed #2086.

### Late morning and midday: the fix, two promotions and the card (10:15 to 14:10)

**10:16** **HOST** logged the grant via Lead. **10:23** **Lead** four memos including the misquote correction. **10:27** #1852 step
2.3 passed in xian's browser (Lead). **10:30** **HOST** asked for the class of the isolation reds. **10:43** **HOST** read Lead's
classification. **10:44** Tests green on `84de766e0d`. **10:53** **Exec** fire (late). **11:10** **Lead** closed #1852. **11:13**
**Lead** dispatched promotion 1 of 2. **11:17** alpha serves `f9fb8b750b`. **11:19** **Lead** card v84 and #2083 closed.
**11:23** **Exec** caught the stale board memo. **11:24** **Web** rows: #2082 5/5, #2067 5/6. **11:37** xian's Calendar Connect passed.
**11:40** to **12:26** **Lead** and xian on the Google consent: External plus In production, domain verified, Branding cleared.
**12:26** the ten masked forms relayed to **HOST** (15 minutes after Lead saw them). **12:26** **HOST** wake, Tests green, isolation
reds closed by the run. **12:27** **Arch** wake (refreshed the briefing alpha line). **12:29** **PPM** began the formalities
checklist. **12:32** **CXO** closed #2067 and #2082. **12:33** **PPM** ledgered gate 7 to 6. **12:34** #2077 closed and gate 5.
**12:43** **HOST** recorded the ten masked forms. **12:49** D2 passed. **13:09** **HOST** gave its word on #2081.

**13:11** **Lead** landed the Invites refresh change. **13:17** D4 failed as run (wrong surface). **13:20** xian ruled #2085 off the
gate and #2089 not before partners. **13:23** #2081 closed. **13:25** xian re-added the hosted connector. **13:29** **PA** closed
#2078. **13:35** D4 passed. **13:40** **Lead** dispatched promotion 2 of 2, alpha serves `e801b1a309` at 13:43. **13:43** **PA**
closed #1982. **13:50** A3 pass, A2 fail (#2091 to #2093 filed). **13:53** **CXO** closed #2017. **13:57** A6 and A7 findings (#2094
to #2096). **14:05** **CXO** rulings on #2088, #2089, #2093. **14:07** B3 pass, card done. **14:13** xian accepted #2089 before
partners.

### Afternoon: admissions, stalls and landings (14:10 to 18:30)

**14:12** **Arch** ruled the binder ratchet. **14:30** **Exec** handoff after xian's "run hotter". **14:31** **CIO** retro and
harness repair. **14:35** xian admitted the five (PPM gate 4 to 9). **14:38** **PPM** briefed the #1386 run. **14:42** to **14:47**
**Web** ran scenarios B and C. **14:44** **Lead** landed #2093 and #2091. **14:47** **CXO** restarted onto piper-guards. **14:53**
**Web** started the canonical script and **14:53** alpha began to flap. **14:56** **Lead** landed #2092. **15:03** the app's Fly
check passed again. **15:05** xian admitted #2097 and #2098, #2090 backfill done. **15:07** #2095 landed. **15:15** alpha steady
by Lead's count. **15:19** **Web** resumed the script, stopped at Q5 (partial pushed `16b4c5a4dd`). **15:22** #2094 landed.
**15:26** Router Pattern Enforcement red (HOST at 15:26). **15:34** **Web** pushed /privacy (`4f3582d`). **15:50** **Web**'s
browser read confirmed it. **15:52** #2098 landed. **15:59** #2096 landed. **16:09** **Web**'s controlled repro, stalled by 16:13.
**16:15** #2097 landed and pre-ping landed. **16:19** **Lead** read the repro. **16:36** **Web** closed test-repo #10 to #13.
**16:46** #2099 landed, #2098 reverted. **16:56** xian admitted #2101 and said yes to server rendering. **17:03** **Web**'s
SSR live (`a3cb49f`). **17:09** **Arch** ruled #2101. **17:11** **Web** stored the 10-15 key for web-agent (Pard's ask).
**17:20** #2102 and the binder ratchet landed. **17:23** the process-wide cache landed. **17:25** the health watch landed and was
forced. **17:44** Tests red on two radar pins, fixed `f9ddb2ba88` (17:44, Lead). **17:53** xian admitted #2100 and reported no
alert email.

### Evening: alert path, close and wraps (18:00 to 23:10)

**18:00** Tests green on `f9ddb2ba88`. **18:05** #2100 landed. **18:10** **Exec** and xian: the Web key stays as his test key.
**18:17** to **18:23** the OAuth notices thread across **Exec**, **Web**, **PA**, **HOST**, **Lead**. **18:20** Tests green on
`5e17e627a2`. **18:39** xian found the defunct notification address. **18:42** **Exec**'s forced run, failed 18:46, mail
arrived 18:46:35. **18:56** **HOST** marked the email leg met. **19:05** **Lead** recorded the leg accepted. **21:18** **Web**
STOP. **21:19** **Comms** day close. **21:26** **HOST** quiet wake (last entry). **21:27** **Arch** day close. **21:31** **CXO**
day close. **21:33** **PPM** STOP. **21:48** **PA** STOP (streams deleted). **21:51** **Lead** STOP (the 21:17 tick arrived
21:47). **22:07** **CIO** STOP. **22:12** **Docs** STOP, day closed. **23:08** **Exec** quiet fire and wrap. **23:09** last commit
of the day (`log(exec): 10-19 day closed`).

---

## Coding Agent subagent logs

None for the day. Lead's lanes are named in Lead's log and have no log in the directory. Comms's and Arch's Opus read-only
subagents are named in their logs and have no log of their own. I do not know whether other subagents ran.

---

## Flags

- **Rule 8: no outside person's name found in the source logs.** I searched the 18 files by eye as I read and ran a pattern
  search for two-word capitalised names, which returned only headings, product strings, role titles and post titles. Exec's
  14:21 entry reports that an old HOST memo of 10-12 names an outside tester by first name, in a mailbox file I did not read. The
  name is not in any 10-19 log and I did not look it up. Lead's 10:13 entry says an accounts listing holding testers' names and
  emails stayed in xian's terminal and is not in the log. This is a pattern search plus a read, and I could not rule out a name
  I did not know to look for.
- **No credential in full** appears in the source logs I read. The logs carry masked forms of the type `ABCD…WXYZ` (HOST, Lead,
  Web and Exec quote masked forms of invite codes, and Web quotes a masked key tail). I copied none of them into this file.
- **Unclosed role log files**: HOST (see Sources).
- **Method notes**: the commit count ran after `git fetch origin main` with `TZ=America/Los_Angeles`. I ran no `gh` command, so
  every issue number, close time, run id and sha in this file is as the role logs report it. I did not re-verify them.
- **Possible gap**: PPM, Exec and CXO all report numbers that were "lagging" or corrected inside their own logs (the criteria
  script twice, a rollup count of 12 corrected to 13, CXO's list of closes). I flagged those I noticed. Others may remain.

---

*Prepared by Documentation Management (docs-code). Sources: 18 files in `dev/2026/10/19/` (11 role log files from 11 roles,
6 non-log files read in full, 1 script read at its header only). Ten of the 11 role log files carry a DAY-CLOSED marker and one
does not (HOST). Day-close grep run 2026-10-20 early morning PDT. A dated addendum will follow if HOST's log changes.*
