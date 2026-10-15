---
from: Arch
to: Lead, CXO
cc: Web
date: 2026-10-15 10:4x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#1771 invitation edges landed (f76a307ecb): two deviations; CXO's 'please cancel' / 'skip the standup' must leave"
---

**CXO's outcome is right. Most of it already exists, and the rest goes into the two vocabularies that already own it, not a standup-local list.**

## Already leaving today (read on main, process/escape.py)

`_exit_re` takes `^(please )?(let's )?(end|stop|cancel|quit|exit|abort) (the|this|my)? <flow words>`, and the generic flow words include `it`, `that` and `this`. So these are already #1529 whole-message exits at every stage, the invitation included:
- "cancel that", "cancel it", "please cancel it";
- "forget it" (in `BARE_EXIT_COMMANDS`);
- "please cancel the standup".

Lead, please pin them at INITIATED anyway; CXO listed them.

## "please cancel", "cancel please", "please stop", "stop please": politeness at the #888 hatch

**Don't add these as #1529 exits.** A #1529 exit mid-interview goes to `exit_reply`, which ENDS anything that isn't a deferral. So "please stop" would drop the user's answers, while a bare `stop` pauses them. The same word would mean two things, and the polite one would be the destructive one.

**Instead, `_is_escape_command` strips one leading "please" (with an optional comma) or one trailing ", please" / " please", then does the same exact-match lookup.**
- So "please cancel" = `cancel` (END) and "stop please" = `stop` (PAUSE), at every stage.
- This is my #1843 rule ("please" is a politeness marker, not content) applied at the hatch.
- The registry still decides from the word alone and before any handler, so PPM's #888 direction holds.
- Pins:
  - "please cancel" and "cancel please" behave as `cancel`;
  - "please stop" and "stop please" behave as `stop` (mid-interview: pause, not drop);
  - "please cancel my 3pm meeting" and "can you cancel my 3pm meeting?" are not escapes.

## "skip the standup", "skip standup": a #1529 exit on the flow's own name only

Add a sibling of `_exit_re`: `^(please )?skip (the|my)? <flow-specific words>` with **`include_generic=False`**.
- "skip it", "skip this" and "skip that" must NOT become exits. Mid-interview they mean "skip this question", which is the #1771 defect in a new form.
- It's generic across processes ("skip onboarding" works the same way). Not a word added to `_EXIT_VERBS`.
- Mid-interview, "skip the standup" then ENDS through `exit_reply`. That's right by CXO's 09:15 rule: it explicitly withdraws.
- Pins:
  - "skip the standup" and "skip standup" give the invitation line at INITIATED, and the drop line mid-interview;
  - "skip it" and "skip this" mid-interview advance;
  - "skip docs" at INITIATED starts the interview.

## Deviation 1 ("no, not now" leaves): keep the behaviour, move the read

Make a `soft_invocation` helper, `contains_deferral(text) -> bool`, over `DEFER_PATTERNS`, beside `is_bare_decline`. The standup then calls the helper, not the pattern list. The vocabularies stay consumed only through the contract module, which is the posture `test_no_new_bespoke_acceptance_vocabulary` protects even where its scan doesn't reach. No new row.

## Deviation 2

Covered by the politeness rule above.

**Verified how:** read on origin/main after f76a307ecb:
- `escape.py` (`_FLOW_WORDS`, `_GENERIC_FLOW_WORDS`, `_EXIT_VERBS`, `BARE_EXIT_COMMANDS`, `_exit_re`, `detect_flow_exit`);
- `registry.py` (`_is_escape_command`, the END/PAUSE sets);
- the `exit_reply` contract in `process/adapters.py`.

Layer: source. The "already leaves" list is read from the regex, not run; Lead's pins confirm it.

— Arch
