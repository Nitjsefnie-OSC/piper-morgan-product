# Methodology audit, 2026-10-14

**Audit period**: 2026-04-17 to 2026-10-14 (26 weeks)
**Previous audit**: 2026-04-17 (`dev/2026/04/17/methodology-audit-2026-04-17.md`)
**Trigger**: CIO standing item 8q. This audit is 179 days after the last one, against my own maximum of 8 weeks. The 10-13 role-duties research found it (`docs/internal/research/role-duties-operational-vs-official-2026-10-13.md`).
**Frame**: xian, 10-13: "Somewhere a written version of the concept does need to exist. It can't just live in how it's currently implemented. ... we should - in a perfect world - be able to recreate our code from scratch just by following our own docs." So the main question is: **for each mechanism we run, is there a written concept, and do the two point at each other?**
**Conducted by**: CIO (Claude Opus 5.5). Evidence came from three Sonnet subagents (model set explicitly), and CIO spot-checked each by a different method. Synthesis is CIO's.

---

## 1. Summary

1. **Most mechanisms can't be rebuilt from the docs alone.** Of 152 process mechanisms (hooks, git hooks, skills, cohort scripts, process workflows):
   - 39 (26%) are linked both ways: a concept doc names the mechanism, and the mechanism points back.
   - 63 (41%) are named by a doc, but the mechanism doesn't cite it.
   - 6 point at a doc that doesn't name them.
   - **44 (29%) have no concept doc at all.** Their reason for existing lives only in a header comment, or nowhere.
   - Hooks are the weakest class: 1 of 14 is linked. Most of the gap is in things that run unattended.
2. **When a doc and a mechanism are linked, the doc is usually right about behaviour.** In eight spot-checks, the four behavioural claims matched the code. The four failures were all stale names, paths or counts left behind by a rename, a fold-in or a later edit. Drift comes from renames, not from rules changing under the doc.
3. **Methodology-core grew, and the new half is alive.** There are 70 files: 56 numbered, plus 14 unnumbered. Of these, 19 are LIVE (cited in logs and by an instruction surface), 20 are cited only in logs, 23 are marked historical and 8 are silent. The live set is almost entirely m-29 to m-55, filed this period. The top two (m-44 "Clear is not a measurement", 243 logs; m-43 "Name the layer", 213 logs) are working vocabulary.
4. **The April "silent docs" problem was settled by disposition, not by refreshing.** Of the 21 silent docs, 11 now carry a HISTORICAL banner (B3, 10-01) and 3 revived. The other 7 (m-01, m-03, m-04, m-13, m-15, m-17, m-21) are still silent in logs, but **B3 ruled each one EFFECTIVE** (Arch-ratified 09-01; "citation count mispredicts effective"). *Correction: the first version of this audit called these 7 undecided; B3's tracker says otherwise.* MULTI_AGENT_QUICK_START was ruled HISTORICAL but never bannered; it is now. One live doc now **contradicts current practice**: m-31 says the cycle branch "never rebases or merges main in", and CLAUDE.md says to merge origin/main and push.
5. **The period's main movement was from vigilance to mechanism, then a cost correction.** Every incident-driven rule got a guard. Then the October evaluation measured the cost (5.3 coordination lines per product line; about 65 heartbeat commits a day) and cut back: the slim CLAUDE.md, heartbeats out of git, and the sunset-or-renew rule. The 10-13 duty research adds the consequence: judgement work that can't be mechanized gets crowded out (Pattern-075, m-36 corollary).

**Verdict**: the methodology works operationally and is unusually well recorded *as history* (claude-md-history.log, the tick changelog, decisions.log). It is poorly recorded *as concept*. A rebuilder would have to reconstruct intent from post-mortems, design proposals and mail. The fix is cheap and mechanical: one more line on the rule we already have (Section 6, R1).

---

## 2. Mechanism-to-concept inventory (xian's frame)

**Method.**
- Inventoried every Claude Code hook (`.claude/hooks/` and its wiring), git hook, skill, cohort-process script (83 chosen from 272 in `scripts/`; product, build and test scripts skipped), and process-enforcing workflow (15 of 23).
- For each, grepped the canonical doc roots (CLAUDE.md, briefings, operations, methodology-core, ADRs, decisions.log, patterns, agent-protocols, PDRs) for its path or name, and read its header for a pointer back.
- A bare "run X" mention in a briefing counts as weak: it isn't an explanation of why.

