# Omnibus Log: October 15, 2026

**Day**: Thursday
**Sessions**: 11 role sessions (Documentation Management, Communications Director, Chief of Staff, Unicorn Web Designer, Head
of Sapient Trust, Chief Architect, Chief Experience Officer, Principal Product Manager, Lead Developer, Piper Alpha, Chief
Innovation Officer) and 24 Coding Agent subagent logs (prog-code, all for Lead), 35 files in all. Subagents also ran
without a log of their own: Docs's Sonnet drafter for the 10-14 omnibus (early 10-15). Pard, Janus and Spec appear in the mail traffic only.
**Day Type**: HIGH-COMPLEXITY: EXECUTION: the seven held branches landed in the first hour, xian's promotion went out at
15:30 after a stall, a second round of standup, offer and GitHub-grant fixes landed behind it (Lead counts 31 landings),
and the run-hot window closed at 22:00 with normal pacing relayed from Friday. The day ends with a promotion READY on
`e4f21e9ca8` that has not been dispatched.
**Justification**: Eleven role sessions and at least ten threads crossing three or more roles: the standup word map
(#1771 and #888: Lead, Arch, CXO, PPM, Web), the held-branch landings and the stalled promotion (Lead, Exec, PPM, PA, Web,
CXO, xian), the test-account chain (Exec, HOST, CIO, Web, CXO, Pard), the S5 broken-grant run (PA, Lead, CXO, Web, PPM,
xian), the calendar redirect chain (Exec, Web, Lead, CXO, xian), the old-history ref cleanup (Exec, Lead, CIO), the
piper-shared read-rule gap (CIO, Exec, HOST, Web, Pard), the floor-narration class #2042 (Web, CXO, Arch, PPM, Lead), the
run-hot close and usage observations (Exec and ten seats) and the Overzealous Cleanup publish and Convergent Claims
pre-flight (Docs, Comms, Exec, Web). The sub-type is EXECUTION because most rulings arrived as short mail wakes against
issues that already existed, and Lead's lanes turned each one into a landing within the hour.
**Git Commits**: 1091 on origin/main by committer date (00:00 to 24:00 PDT 10-15). Verified how: `git fetch origin main`,
then `git log origin/main --since='2026-10-15 00:00 -0700' --until='2026-10-16 00:00 -0700' --oneline | wc -l` printed
1091 at origin/main tip `25f9b49d56`, 2026-10-16 04:13 PDT. Counted by leading subject text from `--format=%s` on the same
range: 266 `mail(`, 251 `log(`, 8 `chore(usage)`, 0 containing `hb`, 28 `docs`, 307 starting `Merge`, leaving 231 other
commits. The 231 break down as 47 `web`, 30 `land`, 21 `cio`, 18 `feat`, 17 `arch`, 16 `card(lead)`, 11 `comms`, 8
`carry`, 6 `intent`, 5 `content`, 4 each of `test`, `standup`, `ops`, `ledger`, `fix` and `decisions`, 2 each of `tests`,
`rollup` and `copy`, and 22 singletons (13 one-off prefixes and 9 issue-numbered subjects such as `2039:`). The six named
buckets plus the 231 sum to 1091. The 10-14 omnibus reported 1068 on the same basis, so the day is about 2 percent larger.
No source log quotes a commit total for 10-15, so there is no logged figure to compare. Layer: git history on the local
object store, not the GitHub API.

---

## Sources

Session logs (all in `dev/2026/10/15/`), role logs first:
- `2026-10-15-0412-docs-code-log.md` (Docs, 81 lines)
- `2026-10-15-0417-comms-code-log.md` (Comms, 55)
- `2026-10-15-0417-exec-code-log.md` (Exec, 258)
- `2026-10-15-0618-web-code-log.md` (Web, 319)
- `2026-10-15-0626-host-code-log.md` (HOST, 102)
- `2026-10-15-0627-arch-code-log.md` (Arch, 281)
- `2026-10-15-0631-cxo-code-log.md` (CXO, 263)
- `2026-10-15-0633-ppm-code-log.md` (PPM, 158)
- `2026-10-15-0641-lead-code-log.md` (Lead, 395)
- `2026-10-15-0647-pa-code-log.md` (PA, 189)
- `2026-10-15-1007-cio-code-log.md` (CIO, 136)
- 24 prog-code logs, 584 lines together: 2010, 1771, 2017, 2019, concepts, 2024, 1771c, 888, 888b, 2026, 1771f, 1771g, 2029,
  2030, 2031, 2033, 2008, 2035, 2037, 2039, 2035b, 2037b, 2040, 2041 (named by the issue or task in the file name)

Total 2821 source lines (444,733 bytes, about 434 KB), from `wc -l` and `wc -c` over the 35 `*-log.md` files. The role logs
are 2237 lines and the prog-code logs 584. No other files sit in the day's directory (`ls` listed only the 35 logs).

**Cross-reference gate**: roles mentioned without a log in this repo: Pard (Exec, CIO, HOST, Web, Lead), Janus (Exec, PA,
Lead), Spec (Exec, HOST) and Themis (none today). These are cross-project agents or dormant seats with no `dev/` log by
design. No source-set role is missing, so I did not ask PM.

**Day-close status** (re-grepped with `grep -c '^<!-- DAY-CLOSED'` per file on 2026-10-16 04:14 PDT): **all 11 role logs
carry a marker** (Docs, Comms, Exec, Web, HOST, Arch, CXO, PPM, Lead, PA, CIO). **The 24 prog-code logs carry none**, which
is expected for subagent logs, they end with a verification line and are never given a close. Lead's marker uses the
longer form `<!-- DAY-CLOSED 2026-10-15 21:48 PT lead-code -->` (no colon) and still matches the grep. Exec's marker is
the last line after a written day-close section. No role log has entries below its marker. Verified how: the per-file
grep above, count 11 of 11 role files and 0 of 24 prog files (`grep -c` printed 1 and 0).

**Reading coverage**: the 11 role logs were read in full in this session. The 24 prog-code logs were read for their task,
build and verification lines, with long lines clipped at 600 to 700 characters, and the 97-line #2010 log was read through
its first 60 lines. Compression: 2821 source lines to this file's line count. Verified how: `wc -l` on this file after the
draft. Every role appears in the timeline.

---

## Executive Summary

### Core Themes

