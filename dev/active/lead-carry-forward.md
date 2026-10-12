# Lead carry-forward — Fable 5.1 seat; Model A worktree ~/Development/piper-morgan-worktrees/lead

## STATE @ 2026-10-12 09:4x PT — START + seven mail wakes drained; five code landings on main (log dev/2026/10/12/2026-10-12-0647-lead-code-log.md, open)
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
- **#1982:** held branch `claude/lead-1982-pat-dual-write` (4400ee3d9f, still on origin) — land when PA relays PM's PAT-only alpha test is
  done; flip `GITHUB_LEGACY_CONTEXT_FALLBACK` to False in the commit that records `legacy=0`.
- **#1459 LANDED a488e4fa65 + CLOSED 10-12 13:12** (Arch GO 13:1x with three amendments, all applied): `Intent.bind_original_message` one
  writer; `__post_init__` normalizes to the attribute + logs; classifier fill deleted with proof; `TestOriginalMessageWriteRatchet1459`
  (four shapes, AST, ceiling 0, denominator asserted). **Addendum 264d3e9549 (Arch's one gap: bare `{}` exempt only under its own
  is-None guard; count stays 0).** **CI GREEN on 264d3e9549: Full Test Suite 38303060151 + Architecture Enforcement 38303060147 (and 38302535677 on a488e4fa65).** Lane worktrees
  removed; branch `claude/lead-1459-setter-ratchet` stays on origin (remote delete is permission-denied, don't retry).
- **#1977 CLOSED 10-12 12:53** (banner + evidence comment + close; the work had been complete since 10-11 19:3x).
- **read_floor_3 wave** (get_project_status + get_top_priority adapters; Arch's four 10-11 20:5x conditions): trigger = the deletion lane's
  next STATUS/PRIORITY pass. Not #1984's lever.
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
  when PA relays PM's PAT-only alpha test is done (merge into cycle, push main, issue comment, decisions.log). Waiting on PM's pipe +
  snapshot + re-encrypt per the runbook; **mine when the report reads `legacy=0`: flip `GITHUB_LEGACY_CONTEXT_FALLBACK` to False in the
  commit that records it.** PM's account is OAuth (PA), so the MCP live check does not wait on the held branch.
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