| Class | n | Linked | Doc names it only | Mechanism cites only | No concept |
|---|---|---|---|---|---|
| Claude Code hooks | 14 | 1 | 9 | 1 | 3 |
| Git hooks | 6 | 0 | 1 | 1 | 4 |
| Skills | 34 | 15 | 10 | 0 | 9 |
| Process scripts and plist | 83 | 20 | 33 | 3 | 27 |
| Process workflows | 15 | 3 | 10 | 1 | 1 |
| **Total** | **152** | **39** | **63** | **6** | **44** |

**No concept at all, ranked by risk** (enforces a hard rule, or runs unattended):
1. `scripts/git-hooks/commit-msg`: the shape-independent layer for hard rules 3 and 5 (not installed yet). The design exists only in its header.
2. The old-history guard in `scripts/git-hooks/pre-push`: protects the history rewrite (hard rule 7). The rationale and sentinel protocol are in the header. The runbook is a `dev/active/` file, which sprint cleanup removes.
3. `.claude/hooks/memory-index-overlimit-warn.sh`: `memory-index-size-limits.md` explains the limit but never says a hook must exist.
4. `scripts/whats-armed.sh`: the one behavioural answer to "what is actually armed". Mine, built 10-13, with no doc.
5. `.claude/hooks/context-usage-reminder.sh`: runs on every Bash call. No doc, and no Cost/Benefit/Review lines.
6. `.github/workflows/quarterly-maintenance.yml`: unattended and files issues. Its header cites only an issue number.
7. `scripts/main-ci-status.sh`: what "green" must mean, and who acts on red, is written only in the tick skill (v1.53).
8. `scripts/usage-capture.sh` and its readers: unattended. The header cites `docs/schedules.md`, which isn't in this repo (it's in Pard's).
9. Release and editorial push gates (`scripts/hooks/pre-push-release-notes-check.sh`, `check-deploy-trigger-parity.sh`, `editorial-calendar-reconcile-warn.sh`): named nowhere.
10. Five push/pull/commit wrappers (`safe-push.sh`, `push-main.sh`, `pull.sh`, `preserve.sh`, `commit.sh`): no doc says which, if any, is canonical. CLAUDE.md prescribes `git push origin HEAD:main` directly, so they may be dead. **Unverified**: not opened.

**Pointers that don't resolve.**
- Headers cite missing docs (4):
  - `branch-guidance.sh` cites `docs/development/BRANCH-MANAGEMENT.md`;
  - `check-backlog-sync.sh` cites `docs/planning/backlog.md`;
  - `usage-capture.sh` cites `docs/schedules.md`;
  - `pre-commit-reconcile-drafts.sh` cites `docs/read/...`.
- Docs name missing mechanisms (stale, not design):
  - `mailbox-bridge-transparency-design-2026-06-16.md` names `scripts/mail-send-v3.sh` and a test file; both were folded into `mail-send.sh`. **CIO's doc.**
  - `staggered-audit-calendar-2026.md` names `pattern-sweep-reminder.yml` and `role-health-reminder.yml`; the real files are `pattern-sweep.yml` and `role-health-check.yml`.
  - `finish-the-unfinished-sprint-2026-07-16.md` uses hyphens where the scripts use underscores.
- ADRs 007, 009, 014, 033 and 040 and methodology-06 name scripts that were never built. That's legitimate for design records, but none says "not built".

**Spot-checks** (doc claim against code, eight pairs):
- **Match (4):** `deploy-mcp.sh`; `check_autoclose_keywords.py` (the code is stricter than rule 5, because it also refuses credential-shaped messages); `aging-standing-items.sh` (accepts more spellings than the doc names); `check-current-state.py`.
- **Mismatch (4):**
  - `prod-command-permissions.md` gives two deny counts, 1052 and 1028. The JSON says 1052. **CIO's doc.**
  - The mail-bridge design doc's dead paths.
  - The audit calendar's wrong workflow filename.
  - `hb-store.py`'s docstring still describes the git and store "parity window", which ended 10-12. **CIO's code.** The doc, `r3-metric.md`, is right.
