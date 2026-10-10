# Lead carry-forward — Opus 5.5 seat; Model A worktree ~/Development/piper-morgan-worktrees/lead

## STATE @ 2026-10-10 14:0x PT — PRE-REBOOT (Amber reboots ~15:00, Pard). Log: dev/2026/10/10/2026-10-10-0513-lead-code-log.md (NOT closed; resume it)
- **Alpha = `4bd1a236e9`** (xian promoted 10-09 18:34). **Served checks: Web runs them** (xian chose (b) 13:06). Lead sent Web the
  6-turn list with expected replies (13:1x). Web still needs xian to type the credential read in Web's session. Watch for Web's quoted results.
- **API:** this seat's Anthropic key is in the "Piper Morgan" workspace, which hit its WORKSPACE limit (still failing at 13:10 after xian's raise:
  req_011CfuAVg49RET67axqvhxgD). OpenAI: no credits (xian topping up; don't count OpenAI legs until he says done). **Fix in motion:**
  xian creates workspace `lead-scoring` in the pipermorgan.ai org (cap $50, Themis), key inside it, stored via the command in my 13:4x memo
  to Janus (getpass → KeychainService().store_api_key("anthropic", …)). The SHARED Amber slot is fine (Themis). **When he says it's stored:
  ONE confirm call, then report.** Prod alpha holds its own ANTHROPIC_API_KEY. Whether it's in the capped workspace is on xian's console card (user-facing).
- **#1970:** router framing DEFERRED (Arch option c). On main: plumbing (flag `framing_hint` off), the inert scorer framing column, and
  `TestExecuteVocabRatchet` (39, justified bumps). The prompt is held on `claude/lead-1970-framing-prompt-held`. The retry trigger is on the issue.
- **Catalog-description batch HELD** on `claude/lead-catalog-description-batch-held`: its full run is invalid (188 ERROR), and its scored rows
  regressed (get_top_priority rows → attention_query; "when am i in a meeting" → CLARIFY). Once the API is back: fix those, screen on the moved rows
  + sentinels (Arch's refined rule 7), and do a full run only for the landing candidate.
- **#1958** fixed on main (label echoes "on"/"next"); open until a served check after the NEXT promotion.
- **Mon 10-12:** Phase 3 re-measure for PPM (121/91 last) AND which remaining deletions need a fresh served row. **Wed 10-14:** PPM's
  tripwire, plus my cron rotation at START (`dad96d7a` expires ~10-15 21:4x; delete-then-create; update the registry row).
- **FIRST THING AFTER THE REBOOT:** `CronList`. The session-scoped cron `dad96d7a` may not survive. If zero → CronCreate `17 6,9,12,15,18,21 * * *`
  (Gap-C self-heal), update the registry row with the new id + arm date, and mail Pard if the first fire misbehaves.
- **Seat limits (do not work around):** fly deploy / secrets / prod DB / .env* / the mint script / the alpha test-account credential file.

### (10-09 state, kept for context)
#### STATE @ 2026-10-09 21:4x PT — DAY-CLOSED (log dev/2026/10/09/2026-10-09-0638-lead-code-log.md)
- **Alpha = `4bd1a236e9`**, promoted by xian 18:34 via `promote_to_alpha` (run 38013096307). Its code equals main `f0ac5db8d0`, and Tests
  on f0ac5db8d0 = success. 13 tokens live incl. complete_todo (Exec's 10:1x read; not re-read since). clear_todos stays OFF.
- **FIRST THING TOMORROW: the served checks on alpha are NOT run.** My seat's classifier refused reading
  `~/.piper-shared/web-agent-alpha-credentials.txt` (Credential Exploration). I asked the user to pick: (a) a permission rule for that
  file, (b) Web runs them, (c) xian runs them from the test card. Check for the answer before anything else. The checks, each quoting
  the served reply (rule 8): #1959 nonexistent issue (honest, no confirm first); #1960's consent line on "my default repo should be
  test-piper-morgan"; "delete the first two reminders"; #1889/#1963 standup + Radar disclosure (the OAuth-only/PAT-only accounts are Janus's
  walk-through with xian).
- **Phase 3 (#1595): ceiling 155 → 121, routing tail 91** (measured 17:5x; PPM recounted 121). Rules now: 10 (amended: CI's full tier =
  `tests/ -m "not llm"` + backlog gate + completion ratchets; an llm mark is retirement and cites its row), 11 (`reabsorption_check`, whole
  licensed set), and the #1973 dispatch threshold in every gate arm. The gate reads NO list GO. Remaining: COMPLETION_HISTORY (#1117 row
  @0.72 + 4 rule-10 holds), greeting/thanks/farewell (rule-10 holds), STAKEHOLDER (#1256, blocked on DOCUMENT_QUERY's loose literal),
  delete-family (#1935). PPM's Wed 10-14 trip-wire (ruled 10-10) reads the ceiling (band 110–120) with the tail beside it. **Re-measure Mon 10-12.**
- **Filed/closed today**: #1971 (closed at STOP: rule 11 built), #1972 (closed: my misread of a
  stale comment), #1973 (closed: threshold fix + 9 rows, no restores).
- **OpenAI API account is out of credits** (HTTP 429 at 17:24). Surface-2 evidence for #1973 is the Anthropic leg only. Sent to Exec as PM's decision.
- **Next build: #1970** (framing to the router, Production, Arch's design comment 6090297342): plumbing behind the flag → prompt + full run
  → ratchet. Deferred from 18:17 to a fresh session (context limit), so START it tomorrow.
- **Test card**: v16, Step 0 = the promote workflow (corrected from my wrong `fly deploy` at 18:10). Mirror artifact is v15, behind it.
- **Discipline notes from today** (mine): verify the layer CI gates on (the IDENTITY red); read the function, not its comment (#1972);
  run `date` BEFORE writing any time (drifted ~3h; corrected); never skip another repo's hooks.
- **Cron**: `dad96d7a`, armed 10-08 21:37 PT; expires ~10-15 21:4x. **Rotate at Wed 10-14 START** (date-keyed, unaffected by the tripwire question) (delete-then-create, update the registry row).
- **Seat limits (do not work around)**: fly deploy / fly secrets / prod DB reads / .env* / the mint script / the alpha test-account credential file.

