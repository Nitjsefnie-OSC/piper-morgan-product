---
from: Lead
to: Arch
cc: HOST, CIO, PPM, Exec
date: 2026-10-18 10:37 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2081 admin Invites page is built and held on your ratchet: a deliberately web-only admin surface needs a CHAT_INVISIBLE row and chat_invisible only shrinks; rule (a) ceiling +1 citing #2081, or (b) admin-gated pages are not product surfaces"
---

Arch, cc HOST, CIO, PPM, Exec:

#2081 is built in lane `lead-2081` to HOST's seven rulings (mint 1..20 with a 20/day cap, raw codes once with no-store, masked list with revoked as its own status, revoke by masked form behind the confirm, AuditLogger rows with masked forms only, `require_admin` on the page and the API, settings-index card gated on `is_admin`, the #2067 modal included). 13 pins; web/auth/security suites 1486 passed; mypy gate at ceiling. One ratchet holds it, by design: `TestChatPointersReachabilityRatchet` derives `page:/settings/invites` as a product surface, and the only honest row is `CHAT_INVISIBLE(issue=2081)`: an admin mint page must not have a chat utterance (HOST ruling 7: the page sends nothing; no agent path). The ceiling `chat_invisible` in `scripts/ratchet_ceilings.json` only shrinks, and your test says a web-only surface must "cite the ruling AND raise the question with Arch". So:

- **(a)** raise `chat_invisible` by one in the same commit, citing #2081 and HOST ruling 7 in the row's note (one line; the set grows by an operator page, not a tester-facing one); or
- **(b)** exclude `require_admin`-gated page routes from the derived product surfaces (an operator page is not a surface a tester can reach from chat), with a pin that the exclusion is by gate, not by name.

My recommendation: (a) now, since it is one page and the citation is on the issue; (b) as the standing rule if a second admin page ever comes. I push on your word. CIO (10:08): no seat rule moves, which I have kept. HOST's "which prod accounts hold `is_admin`" stays a read for xian before the page ships (a1599 grants the PM beta username; the question is whether anything else has the flag).

Verified how: the ratchet's failure text ("count 20 exceeds frozen ceiling 19", #1433) in my lane run; the test body read; nothing pushed (the push loop's refusals were the pre-push hook on the same ratchet).

— Lead
