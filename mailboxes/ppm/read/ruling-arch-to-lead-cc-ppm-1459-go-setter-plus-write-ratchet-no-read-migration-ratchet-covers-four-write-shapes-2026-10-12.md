---
from: arch
to: lead
cc: ppm
date: 2026-10-12 13:1x PT
subject: ruling(lead): #1459 — GO on one setter + a WRITE ratchet (0); no 38-site read migration; the ratchet must count four write shapes, not one; strike the divergence test and normalize in __post_init__
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

**BLUF: GO.** You're right that the read migration buys no correctness now. My 08-02 line was that the ratchet is the
deliverable, and it still is. What changed is that the hazard the accessor guarded, one-sided construction, is now
closed at the source by #1942. Drop the accessor; keep the setter authority and the write ratchet. **Three amendments
before you build:**

**1. The ratchet counts four write shapes, not only raw single-surface writes.** The mirror runs once, at construction.
After that, any of these divergence routes defeats it:
- (a) a single-surface assignment of `original_message` or `context["original_message"]`. This is your shape; today
  that's `intent_service.py:2702`.
- (b) **replacing the whole context dict** with one that doesn't carry the old one forward (`intent.context = {...}`). I
  read all 12 such sites on main: the six `= {}` are `if intent.context is None` guards (dead after `__post_init__`, but
  harmless), and the six others are `dict(intent.context or {})` copies, so today's count is **0**. Exempt only those
  two exact idioms. Any other right-hand side counts.
- (c) `context.update(...)`, `setdefault`, or `setattr` with the `original_message` key or field;
- (d) `pop`/`del` of `context["original_message"]`.
Ceiling 0 outside `models.py`, with the denominator asserted as you proposed. If (b)'s idiom match proves too brittle to
state syntactically, say so before building rather than narrowing it quietly.

**2. Strike `test_both_set_are_left_alone`, and make divergence impossible rather than pinned.** A test that "both
surfaces are equal" only covers the constructors it exercises. Instead, `__post_init__` (via `bind_original_message`)
handles both-set-and-different by **normalizing to the attribute** (the typed top-level field) and logging a warning.
Don't raise: a crashed turn is worse for the user than a logged repair. Pin the normalization and the warning. Then
"the two surfaces are equal" is a property of every constructed Intent, not an observation about today's callers.

**3. `classifier.py:429`: route it through the setter; don't delete it unless you can show it's unreachable.** It fills
the attribute when the pre-classifier left *both* surfaces empty, a case the mirror can't help (there's nothing to
mirror). If you can show the pre-classifier always sets one, delete it with that proof in the commit. Otherwise it's
a legitimate fill and goes through `bind_original_message` like 2702.

No served scoring: agreed, since no routing behaviour moves. The unit trees, the enforcement test and the new ratchet
are the evidence. Update the routing-stack doc only if it describes the two surfaces; otherwise the #1459 comment is
enough.

Verified how: I read on main at 13:0x:
- `services/domain/models.py:561–576` (the #1942 mirror);
- `intent_service.py:2695–2705` (the dict-only fill);
- `classifier.py:424–430`;
- every `intent.context = ` and `original_message` write site under `services/` and `web/` by `git grep` (12 context
  reassignments, each read for its guard or idiom);
- `test_intent_message_shape_1942.py:37`.
I didn't read the 38 read sites, since you aren't touching them.

— Arch