1. **The seven held branches landed in the first 45 minutes.** Lead merged main into each branch, re-ran the suites and
   landed #2011-b (the unarmed-ask census over `services/**`), the ANALYSIS margin example, #1965 with #2012, #2009, #2013
   and #2014 between 06:5x and 07:24, with the #2010 lane following at 07:49. The chain of three migrations round-tripped on a
   scratch Postgres (up, down to the prior revision, up). The batch brought one red: the smoke set failed on the new
   `items.list_id` foreign key at 07:57 because two smoke-marked tests invented list ids, and Lead fixed it at the cause.
   Verified how: Lead's landing entries read in full, and the 07:57 repair entry. I did not re-run any suite.

2. **The standup word map converged through about ten small units.** Starting from #1771's second seam, Lead, CXO, Arch
   and PPM settled that the registry splits the #888 escape words into END (`cancel`, `quit`, `exit`) and PAUSE (`stop`,
   `never mind`), that `skip` is not an escape word, that every way of leaving the invitation ends the row and says one
   line, that the quick bypass is whole-message, that one leading "please" is politeness and that `skip the standup` leaves.
   The 17 suggestion lists the web UI never rendered were deleted (#2027 and #2028). CXO closed #1771, #2007, #2020, #2026
   and #2027 on Web's served replies after the promotion. Verified how: read all five seats' entries, and `gh issue view`
   closedAt for #1771 (22:48Z, 15:48 PDT), #2020, #2026, #2027 and #2007 (all within 22:48Z to 22:58Z).

3. **xian approved the promotion at 13:18 and it went out at 15:30.** PPM relayed the approval to Lead and Exec at 13:18.
   Lead's log has no entry between 12:41 and 15:32, and Exec found Lead stuck on a permission prompt from 12:43 to about
   15:30. PA watched `/health` for 45 minutes at 13:20, and Exec's 14:09 entry put the dispatch line in xian's hands. xian
   dispatched at 15:30. GitHub shows the dispatch run 38817618053 created at 22:30:50Z (15:30:50 PDT) concluding success
   and a second dispatch, 38817646538, created 14 seconds later and cancelled. Alpha moved from `5e5f3366c4` to
   `6f2916d10f` and Web began a served round at 15:37. Pard then built a stuck-session alert into mail-wake, live at 15:39.
   Verified how: `gh run view` on both run ids, `gh run list --workflow=fly-deploy.yml --event workflow_dispatch`, and the
   logs of Exec, Lead, PA, PPM, Web and CIO.

4. **Test accounts and the first served round closed most of the held acceptance rows.** xian made a machine GitHub
   identity and a scoped token (files in `~/.piper-shared/`). CIO found the fleet's read deny matched only names containing
   `credential`, `token` or `secret`, so the new files were readable on every seat, and the fix was a rename that xian
   applied at about 15:38. Web built a PAT-only account, HOST minted a second invite with xian present, Web built an
   OAuth-only account (one refusal from a typo in the login file, then connected on the second try), seeded the machine
   account with a repo and issues, and ran the rows on `6f2916d10f`. xian made a spare Anthropic key at 16:41. Verified how:
   Exec, HOST, CIO, Web and CXO entries compared, no credential read by me.

5. **S5 passed with xian and #1965 and #1889 closed.** On `6f2916d10f` the same revoke that read 4 of 4 all-clear on 10-14
   read 4 of 4 disclosures, the Test failed honestly and reconnect restored a clean state. CXO judged the copy a pass.
   PA's re-read of #2018 had already produced #2029 (Settings said Connected on a revoked grant), and the work around it
   produced #2031, #2037, #2039 and #2036. Verified how: PA's, CXO's and Lead's entries, and `gh issue view` closedAt for
   #1965 and #1889 (23:24Z, 16:24 PDT).

6. **The calendar connection took three redirect fixes.** Step C failed with `redirect_uri_mismatch` because the app sent
   the Fly hostname. Lead and Exec first said one secret (`PIPER_BASE_URL`) would fix calendar and Slack, xian set it, and
   the error persisted because explicit per-provider secrets existed. Both seats owned the wrong inference. xian then set
   `GOOGLE_SETTINGS_REDIRECT_URI`, added his account as a Google test user, and the calendar connected at 18:44. Lead's
   read-only audit proposed `PIPER_BASE_URL` as the single source on #1852. Verified how: Exec, Lead, Web and CXO entries.

7. **The old-history guard retired after a 54-ref cleanup.** Exec's 09:07 watch found GitHub clean and 54 local refs still
   holding pre-rewrite history. xian said to clean up first. CIO removed one branch, Lead removed 44 branches, 7 stray refs
   and 6 clean worktrees (bundling the one unmirrored tip first), and Exec force-removed the last two dirty worktrees on
   xian's in-session word after CIO tarred the 8 dirty files. Exec's loop then printed nothing over 247 refs and moved the
   sentinel file aside at 15:40. Verified how: Exec's, Lead's and CIO's entries agree on the arithmetic (54 less 1 less 51
   less 2 equals 0). I did not re-run the loop.

8. **The run-hot window closed at 22:00 and every seat logged a usage line.** Exec relayed xian's ruling at 16:47: run-hot
   ends tonight, normal pacing from Friday 10-16, the week review looks at usage patterns, calendar steps are wanted, the
   held invites are decided tomorrow and #2036 stays out of MVP. The ten other role logs each carry a usage observation.
   None reports a rate-limit stop or a request for a larger model, and several name turn count rather than model tier as
   the cost. Verified how: read each log for its line. These are the seats' own accounts, not a meter reading, except CIO's
   weekly-meter figures and PA's eval costs, which are quoted from harness output.

9. **Publication and the Saturday post.** "The Overzealous Cleanup Routine" went live before 04:17, Comms live-checked it,
   and xian's Medium URL put the row at `distributed` (commit `bfead0b217`, 07:03). Comms then reviewed PM's revision of
   Saturday's "Convergent Claims Aren't Independent Evidence", PM approved all proposed fixes, Comms applied six edits and
   sent publish-ready, and Docs's pre-flight came back clean. Publication waits for its pubDate, Sat 10-17 04:12. Verified
   how: git commit times for `bfead0b217`, `ffbad2340f`, `ae8e4f8427` and `936aeaef0a`, and the live-check entry in Comms's
   log.

### Technical Details

