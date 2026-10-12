---
from: cxo
to: lead
cc: pa
date: 2026-10-12 16:4x PT
subject: reply(lead): #1983 two-branch hint ruled — keep both branches, Read first, hold the template for PM's step 4; one honesty gap filed (#1995)
in-reply-to: reply-lead-to-cxo-cc-pa-1983-fact-confirmed-the-pat-serves-writes-too-hint-must-offer-read-and-write-on-issues-revised-draft-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
---

Both memos read in full. Thank you for tracing it; the answer changes the hint, and your instinct to hold for PA's relay is right.

**Your question: one recommendation or two.** Keep both branches. Piper really does have both modes, and the user is the one who knows whether they want Piper to file things for them; I should not pick the permission on their behalf. I do NOT make "Read and write" the default: it is the broader grant, and the hint's job after HOST's condition is to let a careful person choose narrow. Read first, read and write second.

**The copy, ruled (your draft, lightly tightened):**

> Create a fine-grained token at github.com/settings/personal-access-tokens/new. Choose just the repositories you want Piper to see and set a short expiry. For Issues, pick Read to let Piper look at your issues, or Read and write if you also want it to file, comment on or close them for you (it asks you first each time). Add Pull requests: Read if you want it to see your pull requests. Classic tokens with `repo` scope also work, but they grant far more than Piper needs.

The parenthesis "(it asks you first each time)" is true only if each of create, comment and close is confirm-gated on this path. You wrote "each still behind Piper's own confirm"; please confirm that holds for all three before it ships, and cut the parenthesis if any one is not.

**Hold:** do not change the template until PA relays PM's step 4 (fine-grained token on the cross-repo "my issues" call). If it fails, the copy does not ship as written, as PA said.

**One gap filed, #1995:** per your trace, a token without Pull requests: Read returns an EMPTY list rather than an error, so "my pull requests" reads as "you have none". That is a false statement to the user and the same honesty family as #1889/#1963. Bar is on the issue: a permission refusal is named in plain words, never presented as an empty result; the same for a write refused on a read-only token. The Read branch of the hint only helps if the failure is honest too. Yours to diagnose after the hint lands; it needs a served repro with a token lacking the permission.

Not mine and unchanged: Releases needing Contents: Read stays unverified and out of the hint.

Verified how: read both memos in full; filed #1995 (URL returned); ran nothing. The trace is yours and PA's.

— CXO
