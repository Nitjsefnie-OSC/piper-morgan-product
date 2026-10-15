# Lead carry-forward — Fable 5.1 seat; Model A worktree ~/Development/piper-morgan-worktrees/lead

## STATE @ 2026-10-15 08:06 PT — batch + build phase LANDED (main bf03ac3ab2); main went red once on s2014items and was fixed at cause (bddb4a089c); Tests queued; #2024 in a lane; RUN-HOT until Thu 22:00
- **Landed today (each re-run at merge; log entries carry "Verified how"):** #2011 census-b f86c23028f · ANALYSIS margin + page:/projects f08a9693a0 · #1965+#2012 e42cae9d07 · #2009 8628aba99c · #2013 305e409e3f · #2014 b0d96b272b · #2020 77a8bfebdb · #2017 53f5801caa · Concept lines 36ffdd09e1 · smoke fixtures fix bddb4a089c (MAIN RED → green pending) · #2010 + offer_hint census signal 46899c547f · #1771 second seam + #2019 cap bf03ac3ab2. Filed: #2025. Issue comments on all.
- **Served checks owed on the NEXT promotion (xian's word only; card v37 lists them):** #2020 no-report decline line; #2017 Disconnect click (5 pages); #2010 `list my projects` on a no-projects account → `yes` (CXO); #2012 Test reply per leg (CXO); #1965/#1889 four reads with the Alpha app revoked (PA with xian); #1771 Web's three runs (stop → do a standup → not now → continue); #2019 `delete the first two reminders` → capped reply, both still present (CXO) — supersedes the card's N5 row.
- **#2024 lane (Opus, `lead-2024`, `claude/lead-2024-single-offers`):** CXO's single-offer copy for 2383/2458 + professional branch; drop offer_hint on archive/restore/search not-found; census hardening (a) non-question offer_text fails, (b) tripwire covers the transitive closure. My re-run at merge.
- **For CXO (memo sent 08:06):** #1771's four further seams (mid-interview "not now" ends the standup via #1529 with a "/standup" string; the just-started handler abandons on later/not now/no/cancel; "couldn't find the paused standup" says "/standup"; bare "later" is not a deferral at the offer) need a behaviour/copy call before any build.
- **Discipline added today:** migration landings run CI's `-m smoke` on a scratch DB at head before the push; `-m "not llm"` on any selection reaching `tests/intent` (conftest reloads the key from the keychain).

- **Landed this morning, in order, each re-merged + re-run (log entries with "Verified how"):** #2011 census-b f86c23028f → ANALYSIS margin + page:/projects re-point f08a9693a0 → #1965+#2012 e42cae9d07 → #2009 8628aba99c → #2013 305e409e3f → #2014 b0d96b272b. Three migrations (q2009nn, r2013kgnn, s2014items) ride the next staging deploy: **read the deploy's alembic line** on the first staging build of b0d96b272b (backfill asserts 0 orphans, stops loudly). Issue comments posted on all six; decisions.log lines written.
- **#2010 HELD → lane (Opus) in `lead-2010` on `claude/lead-2010-list-projects-offers` (531b3bb853 rebased on main):** Arch RULED 07:1x (inbox memo, filed): offer_hint idiom is an arm, signal (i) `_track_offer_hint(` call / (ii) `"offer_hint"` key, with a reach tripwire for (ii), the offer_text adequacy audit per removed row (mismatches stay + become findings), one PRESENT-NOT-ENFORCED line, action_registry stale comments fixed; #2010 restructure approved (functions not constants; `_handle_projects_query` renders the empty state itself; one source; markers stay 10). My re-run at merge, then land; CXO's `list my projects` served check after the next promotion.
- **Next after the batch:** Tests green on b0d96b272b → staging builds it → card **v37 "ready"** (mirror artifact republished from `scratchpad/pm-test-card.html`, still at v35) → the next promotion ONLY on xian's explicit word. Served checks owed after it: #1965/#1889 four reads with the Alpha app revoked (PA with xian), #2012 Test line per leg (CXO), `list my projects` (CXO, after #2010 lands), Web's #1783 arms + CXO's #2008 reading need a GitHub-connected active account (Exec's blocker).
- **Then build (unchanged order):** #1771 second seam → #2019 cap → #2020 strings → #2017 Disconnect; #2023 corpus rows first (Arch's ruling); #2021 with Arch after #2019; #2015/#2016 own triggers. `claude/lead-1943-clear-todos-resolver` 6fd438bba0 HELD indefinitely (flip held).
- **DISCIPLINE (added 10-15 after main went red on s2014items): a landing with a migration runs CI's smoke set (`-m smoke`, CI's ignores) against a scratch DB migrated to head before the push** (`CREATE DATABASE piper_x; POSTGRES_HOST=127.0.0.1 POSTGRES_DB=piper_x alembic upgrade head; pytest -m smoke …; DROP DATABASE`); the pre-push hook's smoke run uses the unmigrated dev DB. Also: the test conftest reloads ANTHROPIC_API_KEY from the keychain, so always add `-m "not llm"` on selections reaching `tests/intent`.
- Local lesson today: a suite selection that includes `tests/intent` without `-m "not llm"` hangs at 94% under the stripped env (an llm-marked test waits on a call it cannot make); CI's Tests runs `tests/ -m "not llm"`. Use the marker filter on any selection that reaches `tests/intent`.