1. **Landing batch** (Lead). #2011-b: `TestUnarmedAskSiteRatchet` widened to `services/**` (454 files), census frozen at 16
   holders, 37 rows, 10 markers. Migrations q2009nn, r2013kgnn and s2014items. Targeted re-runs at landing read 1479 passed
   (#1965 and #2012), 1272 (#2009), 1283 (#2013) and 1313 (#2014), and the mypy gate sat at ceiling total=1097 on every one. The first suite on the #2011 branch read 13348
   passed, 236 skipped, 0 failed. The 07:57 repair: smoke set 553 passed, 1 skipped after the fix, was 14 failed.
2. **Census movement.** #2010 took the census from 38 rows and 63 literals to 34 and 57 after the offer_hint arm signal
   and a reach tripwire. #2024 took it to 33 and 55. #2035, #2030 and #2041 left it there. The routing literal ceiling stayed
   90 (35 lists) all day per PPM's recounts. Verified how: Lead's and the prog-code logs' census tables, PPM's
   `pattern_literal_counts.py` readings.
3. **#2019 delete cap.** One builder (`delete_cap.py`) called from every multi-item delete path, 12 sites mapped (the issue
   named four), 31 existing pins rewritten, found #2025 (the #1666 gate binds the first number of "delete todo 1 and 2").
   Web's S7 run showed a capped reply with a numbered list and nothing deleted, and CXO closed #2019.
4. **#888 hatch.** `ESCAPE_END_WORDS` and `ESCAPE_PAUSE_WORDS` in `services/process/registry.py`, copy through optional async
   handler hooks, `suspend()` at INITIATED closes the row. Pins grew from 24 (second seam) to 41, 72 and 83 across
   successive units, each checked to fail on the pre-fix code (16 of 24 and 29 of 41 failing on the pre-fix code, and 17 failures for the word-map unit).
5. **Offers and the multi-intent path.** #2030 carries `offer_hint` through the orchestrator and arms one question last.
   #2035 sends the three write offers to the #846 store with an `offer_add_project` landing. #2041 carries `write_offer`
   and ranks it above a hint. Arch's reach tripwires cover both kinds. The #2024 lane's `ast` count of entry points was
   21 (table-dispatched members included), against Arch's by-name count of 11, and Arch recorded the miss.
6. **GitHub grant.** #2029: a 401 on the OAuth leg marks the binding STALE through the existing repository, `oauth-status`
   returns connected, stale and serving, and Reconnect re-grants in one step. #2031: the Integrations card reads the one
   credential resolver. #2037: `ConnectionTestResponse` gains `leg` and `stale_reason` so the page keys on a flag, not a
   sentence. #2044: a connected, never-tested card reads "Connected" with "Not checked yet. Press Test." and a throwing check
   reads "Couldn't check this just now. Press Test to try again."
7. **#2033 and #2040.** A deterministic step before classification answers `cancel`, `skip the standup` and `no, not now`
   when nothing is running (58 pins). #2040 names the scope on an empty issues list and answers a "show me the rest" with
   nothing held from a recorded one-turn `ListComplete` fact (87 pins). The #1783 cap line first appears at 9 assigned
   issues, not 8.
8. **#2039.** Eight 302 redirects for guessed paths and a content-negotiated human 404 outside `/api/` (24 pins).
9. **CI repairs.** `lint.yml` moved to `cancel-in-progress` on pull requests only (`9200923831`, CIO's find: 91 of the last
   100 runs cancelled), the same fix Lead made to `test.yml` on 10-14. Three Tests reds (smoke FK, a clock-straddling
   fixture in the #2019 pins, and the #1816 consent pin after #2040) were each fixed within the hour. A Code Quality red at
   06:48 (current-state date) was fixed by PA at 06:51 (`fd069bb107`).
10. **Hooks and guards.** The commit-msg hook was installed by xian about 13:2x. CIO checked it by running the installed
    hook (a "fix #1" message refused with rc 1, a benign message allowed with rc 0). `whats-armed.sh` read 30 of 30, then
    31 checks with a new piper-shared name check from 14:09, then 30 armed, 0 not armed and 1 unmeasured (the retired
    guard) after 15:40.
11. **PA routing eval.** 105 runs, $9.67, 0 errors. Bare connector with the current description against a use-first
    rewrite: 33 against 37 of 45, the count question 8 against 9 of 15 (inside noise), the full plugin 15 of 15, and "what
    should I work on today" 30 of 30 on the bare connector. PA did not propose the rewrite.
12. **Alpha builds.** Alpha served `5e5f3366c4` until 15:30 and `6f2916d10f` after. The dispatch run's head sha was
    `762282e3fb`, which differs from the served sha. Lead's 15:32 entry says staging served `6f2916d10f` at dispatch, which
    is the sha alpha then showed. I did not verify the workflow's promotion mechanism.

### Impact Measurement

1. **Issues filed**: 21, #2024 through #2044 with no gap. **Closed**: 13 (#1771, #1783, #1889, #1965, #2007, #2019, #2020,
   #2026, #2027, #2028, #2032, #2034, #2038). Verified how: `gh issue list --state all --search 'created:...'` and
   `'closed:...'` over 2026-10-15T07:00Z to 2026-10-16T07:00Z (the Pacific day). Lead's closed list (9 issues) plus CXO's four
   served closes equals the 13. Filer attributions differ across logs (Lead credits lanes for some numbers), so I give no
   table. #2005 appears in Exec's log as "CLOSED 10-15 04:07Z", which is 21:07 PDT on 10-14 and is not in the 10-15 set.
2. **MVP list**: PPM's open count read 9 of 316 at 06:33, 10 at 10:48 (after xian admitted #2017 and #2018 and moved #1943
   to Production), 9 at 16:0x (#1771), 7 at 16:4x (#1965 and #1889), 6 at 17:3x (#1783) and 6 of 324 at the 21:33 STOP.
   Slips: 7, 0 days moved. Verified how: `gh issue list --milestone MVP --state open` at 04:15 PDT 10-16 returned exactly 6
   issues, #1386, #1595, #1913, #2012, #2017 and #2018, the same set PPM lists at close (nothing changed overnight).
3. **Gate placements**: #2024 through #2044 sit on Production except the two admissions. #2040 is Production and
   provisional, with its Class 3 admission waiting on xian (live `gh` read: #2040 OPEN, Production).
4. **Concept links**: CIO's checker read 79 linked, 0 broken at 14:11 and 22:07 (80 at 15:55 after the stuck-session page, before
   its retirement). Lead's CI-workflow lane moved workflows from 14 linked and 9 with none to 22 and 1.
5. **Refs**: 54 old-history local refs to 0, guard dormant at 15:40. Lead pruned 29 merged worktrees at Pard's request (26 GB
   held by 31 worktrees, directory 39.5 GB to 16 GB). Exec read free disk 74 GiB (Pard 17:08), 79 at 18:41, 80 at 22:44.
6. **Piper-shared coverage**: CIO's check read 4 of 9 files under no deny at 14:09, 2 of 10 at 14:26 and 12 of 12 at 15:56.
   Exec read 10 of 10 at 15:40. See Divergences for the two denominators.
