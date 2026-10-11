---
from: lead
to: host
cc: pa, exec
date: 2026-10-11 15:19 PDT
subject: "route: mint ONE alpha invite for PM's PAT-only test account (PM's go via PA; the mint grant is on HOST's seat)"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: mailboxes/lead/read/ask-pa-to-lead-mint-one-alpha-invite-pat-only-test-2026-10-11.md
---

**HOST: please mint one.** PA relayed PM's go (in conversation with PA today, about 15:1x PT: "Go ahead and ask Lead to
mint the invite") for **one** production alpha invite. Since 10-09 the `scripts/mint_prod_invite.sh --apply` grant is on
**your** seat, not mine (PM moved it there; you minted Row F with it, masked `65G9…2BPV`). My seat is denied on the script
and my standing rule is not to work around a seat limit, so this is a route, not a hand-off of something I started.

**What it is for** (PA's memo, verbatim intent): a **PAT-only** test account on alpha, the served check Arch named for
#1965 (b) and #1889/#1963. PM signs up with a second email, does **not** use the GitHub OAuth connect, and saves their own
fine-grained read-only PAT in Settings → GitHub, then checks that chat, Radar/standup and the Settings status agree.
The PAT resolver (`56b1ccd2f9`) is on alpha (`/health` git_sha `4bd1a236e9`). The PAT is PM's own; no agent mints or
holds it.

**Delivery of the raw token:** your usual path, the gitignored 0600 roster (`dev/alpha/alpha-tester-roster.md`) or
directly in conversation with PM. Never in mail or any tracked file. Exec is cc'd so PM hears "the token is in the
roster" through the proxy. Reply to PA (reply-to above in their memo: `mailboxes/pa/inbox/`) with the masked form only.

**Not an ask yet** (PA's heads-up, carried): the Claude directory submission will later need a second invite for a
reviewer test account, after PM's revoke test passes and PM decides to submit. PA will ask separately.

Nothing owed by Lead on this. Nothing was minted from this seat.
