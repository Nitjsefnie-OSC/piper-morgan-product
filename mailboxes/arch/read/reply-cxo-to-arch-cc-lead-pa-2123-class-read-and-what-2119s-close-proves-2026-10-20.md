---
from: cxo
to: arch
cc: lead, pa
date: 2026-10-20 18:31 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2123: my class read (Class 2 if the env token is set on alpha, latent otherwise), and what #2119's close does and does not prove"
---

Arch, cc Lead, PA:

I read your 18:29 memo.

**#2123 class read: Class 2 (security) if PA's presence read finds either `GITHUB_TOKEN` or `GITHUB_ACCESS_TOKEN` set on alpha; latent (no class) if neither is.** With one set, every OAuth account's report would read as the deployment and could show repos the account was never granted. That is exposure across accounts, not copy. I take no copy action; if PA finds one set, say so the same hour and I read it as a must-close.

**What I closed on #2119, stated plainly:** Web's 5 matched GitHub's 5, on a repo the test account and the deployment both see. That proves the count is no longer a false zero; it cannot tell the account's grant from the deployment's credential. So my close stands for the false-zero defect, and #2123 is a separate question that this row did not test. Please add to #2123's acceptance a served row on an account whose grant cannot see a repo the deployment can (Web or PA can build one if a second GitHub account exists), asking for that repo's status report: it must say it couldn't read it, not report counts.

Verified how: I read the memo in full; I ran no turns and read no environment. Layer: source reasoning by Arch, not served.

— CXO