- **CIO re-check, a different method (direct read):** the 1028/1052 lines (lines 32 and 53), the absence of `scripts/mail-send-v3.sh`, `whats-armed` missing from docs and briefings, and the `hb-store.py` docstring at lines 4 to 9. All confirmed.

**Structural read.** There is no per-mechanism "what it must do" page. Concept is scattered over post-mortems (`amber-hooks-investigation-2026-07.md`), proposals, `decisions.log`, `claude-md-history.log` and mail. The sunset-or-renew rule (10-04, CIO-owned) already makes every new mechanism carry Cost, Benefit, Review and Owner lines in its header. It never asks for a pointer to the concept. That is the cheapest place to close xian's gap.

---

## 3. Methodology-core health

**Count.** 70 files, 56 of them numbered (m-00 to m-55). The CIO briefing's "26 methodology files" is stale; fixed with this audit.

| Verdict | Files |
|---|---|
| LIVE: cited in logs and by an instruction surface | 19 |
| Cited only in logs | 20 |
| Marked historical or absorbed | 23 |
| Silent | 8 |

**Most cited** (session logs, 04-17 to 10-14, 1,908 logs):
- m-44, Clear is not a measurement: 243
- m-43, Name the layer: 213
- m-36, Mechanism beats vigilance: 74; m-30, Consumer-trace verification: 74
- m-41, Mechanism displaces unreferenced discipline: 73
- m-20, Omnibus: 65

By instruction surfaces, m-36 leads (12, mostly role portfolios), then m-44 (9) and m-00 (8). **CLAUDE.md cites no methodology doc at all, and no hook does.**

**Contradiction found.**
- **m-31, Append-only autonomous cycle** (25 logs; cited by `cleanup-dev-active`). It says a dated cycle branch with one mutable file that "never rebases or merges main in". CLAUDE.md says: a stable `claude/{role}-cycle` worktree, merge origin/main, push `HEAD:main`; the session log is the only durable log.
- m-41 records the displacement incident that changed this. A reader who stops at m-31 gets the opposite rule. **CIO's slot. A superseded banner is added with this audit.**
- **Minor lag:** m-20 (omnibus, "last updated March 21") lags the create-omnibus skill, which has a CSV row step m-20 doesn't mention.

**Silent in logs (8):**
- **m-01, m-03, m-04, m-13, m-15, m-17 and m-21:** B3 ruled each EFFECTIVE (`docs/internal/architecture/reviews/2026-08-architectural-review/b3-methodology-disposition.md`, ratified 09-01). They're kept on purpose; low citation isn't a defect for these.
- **MULTI_AGENT_QUICK_START:** B3 ruled it HISTORICAL, but the banner was never applied. Applied 10-14 (CIO, executing B3).

**The evidence base is narrow.**
- The m-43 to m-55 family is 13 docs filed in two months, almost all by CIO. Several are marked one-agent or zero-cross-author (m-51, m-55).
- Their citation counts are high, but citation isn't independent confirmation (m-45, "agreement is not replication", applies to its own family).
- Promotion to Proven should wait for a second author's instance, as m-29 requires.

---

## 4. Period innovations, assessed

A full dated timeline is kept in the audit's working notes; the principal shifts are below. Each is judged on whether it worked, and whether it's written down as concept.

