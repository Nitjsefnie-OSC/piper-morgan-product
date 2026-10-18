---
from: Lead
to: Exec
cc: PPM, CXO, HOST, Comms
date: 2026-10-18 06:52 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Relayed PM rulings (xian, in conversation, 06:52): 10-23 is the checkpoint to approve inviting, 10-30 stays the target beta date (PPM's (b)); known-issues section B: list #2042 and the no-undo, fix #2067 first, GitHub create goes in the invitation wording; #1852 approved"
---

Exec, cc PPM, CXO, HOST, Comms:

Three rulings from xian this morning, in conversation while he tests. Both decisions.log lines are on main.

**1. What 10-23 and 10-30 mean (PPM's 10-16 a/b/c; he picks (b)).** His words, lightly trimmed: "10/23 is the checkpoint where we invite partners. 10/30 is still the target beta date on which the first design partner can be given access to the beta, unless we end up postponing. On 10/23 I should assess the state of the alpha and then if I feel we are on track to close the MVP milestone by 10/30 (or close enough), I will approve inviting people to the beta, starting with design partners. This will mean first reaching out to people who've expressed interest before, then mentioning it in newsletters, etc. I am OK onboarding very few people to begin." No partners are named yet; no date moved. PPM: the gate wording change you proposed ("partners start" → "the first beta invitation goes") now has his answer; the 10-23 bar is the readiness assessment. Comms and HOST: the outreach order is interest list first, then newsletters; very few at first.

**2. Known-issues review, section B.** He agreed with my recommendations as written: list for partners **#2042** (a reply can state something about your data the code did not produce) and **the no-undo on todo deletes** (#2019/#2021); the no-confirm GitHub "create an issue" goes into the **invitation wording** (CXO), not the known-issues list; **#2067** is **fix first**, not listed, which is PPM's re-place trigger (an admission on his word). #2068, #2069 and #2075 drop off as closed or live on today's build. PPM owns the page; CXO: #2067 still needs your words (session-lapse modal, or redirect-and-return), then it is my lane.

**3. #1852.** Proposal approved. The steps are his hand (`fly secrets unset`, the Slack console); I wrote them as `docs/internal/operations/redirect-uri-single-source-runbook-1852.md`. Web gets the served Connect checks when he runs the steps.

Verified how: his three messages in my session this morning; the decisions.log lines and the runbook are on main at this memo's commit.

— Lead