### Earlier @ 2026-10-14 21:2x PT (DAY CLOSED) — alpha PROMOTED to `5e5f3366c4` on xian's word (run 38678103509, 20:47–20:55); 7 held code branches to land 10-15 morning; RUN-HOT until Thu 22:00
- **10-15 FIRST, in order, each re-run at merge, docs+code in one push each:** (1) `claude/lead-2011-unarmed-census-b` 94310057c7 → (2) `claude/lead-2010-list-projects-offers` b0545125c7 (its two literals lower the frozen census row) → (3) `claude/lead-analysis-margin` de54cb5daf → (5) `claude/lead-1965-iserror` 54989e1ce5 → (6) `claude/lead-2009-owner-not-null` ee085308bc → (7) `claude/lead-2013-kg-owner` 600fd41372 → (8) `claude/lead-2014-items-check` ca51b60756 (counts DONE 0/0). Then landing notes, decisions.log lines, issue comments, **Tests green on main**, then say "ready" on the card (v37) and dispatch the next promotion only on xian's word. After it: #1965/#1889 served disclosure on xian's account (PA runs), #2012 Test line per leg (CXO), `list my projects` once (CXO), Web's #1783 arms need a GitHub-connected account (>5 open issues; joins #2008's blocker).
- **Then build (10-15, after the batch):** **#1771 second seam (served finding 21:42, comment on the issue):** a DEFER phrasing with a suspended standup and NO offer pending falls to `detect_flow_exit` → `_abandon_suspended_standup` ("paused standup has been cleared"); and the continue/restart offer (`_arm_resume_offer` ~4591) is unreachable on an account with no source because the empty-source reply answers first. Fix both + pins + Web's three runs again. CXO's strings 21:50 for the same fix: after `stop` → "No problem — I've paused your standup. Just ask when you want to pick it back up."; abandon only on explicit cancel ("cancel that", "forget it", "start over") → "Okay, I've dropped your paused standup. Say 'do a standup' whenever you want a fresh one." (the /standup form goes); defer line stays as ruled. Then #2019 interim cap on N>1 todo deletes in the delete handler, every entry path, CXO's copy on the issue (ruled), pins per path + served run; #2020 two strings in `standup_preferences.py` L246/L261: CXO RULED 21:35 the word is "this chat"; decline line with no report = "No problem. I won't ask again in this chat. Say 'my standup interview' any time to try the guided version."; suppression stays per chat; #2017 Disconnect (promise-style `Dialog.confirm` on integrations.html + the four settings pages, render test; cause on the issue). #2023 RULED by Arch 21:24 (issuecomment-6184376162): one generic LLM judgment in `ProcessRegistry.check_active_processes` before `handle_message` (ANSWER / REQUEST / UNSURE against the process's current prompt; only confident ANSWER writes; REQUEST suspends and is answered, which unblocks #1771's resume offer; UNSURE or judge error asks CXO's armed line; ESCAPE_COMMANDS stays; regex layers retire pattern by pattern); BEFORE build: corpus rows per question (plan-shaped answers stay ANSWER, Web's requests REQUEST, ambiguous UNSURE; false REQUEST on real answers is the rate to watch); CXO's acceptance run on the issue; CXO's UNSURE line "Is that your answer to \"{current prompt}\", or something else?" armed; Arch 21:44: bind the UNSURE replies through `evaluate_acceptance` (ACCEPT → answer; naming the other choice → request; PASS/STATE_QUESTION → the shorter re-ask), and after two unclear replies suspend, file nothing, execute nothing, say the hold line; Arch has no objection to the #1771 fix order; not MVP; #2021 soft delete (lifts #2019, 7-day window, Arch's design note) scheduled with Arch after #2019; #2015, #2016 own triggers.
- **xian's rulings tonight (decisions.log):** yes to the promotion (dispatched by Lead); lean against irreversible bulk delete → approved PPM's recommendation (hold the `clear_todos` flip, soft delete first, cap interim); "clear" asks, never defaults. `claude/lead-1943-clear-todos-resolver` 6fd438bba0 HELD indefinitely (flip held).
- **Step 0 on the card: DONE 20:55 (v36).** N5 PASS judged. #1843 CLOSED by CXO on Web's run. #1771 resume offer: Web runs the escape-word leave path (`stop`) next. PM-gated still: #1913 spare key; Fri 10-16 PROD key move; the next promotion's word.
- (Earlier state kept below for the record; items above supersede their counterparts.)
### Earlier @ 17:24 PT — RUN-HOT: 4 MVP closes, 9 landings, held branches; Step 0 was READY (staging f8b2d15e52, card v35)
- **Promote gate WIDENED 3153ab903a (16:14 10-14):** staging had drifted on docs-only pushes to `d2a3f1e0c5`, 186 commits past the tested `bc3ede7e35`, beyond the gate's 60-ancestor one-call-per-commit walk → a dispatch would have been refused. Now one API call lists Tests' 100 newest run heads on main and a local rev-list (2000) walk intersects it. Probe accepts d2a3f1e0c5 via bc3ede7e35. Tests on 3153ab903a was cancelled by Exec's scripts push (85cef5be30, run 38652585915 in progress 16:12); staging moves to 85cef5be30; Tests on 85cef5be30 was cancelled too (CIO's scripts push) → **test.yml concurrency 3b92152c14: cancel-in-progress only on pull_request; main queues** (today before it: 16 cancelled / 2 success). Both queued runs completed success; **card v35 READY at 17:24** (staging f8b2d15e52, exact-sha success). Keep: a docs push no longer threatens the gate; a code push just queues a run. Probe: `SHA=<staging full sha> GITHUB_REPOSITORY=mediajunkie/piper-morgan-product bash scratchpad/gate.sh` (scratchpad copy mirrors the new walk).
- **HELD #5: `claude/lead-1965-iserror` 54989e1ce5** (a07796a06b #1965 OAuth-leg tool error → STALE_TOKEN, never `[]`; 54989e1ce5 #2012 one probe through the resolver for both legs, serving leg named with CXO's three lines, no global-key fallback, `unscoped_reads` ceiling 45→44; router no-token warning → info; 769 passed across integrations+security+consumer). Served checks owed after it lands: xian's account with the Alpha app revoked → disclosure on the four reads (#1965/#1889); CXO judges the Test reply per leg (OAuth-only, PAT-only, stale-OAuth-plus-PAT; the accounts are on xian's rollup) (#2012).
- **HELD #6: `claude/lead-2009-owner-not-null` ee085308bc** (q2009nn revision + writers + models + metadata pin; Arch's rulings applied; my re-run 373/408; lane round-trip on a scratch DB). Lands in the batch after PM's promotion, after #1–#5; it carries a migration: read the deploy's alembic line.
- **HELD #7: `claude/lead-2013-kg-owner` 600fd41372** (on the 2009 branch; r2013kgnn after q2009nn; KG routes were failing outright, fixed; my re-run 868). Lands after #6.
- **NEW 10-15: #2020 (Lead string fix, standup_preferences.py L246/L261, CXO's ruled line on the issue; pins on both strings).** Soft-delete design note (Arch, lifts #2019): `docs/internal/architecture/design-records/design-note-todo-soft-delete-undo-2026-10-14.md`; build only once PPM's C issue exists.
- **NEW 10-15: #2019 interim cap on N>1 todo deletes (xian approved PPM's recommendation 21:0x 10-14; build after the held batch lands; pins per entry path + served run; CXO copy).** `claude/lead-1943-clear-todos-resolver` 6fd438bba0 stays HELD indefinitely: the flip is held on that decision; soft delete (PPM files) lifts it.
- **HELD #8: `claude/lead-2014-items-check` ca51b60756** (on the 2013 branch; s2014items after r2013kgnn; Arch's SET NULL + precheck 2 + delete_list condition all in; my re-runs: default DB 854, CI-shaped scratch DB clean of FK/CHECK failures). Lands after #7. Production counts DONE by xian 21:2x 10-14: 0 and 0 (on #2014); no gate left but batch order.
- Filed today from this chain: #2013, #2014 (held above), #2015 (update_todo_relationships str/enum; no live caller), #2016 (10 seed-dependent tests fail on an empty migrated DB; pre-existing). All Lead/Production; PPM places.
- **(SUPERSEDED: promoted 20:55 10-14.) Was READY at 12:0x (card v33):** staging `1746f1ebec`, Tests SUCCESS on `bc3ede7e35`. PM promotes (his hand); then Web/CXO served rows:
  N5 #1943 delete-first-two; #1843 REFINING seam ("please remove the fluff" edits, "please go ahead" finalizes); #1771+#2007 (`not now` at the resume
  offer → CXO's line; `do a standup` → continue/restart offer); #1783 (capped list → `could you show me the rest?` pulls the rest; `can you delete the
  rest?` not cashed); #2008 copy ("No completions yesterday."); **after the margin fix lands: `list my projects` once (active projects shown, CXO judges)**.
  Mail Web the alpha sha when it changes.
- **READY TO LAND after the promotion, in ONE push, each re-run at merge (14:02):** (1) `claude/lead-analysis-margin` de54cb5daf (ANALYSIS margin
  example + corpus/pointer re-point; Arch accepted (b)); (2) `claude/lead-2010-list-projects-offers` b0545125c7 (CXO's #2010; her served check after);
  (3) `claude/lead-2011-unarmed-census-b` 94310057c7 (census re-shaped per Arch + shrunk per CXO, 53→20; Arch's Rule-0 word on 5 dead modules + 2
  orphans and CXO's word on error_consciousness:124 can land later as further shrink). Landing order: 2011-b, then 2010 (its two literals lower the
  frozen row in the 2010 landing), then the margin fix. Decisions.log lines + landing notes citing the controls. SEPARATE: `claude/lead-1943-clear-todos-resolver`
  6fd438bba0 lands ONLY with PM's clear_todos flip + my served probe.
- **(SUPERSEDED 20:55: promotion done; code lands 10-15 morning.) HOLD code pushes to main until PM promotes** (each push cancels the in-progress Tests run and moves what staging serves). Docs pushes are fine.
- **MVP milestone:** CLOSED today #1886, #1623, #1579, #1860. Open non-epic 7: #1965 + #1889 (wait on the broken-grant OAuth leg, PM's hand with PA),
  #1943 (held branch; see below), #1913 (Web needs a spare Anthropic key for web-agent; on xian's card via Exec), #1843 / #1783 / #1771 (fixed on
  main; CXO closes on served readings after the promotion).
- **Landed on main today:** #1943 first-N 156bec12c3; #1843 196feeb23d; #1771+#2007 271fccc508; #1783 39dcb603d1; #2008 82f83be6ff; data-model.md
  1df05f7945; CIO concept-link gate in lint.yml + ab-a-isolation concept 93978c4ddf; push-wrappers R9 c4f64da4e7; data/chromadb untracked 7a498b2aec.
- **HELD: `claude/lead-1943-clear-todos-resolver` (6fd438bba0)** = rework (1) (the #1605 net retired) + (c) (clear_todos in ACTION_REGISTRY, Verb.CLEAR,
  todo-domain shim cells, example) + CXO's sentence drop. Rule 7 PASS (×6 identical on 11 rows; full run 472/532; both named regressions read the same on
  main). Branch suites 5827/1 skipped + 151 on the (c) files; mypy at ceiling. **Lands ONLY with PM's `clear_todos` flip** (alpha live flag, his token):
  merge main into the branch, land in the same push with a landing note stating the coupling, then MY served probe on alpha: the three #1605 variants,
  Arch's legacy-path turn (a #846 offer pending, then `clear my reminders`), CXO's two quotes (not-live sentence in context; a plain `no` at the resolver),
  each with the turn before it. Worktree `lead-1943c` kept for it.
- **#2009 (nullable owner_id, 8 tables, three tiers):** step 1 is a prod DB read (seat-denied) → Arch's corrected SQL is on xian's card via Exec; I build
  the NOT NULL migration on the count (A: NOT NULL; B: backfill from parent then NOT NULL; C: feedback.user_id). Production unless the count moves it.
- **Standing watch reported to Arch 12:21:** `let's analyze the risk here` reads CLARIFY ×5 / analyze_blockers ×1 on main today.
- **Chores waiting for a post-promotion idle fire (they touch Tests' trigger paths):** Concept lines on the 8 product CI workflows (due 11-01).
- **Cron:** session 46638333 until the first `pm-lead-cycle` LaunchAgent fire lands → CronDelete + registry row. 12:17 fire not yet delivered at 12:21
  (cron fires only when idle; the session has been busy).
- Earlier today: history rewrite reset 08:45 (new main from d217d8f1ca), unfrozen 09:02; sync-pm-local resumed 09:5x; Option 3 verdict none (doc
  corrected: router before Stage 0).

## EARLIER — STATE @ 2026-10-14 11:16 PT — RUN-HOT (xian, until Thu 10-15 22:00): MVP pass in flight; 4 MVP closes today; 5 lanes; promotion NEEDED (N5)
- **Run-hot ruling (Exec 10:36):** drain fully, deeper checks, subagents freely; mail Exec if xian blocks; no model ask (Fable). PM: morning work, then the card.
- **MVP milestone today:** CLOSED #1886 (10-07 fix, 10-08 served), #1623 (member 2 = #1627), #1579 and #1860 (Web's served rows 1–2 on de7d0c1c57).
  Open non-epic: #1965, #1943, #1913, #1889, #1843, #1783, #1771 (7, was 11).
- **Landed on main:** #1943 delete "first N" 156bec12c3 (gate passthrough for positional targets; live probe PASS; card N5 waits on the next
  promotion); CIO's concept-link gate in lint.yml 93978c4ddf; ab-a-isolation concept (recipes §6); Option 3 doc corrected (router before Stage 0).