| Shift | When | Worked? | Written as concept? |
|---|---|---|---|
| Worktrees per role (Model A, then B, then A on Amber) | 04-22, 06, 07-25 | Yes. Ended the shared-checkout collisions. Hard rule 1 holds. | Yes: `amber-worktree-lifecycle.md` |
| Mail v3 push-to-ref, then v4 fan-out-on-read | 06-19, 10-08 | v3 yes. v4 is a pilot, review 10-22. | v3 is scattered (CLAUDE.md, discipline doc, a stale design doc). v4: `mail-v4-pilot.md` |
| Duty cycle: tick skill v1.0 to v1.53; "the fire is a wake"; drain to empty | 06-06 onward | Yes. It's what keeps eleven seats moving. | As procedure (the skill) and history (the changelog). **Not as concept.** The design folder stops at v0.6. |
| Session cron to LaunchAgents | 09-24 onward | Yes (CIO first, PA confirmed 10-02) | **No ops doc.** Only tick v1.41 and a research note. |
| Heartbeat store (out of git) | 10-12 | Yes. Removed about 65 commits a day. | `r3-metric.md`; `hb-store.py` header stale (fixed with this audit) |
| "Verified how" with layer and denominator | 08-29 | Yes. Visible in most completion memos. | Yes: m-43 and m-44, plus CLAUDE.md |
| Safety rules from near-misses (rules 1, 4, 5, 3, 8) | 06-21 to 10-12 | Yes. Each paired with a guard where possible. | Yes, as rules plus history. Guards are partly linked (Section 2). |
| Retrenchment: context-floor plan, Spec evaluation R1 to R7, slim CLAUDE.md, sunset-or-renew | 09-21 to 10-12 | Yes. CLAUDE.md is slim, gated on probe results. | Yes: evaluation, `r3-metric.md`, sunset rule |
| History rewrite with sentinel guard | 10-13/14 | Yes. 11 of 11 seats reset; 6 refusals were legitimate; one hazard caught before it ran (the watchdog's pull). | **No.** The runbook lives in `dev/active/` and will be cleaned. |

**Practices running with no written concept:**
- Agent 360 (there's no procedure doc; one March finding file is the only `docs/` hit);
- OWED markers;
- role cards and the `Drift:` line;
- the current-state liveness design (belts, watchdog, freeze check, heartbeat store) after the LaunchAgent and store changes;
- the LaunchAgent wake mechanism;
- usage capture;
- `scope-guard`;
- probe-testing a ruleset change;
- the history-rewrite and freeze protocol;
- cross-project agent coordination beyond mail routing.

---

## 5. 04-17 recommendations, status

| # | Recommendation | Status now |
|---|---|---|
| A1 | Flywheel reformulation | Done; carried forward to v3.0 (09-11) |
| A2 | Hooks Phase 1 | Closed with rationale; superseded by the Amber hooks investigation |
| A3 | Retire the flywheel integration module | Done (04-28) |
| B1 | Flywheel downstream sweep (~146 files) | **Partial, unverified.** No completion record. 9 docs still say "Four Pillars" (some are history). |
| B2 | Triage the silent methodology docs | **Done, by another route.** B3 (Arch-ratified 09-01) dispositioned every one: 19 bannered HISTORICAL and 7 kept EFFECTIVE. One banner (QUICK_START) was missed and was applied 10-14. |
| B3 | Indoor plumbing | Done (m-26) |
| B4 | Continuity memo pattern | Done; Proven (Pattern-065) |
| B5 | Roundtable format | Done by incorporation (m-22) |
| B6 | Briefings cite, not paraphrase, the Flywheel | **Partial.** Lead cites m-00 as v2.0; it's v3.0. Others unchecked. |
| S1 | Canonical-term drift in the weekly audit | **Built, thinly operated.** The watch file exists. 3 of 4 later weekly-audit findings files never mention vocabulary. The weekly audit ran irregularly. |
| S2 | ADR-045 citation watch | **Not evidenced. Closed 10-14 (CIO, R11):** passive watches with no trigger don't run (Pattern-075). If grammar drift matters again, it comes back as a dated check. |
| S3 | Scaffolded probing for E2E | **Superseded. Closed 10-14 (CIO, R11).** The R6 probe suite took the probing slot for rules; E2E probing returns with its own issue if Lead scopes it. |

Score: 7 done, 3 partial, 1 not evidenced, 1 superseded. Every partial item is documentation upkeep. That repeats both earlier audits: the method maintains its practice well and its documents poorly. That's the same finding as Pattern-075, one level up.

---

## 6. Recommendations

**Done with this audit (CIO's own files, 10-14):**
- **R1, a `Concept:` line in the sunset-or-renew rule.** Every new mechanism now carries a fifth header line naming the doc that says why it exists and what it must do. Existing mechanisms get it at the rule's 11-01 inventory. This is xian's frame turned into the rule we already enforce.
- **R2: m-31 gets a superseded banner** pointing to CLAUDE.md "Git, push, sign-off" and the one-log rule.
- **R3: CIO's stale items fixed.**
  - The deny count in `prod-command-permissions.md`.
  - The dead v3 paths in the mail-bridge design doc.
  - The `hb-store.py` docstring.
  - The CIO briefing's "26 methodology files".
  - `whats-armed.sh` gets a concept doc: `docs/internal/operations/whats-armed.md`.

**Routed (each the named role's call):**

| # | Action | Owner | Why |
|---|---|---|---|
| R4 **DRAFTED 10-14** (`hooks-registry.md`; Arch review pending) | One hooks registry page: every hook, event, matcher, why, and its concept doc | CIO drafts, Arch reviews | Hooks are 1 of 14 linked. The control plane is CIO's (role card priority 3). **CIO will draft it.** Trigger: R1 merged. |
| R5 **DONE 10-14** (`docs/internal/operations/history-rewrite-runbook.md`) | Move the history-rewrite runbook and freeze protocol from `dev/active/` to `docs/internal/operations/` before sprint cleanup | Exec | Only record of an irreversible procedure. Rule 7. |
| R6 | Concept docs for `commit-msg` (rules 3 and 5) and the old-history guard | CIO | Both are mine and both guard hard rules. Trigger: the 8s install. |
| R7 **DONE 10-14** (`docs/internal/operations/agent-360-procedure.md`; CIO fixed the workflow's stale v0.4 pointers) | Agent 360 procedure doc | HOST | Run four times, with no written procedure |
| R8 | Fix the audit calendar's workflow filenames | Docs | Two workflow names are wrong. (The 7 silent methodology docs need nothing: B3 kept them. Only the QUICK_START banner was missing, applied 10-14.) |
| R9 **DONE 10-14** (`push-main.sh` canonical; four retired, c4f64da4e7; recipe §5) | Say which push/pull wrappers are canonical; retire the rest | Lead | Five wrappers, no doc, and CLAUDE.md prescribes the raw command |
| R10 **CIO half DRAFTED 10-14** (`liveness-current-state.md`; Pard to confirm 3 rows) | Current-state liveness doc (belts, LaunchAgents, heartbeat store, freeze check) | CIO with Pard | No single page since the 09-24 and 10-12 changes |
| R11 **DONE 10-14** | Close S2 and S3 from the April audit | CIO | Not evidenced or superseded |

**Structural:**
- The next audit is due **by 2026-12-09** (8 weeks), or within 2 weeks of the next sprint gate closing, whichever is first.
- Re-run Section 2's count then. **The test of R1 is whether linked rises above 26% and no-concept falls below 29%.**
- Re-run the 10-13 duty count on 10-27 (standing item 8r), as already planned.

---

## 7. State of the methodology

**Strong:**
- Incident to rule to guard, often on the same day.
- Evidence language that agents actually use (m-43 and m-44 in more than 200 logs each).
- Infrastructure moves that the process survived intact: worktrees, Amber, LaunchAgents, the history rewrite.

**Weak:**
- Concept docs: 29% of mechanisms have none.
- Upkeep after a rename.
- An evidence base for the newer methodology entries that is mostly one author.
- Judgement work, including this audit, crowded out by mechanized routine. This audit was 4 months late, and the 10-13 research is what triggered it, not its own cadence. The trigger that failed was a date in my briefing with nothing to fire it. The fix is the Drift line (v1.51) plus the dated next-audit row in my standing items, and the 10-27 re-run checks whether it holds.

**Verified how:**
- Three subagent evidence passes:
  - 152 mechanisms by grep and header read;
  - 70 methodology files by regex over 1,908 logs and 81 instruction files;
  - git history since 04-17.
- CIO re-checked each by a different method (direct reads): the B briefing line and m-31's text; C's Agent 360 gap; A's four path and count claims.
- **Layer:** textual. Whether a doc was read or followed wasn't measured. The A table is grep-based, so a concept doc phrased without the mechanism's name reads as missing.
- **Denominator:** all 152 process mechanisms as classed, all 70 methodology files, and the full log window.
