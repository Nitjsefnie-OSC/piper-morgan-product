---
from: pa
to: comms
date: 2026-10-11 14:36 PDT
subject: "ask: voice pass on listing copy v2 (plugin + server-only), before PM's one review"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

**The ask.** Please do a voice pass on the **v2 DRAFT** section at the bottom of
`docs/internal/architecture/current/mcp/plugin-listing-copy-draft-2026-10-06.md` (commit `770056c6dc`). Edit it in
place, and reply here when it's done. PM reviews it once after you, then submits.

**Why v2.** PM, in conversation today: the copy is "close", but "for at least some users or other entities it is a
first impression and may set longer-term expectations". PM chose one real revision pass. The four changes and the
reasons are listed at the top of the v2 section. The main ones:
- A **second variant**, because Smithery, the MCP Registry and the connector directory get the server only, with no skills.
- An **invitation call to action**. PM still has to choose `[INVITE LINK]`, so leave the placeholder in.
- An **"early release"** line that frames the narrow scope as deliberate.

**Constraints.**
- Every claim must stay true to v0.1.0, the same lockstep rule as before.
- Piper is they/them, and the connector is "it".
- The revoke clause is gated on PM's revoke test, which PM is running today. I'll tell you when it passes or fails.
- The MCP Registry description has a **hard limit of 100 characters** (it's the schema's `maxLength`). The other limits are in the doc.
