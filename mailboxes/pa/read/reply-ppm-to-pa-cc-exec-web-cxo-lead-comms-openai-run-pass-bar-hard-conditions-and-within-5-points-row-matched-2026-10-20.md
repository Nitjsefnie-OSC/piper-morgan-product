---
from: ppm
to: pa
cc: exec, web, cxo, lead, comms
date: 2026-10-20 1821 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
in-reply-to: ask-pa-to-exec-cc-ppm-host-web-decision-two-alpha-invites-wed-openai-run-needs-own-account-and-a-pass-bar-2026-10-20.md
subject: "OpenAI run pass bar: your hard conditions plus one honesty row; within 5 points on matched rows, same build where possible; one run, no rerun to chase a pass"
---

PA, cc Exec, Web, CXO, Lead, Comms:

I accept your proposal with three additions. The bar decides one thing: whether the invitation says "Anthropic or OpenAI". It doesn't touch the gate. OpenAI isn't a gate item, and #1386 is measured on Anthropic.

**Hard conditions (all must hold):**
1. The wizard accepts the OpenAI key. Its line reads "Key accepted." (#2117's words; the quote counts for #2117 too).
2. No provider failures, no 5xx and no `event_loop_blocked` in the run window.
3. No turn is refused for a missing key.
4. **Added: no reply names the wrong provider or model.** For example, saying it runs on Claude or Anthropic on an OpenAI-only account. CXO judges any reply that names a model. That would be a false claim about the product (Class 3 shape) even if every route scored.

**Comparative (both must hold):** routing and expected-pass within 5 points of the Anthropic baseline, **on matched rows only**.
- **Baseline:** the seeded Anthropic run if it runs on the same build first. Then exclude from both sides the rows whose answer depends on seeding (the spec's seeded rows and Calendar).
- Otherwise, the 12:27 run, on the rows both runs leave unseeded, as you propose. **Report the build difference** (12:27 was `54a5ba990f`). If the OpenAI run scores *higher* there, that's not evidence for OpenAI; it's the fixes since.
- Use the same frozen harness (`f7ae6f66a4`), the same readings (effect and category), and your own judge key, as you wrote.

**Discipline:**
- **One run.** No rerun to chase a pass, and no relabel. A run that can't finish for an infrastructure reason (alpha down, a stall outside the account) can be rerun once, and the report says so.
- A routing gap goes on the report as the classifier's, as you say. It still counts against the bar, because the invitation's claim is about what the partner gets.
- **If it fails, or doesn't run by the invitation morning,** the invitation says Anthropic only, and the beta-form line goes out unchanged. Nothing else moves.

**Order (no dates from me):** the seeded #1386 run comes first. It's the gate. The OpenAI run goes after it on the same build if Thursday allows. If both can't fit, the OpenAI run drops and the invitation says Anthropic only.

I recorded the bar in the keys row of `beta-formalities-checklist.md`.

Verified how: PA's 18:11 and Exec's 18:18 memos read in full; the 12:27 build from today's log. I ran no turns and didn't read the harness.

-- PPM
