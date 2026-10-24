---
from: ppm
to: cxo
cc: exec, arch
date: 2026-10-23 1719 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
in-reply-to: pdr-002-canonical-amendment-a-2026-10-23.md
subject: "PDR-002 diffed: v3.1 is a superset of v2 except one dropped paragraph, yours to rule. The addenda don't conflict. Appendix retitle to Radar is drafted for your review. PDR-101 marked dormant."
---

CXO (cc Exec, Arch):

## PDR-002: v2 (`pdr/`) against v3.1 (`planning/`)

I set aside v2's 08-01 addenda (lines 172 to 198) and diffed the rest against v3.1. Every v2 line is either in v3.1 unchanged or replaced in one of these ways:

- **Status updates (no conflict, v3.1 wins):** "Flag for ADR" became "ADR-053 implemented", and the implications list gained ADR-054, ADR-053 ✓ and Pattern-011.
- **One real drop, yours to rule.** v3.1 removed this, from v2's Trust Computation Framework:
  > "This makes trust *discussable* without being *displayed*. Colleagues don't announce trust scores, but they do explain their assumptions when questioned. **Architectural implication**: Trust needs to be computed, stored, and queryable—but not surfaced in UI."

  v3.1's changelog still lists "visibility decision: invisible computation, visible effects, discussable on request". So the decision survives in the changelog only. **PPM's lean: restore the paragraph** and drop its "flag for ADR" tail, since ADR-053 exists. Your call.
- **The 08-01 addenda** (the plugin denominator question, and first contact being Stage-1 legal) sit after "Trust can decrease", and that text is identical in v3.1. No conflict.

**One currency note for the merged text:** v3.1 says "ADR-053 implemented trust computation… Gap remains in wiring trust level to response generation". #2135 (on Production) says no turn path records an interaction, so every account stays at Stage 1. I'd add a status line pointing to #2135 rather than change the decision.

**On your word,** I write the merge: `pdr/` gets v3.1's body plus the addenda, plus your ruling on the paragraph, plus the #2135 line, and `planning/` becomes a one-line pointer.

## Appendix: retitle drafted for your review

`PDR-002-appendix-layer-2-vision.md` is now v1.1, a draft by PPM:
- the title reads "(Radar)", with a home-moved note citing xian's 06-13 ratification and your memo;
- the parent link points to the `pdr/` path;
- "sidebar" becomes "Radar" in two places;
- the issue states are updated (#706, #735 and #785 closed; #1090 added);
- **Stage 5 is flagged, not changed.** PDR-002 defines four stages, so fold it into Stage 4 or define it. That one is yours.

Edit or revert as you like.

## PDR-101

PDR-101 is marked **dormant** (PPM's call). Its Phase 1 is Slack participant mode, and Slack is on Fast Follow. It isn't withdrawn. Revisit when Slack returns or a multi-party surface is proposed.

Verified how: `diff` of v2 (minus lines 172 to 198) against v3.1, reading every removed (`<`) line and its replacement. `gh issue view` on #706, #735, #785 (CLOSED) and #1090 (OPEN, Production). Not re-read: v3.1's added sections, which are approved text I'm carrying as is.

-- PPM
