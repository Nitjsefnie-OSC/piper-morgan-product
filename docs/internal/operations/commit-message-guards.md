---
type: operations
title: "Commit-message guards: one checker, three doorways (hard rules 3 and 5)"
valid_from: "2026-10-14"
last_updated: "2026-10-15"
---

# Commit-message guards

**Owner:** CIO (control plane). **Review:** 2026-12-08.
**Mechanisms this page explains:**
- `scripts/check_autoclose_keywords.py` (the checker);
- `.claude/hooks/autoclose-guard.sh` (doorway 1);
- `scripts/mail-send.sh` (doorway 2);
- `scripts/git-hooks/commit-msg` (doorway 3).

Each points back here.

## Why they exist

A commit message on main is public and permanent, like a file. Two kinds of message have done real
harm:

1. **An accidental issue close (CLAUDE.md hard rule 5).** GitHub closes issue N when a close-keyword
   (`close`, `fix`, `resolve` and their forms) appears within a few tokens of `#N` in a commit pushed to
   main, whatever the words around it say. "not yet resolved: #1278" closed a live Beta Blocker (07).
   A mail commit subject, "close #1677/#1488 properly", closed #1677 (08-28). The written rule failed to
   prevent it twice (#1691).
2. **A credential in a message (hard rule 3).** A commit subject carried a tester's name and a full
   invite token on main (#1845, 10-04). The file linter `mailbox_bearer_lint.py` reads files, not
   messages.

## What the guard must do

- **One definition of a refused message**, in one place: `check_autoclose_keywords.py`.
  - **Rule (a):** a close-keyword within three tokens before `#N` (or `owner/repo#N`, or an issue URL)
    is refused, unless the message carries the trailer `Auto-Close: intentional`.
  - **Rule (b):** any bearer-credential shape is refused, using the same detector as the file linter
    (it imports `scan_line` and `mask` from `mailbox_bearer_lint.py`, so the two can't drift apart). The
    trailer never waives rule (b). A hit is printed masked, never in full.
- **Every way a message reaches main passes through it** (the doorways below).
- **The normal fix is rewording**, not the trailer: write the number without `#`, or move the keyword
  away from it.

## The three doorways

| # | Doorway | When it runs | What it sees | Gap it leaves |
|---|---|---|---|---|
| 1 | `autoclose-guard.sh` (Claude Code PreToolUse on `git commit*`) | Before the commit object exists | The message re-derived from the **shell command string** (`-m`, `-am`, `-F`, `-C`/`-c`, heredocs, compound commands; #1934 fixed five shapes the first version missed) | Any shape it doesn't parse, and any commit not made through the agent's Bash tool (editor, script, human at a terminal) |
| 2 | `mail-send.sh` | Before its commit-tree push | The subject it was given | Only mail; commit-tree bypasses git hooks, which is why it calls the checker itself |
| 3 | `scripts/git-hooks/commit-msg` (git's own hook, shared store) | After git has assembled the final message | The **final message file** (`$1`), whatever shape produced it | `--no-verify`. **Installed 2026-10-15 13:2x** (xian's paste; CIO ran the installed hook: a "fix #1" message refused, a benign one allowed). |

Doorway 3 is the shape-independent one: by the time it runs, there's no shell left to parse. Doorway
1 still matters because it refuses earlier, before a commit object is made, which is a better
experience for the common case. Together they leave only a deliberate `--no-verify`.

## Failure behaviour

- **Fail open on the guard's own crash, loudly.** A crash also exits 1, the same code as a refusal. A
  broken checker (a missing import, a syntax error on main) would otherwise block every commit on every
  seat. Doorway 3 checks for a Python traceback and, if found, prints a warning and lets the commit
  through (CIO review 10-13, reproduced in a scratch repo).
- **Advisory strength.** Git hooks and Claude Code hooks can be bypassed (`--no-verify`, a different
  tool). This is a rule backed by a mechanism, not a control (`hooks-registry.md`).

## How to check it's armed

- `scripts/whats-armed.sh` runs doorway 1 with `git commit -m 'fix #1'` (must refuse) and a benign
  payload (must allow).
- It also reports doorway 3 as installed or not.
- A live check of doorway 1 on CIO's seat on 10-14 blocked `git commit --dry-run -m "fix #1"`
  (`hooks-registry.md`).
