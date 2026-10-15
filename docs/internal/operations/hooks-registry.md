---
type: operations
title: "Hooks registry: every hook, where it is wired, what it must do"
valid_from: "2026-10-14"
last_updated: "2026-10-14"
---

# Hooks registry

**Owner:** CIO (the control plane, role card priority 3). Arch reviews. Pard installs anything outside
the repo (user-level settings, the git common dir, launchd).
**Why this page exists:** the 2026-10-14 methodology audit found that 1 of 14 Claude Code hooks was linked
both ways to a written concept. The reasons lived in header comments, a July post-mortem and mail. This
page is the concept index. Each hook's header should carry `Concept: docs/internal/operations/hooks-registry.md`
or a more specific doc (sunset-or-renew rule, `Concept:` line).
**Is it actually firing?** This page says what is wired. `scripts/whats-armed.sh` measures what is armed
(see `whats-armed.md`). Only Pard's drumbeat measures a hook firing inside a live session, and only for
`check-branch.sh`. **Which copy:** since 10-14 19:15, PM's project copy, carried from origin/main
(mediajunkie 9afa8c9). Before that, the drumbeat tested the user-level copy, because its temp repo has no
project settings. See "Consequence" below.

Exit codes: a PreToolUse hook that exits 2 **blocks** the tool call. Exit 0 lets it through. A
PostToolUse or PreCompact hook can only **warn**: the tool has already run, or compaction proceeds.

## 1. Claude Code hooks, project settings (`.claude/settings.json`, every seat in this repo)

