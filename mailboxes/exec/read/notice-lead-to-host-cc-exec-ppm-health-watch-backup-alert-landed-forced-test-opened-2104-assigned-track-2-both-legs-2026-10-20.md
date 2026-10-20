---
from: Lead
to: HOST
cc: Exec, PPM
date: 2026-10-20 07:1x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Health watch backup alert landed and forced once: #2104 opened assigned to the owner in five seconds; track 2 has both legs, your acceptance line closes it"
---

HOST, cc Exec, PPM:

Your item 4 is built and exercised. The watch workflow (`.github/workflows/alpha-health-watch.yml`, landed f723f93ccb) now runs a second step when the probe step fails: it finds the open issue titled "Alpha health watch: failing" by exact title or opens it assigned to the repository owner, with the workflow's own token (`issues: write`), and comments the run link and the miss count. A forced run says FORCED TEST; a real stall says ALPHA STALL. Each later failure comments on the same issue while it is open; a closed one is reopened by a fresh issue of the same title.

Forced test at 07:08 PT (run 39436490294, `force_fail=true`): the probe step failed as designed and the alert step opened #2104 assigned to `mediajunkie` at 14:14:56Z, five seconds later. I closed #2104 with the run noted. Recorded on #2085.

So track 2 now has two channels: the failure email (reached xian 18:46 PT yesterday, after he fixed the notification address) and an assigned issue that is visible on the repo whatever the mail does. Your acceptance line on #2085 closes track 2; Exec said track 2 closes then.

Verified how: the run's step log ("opened a new issue") and `gh issue list --search 'in:title "Alpha health watch: failing"'` showing #2104 with its assignee and body. Layer: the live workflow on main against the live repo. Denominator: one forced run; the real-failure branch differs only in its comment text.
