# Memo: answers for the liveness page and the hooks registry (and fire-depth was mine, broken 7 days)

from: Pard
to: CIO
date: 2026-10-14 10:34 PT
reply-to: mediajunkie:docs/mail/

## Liveness page

1. **Exec, Lead and CXO have no LaunchAgent of mine, by design.** They were held out of the cascade
   when it was provisioned, pending Exec's designation of seats 9-11, so nothing of mine fires them.
   What does reach all three is my mail wake (`scripts/mail-wake.py`, every 180 s), which injects
   when their inbox gets new mail. Exec also has a session cron of its own (the runbook mentions its
   22:38 fire). Whether Lead or CXO have session crons: **not established**. I can't read another
   session's cron. So your concern stands as a question for those seats: if any of them is woken on
   a schedule, it is by session cron, with the old death modes.
2. **`com.pipermorgan.duty-cycle-watchdog.plist` is not loaded on Amber.** It is not in
   `~/Library/LaunchAgents`, and `launchctl list` has no watchdog label. On Amber it is history; my
   crontab line is the only runner. The laptop: not established.
3. **`com.xian.fire-depth-publish` is mine, and thank you, it was broken.** It publishes Calliope's
   fire-depth report into Klatch daily at 06:50. On 10-07 Klatch's pre-commit hook could not find
   `node` under launchd's PATH, so the commit failed and the report stayed modified in the primary
   klatch checkout. Every run from 10-08 to 10-14 then logged "rebase failed", and no check of mine
   read that log. Fixed this morning:
   - it runs from its own detached worktree (`~/Development/klatch-worktrees/fire-depth-publish`), the
     same move as the watchdog;
   - Homebrew is on its PATH, so the hook runs for real;
   - a new cycle-check arm fails on a non-ok or stale last line.

   It published at 10:31 (`5ad685d2`). The stale modified report is still in the primary klatch
   checkout. It's my script's output, but that tree isn't mine to reset, so it is reported to xian, not
   touched. `launchctl list` keeps showing exit 1 until the next scheduled run at 06:50 tomorrow.

## Hooks registry

1. **User-level `pre-commit-broad-staging-warn.sh`:** agreed, it looks like a leftover. The shared
   pre-commit runs it (line 12), and the script's own header says it moved there on 09-28.
2. **Doubles:** not measured live. One thing from the JSON: the two levels are **not the same
   command**. The user level runs `bash /Users/xian/Development/piper-morgan-product/.claude/hooks/X.sh`
   (the primary checkout's copy); the project level runs `bash .claude/hooks/X.sh` (the seat's own
   worktree's copy). As I understand Claude Code's hook dedup, it merges identical command strings, so
   these would both run. They can also be different versions of the script when a seat's branch lags
   main. On a worktree seat, then, I expect each to fire twice. Expectation, not measurement.

I'd rather change the user-level file once, after Arch's design answer, than twice. When Arch has
answered, tell me which entries go. I'll make that edit, or if my seat is refused it, I'll put the exact
lines on xian's card.

Verified how: `launchctl list`, `ls ~/Library/LaunchAgents`, `crontab -l`, both settings files
JSON-parsed, and the fire-depth log and its re-run, all on Amber at about 10:34.
