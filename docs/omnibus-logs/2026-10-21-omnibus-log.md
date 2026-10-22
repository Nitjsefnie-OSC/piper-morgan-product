# Omnibus Log: October 21, 2026

**Day**: Wednesday (all times and dates Pacific, PDT)
**Sessions**: 11 role sessions in 11 log files (Documentation Management, Head of Sapient Trust, Unicorn Web Designer,
Communications Director, Chief Architect, Chief Experience Officer, Principal Product Manager, Lead Developer, Piper Alpha,
Chief of Staff, Chief Innovation Officer), plus 3 non-log files in the same directory that I read in full (see Sources). No
Coding Agent (prog-code) log exists for 10-21. **One of the 11 role log files carries no day-close marker: HOST (a gap).**
**Day Type**: HIGH-COMPLEXITY: AN INFRASTRUCTURE OUTAGE FOUND, EXPLAINED AND ROUTED INTO A MUST-CLOSE, ALONGSIDE GATE HARDENING.
Alpha's database became unreachable at about 11:19 (a kernel out-of-memory kill of Postgres per PA), #2124 opened at 11:25,
and xian raised the machine to 512 MB at about 14:12 (HOST, Exec, Lead, PA). The same incident showed that Fly's restart policy
was already on and cannot fire on this crash (PA, 15:05), so xian admitted #2085 as a Class 4 must-close at 15:01 and ruled the
external restarter at 15:11 (Exec). Around it, Lead built and landed the quiet-count promote gate (07:01 to 11:40) and promoted
five times, and the Google Calendar connect went from a Testing refusal to a passing Test once xian enabled the Calendar API
(about 10:24). Three issues closed on served quotes (#2088, #2089, #2100) plus the incident issue #2124. Verified how: Lead, Exec,
PPM, CXO, PA, HOST and Arch agree on the outage window within a few minutes and on the four closes (Divergences lists the
differences). I ran no `gh` command.
**Justification**: Eleven role sessions and at least seven threads crossing three or more roles: the #2124 outage and #2085
recovery design (Lead, PA, HOST, CIO, Arch, Exec, PPM, CXO, Web), the quiet-count promote gate (Lead, CIO, Arch, PPM, CXO,
Exec, Web), the Google Calendar connect and the two Cloud projects (Exec, Web, Lead, PPM, CXO, Comms, HOST, PA, via Janus for
xian), the throwaway Notion workspace and #2100 (Web, CXO, PPM, Exec, HOST), the hosted wizard #2089 and #2088 with #2108
(Lead, CXO, Web, Comms, HOST), the seat-identity finding that every seat acts as xian's admin account (CIO, HOST, Arch, Exec,
Lead, PA), and Ship #065 from final pass to LinkedIn (Comms, Docs, Exec, Web, xian). The sub-type is an
INCIDENT-AND-GATE DAY because one outage tested the gate that Lead had been building all morning. The label is mine.
**Git Commits**: 580 on origin/main by committer date (00:00 to 24:00 PDT 10-21). Verified how: `git fetch origin main` was run
first (it printed `* branch main -> FETCH_HEAD`), then `TZ=America/Los_Angeles git log --since="2026-10-21 00:00"
--until="2026-10-22 00:00" --oneline origin/main | wc -l` printed 580, with `origin/main` at `34ade93412` at that moment (a
10-22 04:13:50 commit, outside the range). The first commit of the day is a `chore(usage)` row at 00:23:06 (`b5f44f6222`). The
last is `log(exec): 10-21 sign-off, day closed` at 23:09:14 (`ce53e1259f`). Counted by leading subject text on the same range
with awk: 228 `mail(`, 155 `log(`, 8 `chore(usage)`, 0 containing `hb`, 87 starting `Merge`, leaving 102 other commits. The 102
break down as 24 starting `cio:`, 17 starting `web log:`, 10 `arch:`, 9 `docs(lead):`, 8 `comms:`, 5 `content(` (the Ship #065 draft),
2 each of `ledger(ppm):`, `fix(gate):`, `feat(gate):`, `docs(omnibus):`, `decisions(exec):` and `chore(ci):`, and 18 singles
(`web:`, `rollup(exec):`, `refactor(integrations):`, `pa:`, `ops(cio):`, `fix(palette):`, `fix(health,gate):`, `fix(calendar):`,
`feat(wizard):`, `feat(health):`, `feat(health,gate):`, `feat(calendar):`, `editorial calendar:`, `docs(publish):`,
`chore(lead):`, `carry-forward(pa):`, `briefs:`). The four named buckets plus the 102 sum to 580. The 10-20 omnibus reported
953 on the same basis, so the day is about 39 percent smaller (computed from the two counts, 373 fewer than 953). No source log
quotes a whole-day commit total for 10-21. Layer: git history on the local object store, not the GitHub API. I did not inspect
what the 87 merge commits contain.

---

## Sources

Session logs (all in `dev/2026/10/21/`), role logs first, line counts from `wc -l`:
- `2026-10-21-0412-docs-code-log.md` (Docs, 76 lines)
- `2026-10-21-0414-host-code-log.md` (HOST, 93)
- `2026-10-21-0423-exec-code-log.md` (Exec, 145, read in full)
- `2026-10-21-0618-web-code-log.md` (Web, 126)
- `2026-10-21-0619-comms-code-log.md` (Comms, 94)
- `2026-10-21-0622-cxo-code-log.md` (CXO, 108)
- `2026-10-21-0625-ppm-code-log.md` (PPM, 194)
- `2026-10-21-0627-arch-code-log.md` (Arch, 88)
- `2026-10-21-0647-lead-code-log.md` (Lead, 201, read in two pages)
- `2026-10-21-0647-pa-code-log.md` (PA, 164)
- `2026-10-21-0701-cio-code-log.md` (CIO, 189)

Non-log files, all read in full. All three were written by PA at 06:49 (PA log) and sit in the directory with file times of 07:12:
- `compare-runs-matched-rows.py` (141 lines): PA's analysis script for Thursday's OpenAI run. It reads two canonical-run CSVs,
  drops the 25 seed-dependent rows of 61 (GitHub Q19/25/41/42/43/45/51/52/53, Calendar Q8/33/34/35/61/62, Piper-side
  Q10 to 14/18/21/30/51/53/55/56) from both sides and reports routing (effect reading), routing (category reading, reported
  only) and expected-pass quality, each with a within-5-points flag. It does not touch the frozen harness (`f7ae6f66a4`).
- `rescore-1227-effect-reading.py` (99 lines): rewrites the 10-20 12:27 canonical CSV on the frozen harness's rules, with
  the expected labels parsed by `ast` from the harness source and the effect map read from the rail registry.
- `canonical-1227-rescored-effect-reading.csv` (152 physical lines, 61 data rows with multi-line cells): the output of that
  script. I parsed it with Python and counted 61 rows of which 56 read `routing_pass` True, matching the 56 of 61 effect
  reading that PA's log reports.

Total 1870 source lines across 14 files: 1478 in the 11 role logs, 152 in the CSV and 240 in the two scripts. Verified how:
`ls -la dev/2026/10/21/` and `wc -l` listed 11 role logs and 3 other files before I started. I read each of the 11 logs in
full (Lead and the rest by line range, no skipping) and each of the 3 other files in full. No prog-code file exists in the
directory (`ls | grep -i prog` returned nothing).

Subagents: Lead's lanes (`lead-quiet`, `lead-quiet4`, `lead-quiet5`, `lead-calapi`, `lead-words`, `lead-wizard`,
`lead-restarter` and others) are named in Lead's log and have no log of their own. Docs delegated nothing on 10-21 that its
log records (the 10-20 omnibus subagent ran on 10-21 at 04:13 and is a 10-20 product). No log in the directory records any
other subagent, and I do not know whether others ran.

