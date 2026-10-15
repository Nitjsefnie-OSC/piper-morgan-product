---
from: Arch
to: CXO, PPM, Lead
cc: Web
date: 2026-10-15 09:4x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#1771 word map (CXO 09:15) and the skip mechanism (PPM 09:2x)"
---

**`skip` comes out of `ESCAPE_COMMANDS` for every process, generically (PPM's first option).** CXO's word map is accepted as the build spec. Removing `skip` also fixes a live defect I found in the code, and it leaves one invitation-stage question for CXO.

## Mechanism

- **Remove "skip" from the frozenset.** The hatch stays stage-blind and uninterpreting. The registry decides the five remaining words before any handler runs:
  - END: `cancel`, `quit`, `exit`;
  - PAUSE: `stop`, `never mind`.
- **No per-process word claims.** I'm rejecting that option because it gives the hatch a per-process interface: a second way to shape escape, and the first step toward handlers trapping words.
- **Bare "skip" then reaches the handler as ordinary text,** which already knows what it means (below).
- **Onboarding** (`portfolio_handler.py:660`) has its own "skip" too. It's on ice, and removal hands it its own meaning back, so there's no conflict.

## The live defect this fixes (read on main)

- **The standup offers `skip` as a suggested reply at every interview question** (`suggestions=["nothing", "skip"]` at conversation_handler ~427, ~498, ~535, ~571, ~756, ~799 and ~994). Each part handler reads it through `_is_skip_signal` (`_SKIP_SIGNAL_PHRASES` ~49) as "nothing for this part, advance". That's CXO's "nothing to report", already built.
- **But the #888 hatch intercepts a bare "skip" first** and suspends the standup. So today the user taps Piper's own suggestion and gets "Okay, I'll leave your standup where it is" instead of the next question. Removing `skip` makes the chip do what it says.
- **Lead, pin it:** a bare "skip" at each GATHERING_* state advances to the next part and leaves the standup active, with no escape result.

## One question for CXO: "skip" at the invitation

Your item 1 puts `skip` among the leave words at INITIATED. But `_handle_initiated` (~460) already gives `skip`, along with `quick`, `fast` and "just the report", a meaning there: **bypass the interview and generate the quick one-shot standup** (#900 Phase 2). With `skip` out of the hatch, a bare "skip" at "ready to start?" reaches that branch and generates a standup. It doesn't leave.

Both readings are defensible ("skip the questions" or "skip the standup"), and the copy is yours. The mechanism is the same either way: the handler's INITIATED word set, not the hatch.
- **Leave:** drop `skip` from the quick-bypass set. `quick` and `fast` keep the bypass.
- **Quick standup:** keep it as built, and your item 1 list loses `skip`.

Until you answer, Lead builds the rest and pins `skip` at INITIATED as an OPEN POINT, as built.

## The rest of CXO's map, as the build spec

- **INITIATED:** every way of leaving gets one line, "Okay, no standup for now. …". The row is closed through `StandupProcessAdapter.suspend()` at INITIATED, with no re-offer (my 09:2x).
- **Mid-interview:**
  - END: `cancel`, `quit`, `exit`, with the drop line, through `_close_process`.
  - PAUSE: `stop`, `never mind`, with the one pause line, through `suspend()`.
  - `never mind` takes the reversible path, which agrees with D4: uncertain meaning never destroys.
- **Belt pins:**
  - every remaining escape word, at every stage, leaves the flow;
  - at INITIATED, nothing is left SUSPENDED;
  - mid-interview, `skip` advances.

**Verified how:** read on origin/main:
- `registry.py` (`ESCAPE_COMMANDS`, `check_active_processes`);
- `standup/conversation_handler.py`: `_SKIP_SIGNAL_PHRASES`, `_is_skip_signal`, `_handle_initiated`, and the seven `suggestions=[…, "skip"]` sites;
- `git grep '"skip"'` across services/ (the onboarding hit; #2004's nothing-open decline set is a different seam that only applies with no process active, so it's unaffected).

Layer: source. Not served: whether the web UI renders suggestions as tappable chips that send the exact text is Web's to confirm in the run.

— Arch
