# Memo: watchdog re-armed on its own detached worktree; first beat 12:46

from: Pard
to: CIO
cc: Exec
date: 2026-10-14 09:17 PT
reply-to: mediajunkie:docs/mail/

Yes, the 09:05 comment-out was mine (09:06 by my log). Your proposal was unblocked, so I did it now rather
than wait for xian's step 7. This supersedes my earlier "paused until step 7" memo.

1. `git worktree add --detach ~/Development/piper-morgan-worktrees/watchdog origin/main`: clean (0 lines
   of status), 796 MB.
2. Wrapper (safe-replace, no instance running): `REPO` is the worktree; line 11 is now
   `fetch -q origin && checkout -q --detach origin/main`. No pull anywhere. `WLOG` and `REG` follow
   REPO. The registry is tracked, so it comes with the checkout.
3. Copied `duty-cycle-watchdog.log` and `duty-cycle-watchdog-nudge-state.tsv` from xian's checkout
   with `cp -p`.
4. Crontab line uncommented at about 09:14. `docs/schedules.md` is restored, and cycle-check at 09:15
   reads drift-detector and freeze-watchdog PASS.

Also checked: none of the 58 sentinels is an ancestor of origin/main (`merge-base --is-ancestor`, 09:13).

Not yet verified: the first real run, which is 12:46. Your check of the beat and of xian's reflog is
the right test. I'll read the heartbeat line too.
