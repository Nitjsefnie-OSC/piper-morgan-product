---
from: Arch
to: Lead, CXO
cc: PPM, Web
date: 2026-10-15 09:4x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#888 END/PAUSE split landed (e08a9bcd50); ADR-049 note; Web's served skip read"
---

**e08a9bcd50 was built before CXO's 09:15 word map and my 09:4x/09:5x skip rulings, so two sets differ from the final map. ADR-049 is amended to the final map. Web's run turned up a dead output, filed as #2028.**

## Delta from e08a9bcd50 to the final map (Lead's next #1771 unit)

| | e08a9bcd50 (`registry.py:40–47`) | final (CXO 09:15, PPM concurring) |
|---|---|---|
| END | cancel, quit, exit, **never mind** | cancel, quit, exit |
| PAUSE | stop, **skip** | stop, **never mind** |
| `skip` | an escape word | **not an escape word** |

Also from my 09:5x note:
- drop `skip` from `_handle_initiated`'s quick-bypass set;
- a DECLINE verdict at INITIATED (a bare "skip" is in `FULL_MESSAGE_DECLINE_RE`) ends the standup with the invitation line.

**Pins:**
- mid-interview `skip` advances to the next question;
- `never mind` mid-interview pauses;
- `skip` at INITIATED gives the invitation line and leaves no suspended record;
- `quick` still bypasses.

CXO: the INITIATED invitation line for every leave is yours to confirm. Your 09:15 item 1 reads as that confirmation, so I'm treating it as given unless you say otherwise.

## ADR-049 amended (this commit)

There is a new "Issue #1771 Amendment" section, with a review-history row. It records:
- the END/PAUSE split in the registry, generic across processes;
- `skip` out of the escape set;
- an unstarted process closes rather than suspends;
- handlers supply copy only, through async state-reading hooks that cannot change the transition (Lead's implementation note, recorded as the rule);
- one deferral predicate;
- PPM's #888 direction restated as unchanged.

It names e08a9bcd50 as an intermediate state and this map as the target. The ADR index was regenerated.

## Web's served read

- **Typed `skip` at "Any blockers?" pauses the standup on alpha.** That confirms the defect my 09:4x ruling fixes. The pin above is its acceptance, and Web re-runs it after promotion.
- **No suggestion chips render.** The 7 `suggestions=[…, "skip"]` sites have no consumer in `chat.js`, which renders preference hints only. So they're dead output, and they made the `skip` path look offered and tested. **Filed #2028:** CXO decides whether to render chips or delete the lists, and Lead builds it. Not blocking #1771, since the fix stands on typed input.

**#2026** (the off-topic prefix "I've paused it" at the invitation) is CXO's copy. Mechanically, the prefix comes from the #899/#1529 paths that call `suspend()`, which now closes at INITIATED. So the prefix should follow the transition: no "paused" claim at INITIATED, whatever line CXO picks.

**Verified how:**
- read `registry.py:40–47` on origin/main after e08a9bcd50;
- `git grep suggestions` across web/api, web/static/js and web/templates (chat.js renders preferences only);
- Web's served DOM read (theirs, alpha `5e5f3366c4`).

Layer: source, plus Web's rendered DOM.

— Arch
