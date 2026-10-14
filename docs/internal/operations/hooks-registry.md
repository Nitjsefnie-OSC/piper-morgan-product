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
`check-branch.sh`.

Exit codes: a PreToolUse hook that exits 2 **blocks** the tool call. Exit 0 lets it through. A
PostToolUse or PreCompact hook can only **warn**: the tool has already run, or compaction proceeds.

## 1. Claude Code hooks, project settings (`.claude/settings.json`, every seat in this repo)

| Hook | Event / matcher / if | Must do | Blocks? | Concept |
|---|---|---|---|---|
| `session-start.sh` | SessionStart (also fires with source `compact`) | Print status within budget: log, mail counts, briefing freshness, role card (from the briefing's `ROLE-CARD` block), deltas | No | CLAUDE.md "Session start"; #853 |
| `check-branch.sh` | PreToolUse Bash, if `git commit*` | Refuse a commit of `mailboxes/**` on any branch but main; warn on other non-main commits | Yes (mailbox case) | `branch-worktree-mailbox-discipline.md`; `amber-hooks-investigation-2026-07.md` |
| `guard-pm-checkout.sh` (+ `guard_pm_checkout.py`) | PreToolUse Bash, every call | Refuse working-tree-discarding git aimed at PM's main checkout | Yes | CLAUDE.md hard rule 1; decisions.log (R6 step 1, 10-04) |
| `pre-commit-reconcile-drafts.sh` | PreToolUse Bash, if `git commit*` | When a commit touches `docs/public/comms/drafts/`, run `reconcile-drafts-calendar.py` for draft and calendar drift | Can exit 2 | decisions.log (Layer C). Header cites a missing `docs/read/...` path. |
| `autoclose-guard.sh` | PreToolUse Bash, if `git commit*` | Pass the message to `scripts/check_autoclose_keywords.py`: refuse close/fix/resolve plus `#N` without `Auto-Close: intentional`, and refuse credential-shaped messages | Yes | CLAUDE.md hard rules 5 and 3; #1691, #1845 |
| `log-maintenance-reminder.sh` | PostToolUse Bash | Every 15 Bash calls, remind if today's session log is missing or stale | No | CLAUDE.md "Role and session log"; methodology-31 and -41 |
| `context-usage-reminder.sh` | PostToolUse Bash | Once per session at roughly 75 to 85% context, suggest compacting at the next break | No | **None written.** Runs on every Bash call. Needs Cost/Benefit/Review (sunset rule, 11-01). |
| `issue-checkbox-lint.sh` | PostToolUse Bash | After a commit that closes an issue, warn if the issue body still has unchecked boxes | Warns (exit 2 is advisory after the fact) | `agent-protocols/issue-closure-protocol.md` |
| `memory-index-overlimit-warn.sh` | PostToolUse Edit, Write, MultiEdit | Warn when the shared memory index nears its silent-truncation limit | No | `memory-index-size-limits.md` (explains the limit; this page names the hook) |

## 2. Claude Code hooks, user level (`~/.claude-pm/settings.json`, every seat on Amber; Pard installs)

These point at the scripts in **PM's checkout path** (`/Users/xian/Development/piper-morgan-product/.claude/hooks/`),
not the seat's worktree. They exist because, in July, project hooks didn't fire reliably in worktree
sessions (`amber-hooks-investigation-2026-07.md`). The repo copy of this config is
`amber-userlevel-hooks-mirror.json`.

| Hook | Event | Must do | Notes |
|---|---|---|---|
| `check-branch.sh` | PreToolUse Bash | As above | **Also wired at project level.** Whether both fire on a worktree seat isn't measured here. |
| `pre-commit-broad-staging-warn.sh` | PreToolUse Bash | Warn on broad staging | **Its own header says it moved to the git pre-commit on 09-28 (#1798)**, which still runs it. This user-level entry may be a leftover double. Open question for Pard. |
| `pre-commit-reconcile-drafts.sh` | PreToolUse Bash | As above | Also wired at project level |
| `log-maintenance-reminder.sh`, `context-usage-reminder.sh`, `issue-checkbox-lint.sh` | PostToolUse Bash | As above | Also wired at project level |
| `precompact-signoff-warning.sh` | PreCompact | Before compaction, warn about uncommitted, unpushed or unmerged work | User level only. Concept: `branch-worktree-mailbox-discipline.md` |

## 3. Seat-local and plugin hooks

| Hook | Where | Must do | Notes |
|---|---|---|---|
| `PROBE-userpromptsubmit.sh` | CIO's `.claude/settings.local.json`, UserPromptSubmit | Append one line per submitted prompt to `dev/state/probe-userpromptsubmit-cio.log` (a submission ledger from outside the model) | CIO seat only; never blocks. It dirties `git status` on every wake (noted in the 10-13 rewrite). |
| `piper-guards` mod (`claude-plugins/piper-guards/`, v0.2.0) | Plugin on CIO's seat (local scope), parallel week to 10-19 | Rules M-1 to M-6 shadow the settings hooks above and add Projects-v2, mail-on-main, bearer-on-write and subagent-model rules | Concept: its README and `dev/2026/10/03/spec-eval/D-propose-ruleset.md`. Fails open. Decision on retiring the settings hooks after the week. |

## 4. Git hooks (shared git store `.git/hooks/`, every worktree by construction; source in `scripts/git-hooks/`)

| Hook | Installed? | Must do | Blocks? | Concept |
|---|---|---|---|---|
| `pre-commit` | Yes | Run the broad-staging and ruff warnings, then `check-branch.sh` on the settled index (Arch's time-of-check ruling, 07-29) | Only via check-branch | Its header; `amber-hooks-investigation-2026-07.md` |
| `pre-push` | Yes (identical to source, 10-13) | (a) The **old-history guard**: refuse a push that contains any sha in `<common-dir>/piper-old-history-sentinels`, logging to `piper-old-history-guard.log`. (b) A fast smoke run on pushes touching code. | Yes | `history-rewrite-runbook.md` (Exec, moved to docs 10-14; the sentinel protocol and as-run record); header; `mechanism-sunset-or-renew.md`. The header's own `Concept:` pointer waits for the hook's next functional edit, because any edit makes the installed copy differ from source until reinstalled (xian's paste). |
| `post-commit` | Yes; a `post-commit.DISARMED-2026-09-21-runaway` copy sits beside it | Delegate to `.claude/hooks/post-commit.sh` (heartbeat auto-fire pilot, ruff advisory) | No | Header points at `amber-hooks-investigation-2026-07.md`. **Current state of the pilot isn't confirmed on this page.** |
| `commit-msg` | **No, deliberately** (until the rewrite settles; CIO 8s, xian's paste) | Shape-independent check for rules 3 and 5 on the final message. Fails open loudly if the checker crashes. | Would block | Its header only. A concept doc is owed (audit R6). |

Smaller push-time scripts in `scripts/hooks/` (`pre-push-release-notes-check.sh`,
`editorial-calendar-reconcile-warn.sh`) aren't installed in the common dir as of 10-14 (`ls .git/hooks`).
The audit lists them as having no concept doc.

## Open questions (each to the named role)

1. **Pard:** is the user-level `pre-commit-broad-staging-warn.sh` PreToolUse entry a leftover from before
   09-28? If so, remove it. The git pre-commit already runs it.
2. **Pard and Arch:** project-level and user-level both wire `check-branch.sh`, `pre-commit-reconcile-drafts.sh`
   and the three PostToolUse reminders. Do worktree seats run each one twice? The July finding that made the
   user-level copies necessary may no longer hold.
3. **CIO:** at the piper-guards week's end (10-19), decide per rule whether the mod replaces the settings hook,
   then update sections 1 and 3.

**Verified how:**
- Read `.claude/settings.json`, `~/.claude-pm/settings.json` and CIO's `settings.local.json` with a JSON
  parser, listing every event, matcher, `if` and command.
- Listed `.git/hooks` in the shared store.
- Read each hook's header and counted its `exit` codes.
- 2026-10-14, about 11:30 PT.
- **Layer:** config and file. Whether each hook fires in a live session isn't measured here.
- **Denominator:**
  - 9 project registrations;
  - 7 user-level registrations;
  - 1 seat-local registration;
  - 1 plugin;
  - 4 git hooks.
