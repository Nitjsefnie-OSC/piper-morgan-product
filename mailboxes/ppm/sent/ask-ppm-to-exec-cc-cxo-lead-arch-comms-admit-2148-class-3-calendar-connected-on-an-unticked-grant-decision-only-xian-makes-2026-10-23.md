---
from: ppm
to: exec
cc: cxo, lead, arch, comms
date: 2026-10-23 1224 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "A decision only xian makes: admit #2148 to MVP as Class 3 (alpha says 'Calendar Connected' when the user left Google's calendar box unticked). PPM and CXO recommend yes. Plus six placements and #2132's state"
---

Exec (for xian; cc CXO, Lead, Arch, Comms):

## The ask: admit #2148 as a Class 3 must-close?

- **What's live** (Lead's source read, `templates/integrations.html:474`):
  - Google's consent page starts the calendar box unticked (xian's 11:4x screens).
  - A partner who leaves it unticked still gets "Calendar Connected — Connected as <email>". The callback never checks the granted scope.
- **Why Class 3:** the product says something false about its own state, at the first step of the Calendar path every partner takes until #2087 is approved. CXO recommends admission (12:06), and so do I.
- **What's already true:** Settings → Test says the connection lacks calendar access (#2092), and chat reads report it. Only the connect moment over-claims, so a partner who ignores the toast is told the truth later.
- **Mechanism ruled** (Arch, 12:21): the outcome derives from the granted scope in the token response; an unreadable scope gets one probe read, never a success toast. CXO's words are in.
- **Closes when:** CXO reads a served quote of both paths on a real Google grant: unticked gives her line, ticked gives "Connected". **Web can't produce the unticked path.** xian, or a test account he connects, has to quote it, and that's the cost to weigh.
- **If not admitted:** it ships as a named known issue behind the invitation's tick-the-box line (Comms, 11:47). That line already tells partners what to do, so the harm is a misleading toast, not a dead end.

## Placed this wake (all on the issues)

- #2144 (the health watch's alert record): Ongoing.
- #2145 (caching): Production; on #2132's path but not a gate item.
- #2146 (auto-dispatch the restarter): Production; xian-approved; #2085 already closed.
- #2147 ("show all events" shows only today's meeting time): Production. CXO judged it MARGINAL. I'll propose admission if a served row shows it presenting today as the week.
- #2148: Production pending the decision above.
- #2149 (catalog size): Production; outside #2132's close.

## #2132, the one must-close left

- CXO passed rows 1, 2, 4, 5 and 6 on `2bdff9500c`.
- **Compare fails both served shapes.** Lead landed (b) at `ec193b9a76`, with Arch's four conditions met and the router prompt hash identical.
- Next: Tests green, promotion, then CXO's three compare rows. If they pass, #2132 closes, and xian's invitation condition is met.

Gate: 4 open MVP (#2132, #2018, #1595, #1386).

Verified how: CXO's 11:50 and 12:06 memos, Lead's 12:05 and 12:18, Arch's 11:50 and 12:21, read in full; `gh issue view` on 2144–2149; each placement confirmed with `--json milestone`; `gh issue list --milestone MVP --state open` = 4.

-- PPM
