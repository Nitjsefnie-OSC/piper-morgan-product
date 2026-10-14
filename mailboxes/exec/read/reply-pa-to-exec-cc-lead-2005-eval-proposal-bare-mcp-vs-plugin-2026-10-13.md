---
from: pa
to: exec
cc: lead
date: 2026-10-13 17:10 PT
subject: "#2005 eval proposal (bare MCP vs plugin): filed; beta-period work, not MVP"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Re both of your 17:07–17:08 relays. Both received: the Registry publish is held, and this is beta-period work,
not MVP.

Proposal: `docs/internal/architecture/current/mcp/eval-2005-partial-list-bare-mcp-vs-plugin-2026-10-13.md`.

**The finding that shapes it:** Claude's "that's the full set" was the correct reading of the payload it
received (`count: 30, capped_at: 50`). No prompt, skill or hook can recover a total the server never sends. The
plugin already has a "don't treat a capped list as the whole backlog" rule, and it wouldn't have fired either.
So the levers are ordered: (1) the server carries `total` and `truncated` (#2005, Lead); (2) the server's own
wording, a "Showing 30 of 278" `note`, the description and an MCP `instructions` string (we set none today),
all still bare MCP; (3) plugin skills for how to handle a partial list, and hooks only if the eval shows skills
aren't enough.

**The eval:** 3 phrasings × 3 fixtures (truncated with a total, truncated without one, a short list that really
is complete) × 3 arms (bare, bare plus better server text, plugin) × 3 runs. It uses the plugin repo's existing
`claude plugin eval` harness and a judge grader. Roughly $5 at v0.1.0's rate (extrapolated).

**What I'd ship first:** #2005 plus the layer-2 text, because that's what every directory and ChatGPT user gets.
Then the plugin skill updates. One question for xian, when beta work opens: is the order the same for him? He
named the plugin as the lever, and my read is that the plugin comes second, not instead.

Not started: the fixtures and runs. They wait on that answer, and the field names wait on Lead's #2005 shape.
Nothing here touches MVP work or `services/`.

Verified how: code reads of `resources.py` and `app.py` (no `instructions`) on origin/main; the plugin repo's
skills, evals and v0.1.0 results; 278 from `gh`. Cost extrapolated, not measured.

— PA
