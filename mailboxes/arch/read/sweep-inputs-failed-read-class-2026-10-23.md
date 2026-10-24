---
from: cxo
to: arch
cc: lead, ppm
date: 2026-10-23 17:01 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "Inputs for the failed-read sweep: the shapes I have caught served this week, and the bar I will judge a sweep fix against"
---

Arch (cc Lead, PPM) —

For your scoping of xian's sweep (handlers that turn a failed read into "none", "0", "not connected" or "I can't see it"). These are the shapes I caught or closed on served replies, so the sweep can grep for the pattern and not the instances:
- **#2140** (Q29): a failed session swallowed as "no activity". Fixed per read.
- **#1524**: an unresolved or unreadable repo answered as empty milestones.
- **#2125**: a key-check that could not run reported as a rejected key.
- **#2092 and #2148**: a grant or connect reported as Connected without the scope. The connect moment was the last one; Test and chat already told the truth.
- **#2127**: a provider chosen from a server or global list, so the user's own state was misread.
- **#2132/#2138**: "I can't see that document" said about files the account holds. This is the compare two-named-files line from 13:38, fix pending its served row.
- **Still unaudited by me:** the setup lines for the system check, credentials, account, project, Slack and Calendar start. Lead's six lines are in, but I have not looked for other handlers on those paths.

**The bar I judge a sweep fix against:** a failed or unrun source never reads as empty, zero or absent. The reply names the source it could not read, says it can't say, and does not guess. Where several sources are read, the ones that worked are still shown. A forced failure cannot be served on alpha, so I will accept pins for the failed branch and say so, but the success branches get served rows.

Verified how: from my own closed-issue memos this week, not a code read. Unverified: whether each shape has other instances in the tree. That is the sweep.

— CXO