**Cross-reference gate**: roles mentioned without a log in this repo: Janus (relays of xian's answers and the Google console
screens, in Exec, PPM, HOST, Comms, PA) and Pard (the fly-permissions regeneration and the mail-wake script, in CIO). Both
are cross-project agents whose own repos take mail, so no `dev/` log is expected. No source-set role is missing, so I did not
ask PM.

**Day-close status** (re-grepped with `grep -c "^<!-- DAY-CLOSED"` per file at the time of writing): **10 of 11 role log files
carry a marker** (Docs, Web, Comms, Arch, CXO, PPM, Lead, PA, Exec, CIO), each reading 1. **One carries none and is unclosed:
HOST** (the grep printed 0). HOST's last entry is the scheduled 21:26 wake ("quiet", no day summary and no sign-off block), and
the log's final line is a "Verified how" line. `git log -1` on the file shows its last commit as `8cfeb786e9` at 21:26:55 on
10-21. I nudged HOST at 04:30 on 10-22 (per the caller's instruction) and the log has not changed since my grep. Lead's marker
reads `<!-- DAY-CLOSED 2026-10-21 lead-code -->` (no colon), Exec's reads `<!-- DAY-CLOSED: 2026-10-21 exec -->` and the other
eight read `<!-- DAY-CLOSED: 2026-10-21 -->`. All match the grep. Web's marker is at line 124 with a "Sign-off outputs" line
below it (lines 126), so it is not that file's final line. For the others I saw the marker as the last line.

**Reading coverage**: every file listed above was read in full. Compression: 1870 source lines to this file's 483 lines.
Every role appears in the timeline.

---

## Executive Summary

### Core Themes

1. **Alpha's database died of a memory kill at about 11:19 and came back at about 14:12 after xian doubled the machine's memory.**
   The Alpha Health Watch run read five of five probes degraded at 11:21 and #2124 opened at 11:25:10 PDT (18:25:10Z per Lead),
   assigned to xian, five seconds after the probe step failed (Lead). Lead's 11:28 incident memo described the same shape as
   #2085 on Monday: Postgres gone inside a started machine with the app up (`database: unreachable`, `web: healthy`). Debate
   ran for about 30 minutes on who restarts it (a dispatchable restart workflow, Fly's restart policy, a reviewer gate) while
   PA at 12:47 ran read-only fly commands and `dmesg` over ssh and found the kernel had killed Postgres (pid 662) at about 11:19
   and haproxy 30 seconds later on the 256 MB machine, with Monday's exit also `oom_killed=true` (PA). Lead settled on 512 MB at
   12:56. xian ran `fly machine update ... --vm-memory 512` at about 14:12 with health checks 3 of 3 and alpha read healthy at
   14:15 (Janus via Exec, HOST, Lead). The outage ran about 11:19 to 14:12 (about 2 h 53 min per HOST). PA kept raw evidence in
   scratch and deleted it at STOP (PA). Verified how: PA, Lead, HOST, Arch, Exec and PPM agree on the cause, the 256 to 512 MB
   change and the 14:12 recovery. I read no Fly output and no `/health` myself.

2. **Fly's restart policy turned out to be already on and unable to fire, so #2085 became a must-close with an external restarter.**
   At 15:01 xian admitted #2085 as a Class 4 must-close and said yes to a restart policy (Exec). PA at 15:05 found the machine
   config already read `restart: always` and `memory_mb: 512`, and read postgres-flex source (`cmd/start/main.go:93`) showing
   Postgres is the one process registered without `WithRestart`, so the machine never exits and the policy cannot fire. Lead
   concurred at 15:07 and CIO sent a correction of its own 12:29 and 12:42 advice ("restart policy first"), which it had given
   without reading the machine config. At 15:10 to 15:11 xian ruled "build (a) after main is protected" (Exec). Lead drafted the
   restarter at 15:16 on the held branch `claude/lead-restarter` (`539693606c`). CIO found at 15:20 that every seat acts on GitHub
   as `mediajunkie`, xian's admin account, so no rule or required reviewer separates a seat from xian, and HOST withdrew its
   12:42 "reviewer = attended" ruling at 15:27. Arch's review (15:29) and a second pass (15:45) and PA's run of guard 1b's parser
   on the live `fly checks list --json` (a map keyed by machine id, which would have read `absent` and refused every run) led
   Lead to `42a9767955`, `e2049f4e9d` and `33573ddb7d`. Arch validated all three guards at 15:58. Arch tested a narrowed Fly
   token (the `IfPresent` form) in a Go program against the macaroon library at 16:49 and sent the paste block, HOST approved
   it with a pre-flight at 18:21, and xian created the `alpha-db` environment (reviewer `mediajunkie`, branch pattern first
   `ops-restarter` and then changed back to `ops/restarter` at 18:25). Lead pushed `ops/restarter` at `33573ddb7d`. At close the
   `alpha-db` secret is empty and the branch ruleset does not exist, so #2085 stays open (CIO 22:07, Exec 23:08).
   Verified how: Exec, PA, Lead, Arch, CIO and HOST agree on the sequence and shas. I ran no `fly` or `gh` command.

3. **Lead built the quiet-count promote gate in the morning and the outage then exercised it.** The recorder
   (`turn_activity.py`, a process-local 30-minute window keyed by a 16-character hash) landed at 07:01 (`420d3fd2b7`, merged
   `f885995a4a`). The promote step "Alpha must be quiet" went through several amendments the same day. 07:48 a down alpha is its
   own branch with `quiet_override` reaching it (`4902f36e04`, CIO's 07:37 question). 08:16 an always-on 30-minute uptime wait
   (`8cdd2afbeb`, CIO 07:50, PPM no objection). 09:44 two fail-opens that Arch found at 09:27 (`_quiet_count` served `accounts: 0` on
   an exception and a recorder failure was swallowed) closed in `43088de246`, merged `52333d4bbc`. 10:23 a boolean shape for the
   public `/health` (`7a746acb19`, merged `d09b7e0d86`, CIO's 10:08 choice because a live count tells a watcher when a partner is
   online). 11:33 a reader bug (`89a9d67778`, an older count shape now reads `legacy`) found when the gate refused Lead's own
   11:25 dispatch. 11:40 a health refusal while `/health` status is not healthy (`97f4dbda1d`, CIO's 11:37 proposal). Lead's
   list of Wednesday promotions has five: `8e61423f1a` (07:34), `95dea16f50` (08:14), `b28d46a97f` (10:04), `ae702f6a04`
   (14:25) and `76789a8988` (15:02). The 11:25 dispatch was refused and does not count (Lead). Lead admitted a mistake at
   11:30: they read past "failure" in the latest watch run before dispatching, and wrote the rule that a failing latest watch
   run stops the dispatch before anything else is read. Arch validated grant condition 3 as served end to end on run
   39683038998 at 15:27. Verified how: Lead, CIO, Arch, Web, Exec and PPM agree on the shas and on the five-promotion count in
   the sha reads each logged. I did not diff any commit.

4. **The Google Calendar connect went from a refusal to a passing Test across three layers, none of them the one first suspected.**
   At 08:01 xian's throwaway account was refused with "app is currently being tested ... 403 access_denied" although xian's
   Audience reading was In production (Exec, Janus). Web read the `client_id` from the authorize URL at 09:18 (project number
   43539582958) and Exec relayed that alpha's client lives in the Google Cloud project "Piper Morgan (Alpha)", in Testing,
   while #2087's work lives in "Piper Morgan" (538609082609, In production). xian set the Alpha project In production by about
   10:0x, consent then passed, but Settings read "Google refused the calendar read (error)" and Lead explained at 10:08 that
   "(error)" is the classifier's catch-all. xian found the Calendar API off in the Alpha project and enabled it, and Web's
   Settings Test read "Test Passed" (Exec 10:24, PPM and CXO give 10:27 for Web's Test). Lead landed an `api_not_enabled` class
   at 10:16 (`c750fa1688`) and CXO's replacement words at about 10:30 (`b2403a3e0d`), and both rode the 14:25 promotion. PPM's
   08:04 guess that Audience had slipped back to Testing was wrong and PPM corrected it at 09:33. The seeded calendar rows are
   six (Q8, Q33, Q34, Q35, Q61, Q62), not nine, which PPM owned as its own unsourced count when PA caught it (PA 09:48, PPM
   09:51). Comms drafted the invitation's Calendar line both ways and applied both in Google's words by 10:18 (CXO accepted at
   10:21). Lead's 10:29 comment on #2092 names the missing API as a probable cause, and xian's 18:09 answer (his calendar did
   have events from 10-19 to 10-26) makes the earlier "no events" a false empty (CXO, Class 3). Verified how: Exec, Web, Lead,
   PPM, CXO and Comms agree on the layers. I opened no Google console.

5. **The throwaway Notion workspace for #2100 landed on real working notes once, and the row closed on a second token at 18:32.**
   CXO accepted a throwaway Notion workspace for both #2100 rows at 06:22 after Web showed the can't-read line renders only for a
   connected integration (`capability_legibility.py:320` per Web). Notion on alpha connects by a pasted integration token, so
   it needed xian. The first token file held the throwaway OpenAI key, masked `sk-p…mVIA` (Web, Exec 10:38), and Web fixed
   its mode from 644 to 600. The re-saved token connected to a workspace whose databases read as real project notes (about
   eight, per Web), and Web disconnected at once, sent no chat and wrote no names or contents (Web, Exec 11:10, CXO). CXO ruled no
   row on that workspace. The token was on alpha for about two minutes and in Web's session output (Exec). Janus reported at
   16:4x that Notion was redone in the test workspace and the earlier connection had been the test workspace, not xian's real
   one (Exec 16:46). Web connected the new token at 18:18 (workspace "Piper Test Calendar", 23 objects, template-like titles),
   row 1 passed, row 2 summarised an uploaded file instead of saying Notion cannot be read, and CXO closed #2100 at 18:32 on the
   three served parts. The two accounts of the real-workspace episode (a different workspace versus the same test workspace) are
   in Divergences. Verified how: Web, CXO, Exec and PPM agree on the close. I opened no Notion workspace.

6. **The hosted wizard (#2089 and #2088) was built, promoted, served and closed in one day, and #2108 was fixed by hiding.**
   At 10:44 Lead found #2089 (admitted 10-19 14:13) and #2088 had no code and no standing row, two days unbuilt in their lane,
   because the admission came through a PPM gate comment and not a memo. They built `wizard_is_hosted()`, the invite-first
   five-step order with no System step and a read-only `POST /api/v1/setup/check-invite` (282f727415, landed as `9d9a8a1354`
   at 10:51). It rode the 14:25 promotion. Web served five rows on `76789a8988` at 15:08 (strip "1. Invite ... 5. Complete",
   heading, help line, empty-code toast and invalid-code toast all as ruled), and CXO closed both issues at 15:32 with
   "Invite" accepted as the strip label. #2108 (the palette's "Start private session" entry) was built as CXO's option (a),
   commented out and pinned (`76789a8988`), and stays open because Web's account read `window.trustStage` 1 and the hidden
   entry only shows at Stage 3 or above. Lead confirmed Stage 3 needs 50 successful interactions and CXO ruled it closes on a
   Stage 3+ palette row after PA's Thursday run puts 61 turns on `web-seed-1386`. Verified how: Lead, Web, CXO, Comms and PPM
   agree on the sequence. I re-ran nothing.

7. **Ship #065 was published, deployed late and posted to LinkedIn the same morning.** xian made five admin-UI saves between
   06:46 and 07:00 (ending `2228f63f5e`), Comms read the word diff against `55d4f53d82`, xian approved seven edits and declined one
   ("at peak") and Comms sent publish-ready to Docs at 07:13 (Comms, Docs). Docs published from the website worktree with
   `--category ship`, `--work-date 2026-10-09`, no image, website commit `8de0fbf`. Web's record shows the push at 07:27:37 and
   the one deployment for that commit created at 07:44:01, 16.4 minutes later. Docs pushed an empty commit (`34175eb`) at
   07:41 to retrigger. Web later found that commit's own deployment at 07:58, 17.5 minutes after it was made, queued behind the
   first, so the retrigger did not help and the cause is on Vercel's side (Web 12:18, Docs 13:12). Three of five website pushes
   were slow (10.5, 16.4 and 17.5 minutes per Web), and Web filed website issue #50. xian posted the LinkedIn crosspost, and
   Docs set the row to distributed at 07:50 with `liPubDate` 2026-10-21 and did not open the LinkedIn URL. Verified how: Web's
   deployment times (from `gh api` deployments per Web) and Docs's validator runs, per those logs, not re-run by me.

8. **Staging got an invite and then stopped on a key length.** HOST minted the staging invite at 18:18 on xian's word, after
   xian cleared a permission screen that had held HOST's session (Exec 18:18). The token went to a 0600 file and was never
   displayed, masked `5E04…FMN5` (HOST). On staging (`d2ca2d0adb38`) Web got `check-invite` 200, but Anthropic key Validate
   returned `valid:false` with a message that the master key must be 32 bytes (AES-256) and the staging value was 48 bytes and Continue stayed disabled (Web 18:23).
   HOST read the key code at 18:27 (the key is base64 of 32 bytes and staging's secret is wrong), and the fix is one `fly secrets
   import` that needs xian to say "set the staging key" in HOST's session. Lead filed #2125 for the wizard's wrong message
   (Lead 18:33, PPM placed it on Production). At 21:18 Web re-probed staging with a fake key and got the same message (Web).
   Verified how: Web, HOST, Lead, Arch and PPM agree. I made no staging request.

9. **PA built Thursday's tooling and rescored the 12:27 baseline.** At 06:49 PA wrote the matched-row compare script and the
   rescore script (see Sources) and reports the rescore at relabelled 10, effect 56 of 61, category 55 of 61, matching the 10-20
   replay (PA). PA's mail on the calendar rows moved the count from nine to six at 09:48, and PA took the Fly restart
   question at 15:05 because Exec asked Lead or PA. Thursday's two runs (#1386 first, then the OpenAI run) have a latest start
   of 12:00 on 10-22. No run happened on 10-21 (PA, Lead, CXO).

10. **Control-plane work ran alongside.** At 07:01 xian asked CIO in conversation whether `to:` and `cc:` should wake differently,
    and CIO answered that the rule has been live since 10-16 (Pard's `mail-wake.py` CC-HOLD) and added a sender-side line to
    `mailboxes/DIRECTORY.md` on xian's yes (CIO). CIO added a "Four in one day, three seats" entry to methodology-49 at 16:07 (a
    safeguard judged by reading it rather than running it) and regenerated the day-closed-marker census for Lead's colonless
    marker form (CIO). CIO's grant condition 3 now names `.quiet`, the 1800-second uptime wait and the by-hand fallback. CIO's
    16:51 reply to Exec confirmed the agents' GitHub identity should be a GitHub App and not `dinp-machine` (its public_repo
    token sits in alpha's database, it is the test user's identity and it uses xian's one free machine account per CIO's ToS
    reading). Verified how: each seat quotes its own reads. I re-ran nothing.

### Technical Details

1. **Landings on main** (from Lead's log, in order, with the log's own shas). `420d3fd2b7` merged `f885995a4a` (quiet count),
   `ee1d905e83` merged `4902f36e04` (down-alpha branch, uptime field), `8cdd2afbeb` (uptime wait), `43088de246` merged
   `52333d4bbc` (two fail-opens), `c750fa1688` (`api_not_enabled`), `7a746acb19` merged `d09b7e0d86` (boolean shape),
   `b2403a3e0d` (CXO's calendar words), `282f727415` merged `9d9a8a1354` (hosted wizard), `89a9d67778` (reader `legacy`),
   `97f4dbda1d` (health refusal), `f663614072` (a rename lane merge), `76789a8988` (#2108 hidden), and on a held branch
   `539693606c` then `42a9767955`, `e2049f4e9d`, `33573ddb7d` (restarter). I did not check any of these shas in git.
2. **Counts quoted by Lead at merge**: whole `tests/unit` 15126 passed with 232 skipped (07:01), 9576 (07:49), 9580 with 8 skipped
   (09:44), 9515 (10:16) and 9584 with 8 skipped (10:23), with smoke 553 at each push. They are Lead's runs. I re-ran none.
3. **Quiet gate branches as built** (Lead 08:17 and 11:40). Four reads in order: no answer from `/health`, status not healthy,
   the quiet verdict (absent, broken, legacy, quiet or busy) and the uptime wait. `quiet_override` reaches each refusal.
   Served `/health` shape from 14:25: `services.chat_turns_last_30m` is `{"quiet": bool, "record_failed_in_window": bool}`,
   with `uptime_seconds` served and counts written to the server log as `quiet_count_computed`. The sha lives in the
   top-level `git_sha` field (Lead's 14:3x read of `commit` used a stale field name).
4. **Restarter guards as validated** (Arch 15:58, Lead 15:51). Guard 1b refuses unless the database machine's own check reads
   `critical` and reads the map-by-machine shape of `fly checks list --json`. Guard 2 refuses on a run it cannot read and counts
   a restart step that ran at all. Capture is tried per read and must not block the restart. The job is dispatch-only under the
   `alpha-db` environment. A drill (run 39686201600) confirmed that `gh workflow run --ref` runs the ref's copy and the file
   must also exist on main to be dispatchable (Lead 15:25).
5. **Seat identity** (CIO 15:21, Exec 15:28). Every seat acts as `mediajunkie`, admin, with `current_user_can_bypass: always`
   on the only ruleset. Push rulesets exist only for private or internal repos and this repo is public. The approval API for
   a pending deployment was used on 10-12. The proposed fix is a seat account at Write (a GitHub App per CIO 16:51 and Exec
   16:56), then a branch ruleset on `ops/restarter`, with the narrowed Fly token capping a seat-approved run at one restart.
6. **Held for Thursday.** PA's two runs (start by 12:00), Web's calendar rows on `web-seed-1386` (#2112, #2091, #2092) and the
   #2108 Stage 3 palette row, with no promotion from PA's start mail to the end of both runs (Lead). On xian's side: run the
   token block in a plain Terminal, set the ruleset, say "set the staging key" in HOST's session, pick the seat identity, the
   #2096 admin read, the partner list and the Terms rewrite (Exec, HOST, Lead, CXO).

### Impact Measurement

1. **Issues filed**: #2124 (the Alpha Health Watch alert, opened at 11:25:10 and assigned to xian), #2125 (Lead, 18:33) and
   website issue #50 (Web, 12:18). Exec, Arch, CIO and HOST each record filing none, and no other log records a filing. Verified
   how: I read the "filed" lines and wrap lines of all 11 logs. I did not run `gh issue list`.
2. **Issues closed**: #2124 (Lead 14:39 after two green watch runs), #2089 and #2088 (CXO 15:32) and #2100 (CXO 18:32), which is 4.
   I computed it from the Lead, CXO, PPM and Exec lines and did not confirm any on GitHub.
3. **MVP gate**: 9 open at 06:33 with 6 must-close (PPM, Exec). 8 after #2089 closed (15:32). Back to 9 when #2085 was admitted on
   xian's word (15:01 per Exec and PPM, ledgered at PPM's 15:33 fire, the thirty-fifth ledger entry per PPM, which I cannot
   check). 8 after #2100 closed (18:32). Must-close went 6 to 5. Exec's 23:08 entry lists the eight open (#2112, #2096, #2092,
   #2091, #2085, #2018, #1595, #1386) and PPM names the five must-close (#2112, #2091, #2092, #2096, #2085). Dates unchanged
   and no slip row (PPM). Arithmetic check: 9 minus 2 closes plus 1 admission is 8. Verified how: PPM's ledger entries and Exec's
   counts agree, and Lead's 18:36 tracker line differs (see Divergences). I ran no `gh` command.
4. **Promotions**: 5 reached alpha (list in theme 3) and 1 dispatch was refused (11:25). Alpha `/health` at close is `76789a8988`
   with the database healthy in Lead (21:48), Arch (21:27), CXO (21:32), PPM (21:33), PA (21:47) and Exec (23:08).
5. **Canonical runs on alpha**: none on 10-21. The 12:27 baseline was rescored offline (theme 9).
6. **Served rows** (Web): #2100 row 1 on `edf95b5c0c` (two turns, the can't-read line absent on an unconnected account), the
   wizard rows on `76789a8988` (five of five pass), the #2108 palette row (four entries, not served because the account was
   Stage 1), #2100 rows 1 and 2 on the new token (row 1 pass, row 2 summarised the uploaded file) and the staging validate-key
   probes (two, same 48-byte error).
7. **CI**: read 12 of 12 green at the starts and closes of Web, HOST, Exec, PA, CIO, Lead, Arch, CXO and PPM. Arch records Code
   Quality and Tests success at each of its fires. Lead notes the Tests queue was slow at 10:30. I found no red window on main in the
   logs.
8. **Ship #066 count**: PPM reports the Ship #066 count of PPM-judged admissions as still 3, since #2085 was on xian's word.
9. **Mail**: the git `mail(` count (228) is the only whole-day figure. I did not count other roles' mail from logs.
10. **Exec's rollup**: versions v482 (06:4x) through v513 (18:34), with the Artifact version running about 6 above (v488 to v515
    per Exec's entries). I did not open the artifact.

### Session Learnings

1. **Read the machine before debating who restarts it.** The restart thread ran about 30 minutes on mechanics while one read-only
   `dmesg` held the cause. The reading changed the question from who restarts it to how much memory (PA's "path" signal).
2. **A config value that is present is not a behaviour that fires.** `restart: always` was set through both outages. Postgres
   dies inside a machine that stays started, so the policy never acts. CIO logged this as methodology-49 with four same-day
   instances from three seats (Lead twice, CIO, Arch) (CIO 16:07, PA 15:05).
3. **Run a guard's own code on the tool's real output.** Two reviews validated guard 1b against its assumed input shape. PA's
   one run on the live JSON showed it would read `absent` for every status and refuse every dispatch (PA 15:47, Arch 15:58, Lead
   15:51). Arch separately wrote that its 15:45 validation had not run the parser.
4. **A failing latest check stops the dispatch before anything else is read.** Lead read past "failure" at 11:25 (Lead).
5. **A pin that executes the embedded reader beats one that greps the YAML.** Lead's `legacy` fix pins the reader on eleven
   bodies (Lead 11:33), and the health refusal pins five bodies.
6. **An admission on an issue is a standing row whoever relays it.** #2089 and #2088 sat two days without code (Lead 10:44).
7. **Check a credential's scope before proposing a new use for it.** The deploy token was app-scoped to `piper-morgan` and could
   not act on `piper-morgan-db` (CIO 12:28, Lead 12:37).
8. **Check what a file holds before using it.** The Notion token file held the OpenAI key (Web 10:28, mode set to 600), and
   Exec read credential files by a count-only grep that it recorded as a slip (Exec 06:4x).
9. **A read is stale once someone else is editing the thing.** CIO's hyphen memo went out a minute after xian changed the branch
   pattern back (CIO 18:37).
10. **Estimated timestamps keep recurring.** Exec (v504 and v505), Arch (decisions line 09:35 vs 09:28), Lead (an issue comment
    "10:4x"), Web (a memo draft) and CIO (two stamps) each logged a guessed time that the clock or `mail-send`'s stamp check
    corrected before commit (Exec 15:10, Arch 09:27, Lead 10:30, Web 18:23, CIO wrap).
11. **Filename length is gated by the sender.** `mail-send` refused a 180-character filename twice for Lead and once for PPM, and
    Lead's rule is to gate the send on the printed length (Lead 14:39, 15:35, PPM wrap).

### Divergences and Notes

- **Day-close markers.** 10 of 11 role log files carry one. HOST carries none (see Sources). Web's marker is not the final line.
- **When the outage began.** Lead, Exec and CIO write "between 10:55 and 11:21". PA and HOST give the OOM kill at about 11:19
  (PA's boot-time arithmetic) and HOST computes 11:19 to 14:12 at about 2 h 53 min. Arch writes "since ~11:21". PPM writes "since
  about 11:00". PA's day arc says "about three hours". #2124 opened at 11:25:10 (Lead). I report about 11:19 on PA's dmesg read.
- **When it recovered.** HOST, Exec, Lead, PPM and PA say xian ran the update at about 14:12, PA's day arc and Arch say 14:13, and
  Exec's wrap says 14:14. I report about 14:12.
- **Ship #065 time.** Docs's heading is 07:44 (the time it logged) and its STOP line says "published (07:27)". Web's deployment
  data gives the push at 07:27:37 and the deployment at 07:44:01. The Docs publish commit in this repo is `6c749f29ee` at
  07:44:31 per git. Docs's 07:44 entry says the page went live soon after its retrigger and Docs's 13:12 entry withdraws that
  (the original push deployed). Docs says the 404 lasted about 17 minutes, Web measures 16.4. I report 07:27 for the website push
  and 16.4 minutes for the deployment lag.
- **Docs's own publish-ready time.** Docs and Comms both give 07:13. Exec's entry that records it is stamped 07:47.
- **The real-workspace Notion episode.** Web, CXO and Exec describe the 11:10 connection as landing on xian's real working
  pages. Exec's 16:46 entry relays Janus saying the earlier connection was the test workspace and not xian's real one. The logs do
  not resolve which, and Exec records the row `notion-decision` as closed. Web's 18:34 entry and CXO's close both stay careful to
  say the test workspace only.
- **MVP gate count at 18:36.** Lead's 18:36 tracker line reads "gate 9 open / 6 must-close", while Exec (18:34), CXO (18:32) and
  PPM (18:33) read 8 open and 5 must-close after #2100 closed at 18:32. Lead's 18:33 entry does not mention that close, so the
  tracker was probably built a few minutes before it. I report 8 and 5.
- **Staging key.** Lead's 21:48 entry says staging restarted about 18:37 (HOST's key reset, unverified by Lead). HOST's 21:26
  entry says the key is still unset, waiting on xian saying "set the staging key", and Web's 21:18 probe still returned the
  48-byte error. I report the key as not fixed, since two logs give a direct reading and Lead's is marked unverified.
- **HOST's list versus Exec's corrections.** HOST's 18:18 blocked-on-xian list still includes the Google sign-in (Thu ~09:00),
  the Notion revoke and the Audience/project fix. Exec's 18:20 memo told HOST that four items were stale. HOST's 21:26 list drops
  them. The consent and Test results at 10:24 to 10:27 (Web, Exec) support Exec.
- **Calendar row count.** The 10-20 mail said nine. PA's spec gives six (Q8, Q33, Q34, Q35, Q61, Q62) and PPM owns "nine" as its
  own unsourced count. Lead's 09:06 memo and PPM's 08:04 memo still said nine before the correction.
- **Promotion numbering.** Lead's headings say "PROMOTION 11 (first of Wednesday)" and "PROMOTION 13 (Wednesday's third)", then
  "fourth update" and "FIFTH promotion", which continue 10-20's count of ten. I report five on 10-21. No log lists the 10-21
  promotions in one place.
- **Calendar Test time.** Exec's 10:24 entry relays Janus, and PPM (10:34) and CXO (12:32) cite 10:27 as Web's Test time. Web's
  entry has no time in its heading. Treated as the same event.
- **Restart policy statement.** Lead's 11:28 memo says Postgres died "inside a started machine" and Exec flagged at 15:01 that a
  restart policy acts on machine exit. PA confirmed this at 15:05. CIO's 12:29 "restart policy first" advice was withdrawn by CIO
  at about 15:09.
- **Estimated stamps in headings.** Exec uses `06:4x` and `10:0x` forms, Web has several untimed "MAIL WAKE" headings, PPM and
  Comms have "07:1x" and "09:3x" stamps inside entries, and Comms's 07:13 entry says "logged, ask received after 07:00".
  Times in this file are as the logs wrote them.
- **HOST's 10-20 close time.** HOST logs the late close of its 10-20 log at 04:14, Docs logs the close at 04:13 and my 10-20
  addendum said commit time 04:13. Treated as the same event.
- **Reading depth.** Web skimmed one long PPM reply (first 700 characters per line, 09:18) and read two further batches to about
  the first 20 to 24 lines each (09:21 and 15:08 entries). Web flags these itself. I treat memos only as quoted.
- **Model mix.** Headers record Fable 5.1 (Lead), Opus 5.5 (Comms, Arch, PPM, PA, Exec and CIO) and Sonnet 5.5 (Docs, HOST, Web
  and CXO, whose header says `claude-sonnet-5-5`).
- **Rule 8.** See Flags.

### Process Findings

1. **Eight of 11 role logs record a correction of the seat's own earlier statement or omission.** Docs (the 07:44 retrigger
   claim, corrected at 13:12), HOST (its 12:42 ruling withdrawn at 15:27), Web (a first deploy note that called `4f3582d` fine
   without checking, and a palette row that did not cover Stage 3), Arch (guard 1b validated without running the parser, the
   15:29 caveat found wrong at 16:49, a guessed stamp), PPM (the Testing guess and the "nine" rows), Lead (the 11:25 dispatch,
   the reader claim, the token scope), Exec (the 09:2x lean, the credential-file grep, guessed times) and CIO (the restart-policy
   advice, the hyphen memo). Counted by reading each log. Comms, CXO and PA record none that I could find. Several were caught by
   a second seat within the hour (PA caught PPM's and Arch's, Web caught Exec's and Lead's).
2. **xian worked through Janus and Exec for much of the day, and was in session three times.** xian was in conversation with CIO at
   07:01, with Exec at 15:10 and 18:09 (and again at 18:22), and with HOST at 18:18 (Exec, CIO, HOST). The 15:01 and 15:11 rulings
   and the 15:45 to 16:56 seat-account discussion landed as relays and in `decisions.log` (Exec).
3. **Defects came from use again and from the gate itself.** The refused dispatch found the reader bug, PA's real-output run found
   guard 1b, Web's served rows found the palette row gap and the staging key, and Arch's source read found both fail-opens and
   the #2125 catch-all.
4. **Open decisions with xian at close**: the token block in a plain Terminal, the `ops/restarter` ruleset, the seat-account route
   (a GitHub App), the staging key word, #2096's admin read, the partner list and held sends, and the Terms rewrite with its HALT
   pass (Exec, HOST, CIO, Lead, CXO). Thu 10-22's post "The Tracker That Lost Track" has no rewrite (last draft commit 10-02),
   which Comms treats as a normal day-before rewrite.
5. **Deferrals with a named trigger.** Docs's Tracker and Inset publishes wait on Comms setting `ready-for-docs`, and the #1909
   fixtures box waits on Lead after 10-30. PA's two runs wait on Web's go or 12:00. The restarter main copy waits on Exec's word
   after the ruleset and secret (Lead). CXO's #2108, #2112, #2091 and #2092 rows wait on PA's runs. The readiness read waits on
   PPM's 10-22 START (PPM).
6. **Fire coverage.** Docs fired at 04:12, 07:12, 10:12, 13:12, 16:12, 19:12 and 22:12. HOST ran scheduled wakes at 06:26,
   09:26, 12:26, 15:26, 18:26 and 21:26 with mail wakes between (04:14, 04:26, 11:30, 12:42, 12:55, 14:15, 16:50, 18:18, 18:21 and
   18:44). Lead's cron fires arrived 30 minutes late (06:17, 15:17, 18:17, 21:17) and about 94 minutes late (the 12:17 tick at
   13:51). Exec's fires ran late as well (10:38 at 10:54, 14:38 at 14:53, 18:38 at 18:53 and 22:38 at 23:08). Comms fired at
   06:19, 09:19, 12:19, 15:19, 18:19 and 21:19 plus the 07:13 ask and a 10:18 mail wake. CIO ran START at 10:07, a work fire at
   16:07 and STOP at 22:07 plus mail wakes.
7. **Unclosed logs.** One role log (HOST). Docs's 22:12 STOP entry does not mention a nudge to HOST, so the Thursday 04:12 START
   owes the 10-21 omnibus and nudges (Docs). The caller's 04:30 nudge on 10-22 is the first.
8. **Sign-off blocks are uneven.** Lead's block prints ` M` files and ends with an empty `git log` line labelled "before the
   final commit" and no final verification line. CIO's lists the hook's probe log as unstaged. PPM says the post-push check is in
   the fire summary and not the log. Exec, CXO, Arch and PA print full clean outputs.

---

## Timeline (PDT)

Times are as each log wrote them. Where a log flags that its stamp was estimated, that is noted.

### Overnight into the START fires (00:00 to 06:30)

**00:23** first commit of the day (`chore(usage)`). **04:12** **Docs** START, 10-20 omnibus subagent, committed 04:20. **04:14**
**HOST** closed its 10-20 log after Docs's nudge. **04:21** **Docs** added the HOST addendum. **04:23** **Exec** mail wake,
the omnibus flag. **04:26** **HOST** mail wake from Exec (Rule 8 note). **06:18** **Web** START. **06:19** **Comms** START.
**06:22** **CXO** mail wake (#2100 throwaway Notion accepted). **06:25** **PPM** mail wake. **06:26** **HOST** scheduled wake
(logged 06:28). **06:27** **Arch** fire. **06:31** **CXO** START fire. **06:33** **PPM** START fire.

### Morning: the quiet gate, Ship #065 and the Calendar connect (06:45 to 10:55)

**06:47** **Lead** START (06:17 fire, 30 minutes late) and **PA** START. **06:49** **PA** wrote the compare and rescore scripts.
**06:52** **Lead** built the quiet count. **06:53** **Exec** fire (06:38). **07:01** quiet count landed, and **CIO** answered
xian's to/cc question. **07:13** **Comms** sent publish-ready for Ship #065. **07:27** website commit `8de0fbf` pushed (Web).
**07:34** promotion `8e61423f1a`, **07:37** **CIO** updated condition 3. **07:41** **Docs** pushed the empty retrigger commit.
**07:44** the Ship deployment was created (Web) and **Docs** logged the publish. **07:48** down-alpha fix landed. **07:50**
xian's LinkedIn post, **Docs** set the row to distributed. **08:01** **Exec** mail wake: calendar seeded, connect refused.
**08:14** promotion `95dea16f50`. **08:17** uptime wait landed. **09:02** **Exec** asked Lead which client. **09:06** **Lead**
answered from source. **09:18** **Web** read client id 43539582958. **09:27** **Arch** found the quiet-count fail-opens.
**09:32** **CXO** ruled the Testing-case Calendar line. **09:42** Janus: two Cloud projects. **09:44** fail-opens landed.
**09:48** **PA** fire, six calendar rows. **09:52** Alpha project In production, first read refused. **10:01** promotion
`b28d46a97f` dispatched (success 10:04). **10:07** **CIO** START. **10:08** **Lead** answered "(error)" from source.
**10:16** `api_not_enabled` landed. **10:18** **Comms** applied both Calendar lines. **10:23** boolean quiet shape landed.
**10:24** Janus: Calendar API enabled, Test passed. **10:27** Web's Test (per PPM, CXO). **10:34** **PPM** mail wake. **10:44**
**Lead** found #2089 and #2088 unbuilt and built the wizard. **10:51** wizard landed (`9d9a8a1354`).

### Midday: the outage (10:55 to 14:45)

**10:57** Notion token re-saved (Exec relay). **11:10** Web disconnected the token that reached real pages (Exec). **11:19**
approximate OOM kill (PA). **11:21** a watch run failed. **11:25** #2124 opened at 11:25:10 and **Lead**'s dispatch was
refused, and HOST's mailbox got three messages at 11:25:32 to 11:25:33. **11:30** Lead's incident memo, **HOST** mail wake
and **Exec**'s urgent relay to Janus. **11:33** reader fix. **11:40** health refusal landed. **12:18** **Web** read `/health`
degraded. **12:27** **Lead**, **Arch** and **HOST** noted the hour-plus outage. **12:42** **HOST** ruled on the restart
workflow. **12:47** **PA** read the machine (OOM). **12:56** **Lead** said 512 MB. **13:12** **Docs** corrected the retrigger
claim. **14:12** xian ran the memory update. **14:15** **HOST**, **Exec** and **Lead** read alpha healthy. **14:25** promotion
`ae702f6a04`. **14:29** **CXO** ruled #2108 (a). **14:39** **Lead** closed #2124.

### Afternoon: the restarter (15:00 to 18:00)

**15:01** xian admitted #2085 and said yes to the restart policy (Exec). **15:02** promotion `76789a8988`. **15:05** **PA**
found the policy cannot fire. **15:08** **Web** served the five wizard rows. **15:10** xian ruled (a) after main is protected
(Exec 15:10 and 15:11). **15:16** restarter drafted. **15:18** **Web** corrected the palette row. **15:19** **Comms** fire.
**15:21** **CIO** posted the seat-identity finding. **15:25** **Lead** dispatch drill. **15:27** **HOST** withdrew its ruling.
**15:32** **CXO** closed #2088 and #2089. **15:33** **PPM** ledgered 9 to 8 and the #2085 admission. **15:45** **Arch** reviewed
guard 2. **15:51** **PA** and **Lead** found and fixed guard 1b. **15:58** **Arch** validated. **16:46** **Exec** mail wake.
**16:49** **Arch** token steps, **16:54** revised. **16:50** **HOST** custody lines. **16:51** **CIO** GitHub App route.

### Evening: staging, the token block and close (18:00 to 23:10)

**18:09** xian in session (Exec). **18:18** **HOST** minted the staging invite. **18:19** **Comms** fire. **18:21** **HOST**
approved the token block. **18:22** `alpha-db` created. **18:23** **Web** blocked on the staging key. **18:25** branch pattern
changed to `ops/restarter`. **18:27** **HOST** read the key code. **18:32** **CXO** closed #2100. **18:33** `ops/restarter`
pushed and #2125 filed (**Lead**). **18:36** **Lead** card v101. **21:18** **Web** STOP. **21:19** **Comms** day close.
**21:26** **HOST** quiet wake (last entry). **21:27** **Arch** day wrap. **21:32** **CXO** day close. **21:33** **PPM** STOP.
**21:47** **PA** STOP. **21:48** **Lead** STOP. **22:07** **CIO** STOP. **22:12** **Docs** STOP, day closed. **23:08**
**Exec** quiet fire and wrap. **23:09** last commit of the day (`log(exec): 10-21 sign-off, day closed`, `ce53e1259f`).

---

## Coding Agent subagent logs

None exist for 10-21. `ls dev/2026/10/21/` listed 11 role logs and 3 non-log files, and `ls | grep -i prog` returned nothing.
Lead's lanes are named in Lead's log and have no log of their own. I do not know whether other subagents ran.

---

## Flags

- **Rule 8: no outside person's name found in the 10-21 logs, and one location detail omitted.** PPM's 10:34 entry, CIO's
  10:30 and 10:44 entries and Exec's 10:38 entry discuss a partner's country that appears in a checklist row. I did not repeat
  it. PPM left the row as written, CIO kept it out of the grant and Exec recorded it on row 102. HOST's 04:26 entry and Exec's
  04:23 and 16:46 entries refer to older outside-name mentions (a 10-20 HOST entry and a 10-09 memo) and do not repeat the
  names, and I did not repeat them either. Arch's 06:27 entry says "an outside commenter" on #1152 without a name. I read all
  14 files in full but did not run a capitalised-name pattern search, so a name I did not know to look for could still be
  present.
- **No credential in full** appears in the source logs I read. HOST, Exec and Web quote masked forms (`5E04…FMN5` for the
  staging invite and `sk-p…mVIA` for the throwaway OpenAI key) and a Notion token prefix and length only. I copied no unmasked
  value into this file.
- **Unclosed log file**: HOST (no marker). I nudged HOST at 04:30 on 10-22 (per the caller) and the log was unchanged at my grep.
  A dated addendum will follow if it closes.
- **Method notes**: the commit count ran after `git fetch origin main` with `TZ=America/Los_Angeles`. I ran no `gh` command and
  no fly command, so every issue number, close time, run id and sha in this file is as the role logs report it. I did not
  re-verify them, and where I wrote "computed" the arithmetic is mine from the logs' numbers.
- **Possible gap**: several roles correct their own numbers inside their logs (see Process Findings item 1). I flagged those I
  noticed. Others may remain. Lead's sign-off block is incomplete as noted in Process Findings item 8.

---

*Prepared by Documentation Management (docs-code) via a Sonnet subagent. Sources: 14 files in `dev/2026/10/21/` (11 role log
files from 11 roles and 3 non-log files, all read in full). Ten of the 11 role log files carry a DAY-CLOSED marker and one
does not (HOST). No prog-code log exists for the day. Day-close grep run 2026-10-22 early morning PDT. A dated addendum will
follow if HOST's log changes.*
