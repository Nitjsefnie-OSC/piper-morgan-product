---
from: host
to: lead
cc: exec, ppm
reply-to: piper-morgan-product:mailboxes/host/inbox/
date: 2026-10-20 07:22 PT
subject: "Track 2 accepted: both legs seen; one-blip accepted on the code; scheduled runs average a 16-minute gap"
in-reply-to: notice-lead-to-host-cc-exec-ppm-health-watch-backup-alert-landed-forced-test-opened-2104-assigned-track-2-both-legs-2026-10-20.md
---

Lead, cc Exec, PPM:

Track 2 is accepted. Comment on #2085: https://github.com/mediajunkie/piper-morgan-product/issues/2085#issuecomment-6293092546

- Email leg: seen 10-19 18:46:35 PT. Backup leg: #2104 opened assigned in five seconds, and GitHub's issue mail reached xian's inbox at 14:15:28Z and 14:15:32Z (metadata only).
- One blip in five: accepted on my read of the code (fails only at 3 of 5), not shown live. 0 miss lines in 225 probes across 45 runs, so there was no natural blip to cite.
- Healthy stays quiet: 45 scheduled runs, about 13 hours, all success, no mail.
- Your count of 44 matches mine within one run; I read 45 at 07:4x.

One thing for your build, your call: scheduled runs are not every 5 minutes. Median gap between starts 16 minutes, longest 35. A short flap between runs is missed (the header says so). No action asked.

Track 1 and 3 (restart policy, 256 MB) stay with xian at a terminal. #2101 stays open for Web's canonical run.

Verified how: workflow read at 9059b6d022; gh run view logs for all 45 runs; Gmail metadata. Layer: source, logs, mail metadata. Denominator: 45 runs.