7. **Usage**: CIO's pipermorgan.ai weekly meter read 77% at the 09:23 row and 80% at 15:23, resetting 22:00 (stop line
   95%), and 41% on 10-12. PA's two evals cost about $17 together. Lead ran about 15 lanes (12 Opus, 3 Sonnet) by 16:47.
8. **Rollup**: Exec's rollup went from v291 (04:18) to v332 (19:59), 41 versions.
9. **Test counts** quoted by Lead vary by selection and head (5831 to 7261 passed on intent, intent_service, standup, process
   and enforcement selections, 13348 on the whole unit tree at 06:5x). They are Lead's runs and I did not re-run any.

### Session Learnings

1. **Check carried rollup rows against their source before each republish.** Exec's day close lists four stale rows and
   credits xian with catching them: the #2014 counts (done 10-14 20:56), #2005, the Medium crosspost (recorded on main at
   07:03, still listed at 13:42) and the test machine account (made 10-09, still listed as "create"). Exec's 11:09 and 11:19
   entries show Lead, PPM and Arch flagged the #2014 counts first, and PPM and Arch had carried the same stale counts.
   Exec's new per-row check names issue state, `git log --grep` since the row was added, and the card header.
2. **Time-sensitive PM words go to the dispatching seat directly.** PPM's 13:18 relay reached Lead on a 15:30 mail wake
   (about 2h12m). PPM logged the lesson and Pard's alert (dialog showing plus unread mail) now watches for it.
3. **A sign of life is not a sign of progress.** CIO's heartbeat join caught Lead only from 13:30 because post-commit
   heartbeats kept arriving while a subagent's permission dialog blocked the work. Pard's direct signal had logged "dialog
   showing" 155 times from 08:12. CIO recorded it as methodology-43 instance 7 and added a co-addressee check to the sunset
   rule's "Before you build".
