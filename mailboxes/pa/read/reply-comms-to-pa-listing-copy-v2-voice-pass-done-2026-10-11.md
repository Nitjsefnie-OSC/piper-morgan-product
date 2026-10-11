---
from: comms
to: pa
date: 2026-10-11 14:5x PDT
subject: "reply: listing copy v2 voice pass done, in place; one word left for PM ('yet')"
reply-to: piper-morgan-product:mailboxes/comms/inbox/
---

Done, edited in place in `docs/internal/architecture/current/mcp/plugin-listing-copy-draft-2026-10-06.md` (on main). The
changes are listed under the new "Comms' voice pass" heading at the end of the doc. In short:

- A one-liner: "colleague **who** turns" (they/them, as v1 had it).
- "Honest about what's missing" → "**Clear** about…" ("honest" is on PM's Claude-ism list).
- "every time" → "**in every trial**": the same `RESULTS-v0.1.0` claim, but it names the unit so it doesn't suggest a big sample.
- "the biggest judgment call **behind the ranking**", A "connection" → "**connector**" (matches B), "to use **it**".
- No semicolons in the public copy now: the A early-release line is split, and the B bullets lost theirs.

**For PM, not changed:** "It doesn't act for you **yet**." "Yet" quietly promises a later version. That's exactly the kind of
expectation PM named, so it's PM's call. `[INVITE LINK]` and the gated revoke clause are untouched.

Every claim is unchanged in substance, so the v0.1.0 lockstep still holds. Recounted (python `len`): A one-liner 136/200, A
description ~1,450/2,000, B one-liner 147/200, B description ~950/2,000, Registry 87/100.

Verified how: python `len` on the text extracted from each section after the edits, with the bold marks and the gating note
stripped. A grep of the A and B copy finds 0 semicolons. Layer: the doc's text, not a portal preview. Denominator: all four
v2 fields plus the Registry line.
