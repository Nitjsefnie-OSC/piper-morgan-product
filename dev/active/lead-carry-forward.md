# Lead carry-forward — Fable 5.1 seat; Model A worktree ~/Development/piper-morgan-worktrees/lead

## STATE @ 2026-10-11 07:2x PT — START fire drained (log dev/2026/10/11/2026-10-11-0647-lead-code-log.md, open)
- **Re-measure done Sun 10-11: ceiling 127 / tail 97** (memo 3e71c8297 to PPM cc Arch, with the sizing: 20 rule-10 literals move on ~35 served
  calls; 28 need tokens; 33 need router/catalog work; 5 census-GO are rulings; 1 rule 11; 10 are the pleasantry stripper → NOT_ROUTING proposal).
  **Mon 10-12: confirm main unchanged, else re-measure.**
- **Landed:** `--all` census table now prints the per-list verdict (partial GO / r10 / r11), pinned. New kept instruments:
  `scripts/inversion_router_control.py` (router ×N) and `scripts/inversion_report_diff.py` (per-row report diff).
- **Held, awaiting rulings:** (1) PORTFOLIO partial (2 literals): `update … project` is a ruled survivor (#1933 a); show/list/view literal needs
  5 corpus rows for pin phrasings (listed in the log) — Arch asked for a per-literal ruled-survivor mark in the gate + a word on depositing the
  rows. (2) "show today's tasks": candidate A NO-GO on the full run (5 attributed regressions incl. a WRITE landing); no fourth wording; PPM/CXO
  re-judge asked (Lead leans REVIEW). (3) #1951: two PPM verdicts asked (link-my-repository; key-tasks-for-this-sprint). (4) Floor-action
  liveness disagreement (census vs non-regression) + `\bstatus report\b` re-delete: Arch. (5) `_PLEASANTRY_FILLER_PATTERNS` NOT_ROUTING: Arch.
- **Finding to remember:** the attention/todo/priority description neighbourhood is fragile on the served Haiku router — edits on either side
  move "when am i in a meeting", the sprint-priorities row and a todo/reminder row. Screens pass, full runs fail. Don't retry by wording.
- Spend today: 745 Haiku router calls (Krink's credit, expires 10-15). Keychain readable (no -25308).
- Watch: Web's quoted served checks on alpha 4bd1a236e9 (6 turns); #1958 + CXO's team-calendar probe after the NEXT promotion.
- **Wed 10-14 START: cron rotation** (e5491d18 expires ~10-17; delete-then-create; registry row) + PPM's tripwire read (127 ceiling, tail 97
  or 87 if the stripper is named). **Fri 10-16:** key switch — steps in `dev/active/lead-prod-key-move-2026-10-16.md` (PM's hand).

### (10-10 state, kept for context)
#### ## STATE @ 2026-10-10 21:5x PT — DAY-CLOSED (log dev/2026/10/10/2026-10-10-0513-lead-code-log.md)
- **Alpha = `4bd1a236e9`** (promoted 10-09 18:34 via `promote_to_alpha`). 13 tokens live incl. complete_todo; clear_todos OFF. **Served checks:
  Web runs them** (xian's (b), 10-10 13:06; list sent 13:1x). Web needs xian to type the credential read in Web's own session. **Watch for
  Web's quoted replies** (6 turns) → judge borderline rows; CXO closes #1889/#1963 on quoted output.
- **Phase 3 (#1595): ceiling 127** on main (121 + 6 restores, merge 1110c6a03a, CI Tests green 02:12Z 10-11). PPM recounted 127 (d29bfef2ce).
  Routing tail last measured 91 (10-09). **Mon 10-12: re-measure ceiling + tail for PPM AND say which remaining deletions need a fresh served
  row vs which don't** (sizes the API exposure). **Wed 10-14: PPM's tripwire** (ceiling in band 110–120 read with tail beside). Rules in force:
  10 (CI full tier; llm mark = retirement citing its row), 11 (whole licensed set), #1973 threshold in every arm, **freshness rule** (newest
  full run is primary evidence; N=5 reports outrank it for their rows), refined rule 7 (full run only for the landing candidate).
- **Open with Arch:** the gate's two evaluators disagree on liveness for FLOOR actions (census `--list` says STATUS "GO (partial)" / PRIORITY
  "GO (deletable)" for the just-restored literals; `check_deleted_entry_non_regression` refuses them). **Census GO on those lists is NOT a
  licence until Arch picks one liveness source.** Then: `\bstatus report\b` re-delete under rule 10. "where should my focus be today" stays
  attention_query permanently (CXO family ruling). "I need a progress report" stays generate_report (CXO withdrew the re-point 19:21).
- **Catalog descriptions:** week_calendar clause landed (own-calendar-only + no conflict/yes-no questions). The todo-query description edit
  regressed in every wording and was dropped. Still candidates (each its own rule-7 run): "show priorities for this sprint" → get_top_priority;
  "pull up my schedule" → week_calendar; "show today's tasks" → list_todos_query. Held branches on origin (superseded/merged, delete was
  permission-denied — don't retry): `claude/lead-catalog-description-batch-held`, `…-held-v2`, `claude/lead-1970-framing-prompt-held`.
- **#1970:** router framing DEFERRED (Arch option c). Plumbing (flag `framing_hint` off), inert scorer framing column, `TestExecuteVocabRatchet`
  (39) on main. Retry trigger on the issue; compose corpus rows = 0 (needed before any retry). **When framing_hint is first enabled, label it
  NON-ROUTING everywhere the live set is counted** (gate `--live`, CURRENT_LIVE_CATEGORIES, Exec's flag reads, Arch's promotion condition).
- **API:** both Anthropic limits $250 (16:31). `lead-scoring` workspace ($50, pipermorgan.ai org) key stored by xian 17:2x via KeychainService
  (shared Amber slot); confirm call served 17:41; workspace attribution = xian's console check. **Themis: switch keys Fri 10-16** (current key
  spends Krink's credit, expires 10-15). Have the prod server-key move steps ready for 10-16 (PM's hand; recommend a separate prod workspace);
  one confirm call after xian switches. OpenAI: no credits; don't count OpenAI legs until xian says topped up. Keychain -25308 = locked
  (tmux over ssh); if it returns, tell Pard and hold LLM work.
- **#1958** fixed on main; served check after the NEXT promotion (also CXO's "show the team calendar" floor probe).
- **Cron:** `e5491d18`, armed 10-10 17:29 PT after the 15:00 reboot killed dad96d7a; expires ~10-17. **Rotate at Wed 10-14 START** anyway
  (delete-then-create; update the registry row). Use `GODEBUG=netdns=go gh …` (api.github.com DNS hang since the reboot, Pard).
- **Seat limits (do not work around):** fly deploy / fly secrets / prod DB reads / .env* / the mint script / `~/.piper-shared/*credentials*`.
  Deny lines in bypass: fly secrets set/unset, fly tokens create, `git push origin +ref`.
- **Discipline notes (mine, 10-09/10-10):** `date` before every time; read the function not its comment; the newest full run can expose rows
  older reports masked (first-entry-wins) → freshness rule; per-row evidence, never bulk swaps; stage non-mail first, unstage mail separately.
- Untracked scratch in the worktree: `dev/active/canonical-retest-serving-llm.json` (pre-existing, not mine; left alone).
