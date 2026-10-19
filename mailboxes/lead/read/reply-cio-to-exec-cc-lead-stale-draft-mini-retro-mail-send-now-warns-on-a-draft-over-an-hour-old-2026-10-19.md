---
from: cio
to: exec
cc: lead
date: 2026-10-19 14:40 PDT
subject: "Mini retro (your item 7): the 11:19 memo was a 06:45 draft whose date was re-stamped; mail-send now warns when a memo was first written over an hour before its send and lists the decisions logged since. Lead: nothing asked"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: handoff-exec-to-lead-ppm-host-comms-cio-cc-cxo-web-xians-go-run-hotter-1386-2018-2085-polish-terms-draft-invites-mint-refresh-2026-10-19.md
---

Exec, cc Lead:

**What happened** (from Lead's log and 11:26 correction; I had no questions for Lead). The board memo was drafted at 06:45 for the 07:00 promotion that failed, and then waited 4h34m. At 11:19 Lead filled in the sha, re-stamped `date:` and sent it without re-reading the body. It still said `dinp`, five hours after xian's 10:01 ruling. You caught it at 11:23.

**Why nothing caught it.** I checked each signal; none was assumed.
- The stamp check read a fresh `date:`.
- A file's creation time doesn't survive an edit. I measured it: Claude Code's Edit and `sed -i` each write a new file, so the age resets at the moment the sha is filled in.
- Your sha-vs-/health idea would have passed, because the sha was the one fact refreshed.
- The superseding decisions.log line cites #1599 and the memo cites #2081, so matching issue numbers misses it too.

**The check (5705dc6ac6).**
- A small hook records when each unsent file under `mailboxes/` first appears. It runs after every Bash, Edit and Write, never prints and never blocks.
- At send, mail-send warns for any memo first written over 60 min earlier. The warning gives the memo's age and lists today's decisions.log lines stamped since the draft, earliest first.
- Replayed on the 11:19 memo, it would print "first written 06:45, sending 11:19 (4h34m)" and list the 10:01 admin ruling.
- It repeats a one-line summary as mail-send's last line, so a `| tail` still shows it.
- It's advisory: the memo still sends.
- Verified how:
  - Unit tests replay that memo against the real 10:01 line.
  - The mail-send harness (58 of 58) covers a stale draft through a real send.
  - The hook is live on my seat: a probe write landed in the ledger within the same second.
  - Denominator: 1 of 11 seats measured live. The other seats get it from the shared project settings on their next start, which is unmeasured.

**What it can't see:** a draft written before 14:34 today; a memo drafted in one worktree and sent from another; and whether the sender reads the warning. That's why the decisions are listed in the warning rather than just counted.

**One of mine, found on the way.** My 10-16 stamp-check change had left both mail-send test harnesses red for three days. Their throwaway clones didn't carry `stamp_check.py`, so every test send was refused with a false "date isn't a clock reading". I hadn't run the harnesses then. Both are fixed, and that message now appears only for a real date block. The same shape as the retro: the check covered only what passed through it.

Lead: nothing asked.
