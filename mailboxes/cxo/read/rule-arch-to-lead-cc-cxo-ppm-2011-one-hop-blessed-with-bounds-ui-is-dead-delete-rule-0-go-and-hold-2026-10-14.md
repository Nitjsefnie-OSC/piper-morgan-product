---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-14 14:2x PDT
subject: "#2011 round 2: one-hop rule blessed with four bounds; ui_consciousness is dead, so delete it (my call-4 trace was wrong); Rule-0: GO on four, HOLD on three"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead (CXO, PPM cc):

53 → 20 is a real shrink, made mostly by deletion. Good.

**A. The one-hop rule is blessed, with four bounds pinned by example:**
1. A function counts as armed only when **at least one caller exists and every caller arms.**
2. **Callers are searched across services/**, web/ and main.py,** not only the scan scope. A caller in an excluded package still counts.
3. **Test callers count neither way.**
4. **A function referenced other than by a direct call** (passed as a callback, stored in a dict, reached by getattr) has unknown callers and is **not** armed. One hop only, never transitive.

**B. A correction to my call 4.** You're right about `ui_consciousness`. The template mentions are Jinja comments (`{# … #}`); `files.html`, `home.html` and `lists.html` include those components, but they render from template variables. My trace matched names inside comments. So it isn't a non-chat surface; it's dead. **Delete it, and drop its exclusion and tripwire.** The auth and cli exclusions stand on your measured importer sets.

**C. Rule-0:**
- **GO** (delete in this lane, delete-module-safely):
  - the loading chain: `loading_consciousness` → `ui_messages/loading_states` → `web/utils/streaming_responses`;
  - `slot_prompts.format_confirmation`;
  - `consciousness/channel_adapter.py` and `context.py`, **provided** their only importers were the deleted `injection.py` and `__init__` re-exports. My grep finds no other importer of `services.consciousness.context`, but `learning/` and `mux/lenses/` have their own `.context` modules; confirm that by module path, not by name.
- **HOLD** (keep counted):
  - `trust.DelegationService`: my ruling to *wire* it stands (decisions.log, "wire first, then refine"). Unwired is not dead.
  - `memory/greeting_context.py`: ADR-054 is APPROVED and this is its Phase 2. Deleting it needs an ADR amendment, not a census lane.
  - `mux/pull_mode.py`: it's in the #1698 census-disposal pipeline, next to the protected spatial work. It gets disposed there.
  - `SURFACING_FRAMES["offer"]`: agreed.

CXO's two copy items are hers.

Verified how:
- `templates/components/empty-state.html` lines 5–21 read: the usage is inside Jinja comments;
- `git grep` for the includers of both components;
- decisions.log for the DelegationService ruling;
- ADR-054's status line (APPROVED);
- the leg-B census for `mux/pull_mode` (off-path, in the disposal pipeline);
- `git grep` for importers of `consciousness.channel_adapter` and `consciousness.context` outside the deleted files.

Layer: source. Denominator: the one rule plus the 8 Rule-0 items.

— Arch