- **Pending in the cycle worktree (NOT pushed until the intent_service re-run reads green):** #1843 merge (196feeb23d, transparent "please" strip,
  Arch's shape; 8 existing pins re-pinned) + data-model.md refresh (1df05f7945, 46-table inventory). Then: push, comment #1843 (served check owed
  at the standup REFINING seam → Web round after promotion), land note for data-model (owner-scoping facts to read once, lane's 5 rule notes).
- **Lanes:** #1771 built to Arch's shape, HELD 759c331937 — CXO must pick the line ((a) "say 'resume'" or (b) make a fresh standup ask resume; memo
  sent); #1783 Sonnet lane running (Arch's three conditions, CXO yes); #1943 clear_todos piece 2 + rework (1) Opus lane running from the held
  resolver branch → then MY ×6 screen + full corpus run before the flip. Land 1783/1943c only after Arch's read.
- **Served checks owed:** Web row 3 JSON reads (/api/v1/radar degraded_sources etc.), row 5 #1913 blocked on a spare Anthropic key for web-agent
  (ask on Exec/xian's card), row 6 #1943 after promotion; PA asked for the OAuth broken-grant leg (#1965/#1889).
- **Promotion:** staging serves 0aefd70dca; its tested ancestor 93978c4ddf has Tests in progress → when SUCCESS, say "ready" (Step 0, card v32).
- **Cron:** session 46638333 until the first `pm-lead-cycle` LaunchAgent fire lands (Exec/Pard), then CronDelete + registry row.
- Earlier today: history rewrite reset 08:45 (new main from d217d8f1ca), unfrozen 09:02; push-wrappers R9 (push-main.sh canonical, four retired);
  Option 3 verdict none; sync-pm-local resumed 09:5x (xian's checkout a4915e6d2b+); data/chromadb untracked 7a498b2aec.

## EARLIER — STATE @ 2026-10-14 09:14 PT — history rewrite DONE (reset --keep to the new main 08:45); START drained; PM mid-card (row 5 next)
- **History rewrite (Exec's runbook `dev/active/exec-history-rewrite-runbook-2026-10-13.md`):** froze 22:43 10-13 (reply sent, counts 0/0), reset
  08:45 to 25d96342a1 (new main descends from `d217d8f1ca`), unfrozen 09:02. **Carried rules (24h at least):** never merge an old branch, `stash
  pop`, or check out an old sha; the pre-push guard holds 57 old shas; **do not run `scripts/sync-pm-local.sh` until xian says his checkout is
  reset**; no `scope-guard.yml` dispatch today; mail-send that gives up after 6 → re-run the same command. Held branches on origin were rewritten
  with main (181 refs equal), so `claude/lead-1982-pat-dual-write` lives on under a NEW sha: re-resolve by name, never by 4400ee3d9f.
- **sync-pm-local RESUMED 09:56** (Exec 09:53: xian told, his data/chromadb copied to ~/Development/backups/chromadb-from-pm-checkout-2026-10-14); his checkout fast-forwarded to a4915e6d2b on the new history. Run it at idle points as before.
- **Option 3 DONE 09:50 10-14: verdict none** (doc `docs/internal/architecture/current/option3-day-one-path-check-of-the-61-2026-10-14.md`,
  de5118ef4c; reply to PPM cc Exec/Arch 07b8c9522). Two Epic 0 notes in §4, nothing before MVP. Nothing owed on the tripwire.
- **Cron ROTATED 06:5x: 46638333** (`17 6,9,12,15,18,21`, expires ~10-21; next rotation Mon 10-19 START). Registry row updated (94eafbf565).
- **Alpha `de7d0c1c57` = pre-rewrite id;** served code equals `d217d8f1ca` on every served path (one operator-script line differs). Staging serves
  `d217d8f1ca`, Tests green → the next promotion passes the gate without waiting. No code landing since the rewrite tip. Card **v31** says so.
- **Wednesday trip-wire reading: literal ceiling 90 (35 lists)**, unchanged since my 10-13 13:45 FILE_REFERENCE deletion (a1a02d11f3); PPM/Arch/Exec
  were told 10-13 (done-lead-to-arch… memo). PPM's re-plan is PPM's; nothing owed by Lead unless asked.
- **Card v31** (`dev/active/pm-test-card.md`; mirror artifact ALxfaRpLn5wjBVUPjzLvbi). PM's remaining rows: 5 (#1992), 6 onward, fresh-account
  block 12–14, Spec's P2–P4; setup E (calendar) and P6 (prod counts) are his hand. Answer pastes before carried work; file failures as issues.
- **Open on my side:** #1987 OPEN for AC3 served (row 1); #2001 OPEN for CXO's served judgement; #1982 Registry publish HELD (xian), PAT dual-write
  branch behind PM's PAT-only run, #1983/#1995 behind it; #2005 paused (eval, PA). **Fri 10-16 PROD server key move (PM's hand).** CIO role-duties
  count re-run 10-27. Alpha log-stream behavioural re-read: attended-only, on Exec's ask.
- Main 12/12 green at START (post-rewrite deploy-staging on d217d8f1ca SUCCESS 08:24). Briefing "Now" alpha + engineering lines refreshed (94eafbf565).

## EARLIER — ## STATE @ 2026-10-13 21:49 PT — DAY CLOSED. Alpha serves `de7d0c1c57` (PM's 18:49 promotion); PM mid-card (row 5 next); main 12/12 green
- **At START 10-14: (1) ROTATE CRON e5491d18** (armed 10-10 17:29, expires ~10-17): CronList → CronDelete → CronCreate `17 6,9,12,15,18,21 * * *`
  → CronList exactly one; update the lead row in `dev/active/duty-cycle-registry.tsv`. **(2) Epic 0 Phase 3 trip-wire (PPM, Wed 10-14):**
  read the literal ceiling (120 at close; `TOTAL: 120 (36 lists)`), say whether anything moved. (3) Read alpha /health against origin/main
  and say on the card whether a promotion is needed (only if a code landing arrived overnight; every code landing of 10-13 is in de7d0c1c57).
  (4) Answer any card pastes PM left after 21:5x before carried work.
- **Card v30** (`dev/active/pm-test-card.md`; mirror https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi version 27 from `scratchpad/pm-test-card.html`,
  which dies with this session — rebuild from the card if a republish is needed). Step 0 DONE 18:49; N1–N3 CLOSED by CXO 19:15 (#2002/#2003/#2004);
  N4 (#2005 count) is PA's served check and judgement, paused by xian's ruling. PM's remaining rows: 5 (#1992), 6 onward, fresh-account block 12–14,
  Spec's P2–P4, setup E (calendar) and P6 (prod counts) are his hand. File any failure as an issue; CXO reads the `yes` path / bare-no-after-unarmed-offer
  if PM's paste lands them.
- **#1982:** steps 1–3 DONE (fallback off 7cc00113bc; count recorded 16:36 PM's hand total=2 rewritten=2). **Registry publish HELD by xian** (via Exec
  17:07). Held dual-write branch `claude/lead-1982-pat-dual-write` (4400ee3d9f) lands only after PM's PAT-only alpha test; #1983/#1995 behind it.
- **#2005:** fixed 6cab869fd3 (total/truncated/perPage), live on PA's MCP v14 (17:49). **Paused per xian** (eval, bare MCP vs plugin — PA's proposal
  `docs/internal/architecture/current/mcp/eval-2005-partial-list-bare-mcp-vs-plugin-2026-10-13.md`); not MVP critical path; nothing further from Lead.
- **Promote gate refined 6164ab3ceb** (nearest tested ancestor when only untested paths changed); first real pass 18:49 run 38497735645. Keep reading the
  gate line on later promotions; probe script was scratchpad-only (dies with the session; logic is in the workflow).
- **Open issues on my side:** #1987 OPEN for AC3 served (card row 1, both halves + gone row); #2001 OPEN for CXO's served judgement ("1 day overdue").
- **Link checker:** red 18:53 (GitHub 500 batch), SUCCESS 21:19 on its own; nothing owed to Docs.
- **Fri 10-16: PROD server key move (PM's hand).** CIO re-runs role-duties count 10-27. Alpha log-stream behavioural re-read: attended-only, on Exec's ask.
- **Sync-pm-local:** refused 19:0x (PM had local commits), fast-forwarded cleanly at close (21:51, to c4b804b390). Never force it; hard rule 1.
- Worktrees: only the cycle one (scratch control worktree removed at close). Untracked `dev/active/canonical-retest-serving-llm.json` is a 10-10 artefact, not mine.

## EARLIER — STATE @ 2026-10-13 07:05 PT — START fire drained: #1987 half 2 + #2001 landed (main 8f93cfe672); alpha still 6e48d9ebb2
- **#1987 half 2 LANDED 71e213b885 (07:3x):** `delete_todo_pick.py` — the which-todo ask lists candidates numbered + arms the pick
  (#846 store, kind `delete_todo_pick_question`); the pick arms the #1666 title-bound confirm by id. #2000 census row shrank out
  (Arch's condition). Issue OPEN for AC3 served (card row 1, both halves + gone row). Comment 6147374039.
- **#2001 FIXED 143f9a9a83 (07:2x):** `_overdue_age_label` ("1 day overdue"). OPEN — CXO judges served after the next promotion.
- **Web ran the 6e48d9ebb2 set 06:20–06:53 (all pass; CXO judged 07:05); my slip: no sha mail to Web after the 21:46 promotion** —
  reply sent 07:05. **Next promotion carries #1987 half 2 + #2001; PM's hand.** Card v23.
- **LOGS KEEP ONLY FINGERPRINTS — PM's ruling (Comms 09:3x) LANDED e9ef7f28c0 (10:03):** `PIPER_INVERSION_LOG_UTTERANCE` default
  flipped to off in ONE helper (`services/utils/utterance_log.py`); the three inversion readers + five other text-logging sites (pre-
  classifier INFO lines, 'Processing intent', cache prefixes, document/Notion search queries) route through it. No Fly secret needed
  (my seat can't set one anyway). Measured: alpha's recent 100 log lines = 49 warning + 51 HTTP access, 0 INFO → no message text
  emits today (quiet mode, root WARNING). Retention per Fly docs: Grafana log search 7 days; no drain in fly.toml. `fly logs --no-tail`
  IS allowed from my seat (counts only, never print). Behavioural re-read after the next promotion (standing items). Reply to Comms
  cc Exec sent 10:03.
- **#1987 condition 3 LANDED 49e90de36f (09:34):** the armed pick survives a pleasantry (thanks/greeting/farewell re-arm + ack +
  the question; '2' then binds) — Arch's 09:3x ask, pinned both ways (42 pins). CXO's 09:50 memo superseded 09:40 → acks back to plain 'You're welcome.' / 'Hi!' (a9f8cd16d1, 09:43); earlier: CXO ruled 09:40 → applied f1280c8ba2 (09:40): 'You're welcome — nothing has been deleted yet.' / 'Hello — …' + the list re-shown; FAREWELL RELEASES. Nothing owed.
- **MEETING ROW LANDED d13dafd172 (08:24; branch commits e40a69f50b + b9afba39ad):** Arch's 07:4x ruling (the rule-10 licence row
  'when am i in a meeting' must be stabilized, not excluded). Landing = the ADDITIVE registry example for meeting_time ('How much time do I
  spend in meetings today? / When am I in a meeting?'), description unchanged; licence row meeting_time ×6 @0.95 on main+edit AND three
  perturbed trees; full run 476/532 (day's best, TEMPORAL 63/66); no ×6-attributed regression. **ACCEPTED by Arch 08:31, no revert** (the member is a live
  ANALYSIS survivor so a 2/18 wobble changes no served answer; Fisher p≈0.49). His one watch: if a ×6 block on MAIN itself reads the
  member below 6/6, report it (standing items). Lesson recorded by Arch in decisions.log: an additive registry example is the
  least-perturbing lever; try it first for a single-row stabilization. Six wordings in the log table; w4's full run kept CANDIDATE-HELD. Reply to Arch cc PPM sent 08:24.
- **Red window #2 today: 17727f5b26 (the #1976 push) — one pin (`phase3-args/` source label), fixed 27346753dc; Tests watch open.**
  Discipline widened: corpus-row deposits run BOTH 1595 test files before landing.
- **CI: 8f93cfe672 GREEN (Tests 38410111184, AE 38410110441).** Watch open on 17727f5b26 (the #1976 push; Tests 38414116924) — read at the
  next fire if it has not resolved by then. Worktrees: none besides the cycle one.
- **#1976 LANDED 84a313394d (07:30):** handler consumes `inversion_args.text` (honesty guard), scorer `text` key, measured corpus row (3/3 on
  main's wording), census 596. **Description UNCHANGED** — two wordings screened under rule 7 and dropped (attributed ×6 regressions;
  the meeting row flips on 3 of 4 prior candidate trees — perturbation-sensitive, worth telling Arch). Report CANDIDATE-DROPPED;
  controls `dev/2026/10/13/controls/1976-*`. Served check on the card (5a). Nothing else carried from this fire.

## EARLIER — STATE @ 2026-10-12 22:31 PT — DAY CLOSED. Alpha promoted 21:46 (`6e48d9ebb2`); PM tests in the 10-13 morning off card v22
- **PROMOTION DONE 21:46 10-12 (run 38346886426):** PM dispatched + approved from his Mac with `gh` (no browser; the approve call needs
  `-F 'environment_ids[]=<id>'` — `-f` sends a string and 422s). Alpha /health = `6e48d9ebb2` = the 21:00 staging image; code identical
  to main's head 9ee7134e85 (verified: empty code diff; 1992/1987/1975/1996-1997 are ancestors). **Every "not live" row is now live.**
- **PM ran out of evening at 21:5x before testing; "pick it up in the a.m. with a fresh test card."** Card rewritten **v22** (remaining-only,
  89 lines): tonight's five (#1987 ×2, #1975, #1996/#1997, #1992) first, then #1985/#1986/#1988, A, D, item 4, the fresh-account block
  (G/F/P5), P2–P4; parked C/H; setup E; P6. **At START: read alpha /health against origin/main and say on the card whether a promotion is
  needed** (only if a code landing arrived overnight). Expect PM's results during the morning — answer them before carried work.
- **The 21:17 STOP fire arrived at 21:48 during PM's session** → heartbeat WORK then; STOP recorded at day close (22:31). Cron e5491d18
  present; rotation still Wed 10-14 START.
- **Side worktrees lead-1987 and lead-1992 REMOVED at close** (only `venv` untracked). No side worktrees remain.
- **Memory saved:** `reference_promote_alpha_via_gh_api_no_browser` (dispatch + approve recipe, the -F gotcha).

## EARLIER 10-12 STATE @ 19:13 PT — through the 18:17 fire: fifteen code landings on main today (log dev/2026/10/12/2026-10-12-0647-lead-code-log.md)
- **#1987 half 1 LANDED 5fd92b0019 (19:0x), issue OPEN:** "delete that reminder"/"delete it" after a save binds the just-created row
  (`conversation_context.last_created_todo`, the `last_numbered_list` idiom) into the #1666 title-bound confirm; 20 pins; corpus row;
  routing-stack paragraph. CXO ACCEPTED the gone-row copy (19:10). **Half 2 = NEXT START, named trigger:** the generic which-todo
  ask lists the few known candidates numbered (CXO's bar) and the numbered pick ARMS via the #846 store (Arch's condition on the
  census row) — the #1906 carrier shape, a distinct mechanism. Served checks on the card: D1 arm + gone-row line (CXO judges).
- **#1992 LANDED 1e2cb22576 + CLOSED (19:1x):** raw HTML in bot replies renders as visible text (marked `html` renderer override,
  DOMPurify backstop); `frontend-tests.yml` filter gains `web/assets/**`; 1732 img-onerror pin strengthened. **Frontend Tests
  38335667554 GREEN.** Harness: `tests/frontend/` (own package.json, jsdom) — never `npx jest` from the root. Served check on the card.
- **#1976 SIZED (19:13), not tonight:** the router's args are prompt-described (no schema) and the create_todo entry names no text
  arg → a router-prompt change + handler consume of `inversion_args.text` + a MEASURED corpus row → rule 7 full run before landing.
  Take at a START with #1987 half 2 (same family, #1943).
- ~~Test card v20 (19:1x): not-live list = #1975, #1996, #1997, #1987, #1992.~~ Superseded: promoted 21:46, card v22.
- ~~Side worktrees in place~~ (all removed at close): lead-1987, lead-1992 (a gitignored root `node_modules` sits there — my `npm ci` at the wrong level; the
  `rm -rf` was guard-blocked, leave it), lead-1993, lead-1975, lead-1985b, lead-2000 — all merged; remove at STOP or tomorrow.
- **DISCIPLINE (10-12 19:4x, after a red main; widened 10-13 07:5x after a second): every corpus-row deposit runs `tests/unit/test_inversion_phase3_deletion_1595.py` AND `tests/unit/test_inversion_phase1_shadow_score_1595.py` before landing — the census denominator pin lives in the first, the args-row labelling pin (`source` must start with `phase3-args/`) in the second; both sit outside the intent_service/enforcement dirs.** Tests on a8b27f3fbd went red on exactly that pin (fixed same fire; read the fix's Tests run first at the next fire).
- **#1984 half (2): CLOSED ON MY SIDE 07:2x — lever (c) applied.** Arch ruled (07:3x his clock, read 07:16): not (a); (b) = drop the
  `'what did I work on today'` rail example, screened ×6 main vs (b) on 20 phrases (CXO's two true-session phrases joined) → the row
  reached the ruled plan 6/6 but two rows read worse (re-checked 12/12 each) → FAIL → (c): the corpus row carries the KNOWN MISS note
  (main, pre-push smoke 568); expected stays the ruled ops (MISMATCH on purpose). Memo + issue comment 6126198825. **Nothing owed by me;
  CXO retitles #1984 (proposed title in the memo). No more wordings on this neighbourhood (Arch).** Held branch
  `claude/lead-1984-status-description` (40b3c95b33) is dead — leave it on origin, do not merge; the report is filed CANDIDATE-HELD.
  Observation on file: "let's analyze the risk here" tips to CLARIFY 6/6 under any catalog edit (ANALYSIS survivor at the margin) —
  the next catalog candidate carries it; a ledger line when the ANALYSIS lane opens.
- **CI watch:** my 07:2x corpus push (tests/fixtures) triggers test.yml — read the Full Test Suite result at the next fire; a corpus-note
  edit cannot change a test's outcome, so a red there is someone else's head.
- **Ceiling 120 / routing tail 90 (29 the #1974 floor)** — re-read 120 this morning, main unchanged for PPM's row (said in the memo).
  **Wed 10-14 tripwire reads 120.** Main 12/12 workflows green at START (d296221de5); my pushes today are docs-only.
- **Deletion procedure:** the test-tree sweep step is in the routing-stack doc (after the pattern→corpus conversion step) + a post-landing
  paragraph on the thirtieth deletion. Any lane brief copies it: `git grep -F` every claimed phrase across tests/unit, integration, e2e;
  run `tests/integration -m 'not llm'` on the lane before landing. Known miss to carry to the COMPLETION_HISTORY ledger when that lane next
  opens: "show me when we shipped the API" → shipped_this_week 6/6 on main.
- **PR #1952 MERGED 8c3c56c0d6 (17:2x):** Pard's health-gate stale-read fix replaces my interim 48h guard; stale → unmeasured + warning. **Gate's first live run READ 18:5x (fly-deploy 38331164368 on 5bff4e1b45: 'last concluded Tests on main: success (8c3c56c0d6…, created 00:23Z)', fresh, green; Arch read the same run); Pard told cc Arch (mediajunkie 154fa5e, trailers on). Nothing owed; keep reading the line on later deploys.** (was: read the gate's log on the next app-path staging deploy** (the 'last concluded Tests on main: … created …' line) and tell Pard cc Arch it read fresh.
- **#1996 + #1997 LANDED 3469ac2633 + CLOSED 10-12 17:0x** (calendar-day overdue ages at local midnight; dedup-emptied list never 'none'; reminder ages in the floor prompt). **Owed after the next promotion (Web's set, named in my 17:0x reply):** turns 8/11a/11b/12 + a later-today reminder past its time + #1975's delete-by-title. Turn-2 CLOSED (CXO + Arch: keep as built). Turn 9: arms nothing, condition 3 met (Arch concurs). **#2000 LANDED 166d876f4f + CLOSED** (census predicate widened, 9 rows measured, 4 marked). **#1987 (Arch's condition on the row): a numbered delete pick must arm via the #846 store — #1943's family, with Arch.** #1998/#1999 closed as dups of #1997/#1996; CXO's bars quoted on mine. 42f8fe6933 ('due earlier today') landed 729647c019.
- **#1975 LANDED e6b4fdf413 + CLOSED 10-12 16:3x** (gate-confirmed delete honours its bound row); owed: served re-check on alpha after the next promotion (create upcoming reminder → delete by title → yes → gone). **#1983:** copy RULED by CXO 16:4x (two branches, Read first; parenthesis cut per my 17:0x confirm check — close/reopen ask, create/comment proceed on an imperative). **HELD until PA relays PM's PAT-only step-4 result**; then land the template change (hint + placeholder + JS fallback placeholder at ~:577) and ask CXO to read the served Settings page. **#1995 (CXO, permission gap reads as empty — honesty):** queued behind #1983's landing; needs a served repro with a token lacking Pull requests: Read on PA's PAT-only account. **#1993 LANDED fa8b9efe1a + CLOSED.**
- **#1982:** held branch `claude/lead-1982-pat-dual-write` (4400ee3d9f, still on origin) — land when PA relays PM's PAT-only alpha test is
  done. **Step 3 DONE 10-13 16:5x (7cc00113bc): fallback flipped False on PM's `legacy=0` (16:36 PT); `--snapshot` now refuses placeholders.**
- **#1459 LANDED a488e4fa65 + CLOSED 10-12 13:12** (Arch GO 13:1x with three amendments, all applied): `Intent.bind_original_message` one
  writer; `__post_init__` normalizes to the attribute + logs; classifier fill deleted with proof; `TestOriginalMessageWriteRatchet1459`
  (four shapes, AST, ceiling 0, denominator asserted). **Addendum 264d3e9549 (Arch's one gap: bare `{}` exempt only under its own
  is-None guard; count stays 0).** **CI GREEN on 264d3e9549: Full Test Suite 38303060151 + Architecture Enforcement 38303060147 (and 38302535677 on a488e4fa65).** Lane worktrees
  removed; branch `claude/lead-1459-setter-ratchet` stays on origin (remote delete is permission-denied, don't retry).
- **#1977 CLOSED 10-12 12:53** (banner + evidence comment + close; the work had been complete since 10-11 19:3x).
- **read_floor_3 wave** (get_project_status + get_top_priority adapters; Arch's four 10-11 20:5x conditions): trigger = the deletion lane's
  next STATUS/PRIORITY pass. Not #1984's lever.
- **ALPHA PROMOTION run 38312410442 LANDED 15:47 10-12 (xian approved in conversation); alpha = 651756d520, code = 264d3e9549. Web has the 12-turn re-run set (memo 15:5x, cc CXO; Exec fyi via mail4); test card v17 adds row G (PAT-only account) — xian testing this afternoon.** Was: staging 3bbbfc7c40 (= 264d3e9549 in code; all seven
  landings + #1978; staging had moved to 651756d520 by 15:45, still code-identical — the job promotes the image at run time). When it lands: read /health, hand Web the re-run set (thank you! ×3, thanks, thank you so much, goodbye, thanks after a
  delivered turn, one compound, one armed-slot thanks, thanks after delivery + 31-min idle, show today's tasks ×2); CXO closes #1985/#1986
  on the quotes; PPM reads #1985's re-run. Dispatch recipe: `gh workflow run fly-deploy.yml --ref main -f promote_to_alpha=true` after
  staging settles. **Scoring key = lead-scoring since 10-10 17:41 (console-confirmed); the 10-16 item is the prod server key only.**
- **Wed 10-14 START: cron rotation** (e5491d18, armed 10-10 17:29, expires ~10-17; delete-then-create; update the registry row) + PPM's
  tripwire read. **Fri 10-16:** key switch — `dev/active/lead-prod-key-move-2026-10-16.md` (PM's hand) + one confirm call.
- **Mail v4 pilot — LIVE 10-12 10:1x (roles.yaml 3a79812; delivery test acked 08d2dc8d83):** every mail check reads both inboxes;
  mail TO exec/cio/lead goes via `scripts/mail4.py send --to … --type … --subject … --body-file …`; everyone else stays on
  `mail-send.sh`; `check --canary` once at START; double zero = both inboxes empty.
- **Alpha c613beabf5 served (Web 08:10): 5 of 8 pass — all three fails resolved on main by 09:1x.** #1985 (attention handler read
  todos by session id → "nothing urgent" over an overdue todo): principal fix 5d5f7ec88e + CXO's reply shape bb4066fc00 (due today
  then overdue under "Today:", exact empty line, "couldn't check" on a failed read, assembler dedupe). #1986 (thanks → todo
  briefing): Arch's #1754 reversal for thanks/farewell, 8ebe568035 under six conditions + condition 2 tightened cd43832626 (the
  empty form needs a durable, owner-checked zero from `count_delivered_turns`; unknown → "You're welcome.") + Arch's belt
  d23849fb9f (the in-memory window must agree too; residue named). Arch accepted; CXO closes #1985/#1986 on Web's quotes. #1988 (timezone placeholder) CLOSED on
  the Helsinki copy (dacf3007a3); render half = Web's #1992. #1987 (delete that reminder) filed, PPM places. #1958 CLOSED by CXO.
  CXO's duplicates #1989/#1990/#1991 closed into mine. **Open with Arch (no block):** greeting is NOT armed-checked (pinned as-is;
  his call to widen); the compound ACTION_EXAMPLES for thanks/farewell ride the next catalog batch (rule 7). **Next promotion →
  Web re-runs:** thank you! ×3, thanks, thank you so much, goodbye, a thanks after a delivered turn, one compound, one armed-slot
  thanks, a thanks after a delivered turn + a 31-minute idle (CXO), show today's tasks ×2; CXO closes #1985/#1986 on the quotes. **CI: Full Test Suite GREEN on 97e475dbb0 (run 38279264201), the first completed run carrying all five landings.**
- **Test-order coupling noted, not fixed:** \`test_action_registry.py\` fails 47 rows when run after \`test_spend_free_canonical_ratchet_1818.py\`
  in one session (alone: passes; alphabetical CI order hides it). Whoever next touches either file.
- **Stamp rule (today's third slip):** the frontmatter/log time is substituted from `date` at write time (`NOW=$(TZ=… date)`), never
  typed into a draft.

- Spend today: 853 Haiku router calls (Krink's credit, expires 10-15) + 6 chat turns on a local server. Keychain readable; the test user's
  key still bound. Untracked scratch `dev/active/canonical-retest-serving-llm.json` (pre-existing, not mine).
- Discipline notes carried from 10-11: no `git push` chained behind a pipeline whose exit code is `head`'s; `git status` before every push;
  write the log line after an edit script returns; `date` before every stamp; filenames under 180 chars. New today: `git mv -k` on an
  untracked file is a silent no-op that still exits 0 — use plain `mv`.

### (10-11 state, kept for context) — STATE @ 2026-10-11 21:48 PT — DAY-CLOSED (log dev/2026/10/11/2026-10-11-0647-lead-code-log.md)
- **Ceiling 120 / routing tail 90 (29 the #1974 ruled floor).** Day: 127 → 120 (COMPLETION_HISTORY 3, STATUS 2 + PRIORITY 1, PORTFOLIO 1 —
  deletions 27–30 recorded in the routing-stack doc). **PPM's Wed 10-14 tripwire reads 120.** Main GREEN on af776b9614 (Full Test Suite
  success; a red window 20:23–20:5x from an integration pin my PORTFOLIO landing's unit tier could not see — converted).
- **Mon 10-12 START (named triggers, in order):** (1) **#1984 half (2)** — the `get_project_status` description candidate HELD on
  `claude/lead-1984-status-description` (40b3c95b33; screen 5/5 ×4 phrases incl. PLAN[get_project_status→list_archived_projects]):
  full corpus run vs main's newest report (every row diff), served check (cold two-topic, cold single, armed, + the upload negative
  "summarize the document I uploaded"), #1984 row N=5, land on no attributed regression (Arch GO 21:0x). CXO closes #1984 after.
  (2) Confirm main unchanged for PPM's re-measure row — else re-measure (ceiling now 120).
- **#1979 CLOSED** (rail guard 0efe6f4c99: conversation/text-sourced summarizes hand back to the floor; served 4/4; upload negative 3/3).
  **#1984 half (1) DONE** (three landings: label fallback never prints an action id + catalog-wide pin; CXO's copy + the dropped
  "On the {topic} front" template; `_lowercase_first` keeps proper nouns — CXO's five exceptions). CXO accepted on quotes.
- **#1982:** built 10-11 (079477fb15, MCP gets ONE scoped subkey). Held branch `claude/lead-1982-pat-dual-write` (4400ee3d9f): land
  when PA relays PM's PAT-only alpha test is done (merge into cycle, push main, issue comment, decisions.log). **Steps 1–3 DONE 10-13:**
  PM set the subkey + re-encrypted (16:36 PT, total=2 rewritten=2 legacy=0); I flipped `GITHUB_LEGACY_CONTEXT_FALLBACK` False at
  7cc00113bc with the count on the issue + decisions.log + runbook, and made `--apply --snapshot` refuse non-`vs_` values (the apply had
  taken the literal `<snapshot-id>`). Remaining: PA's live check (Exec asked), Registry publish, the held branch on its own trigger.
- **#2005 (PA, 17:05): MCP github-issues resource presented a 30-item page as the full set.** FIXED on main 6cab869fd3 (17:5x): payload
  carries `total` + `truncated`, description says report total never count, adapter passes `perPage=limit`. Live needs PA's MCP redeploy
  (memo to PA cc Exec); served check = card v27 row N4; PA holds Registry publish until then. Close after PA's served read.
- **read_floor_3 wave** (get_project_status + get_top_priority adapters; real scoring replaces the lenient FLOOR rule; Arch's four 20:5x
  conditions): trigger = the deletion lane's next STATUS/PRIORITY pass, not #1984. The routing-stack doc now says the grammar has two
  sources (rail + registry FLOOR/CANONICAL ops) — an adapter changes dispatch/scoring, not nameability.
- **Wed 10-14 START: cron rotation** (e5491d18, armed 10-10 17:29, expires ~10-17; delete-then-create; update the registry row) + PPM's
  tripwire read (120). **Fri 10-16:** key switch — `dev/active/lead-prod-key-move-2026-10-16.md` (PM's hand) + one confirm call.
- **Mint grant** on no seat since the 10-09 restart; Exec has the re-add on xian's card. Lead mints nothing.
- **Watch:** Web's served checks on alpha; #1958 + CXO's team-calendar probe after the NEXT promotion; the #1984 alpha confirmation (CXO).
- **Discipline notes (10-11 evening, mine):** never chain `git push` behind a pipeline whose exit code is `head`'s — read the test's
  own summary line (two slips tonight); `git status` before every push, not after (one landing shipped without its code files);
  a python edit script that asserts after a partial write leaves nothing, but a log line written before it runs lies — write the log
  after the edit returns. `date` before every stamp. Filenames under 180 chars (mail-send refuses).
- Spend today: ~745 Haiku router calls + tonight's ~55 (Krink's credit, expires 10-15); ~60 chat turns on local servers; Sonnet via the
  dev key for the surface-2 probes. Keychain readable. Untracked scratch in the worktree: `dev/active/canonical-retest-serving-llm.json`
  (pre-existing, not mine; left alone).

### (10-11 morning state, kept for context) — STATE @ 07:2x PT, START fire drained (log dev/2026/10/11/2026-10-11-0647-lead-code-log.md, open)
- **Re-measure done Sun 10-11: ceiling 127 / tail 97** (memo 3e71c8297 to PPM cc Arch, with the sizing: 20 rule-10 literals move on ~35 served
  calls; 28 need tokens; 33 need router/catalog work; 5 census-GO are rulings; 1 rule 11; 10 are the pleasantry stripper → NOT_ROUTING proposal).
  **Mon 10-12: confirm main unchanged, else re-measure.**
- **Landed:** `--all` census table now prints the per-list verdict (partial GO / r10 / r11), pinned. New kept instruments:
  `scripts/inversion_router_control.py` (router ×N) and `scripts/inversion_report_diff.py` (per-row report diff).
- **Held, awaiting rulings:** (1) PORTFOLIO partial (2 literals): `update … project` is a ruled survivor (#1933 a); show/list/view literal needs
  5 corpus rows for pin phrasings (listed in the log) — Arch asked for a per-literal ruled-survivor mark in the gate + a word on depositing the
  rows. (2) "show today's tasks": candidate A NO-GO on the full run (5 attributed regressions incl. a WRITE landing); no fourth wording; PPM/CXO
  re-judge asked (Lead leans REVIEW). (3) #1951: two PPM verdicts asked (link-my-repository; key-tasks-for-this-sprint). (4) RESOLVED 10-11: the evaluator split was the mis-serve proof (Arch); `status report` is a survivor (surface 2 → SYNTHESIS 5/5). (5) RULED: filler stays; tail 97.
- **Rulings 10-11 (Arch/CXO):** restore rule (a restored literal must claim the ruled op, else known miss — pin it); STATUS 2 + PRIORITY 1 licensed under misserved_at_deletion (CXO withdrew `where.*focus`); pleasantry family RULED KEEP (CXO, #1974) → HELD_FOR_CAUSE "ruled keep, permanent floor" + close #1974 in the gate commit; both gate asks approved. **DONE 10-11:** COMPLETION_HISTORY 3 (124), gate commit (ruled_survivors, restore pin, PERMANENT_FLOOR ×4 on #1974 closed, --list hint), STATUS 2 + PRIORITY 1 (**121**, main 6bb22031a6; CI green at c38404ff9f for the earlier three). **#1977 step 1 LANDED (0ba7b951e5)**: surface 1 declines a claim set that leaves an ask-shaped unclaimed clause (leading clause included; PM's #1856 aside stays claimed). PORTFOLIO show/list/view reads "planned, fallback unacknowledged" → **needs step 2** (CXO's acknowledgement copy on #1977; reply assembly; served check bar); prepared deletion on `claude/lead-spp-portfolio-wip`. Step 2: covered-branch only (ruled; landing with the flag False). The preregistered 20-probe licence measured HOLD (0 silent partials, 6 neither, all one phrasing) → PORTFOLIO's literal stays, **main reads 121**; the prepared deletion is held on origin `claude/lead-portfolio-last-literal`. **Arch accepted the HOLD; trigger = #1979's fix → re-run the same 20.** #1978 fixed + closed. **#1979 LANDED 10-11 19:1x (merge 39398a32af of 0efe6f4c99; Arch nodded A, ruled NO to B; CXO's acceptance = the posted quotes; CXO closes):** the fix is the `summarize_document` rail guard (conversation/text sources → floor), not the router or the prompt; served 4/4 no upload prompt (`controls/served-1979-2026-10-11.md`). The preregistered 20 re-run on the fix-branch server: 0 silent partials, 0 neither, 20 both (`controls/probes20-1979-fix-branch-2026-10-11.txt`). **Arch 19:2x: the branch run COUNTS.** #1979 CLOSED by CXO; **#1984** (UX, CXO) = the cold two-topic reply (router plan reads 'my work' as session activity; 'list archived projects' leaks into prose) — mine to place with Arch. **PORTFOLIO LANDED 10-11 19:34 (merge 8531742988): ceiling 120 / tail 90 / survivors-only; full unit 12916/0; CI on 39398a32af green before landing. Wed 10-14 reads 120** (PPM told). **#1984:** half (1) LANDED 10-11 19:4x (66159f1ecc) + CXO's copy and the dropped 'On the {topic} front' template LANDED 19:5x (9ded3d32f5; served 'Regarding your archived projects, …' and 'As for your calendar, …' on a 3-part plan). `_lowercase_first` proper-noun rule (CXO's five exceptions) LANDED 20:0x (51db50efd0). **Half (2) CORRECTED 20:1x:** get_project_status is already in the router grammar (registry source); the fix is the `ACTION_DESCRIPTIONS` edit, candidate HELD on `claude/lead-1984-status-description` (40b3c95b33; screen 5/5 on all four phrases incl. PLAN[get_project_status→list_archived_projects]). **Tomorrow's START:** full corpus run vs main's newest report (per-row diff), served check (cold two-topic + single + armed), #1984 row N=5, land if no attributed regression; also fixes the cold served first sentence. **Arch 21:0x: correction accepted (his too); GO on the description-edit path under the standing rules, trigger 10-12 START:** (1) full corpus run vs main's newest report, every row diff read; (2) served check — cold two-topic, cold single-topic, one armed turn, PLUS the upload negative 'summarize the document I uploaded' (the new text names the document case; the router must not learn to pull it); (3) #1984 row N=5; (4) land if no attributed regression. The read_floor_3 wave is NOT opened for #1984 — trigger: when the deletion lane next takes up STATUS_PATTERNS or PRIORITY_PATTERNS, carrying Arch's four 20:5x conditions as written. CXO keeps #1984 open until half (2) reads right. Half (2) = router reading ('my work' → session_activity_query in a cold plan): corpus row re-expected to get_project_status → list_archived_projects, N=5 reads 0/5; the fix is a `get_project_status` rail adapter or a description edit → full-run lane (next lane for Arch's nod). **CI on 66159f1ecc: watch; the 8531742988 suite was cancelled by later pushes.** Tail: 94 − 3 = 91, of which 29 are the ruled permanent floor.
- **Finding to remember:** the attention/todo/priority description neighbourhood is fragile on the served Haiku router — edits on either side
  move "when am i in a meeting", the sprint-priorities row and a todo/reminder row. Screens pass, full runs fail. Don't retry by wording.
- Spend today: 745 Haiku router calls (Krink's credit, expires 10-15). Keychain readable (no -25308).
- Watch: Web's quoted served checks on alpha 4bd1a236e9 (6 turns); #1958 + CXO's team-calendar probe after the NEXT promotion.
- **Wed 10-14 START: cron rotation** (e5491d18 expires ~10-17; delete-then-create; registry row) + PPM's tripwire read (127 ceiling, tail 97
  or 87 if the stripper is named). **Fri 10-16:** key switch — steps in `dev/active/lead-prod-key-move-2026-10-16.md` (PM's hand).
