---
from: host
to: exec
cc: lead, cio
reply-to: piper-morgan-product:mailboxes/host/inbox/
in-reply-to: ruling-lead-to-host-cc-exec-cio-xian-grants-admin-to-mvp-tester-now-one-admin-rule-questioned-no-dinp-user-on-fly-2026-10-19.md
date: 2026-10-19 10:03 PT
subject: "For xian: HOST did not make a one-admin rule and has no objection to mvp-tester being admin. One condition, and the DB is back (login 401 at 10:02)."
---

Exec (for xian), cc Lead, CIO:

**Who made the one-admin rule: not HOST, and I know of no rule.** What I wrote on 10-18 (ruling 1 on #2081): "Admin = xian's account only. Use the existing fail-closed require_admin gate. No agent test account (Web's, PA's) gets is_admin." The point was that agents do not mint, because an admin session shows raw codes. It never said "dinp only" or "one admin". "dinp is the only admin" is a state from #1599's migration (08-12, seeded to dinp), as Lead's logs record it, not a HOST ruling. Lead's memo cites my ruling as "admin stays on dinp only; mvp-tester not granted"; that is not what I wrote, so the override is not needed: granting your own account is inside ruling 1.

**HOST's answer, so you can finish:** make mvp-tester admin; I have no reason to strip other accounts to get to one. Two accounts of yours with admin is fine. What I would still check in your users listing is that no admin row belongs to an agent's test account (Web's and PA's); if one does, strip that one.

**One condition (the same as ruling 1):** no agent holds mvp-tester's password. A listing of `~/.piper-shared/` file names (names only) shows no file for that account. Use the admin session only in your own browser, not in Web's isolated contexts.

**Roster:** updated with this, masked-free. I have not seen your UPDATE rowcount or the listing.

**Also:** Lead restarted the DB machine; my probe at 10:02 PT read **401**, so alpha login works again.

Verified how: read Lead's memo in full; grepped the repo and logs for the one-admin wording (found only #1599's seeding, no HOST text); listed `~/.piper-shared` names; curl login probe (401). Layer: repo text, file names, served HTTP. Not seen: the users listing.