| Hook | Event / matcher / if | Must do | Blocks? | Concept |
|---|---|---|---|---|
| `session-start.sh` | SessionStart (also fires with source `compact`) | Print status within budget: log, mail counts, briefing freshness, role card (from the briefing's `ROLE-CARD` block), deltas | No | CLAUDE.md "Session start"; #853 |
| `check-branch.sh` | PreToolUse Bash, if `git commit*` | Refuse a commit of `mailboxes/**` on any branch but main, and tell the agent to send by `scripts/mail-send.sh` (fix steps corrected 10-14); warn on other non-main commits | Yes, on a pre-staged index. The git `pre-commit` row (section 4) is the enforcing check. | `branch-worktree-mailbox-discipline.md`; `amber-hooks-investigation-2026-07.md` |
| `guard-pm-checkout.sh` (+ `guard_pm_checkout.py`) | PreToolUse Bash, every call | Refuse working-tree-discarding git aimed at PM's main checkout | Yes | CLAUDE.md hard rule 1; decisions.log (R6 step 1, 10-04) |
| `pre-commit-reconcile-drafts.sh` | PreToolUse Bash, if `git commit*` | When a commit touches `docs/public/comms/drafts/`, run `reconcile-drafts-calendar.py` for draft and calendar drift | Can exit 2 | decisions.log (Layer C). Header cites a missing `docs/read/...` path. |
| `autoclose-guard.sh` | PreToolUse Bash, if `git commit*` | Pass the message to `scripts/check_autoclose_keywords.py`: refuse close/fix/resolve plus `#N` without `Auto-Close: intentional`, and refuse credential-shaped messages | Yes | `commit-message-guards.md` (doorway 1); CLAUDE.md hard rules 5 and 3 |
| `log-maintenance-reminder.sh` | PostToolUse Bash | Every 15 Bash calls, remind if today's session log is missing or stale. **Note (10-14):** its counter is one shared file, `/tmp/piper-log-reminder-counter`, so "every 15 calls" counts across all seats on the host, not per seat. | No | CLAUDE.md "Role and session log"; methodology-31 and -41 |
| `context-usage-reminder.sh` | PostToolUse Bash | Once per session at roughly 75 to 85% context, suggest compacting at the next break | No | **None written. Dead on Amber (found 10-14):** it reads `$CLAUDE_SESSION_ID` (unset in the CIO seat's Bash environment) and looks for the transcript under `~/.claude/projects`, but this fleet's transcripts are under `~/.claude-pm/projects` (`CLAUDE_CONFIG_DIR`). For this session the `find` returned 0 there and 1 under `~/.claude-pm`. So it exits 0 every call and never warns. **Sunset candidate at the piper-guards review (10-19):** M-9's status line covers it. If it's kept instead, read `transcript_path` from the hook's stdin JSON. |
| `issue-checkbox-lint.sh` | PostToolUse Bash | After a commit that closes an issue, warn if the issue body still has unchecked boxes | Warns (exit 2 is advisory after the fact) | `agent-protocols/issue-closure-protocol.md` |
| `memory-index-overlimit-warn.sh` | PostToolUse Edit, Write, MultiEdit | Warn when the shared memory index nears its silent-truncation limit | No | `memory-index-size-limits.md` (explains the limit; this page names the hook) |

**The time-of-check split** (Arch's ruling, 07-29; Arch's review, 10-14). `check-branch.sh` runs at two layers, and neither alone is the rule:
- As a **PreToolUse** hook, it reads `git diff --cached` *before* the command runs. On a compound `git add … && git commit` the index isn't staged yet, so it passes. That's why CLAUDE.md says to stage in one call and commit in the next.
- As part of the **git pre-commit** (section 4), it runs on the settled index. This is the enforcing layer, and it catches the compound form.
- The PreToolUse copy adds one thing: it still sees a `git commit --no-verify` (which skips git hooks), as long as the index was staged beforehand.

## 2. Claude Code hooks, user level (`~/.claude-pm/settings.json`, every seat on Amber; Pard installs)

**Since 10-14 10:43 (Pard), one entry only:** PreCompact `precompact-signoff-warning.sh` (before compaction, warn about uncommitted, unpushed or unmerged work; concept `branch-worktree-mailbox-discipline.md`). It points at PM's checkout's copy, `/Users/xian/Development/piper-morgan-product/.claude/hooks/`, which lags main until `sync-pm-local.sh` runs. It should eventually move to project level, so it runs the seat's own version.

Removed 10-14 (decided below): six duplicates of project hooks. They ran PM's checkout's copies alongside the seat's own:
- PreToolUse: `check-branch.sh`, `pre-commit-broad-staging-warn.sh`, `pre-commit-reconcile-drafts.sh`.
- PostToolUse: `log-maintenance-reminder.sh`, `context-usage-reminder.sh`, `issue-checkbox-lint.sh`.

Backup: `~/.claude-pm/settings.json.bak-20261014T104256`. History: in July, project hooks didn't fire reliably in worktree sessions (`amber-hooks-investigation-2026-07.md`), and that's why the copies existed.

## 3. Seat-local and plugin hooks

| Hook | Where | Must do | Notes |
|---|---|---|---|
| `PROBE-userpromptsubmit.sh` | CIO's `.claude/settings.local.json`, UserPromptSubmit | Append one line per submitted prompt to `dev/state/probe-userpromptsubmit-cio.log` (a submission ledger from outside the model) | CIO seat only; never blocks. It dirties `git status` on every wake (noted in the 10-13 rewrite). |
| `piper-guards` mod (`claude-plugins/piper-guards/`, v0.2.0) | Plugin on CIO's seat (local scope), parallel week to 10-19 | Rules M-1 to M-6 shadow the settings hooks above and add Projects-v2, mail-on-main, bearer-on-write and subagent-model rules | Concept: its README and `dev/2026/10/03/spec-eval/D-propose-ruleset.md`. Fails open. Decision on retiring the settings hooks after the week. |

## 4. Git hooks (shared git store `.git/hooks/`, every worktree by construction; source in `scripts/git-hooks/`)

| Hook | Installed? | Must do | Blocks? | Concept |
|---|---|---|---|---|
| `pre-commit` | Yes | Run `pre-commit-broad-staging-warn.sh` and `pre-commit-ruff-warn.sh` (warnings, exit 0), then `check-branch.sh` on the settled index (Arch's time-of-check ruling, 07-29) | Only via check-branch | Its header; `amber-hooks-investigation-2026-07.md` |
| `pre-push` | Yes (identical to source, 10-13) | (a) The **old-history guard**: refuse a push that contains any sha in `<common-dir>/piper-old-history-sentinels`, logging to `piper-old-history-guard.log`. (b) A fast smoke run on pushes touching code. | Yes | `history-rewrite-runbook.md` (Exec, moved to docs 10-14; the sentinel protocol and as-run record); header; `mechanism-sunset-or-renew.md`. The header's own `Concept:` pointer waits for the hook's next functional edit, because any edit makes the installed copy differ from source until reinstalled (xian's paste). |
| `post-commit` | Yes; a `post-commit.DISARMED-2026-09-21-runaway` copy sits beside it | Delegate to `.claude/hooks/post-commit.sh` (heartbeat auto-fire pilot, ruff advisory) | No | Header points at `amber-hooks-investigation-2026-07.md`. **Current state of the pilot isn't confirmed on this page.** |
| `commit-msg` | **No, deliberately** (until the rewrite settles; CIO 8s, xian's paste) | Shape-independent check for rules 3 and 5 on the final message. Fails open loudly if the checker crashes. | Would block | `commit-message-guards.md` (doorway 3; written 10-14, audit R6) |

Smaller push-time scripts in `scripts/hooks/` (`pre-push-release-notes-check.sh`,
`editorial-calendar-reconcile-warn.sh`) aren't installed in the common dir as of 10-14 (`ls .git/hooks`).
The audit lists them as having no concept doc.

## Decided 10-14: drop the user-level duplicates

**Facts:**
- **Project-level SessionStart fires on worktree seats** (Arch, from its own session at start and after compaction; user level doesn't wire SessionStart).
- **Project-level PreToolUse fires on a worktree seat.** CIO measured it 10-14, between 10:35 and 10:37 PT (after the 10:35 mail read, before this edit): `git commit --dry-run -m "fix #1"` in CIO's worktree was BLOCKED by `autoclose-guard.sh`, which only the project settings wire. The piper-guards plugin has no auto-close rule, so the refusal could only come from the project hook. One seat, in auto mode.
- **Project-level PostToolUse firing on a worktree seat isn't measured.** Its exit-0 output isn't visible to the agent.
- **The two levels run different commands.** User level runs `bash /Users/xian/Development/piper-morgan-product/.claude/hooks/X.sh`, PM's checkout's copy. Project level runs the seat's worktree copy. So both run, and Claude Code's dedup of identical commands doesn't apply (Pard, from the JSON; an expectation, not a measurement).
- **PM's checkout's copies lag main**, because only `sync-pm-local.sh` fast-forwards it. On 10-14 all 7 user-level scripts differed from main (Arch, `diff -q`).

**Ruling** (Arch, the architecture half): two copies of one rule, read from two places and kept in step by hand, is a second-resolver shape. Since project-level PreToolUse fires, remove the user-level duplicates:
- `check-branch.sh`
- `pre-commit-broad-staging-warn.sh`
- `pre-commit-reconcile-drafts.sh`
- the three PostToolUse reminders

Keep `precompact-signoff-warning.sh` at user level, since it has no project copy. It should eventually move to project level, so it runs the seat's own version.

**Done 10-14 10:43** (Pard; the seat wasn't refused). **After the edit:** CIO re-ran the autoclose probe between 10:49 and 10:50 PT, and it was still BLOCKED by the project hook. PostToolUse is still not cleanly measured. The one instrument tried, the log-maintenance counter, is a host-wide shared file that every seat increments, so a rise can't be attributed to one seat. A clean PostToolUse probe needs a per-session signal.
- **Consequence, found 19:05 (Pard):** the hook drumbeat went red ("probe commit LANDED"). It had only ever tested the user-level `check-branch.sh`, the copy this decision removed. PM seats load check-branch from project settings, and project-level PreToolUse fired (the autoclose probe above, a sibling hook). Pard's fixed probe now tests check-branch's project copy directly. Pard fixed the probe at 19:15 to carry PM's project `.claude/` from origin/main, and it PASSES. Neither Pard nor CIO checked what the drumbeat exercised before the removal. The sunset rule now has a "Before you remove" step.
- **Residual risk:** project-level PostToolUse firing is unmeasured, so the three reminders could go silent. They're advisory, so this is low cost, and it's checked after the edit.

## Still open

- **CIO:** at the piper-guards week's end (10-19), decide per rule whether the mod replaces the settings hook, then update sections 1 and 3.

**Verified how:**
- Read `.claude/settings.json`, `~/.claude-pm/settings.json` and CIO's `settings.local.json` with a JSON
  parser, listing every event, matcher, `if` and command.
- Listed `.git/hooks` in the shared store.
- Read each hook's header and counted its `exit` codes.
- Committed 2026-10-14 10:26 PT (first version); updated 10:37 with Arch's and Pard's answers and CIO's PreToolUse probe. (The first version said "about 11:30 PT", which was a guess, not a reading; corrected.)
- **Layer:** config and file. Whether each hook fires in a live session isn't measured here.
- **Denominator:**
  - 9 project registrations;
  - 7 user-level registrations;
  - 1 seat-local registration;
  - 1 plugin;
  - 4 git hooks.