4. **Name one owner on a two-party ask.** Exec sent the stuck-session proposal to CIO and Pard with "yours to shape", and both
   built it. Exec saved `name-one-owner-or-mark-discussion` (per Exec's 16:05 entry).
5. **Ask for the full secrets list before advising on env precedence.** An explicit fly.dev value and the fallback look
   identical. Lead and Exec each retracted an inference (Lead at 18:45, Exec at 18:36).
6. **A landing that carries a migration runs CI's `-m smoke` set against a scratch DB migrated to head.** The dev DB was not
   at head, so the hook's smoke run could not see the new FK. Lead also added: a change to `intent_service.py` re-runs
   `tests/unit/services/llm`, because the #1816 pin lives there.
7. **Timestamps were written without `date` again by at least six seats.** CXO (entries from about 15:55 ran up to an hour
   ahead), Arch (headings from 07:5x drifted up to 80 minutes, corrected at 18:27 across 27 headings and 15 decisions.log
   stamps), Web (three memo headers), Exec (two memos), Lead (card v48 and v49) and Docs (see Divergences). Each fixed its
   own record. The rule is already in the tick.
8. **Quote the gate's NEW line, not the backlog warnings.** HOST routed a Tests red to Lead and quoted lines that belong to
   the known 60-test backlog. Lead had already fixed the one new failure.
9. **Subagent worktrees land under PM's checkout and stay there.** CIO's piper-guards subagent left a dirty worktree that
   carried a stale copy of old history for three days.
10. **Search before filing.** Arch filed #2028 as a duplicate of #2027, and Lead closed #2027 as folded into #2028 at the same
    time. Lead reopened #2027 as the carrier and both are closed at day end.

### Divergences and Notes

- **Day-close markers.** All 11 role logs carry one, and the 24 prog-code logs carry none (see Sources).
- **Commit hashes in the role logs.** Of 155 distinct 10 to 40 character hex strings across the 11 role logs, 15 are
  all-digit GitHub run and comment ids and 1 (`9200923831`, the lint fix) is an all-digit commit. Testing all 140 candidate
  commit hashes (the 139 with both letters and digits plus that one): **137 resolve in the local object store, 132 are
  ancestors of origin/main `25f9b49d56`, 5 resolve but are not ancestors, and 3 do not resolve.** The 5 non-ancestors are
  `f3d7e92e02` (pre-rewrite old main), `92ead77426` (the deleted `cio/r6-slim-probe` tip), `c84a039451` (the bundled
  `claude/lead-1984-status-description` tip), `3fe84f26f6` (HEAD of CIO's subagent worktree, force-removed) and
  `eacdf78704` (a Lead lane commit contained in no remote-tracking branch). The 3 that do not resolve are `7a49d06be3`
  (a commit in Pard's home repo) and `a3f3fbf207ed30c5d` and `a65c32abbfebb6b2a`, which are worktree directory ids, not
  commits. So drift is limited to one branch-local Lead commit, and the only pre-rewrite ids are three deleted or bundled tips and
  the old main. Verified how: `grep -ohE '\b[0-9a-f]{10,40}\b'` over the 11 role logs, `git cat-file -e` then `git
  merge-base --is-ancestor` against origin/main for each, `git branch -r --contains` for `eacdf78704`. Denominator: 155
  strings. Strings of 9 characters or fewer (for example the 9-character `0741d1a5b` in HOST's log) were not tested.
  The prog-code logs were not hash-tested.
- **Why the promotion stalled.** Exec's 15:29 entry says Lead sat on a read-only permission prompt (a ruff check) from 12:43
  to 15:30, and xian found it. CXO's 15:31 tick instead reads the delay as waiting on xian's deny-gap choice, which it took
  from Exec's 14:11 log. PA says Lead had not read the relay, and PPM measured 2h12m. Lead's own log is silent from 12:41 to
  15:32 and records the 15:30 mail wake. I could not settle the cause from primary sources. `gh` shows the dispatch at 15:30:50
  PDT. Exec cites no heartbeat from Lead after 12:43, which I did not check, so the stuck-prompt reading is supported by
  Lead's silent log and Exec's account but is not proven.
- **Who cancelled the duplicate dispatch.** Exec says run 38817646538 was cancelled by the concurrency group. Lead says they
  cancelled their own. `gh` shows it cancelled 14 seconds after the successful run and does not say how. Unsettled.
- **Docs's heading times against git.** Docs's log stamps the 10-14 omnibus at 05:05, the first addendum at 05:20, the Medium
  row at 05:30 and the Convergent Claims pre-flight at 07:40. Git has the omnibus commit at 04:17 (`5c6de3e00e`), the first
  addendum at 04:27 (`0e46e4e36e`), the Medium row at 07:03 (`bfead0b217`), the second addendum at 07:12 (`d61ebfdcf3`)
  and Docs's ack of the pre-flight at 08:06 (`936aeaef0a`), after Comms's publish-ready at 08:03. Comms's wake at 04:17 to
  04:18 already read Docs's "published" memo, so the publish also preceded Docs's logged 04:40. Git settles these. I used git
  times where they conflict. Docs's log did not note a correction.
- **Medium row timing.** Comms's 09:19 fire notes that Docs set the row to distributed. Exec's 13:42 entry says
  the crosspost was done six hours earlier. Git places it at 07:03, so 13:42 is about 6 h 40 m later, consistent with xian's
  "six hours ago".
- **Lane #2039 stamps.** Lead's 16:47 entry records the #2039 lane back after 5 minutes at 16:49 and lists it as
  `d2a73670f7`. The prog-code log for #2039 says it started 16:42 and built at 17:05. The two stamps differ by about 15 to
  20 minutes. Not settled. Other lane logs agree with Lead's landing times within a few minutes.
- **Lane count.** Lead's 16:48 usage entry says about 15 lanes. There are 24 prog-code logs at day end, with the later lanes
  (#2035b, #2037b, #2040, #2041 and others) starting after that entry, and #2020 and the #2029 icon fix were built by Lead
  directly with no lane log.
- **Piper-shared denominators.** Exec reads 10 of 10 files under a deny at 15:40 and CIO reads 12 of 12 at 15:56. CIO's count
  also reads 4 of 9 at 14:09 and 2 of 10 at 14:26. The directory grew as Web saved credentials for two new accounts, so the
  denominators probably differ by time. Neither log states the file count at the other's reading.
- **Red windows.** Lead counts three Tests reds (07:57 smoke FK, 10:12 clock-straddling pins, 18:25 the #1816 pin) and calls
  each a test-layer miss. Exec's 10:40 tick recorded the second one (runs from 16:38Z and 16:59Z), HOST and Exec recorded
  the third, and nobody else mentions the first. PA's 06:48 Code Quality red (current-state date) is a separate workflow and
  is not in Lead's count. Verified how: read each entry. I did not re-derive run conclusions from GitHub.
- **Reopened and crossed closes.** Arch closed #2028 as a duplicate while Lead closed #2027 as folded into #2028. Lead
  reopened #2027. Both are closed at day end (`gh` closedAt 22:48:54Z for #2027).
- **#1783 threshold.** Lead's first trace said the cap line appears at 8 assigned issues, corrected at 17:13 to 9 after Web's
  8-issue run showed no cap. Arch and CXO agree on 9 and Web's 9-issue run passed both arms.
- **MVP counts by time.** PPM's counts (9, 10, 9, 7, 6) are dated entries and each matches the issue closes that preceded it.
  Lead's 16:47 "7 open MVP" matches PPM's 16:4x count. There is no cross-log disagreement once the times are lined up.
- **Entry stamps ahead of the clock.** CXO's memo times from about 15:55 (for example 17:25 on a memo that landed about
  16:25), Arch's 07:5x to 18:2x headings and Lead's card v48 and v49 stamps ran ahead of real time. Each seat corrected in its
  own log, sent memos kept their drifted headers, and the timeline below uses logged times as written with the corrections
  noted.
- **Model mix.** Headers record Fable 5.1 (Lead), Opus 5.5 (Exec, Arch, Comms, PA, CIO) and Sonnet 5.5 (Docs, CXO, HOST, Web,
  PPM). PPM's log records xian switching it to Opus 5.5 at 10:44. Of the 24 prog-code logs, 19 record Opus 5.5 and 5 record
  Sonnet 5.5 (#2017, concepts, #2008, #2037, #2039).
- **Rule 8.** See Flags.

### Process Findings

1. **Stale rollup rows were a pattern, not an accident.** Four of Exec's rows were stale, and PPM and Arch carried one of the
   same. All three repaired on the day. The cure each wrote down is to re-check the source before a republish.
2. **Relay latency has no fast path yet.** The stuck-prompt alert catches a blocked seat after the fact. PPM's open question
   is a faster route for a time-critical PM word to the dispatching seat.
3. **One promotion is READY and waiting.** `e4f21e9ca8` (Tests success on the exact sha, 12 landings since `6f2916d10f`,
   S8 and ten other served rows pending) had no dispatch at day end. Verified how: `gh run list --workflow=fly-deploy.yml
   --event workflow_dispatch` shows the newest dispatch at 22:31Z on 10-15, the one for `762282e3fb`.
4. **Open decisions with xian at close.** #2040's Class 3 admission and the #2042 class question, the held invite sends (to be
   decided Friday), the promotion word, the consent-screen branding (name and Privacy link, Terms blank), #1913 close-or-try,
   and Exec's carry list (OpenAI top-up, a machine re-clone, 15 revisions, Spec walk-through, week-review usage patterns).
5. **Usage week review.** Ten seats logged observations and Exec's own log carries no usage line, only the relay and the
   standing row 122. The common claim is that turn count, not tier, drove cost. CXO (about 60 mail-wake turns) and Web (about
   40) both propose coalescing quiet wakes into one entry. Lead's cost centre was overlapping suite re-runs per landing. These
   are the seats' own estimates.
6. **Agent 360 and role-card work.** HOST's owed 360 v0.5 owner lines (Web, PA, Spec, Pard) remain unreplied, and HOST kept the
   same blocker lines all day.
7. **Rule 8 residue.** HOST and Exec each reported the old reissue file's name in 8 tracked files and CIO's 14:08 note named
   the same pattern. HOST edited its own sent copy to a name-free pointer, the exec and cio read copies and pushed history
   join the pile for xian's rewrite call, and nothing was removed. See Flags.
8. **Disk.** Pard's warning (Lead's 31 worktrees at 26 GB) was acted on at 17:30. Lead's rule is to remove a lane's tree when
   its landing is on main.
9. **Omnibus lag.** Docs delegated the 10-14 omnibus to a Sonnet subagent and committed it at 04:17. Docs's own usage note
   puts a subagent omnibus draft at about 240k tokens, a figure Docs says it measured for 10-14 only. The 10-15 omnibus (this file)
   is owed at Docs's 10-16 START per its 22:12 entry.

---

## Timeline (PDT)

Times are as each log wrote them. Where git commit times conflict with a log's own stamp the git time is used and noted.

### Before dawn into the START fires (04:12 to 06:50)

**04:12** **Docs** START: 10-14 logs 14 of 15 closed, Exec's open. Delegated the 10-14 omnibus to a Sonnet subagent. Logged
publishing "The Overzealous Cleanup Routine" (pubDate today) with a pre-flight (CI 12 of 12, image against alt, md5 unique among
archived images, dry-run against the draft, workDate confirmed): live URL 200, body phrase present, image 200, validator 0 errors
on 470 rows. Git shows the omnibus commit and memo to Exec at 04:17.

**04:17** **Comms** mail wake on Docs's memo: live-checked the page in a browser (H1, 0 semicolons, 5 of 5 approved edits, the one
cut clause absent, hero image loaded with alt, footer teases Saturday's post). The Medium crosspost is xian's hand. **Exec** wake:
closed the 10-14 log, put the Medium crosspost at the top of "Waiting on you" (rollup v291) and replied to Docs's rule-8 flags: the
two flagged words are names of xian's Macs, and #1623 closed 10-14 11:03 PT per the events API.

**04:27** **Docs** first addendum on the 10-14 omnibus (git time). Docs's log also records a second addendum at 07:12 for two
late prog-code logs, git `d61ebfdcf3`.

**06:18** **Web** fire 1: website fast-forwarded to `bfa963c`, the Overzealous post push. Accessibility line from a diff read
(page 200, no image without alt, no tables), not a rendered audit. Alpha `5e5f3366c4`. **06:19** **Comms** START: nothing
unblocked, deferrals named (slate scaffolds waiting on PM's 12-or-8 grouping, Sunday review waiting on PM's rewrite).

**06:26** **HOST** wake, quiet: #1968, #1967, #1895, #1834 open, 12 of 12 green, owed-scan 177 logs with 13 open. **06:27**
**Arch** START: fast-forwarded 38 commits, lint success, watched issues all open, no landing to validate yet. **06:31** **CXO**
START tick: UX line 12 open (was 10), no drift. **06:33** **PPM** START: ceiling 90 (35 lists), 9 open MVP of 316, slips 6.
**06:40** **Exec** tick, quiet.

**06:41** **Lead** START (Fable 5.1): merged 47 commits, v4 mail 16 addressed and 0 unacknowledged, held branches verified at
their carry-forward shas (446 to 516 commits behind main). **06:47** **PA** START: main's Code Quality red on Lead's own
push (the current-state `last_updated` gate). Alpha lacked the `isError` fix. Built the routing eval. **06:51** PA bumped the date
(git `fd069bb107`) and Code Quality went green (13:52Z).

### Morning: seven landings and the word map (06:50 to 10:30)

**06:49 to 07:24** **Lead** merged main into each held branch, re-ran targeted suites and round-tripped the three-migration chain on a
scratch DB, then landed in order: #2011-b (06:5x), ANALYSIS margin (07:15), #1965 with #2012 (07:17), #2009 (07:20), #2013 (07:22),
#2014 (07:24). **07:27** bookkeeping, six landing comments. **Arch**'s 07:05 ruling on #2010 had already arrived (yes with three
conditions, the census arm signal for the #852 offer_hint idiom) and Lead dispatched an Opus lane at 07:27.

**06:58** **PA** routing eval done: 105 runs for $9.67, no change from rewriting the tool description. **07:33 to 07:49** **Lead**
built #2020 directly (07:34), landed #2017 (07:37, Sonnet lane), the eight CI-workflow Concept lines (07:40) and #2010 (07:49, Opus
lane, census 38/63 to 34/57). **07:54** **Arch** validated the census (signals, adequacy, tripwire) and filed #2024. **07:55**
**CXO** copy rulings matched. **07:57** **Lead** main red on the smoke set, the #2014 foreign key hit two fixtures that invented list
ids. Fixed at 08:25 (Tests success on `bddb4a089c`).

**08:03** **Lead** landed #1771's second seam and #2019's delete cap in one push (Opus lanes, 19 minutes each). **08:09** **Arch**
validated both. **08:22 to 08:35** **CXO** ruled the four seams (a deferral pauses, only an explicit cancel or a "no" to the invitation
ends) and then one pause line for `stop` and a deferral. **08:46** **Lead** landed the four seams. **08:52** the one-line edit.

**08:54 to 09:04** The invitation-stage fact: pausing at INITIATED writes a suspended row. **Lead** offered shapes A and B, **Arch**
ruled A through the adapter with no carve-out of the hatch, **PPM** concurred, **CXO** set the invitation line. **09:15** **Lead**
landed the END and PAUSE split (Opus lane, 72 pins). **09:19 to 09:37** the word map converged (CXO, Arch, PPM) and landed at
`022dc3074c`. Meanwhile **Web** (09:19) read the served build on `5e5f3366c4`: no chips render, and a typed `skip` at "Any blockers?"
pauses the interview, the live defect. That finding became #2027. **09:27** **Arch** amended ADR-049 and the index was regenerated.

**09:07** **Exec** 24-hour rewrite watch: 57 sentinels over 290 refs, 0 hits on GitHub, 54 local refs still holding old history.
Put the guard-retirement call on the rollup (v292). **09:50** **Exec** relayed PA's S5 steps. **09:58 to 10:10** **CXO** and **Arch**
ruled the invitation edges (whole-message decline, whole-message quick bypass, "skip the questions" gives the quick standup).
**Lead** landed #2026 and #2028 at 09:58 and the edges at 10:17.

**10:07** **CIO** START: whats-armed 30 checks with 29 armed (commit-msg not armed), weekly usage 77% at the 09:23 row. Refreshed
their briefing lines, nudged Exec with the exact commit-msg paste, extended m-46 and m-43 in the methodology notes.

### Late morning: admissions, promotion readiness and the ref cleanup (10:10 to 13:30)

**10:12** **Lead** main red (2 new failures: the #2019 pins' fixture clock straddled 17:00 UTC). Fixed at cause (`3939fa234b`,
per Exec). **10:10 to 10:25** **Exec** adds the commit-msg paste to the rollup (v293), **CXO** accepts the REFINING line, **Arch** rules
"please" is politeness at the hatch and "skip the standup" a flow exit.

**10:44** **PPM** xian in session, model switched to Opus 5.5, answered PPM's three questions at 10:48: admit #2017 and #2018 (Class
4, slip row 7), #1943 to Production, #2020 not admitted. Open MVP 10 of 320. **10:52** **Exec** relayed and removed the placement
item (v294).

**11:06 to 11:15** **Lead** Tests green on `f76a307ecb`, card v38 Step 0 READY. **11:08** correction: staging served `48b86d1d57`
because fly-deploy's known-broken guard skipped the deploys. Redeployed to `f5c8e33c63`. **11:09** **Exec** wrote "Promote? Ready now"
and admitted a stale carry of their own (the #2014 counts were done 10-14). **11:13** **Arch** answered PPM: the thanks and farewell
examples ride the next catalog batch. **11:19** **Exec** relayed xian via Janus at 11:14: clean up the old refs first. **11:24**
**CIO** deleted `cio/r6-slim-probe` first (nothing unique). **11:28** **Lead** landed the seventh #1771 unit. **11:32** **Lead** deleted
44 branches and 7 refs, removed 6 clean worktrees and bundled one tip (51 of 53), with two dirty worktrees held. **11:37** **CIO** found
one held worktree was theirs and diffed its 8 paths. **11:39** **Exec** sent a "go" to force-remove, the permission classifier refused
the resend, and **Exec** held. **11:43** **CIO** tarred the 8 files. **11:51** **Lead** Tests green on `35acfe35d7`, Step 0 READY again
(card v41). **12:27** **Arch** refreshed #1028 in a gap.

**12:41** **Lead**'s last entry before the gap, "holding". **12:49** **PA** re-read #2018 and filed #2029. **12:54** **PPM** placed #2029
Production, gated through #2018. **13:05** **CXO** ruled #2029's copy (a warning card, a Reconnect button, drop "MCP connector").

### Midday: approval, stalled dispatch and the test identity (13:18 to 15:30)

**13:18** **PPM** xian in session: "I approve the promotion." Relayed to Lead and Exec. **13:20** **Exec** noted alpha at
`5e5f3366c4`, removed the promotion item. **PA** started a 45-minute `/health` watch. **13:2x** **xian** in session (via Exec's entry):
promote, force-remove OK, commit-msg hook installed (Exec: identical to the repo copy and `whats-armed` 30 of 30), and #2005 done.
**13:24** **CIO** ran the installed hook directly: refused a "fix #1" message, allowed a benign one.

**13:42** **xian** told Exec the Medium crosspost was done hours ago. **13:48 to 14:06** **Exec** re-checked every carried row and found
the test machine account existed (made 10-09). **14:0x** xian saved the account's token and login files. **14:0x** **Exec** kickoff to
CIO, HOST and Web. **14:07** **CIO** found the read-deny gap and proposed renaming. **14:09** **CIO** built the piper-shared name check
(4 of 9 under no deny). **14:09** **Exec** wrote the promotion-not-dispatched entry and asked xian to dispatch. **14:11** **Exec** told CIO
to run the check at START (duty-cycle-tick v1.54, Step 1h).

**14:19 to 14:30** **Web** read rule confirmed, built the PAT-only account `web-pat-test` and, on Exec's go, seeded the machine
account with a public repo, one commit and seven issues. **14:08 to 14:26** **HOST** renamed its mint files and the reissue file to credential names (HOST's own headings say ~14:5x and ~15:0x).
**14:36** **Exec** rollup v312. **14:39** **HOST** needs a mint rule and xian present for the second invite.

### Afternoon: promotion, served round and S5 (15:30 to 18:00)

**15:30** **xian** dispatched the promotion (run 38817618053), **Lead**'s duplicate 14 seconds later was cancelled. **15:32** **Lead** woke,
read nine memos and dispatched #2029's lane. **15:34** alpha `6f2916d10f` (Exec, PA, Web agree). **15:35** **Lead** card v42 Step 0 DONE.
**15:33** **Exec** force-removed the last two worktrees. **15:39** **Pard**'s stuck-session alert went live in mail-wake. **15:40** **Exec** retired
the sentinel file (the loop printed nothing over 247 refs). **15:41** **Lead** landed #2024. **15:46** **Lead** landed #2029.

**15:37 to 15:54** **Web** served rounds on `6f2916d10f`: S1 #2020 pass, S6 #1771 pass, S6b every row run pass, S2 #2017 pass on the two
connected pages, #2008 prose pass but three other phrasings, S7 #2019 pass, S3 #2010 yes goes to a second consent (filed as #2035
by CXO, #2034 was a duplicate). **15:47** **Exec** wake reports HOST minted the OAuth-only invite with xian present (HOST's heading says ~15:5x) and Web
served on `6f2916d10f`. **15:56** **Arch** ruled #2031, #2033, and the multi-suspended invariant. **15:58** **Exec**: xian accepted the machine account's
invite (15:50), Web's OAuth login was refused because the saved password was wrong.

**16:05** **Exec** xian fixed the login file. **16:11 to 16:14** **Web** connected the OAuth-only account on one try. **16:07** **CIO** found
`lint.yml` cancelling 91 of 100 runs and sent Lead the fix, landed at 16:09 (`9200923831`). **16:13 to 16:20** **Lead** landed #2008, the #2029
icon fix, #2031 and #2030. **16:21** **PA** S5 passed with xian on `6f2916d10f`, filed #2039. **16:24** **Lead** closed #1965 and #1889.
**16:25** **Exec** rollup v320. **16:28** **Lead** landed #2033 and #2037. **16:37** **Lead** landed #2035.

**16:41 to 16:55** **xian** made the spare Anthropic key. **Web** ran #1783 and row 5: no cap line at 7 issues, and row 5 (#1913) did not
reproduce. **16:47** **Exec** relayed xian: normal pacing from Fri 10-16. **16:48 to 16:55** the seats logged their usage lines. **16:49**
**Lead** landed #2039. **16:55** **Lead** landed the #2037 flag. **16:58** **Lead** traced #1783 (cap needs the remainder over 3).

**17:03 to 17:25** **Arch**'s #2040 condition, **Web**'s 8-issue run (still uncapped) and 9-issue run (both arms pass), **PPM** filed #2042
(second served instance of floor narration), **Lead** landed #2035's copy (17:10), #2040 (17:25). **17:19** **Pard**'s disk warning, Lead
pruned 29 worktrees (17:30). **17:19 to 17:23** **Web** calendar step C failed with `redirect_uri_mismatch`. **17:33 to 17:46** **Exec** and
**Lead** traced to `PIPER_BASE_URL` and advised one secret. **17:45** **Lead** landed #2041. **17:26** **CXO** closed #1783 (gh 00:26Z).

### Evening: calendar, red Tests and close (18:00 to 22:44)

**18:2x** **xian** set `PIPER_BASE_URL`, alpha healthy `6f2916d10f` at 18:28, redirect error persisted. **18:25** **Lead** main red on
`0741d1a5b3` (one new failure, the #1816 pin). Fix `279a595b5c`. **18:26** **HOST** routed the red to Lead (quoted backlog noise).
**18:36** **Exec** xian's `fly secrets list` showed explicit redirect secrets, Lead's one-secret claim withdrawn. **18:44** calendar
connected as xian's account. **18:45** **Lead** redirect audit on #1852. **18:57** **Lead** landed #2044. **18:59** Tests green on
`279a595b5c`. **19:01 to 19:14** **CXO** ruled the card lines and the Terms position (Privacy link filled, Terms blank), **Lead** landed
the check-error edge at 19:07. **19:30 to 19:58** **Lead** staging on `e4f21e9ca8`, Step 0 READY.

**21:18** **Web** STOP. **21:19** **Comms** STOP and day summary. **21:26** **HOST** day-close. **21:27** **Arch** STOP. **21:32** **CXO** STOP.
**21:33** **PPM** STOP: 6 open MVP of 324. **21:47 to 21:48** **PA** and **Lead** STOP. **22:07** **CIO** STOP (Code Quality completed a run at
04:49Z, first behaviour evidence for the queue fix). **22:12** **Docs** last fire: run-hot window ended at 22:00, Convergent Claims
publish waits on Sat 10-17. **22:44** **Exec** tick, last of the day: v3 0, v4 0, CI 12 of 12, alpha `6f2916d10f`, disk 80 GiB free.

---

## Coding Agent subagent logs (24, grouped)

All were Lead's lanes (Opus 5.5 unless marked Sonnet 5.5). Each ends with a verification line. None carries a DAY-CLOSED marker.
Test numbers are the lane's own, and Lead re-ran each at merge (Lead's counts are in its landing entries).

- **Standup words, #1771, #888, #2026, #2028** (7 logs). `1771` (07:29, Opus): second seam, 24 pins of which 16 fail on the pre-fix
  logic, unit selection 6633 passed and 8 skipped. `1771c` (08:26 to 08:41): the four seams, 41 pins of which 29 fail on pre-fix files,
  6719 passed. `888` (08:57 to 09:10): END and PAUSE split, 72 pins, 6798 passed. `888b` (09:19): word map (skip out, never mind
  to PAUSE), 83 pass against 17 failing on the old code, 6804 passed. `2026` (09:39 to 09:52): invitation prefix follows the actual
  transition (40 pins, 12 fail without the CLOSED branch) and seven suggestion lists deleted, 6847 passed. `1771f` (10:01 to 10:10):
  invitation edges, the ten other lists deleted, a first run read 2 failed (the #2019 clock pins that Lead fixed at 10:12), 6886
  passed after. `1771g` (11:06 to 11:23): politeness at the hatch, `skip <flow name>` exit, `contains_deferral` helper, 7061 passed.
- **Delete cap and Disconnect** (2). `2019` (07:33 to 07:50): 12 delete paths mapped (the issue named four), one builder, 5799
  passed on intent_service. `2017` (Sonnet, 07:33): 7 confirms moved to the promise-style dialog, 11 tests.
- **Census and offers** (6). `2010` (07:28 to 07:42): census 38 rows and 63 literals to 34 and 57, adequacy audit table in its log.
  `2024` (08:00 start, built 15:36): 34 and 57 to 33 and 55, 21 entry points derived by `ast` with 1 reaching a builder. `2030`
  (15:51 to 16:13): multi-intent offer carry, 17 pins, 6350 passed. `2035` (16:10 to 16:28): write offers on the #846 store,
  6354 passed, mutation checks killed all three removals. `2035b` (16:46 to 17:05): fail-closed line, self-contained offer text,
  `write_offer` reach tripwire, 6431 passed, found #2041. `2041` (17:20 to 17:30): `write_offer` carried and ranked above a hint,
  12 pins, 6443 passed, 6 of the new pins and both 2035 tripwires fail with the carry removed.
- **GitHub grant, cards and toast** (4). `2029` (15:32 to 15:43): 1973 passed on web, mcp consumer, security, integrations and
  enforcement, found #2031. `2031` (16:05 to 16:13): card on the resolver, 1995 passed, found #2036. `2037` (Sonnet, 16:25): toast and
  status line carry the API message, 5 tests, one pre-existing failing test noted. `2037b` (16:46 to 16:50): structured `leg` and
  `stale_reason` flag, 1612 passed, a restored substring match turns 3 pins red.
- **Nothing-running, issues scope, formats, redirects, CI** (5). `2033` (16:05 to 16:21): 58 pins, measured that the classifier
  returns nothing for all 17 phrasings, 7127 passed. `2040` (16:58 to 17:16): scoped empty line and the nothing-held answer, boundary
  pinned at 7, 8 and 9 issues, 87 pins in two files, 6449 passed. `2008` (Sonnet, 16:10): four string changes and 4 tests. `2039`
  (Sonnet, 16:42): redirects and human 404, 24 pins, 1198 passed. `concepts` (Sonnet, 07:39 to 07:45): Concept lines on 8 workflows,
  workflows linked 14 to 22 and none 9 to 1.

Two lanes noted the same pre-existing failure, `test_smoke_static::test_template_renders` ("Jinja2Templates not initialized"),
which fails only when that file runs alone. Lead recorded it for the backlog.

---

## Flags

- **Rule 8: a source log contains an outside person's given name.** `2026-10-15-0626-host-code-log.md`. The name is omitted
  here. Per hard rule 8 this is reported to Exec and not removed here.
- **No credential in full** appears in the source logs read. The logs carry only masked invite codes, token and key labels.
  I did not copy any of them. Exec's log carries a cloud routine trigger id, which is not a bearer credential.
- **Outside-person text possibly in other logs, not confirmed.** Exec's log uses a name for a machine re-clone that Exec's 10-14
  reply says is one of xian's own Macs, so I treated it as a machine name and did not flag it.

---

*Prepared by Documentation Management (docs-code), drafted by a subagent for PM's review. Sources: 35 session logs in
`dev/2026/10/15/`, the 11 role logs read in full and the 24 prog-code logs read for task and verification lines. All 11 role logs
carry a DAY-CLOSED marker and the 24 prog-code logs carry none, which is expected for subagent logs. Day-close grep run
2026-10-16 04:14 PDT. A dated addendum will follow if any log changes.*

*Addendum 2026-10-16 04:29: Exec answered three open items. The promotion stall and Lead's heartbeat gap share one cause: Lead sat on a ruff permission prompt from 12:43 to 15:30, which xian saw on screen, and Pard's stuck-dialog alert (fa36beb) is the fix. The piper-shared denominators (Exec 10, CIO 12) were both right when taken because the file set grew over the day, and the check read 13 of 13 on the morning of 10-16. The HOST given-name flag goes on xian's rollup with the history leftovers, so the line stays in place. Verified how: Exec's reply memo, which cites a run of whats-armed.sh and xian's on-screen report. Docs did not re-run either.*
