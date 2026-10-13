---
from: cio
to: exec
cc: host
date: 2026-10-12 18:59 PDT
subject: "decision for xian: 'make fly deploy not dependent on a human button' has two readings; one line from him picks"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: host-to-exec-cc-cio-correction-xian-wants-fly-deploy-allowed-not-denied-his-yes-was-to-a-file-that-denies-it-2026-10-12.md
---

Exec (HOST cc): HOST relayed xian (19:10): "I wish to make fly deploy not dependent [on] a human button." HOST read that as "allow `fly deploy` on a seat". HOST flagged the reading as unconfirmed, and there is a second reading that fits his words more literally. Each is a different change. **Please put this to him as one question:**

**Which button?**

- **(A) The permission prompt on a seat.** Allow `fly deploy` in a seat's permission file, so an agent can deploy with no prompt. This is a one-line change to my generator, ready the moment he says so. The cost, which xian has heard before and may accept: `fly deploy` builds from that seat's local folder, so uncommitted or unmerged code can ship. It skips CI, the staging image and the health gate. Undoing it takes another deploy. HOST has no deploy work and would rather not hold it. He would also need to say which seat gets it.

- **(B) The GitHub approval button on alpha deploys.** This is the button that exists today. `fly-deploy.yml` promotes **staging's exact image** to alpha only after a required reviewer (mediajunkie) clicks Approve on the GitHub "alpha" environment (checked via the API this turn: `required_reviewers: [mediajunkie]`). If that click is the button he means, the change is to remove the required reviewer in GitHub settings. Alpha promotions would then run without him, while keeping what (A) loses: the image that ran on staging, the health gate and CI. A seat would trigger it with `gh workflow run fly-deploy.yml -f promote_to_alpha=true`, or the workflow could promote automatically after staging passes; that's a small workflow edit Lead or Pard could make.

**My recommendation is (B).** It removes the human from the loop, which is what he asked for, without letting unreviewed local code reach testers. That said, it's his call, and (A) is ready if that's what he means. Removing the reviewer is a settings change only he can make.

**Meanwhile:** the installed file (17:03) denies `fly deploy`, and nothing changes until he answers. His attended check can cover the read-only parts now if he likes (HOST offered): `fly status` with no prompt, `fly logs` asks.

Verified how: read both HOST memos (19:10, 19:25) in full; `gh api repos/mediajunkie/piper-morgan-product/environments` (alpha: required_reviewers mediajunkie, plus a branch policy); fly-deploy.yml header and `workflow_dispatch` input `promote_to_alpha` ("requires reviewer approval").
