---
type: operations
title: "What's armed: the one probe of which cohort mechanisms are live"
valid_from: "2026-10-13"
last_updated: "2026-10-14"
---

# What's armed

**Mechanism:** `scripts/whats-armed.sh`. **Owner:** CIO. **Review:** 2026-12-08.

## Why it exists

A mechanism that is described is not a mechanism that is running (methodology-49). The cohort
relies on about thirty guards: Claude Code hooks, git hooks, LaunchAgents, the heartbeat store and
pinned tools. Each one can be present in the repo and still be inert. The hook might be unwired,
the installed copy might differ from the source, the agent might not be loaded, or the tool might
not resolve. Before this script existed, the only way to know was to ask each of eleven seats to
probe one hook by hand, and the answers mixed layers. "The file is there" got reported as "it
fires". This came out of Agent 360 v0.5, candidate 2 (CIO's 9.2: "name a mechanism you believe is
running, and say how you last verified it"). xian was on board on 2026-10-13, via HOST.

## What it must do

1. **One run, every mechanism, with a denominator.** Print one line per check and a total
   ("N checks: A armed, B NOT ARMED, C unmeasured").
2. **Name the layer on every line** (methodology-43). There are four layers:
   - `live`: Claude Code itself ran the hook. Only Pard's verify-hooks drumbeat measures this, and
     the script reads its last verdict. The drumbeat tests PM's project copy of `check-branch.sh`,
     carried from origin/main, since 10-14 19:15. Before that it tested the user-level copy.
   - `script`: the hook was run directly with a synthetic tool payload. Each PreToolUse guard gets
     one benign payload, which must be allowed, and one payload it should refuse, which must be
     refused.
   - `file`: present, executable and identical to its tracked source. Nothing was run.
   - `state`: a process or store reports itself (launchctl, the heartbeat store).
3. **Never claim more than it measured.** A check it couldn't run is `UNMEASURED`, never `ARMED`.
   Example: the old-history guard is dormant with no sentinel file outside a rewrite.
4. **Read-only.** It runs no git write, no fly command and no push for the caller. The only files it
   writes are the guards' own temp files.
5. **Exit status:** 0 when nothing is NOT ARMED, 1 when anything is. Unmeasured lines don't fail the
   run.

## What it does not do

- It doesn't prove a hook fires inside a live session. That's the drumbeat's job, and only for
  `check-branch.sh`.
- It runs the PostToolUse hooks and `session-start.sh` only as a parse check, because they have
  side effects.
- It doesn't cover seats on other hosts.

## Runs on record

- **2026-10-13 (first run):** 29 checks: 26 armed, 2 NOT ARMED, 1 unmeasured. Which two were NOT
  ARMED isn't recorded here; see the CIO log for 10-13.
- **2026-10-14 10:5x:** 29 checks: 28 armed, 1 NOT ARMED, 0 unmeasured. The NOT ARMED line is
  `git hook commit-msg` ("source exists, not installed"). That's deliberate: it waits until the
  history rewrite settles (CIO standing item 8s, xian's paste). The old-history guard reads as
  armed while its sentinel file exists, which is through the rewrite's 24-hour watch.
- **2026-10-15 13:2x:** 30 checks: **30 armed**, 0 NOT ARMED, 0 unmeasured (Exec's run, then CIO's). commit-msg was
  installed by xian; the 30th check was added between 10-14 and 10-15.

## Adding a mechanism

A new guard named in `mechanism-sunset-or-renew.md` gets a line here, at the highest layer the
script can reach without side effects.
