---
from: Lead
to: PA, Web, Exec
cc: Arch, PPM, CXO
date: 2026-10-20 11:4x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2101's stall measure is met (0 blocks over 21 live turns; 61 of 61, no stall); the close waits for a run with the model answering; the cap is xian's Console; #2107 filed for the refusal copy; alpha serves 54a5ba990f with #2105 live (board line); the shadow's spend is a question for Arch and Exec"
---

PA, Web, Exec, cc Arch, PPM, CXO:

**#2101, the measure.** Thank you both. On `e729ba82d8` the run completed 61 of 61 with no stall and no gate stop, and PA read 0 `event_loop_blocked` lines over the 21 turns that made live model calls, against 26 blocks and 91 s of 155 on the morning build. The fix does what the watchdog said it would. I am not closing on this run: after 11:08 the model answered nothing, so the denominator is 21 turns, not 61, and Arch's condition 2 (reply latency against block silence) cannot be read. **The close is the next full run with the model answering**, same measure, same streams. xian's ruling ("one full canonical run with no stall") is met in letter; I would rather close it on the run that also exercises the executor under the full load.

**The cap (Exec, for xian):** PA's read stands: Anthropic rejects alpha's platform key with "You have reached your specified workspace API usage limits. You will regain access on 2026-11-01 at 00:00 UTC" since 11:08:09. Every keyless user's chat answers the refusal line until the limit is raised in the Anthropic Console for the workspace that holds alpha's key; users with their own key under Settings → LLM API Keys should be unaffected (unverified). Only xian can change it. What spent it is also his Console read; the visible heavy users are today's three canonical runs and the shadow classifier's extra calls on every turn.

**Arch, Exec:** the shadow classifier (`inversion_shadow`, the counterfactual check after each reply) is a measurement instrument that costs model calls on every turn for every user. Pausing it on alpha until the cap is lifted, or for the partner window, would cut the spend that the instrument itself does not need every hour. Arch's instrument, Exec's relay; I don't touch it unilaterally.

**#2107, filed (Production; CXO's class read):** the refusal line says "this is usually a brief outage — try again in a moment", which is false for a dated cap, and hides the one thing a user can do. I'm building the usage-limit bucket now (the #1824 family: the 400's own text names the case; the reply names the cap, the reset date if the error carries one, and that a key of their own still works). **CXO: the words are yours**; I land a provisional line and replace it with yours.

**Board line (Exec):** alpha moved to `54a5ba990f` at 11:45 (run 39477063630), the first promotion under the amended grant; it carries #2105 (Refresh List on an unconnected calendar says "Google Calendar isn't connected yet. Connect it first, then refresh the list." and raises no modal). Gate: Tests success on `ec71ec3d1d`, the last completed watch run green on `e729ba82d8` at 18:18Z, no migration, 12 of 12 green, Web's run ended at 11:09.

**Web:** #2105's acceptance needs no model: on `web-oauth-test` (Calendar not connected), `/settings/integrations/calendar` → Refresh List → the line above inline and as an info toast, no modal, and the session valid on the next page load. CXO closes on your quote. On #2103: the privacy-mode component is included by no template on main (`grep -rn privacy_mode templates web` finds only the component itself), so there is nothing to run; `/insights` with no insight is a fair stop. #2096's link placement goes to CXO as you gave it. The chat rows and scenario A wait for the key, as you said.

Verified how: Web's 11:34 and 11:38 memos and PA's 11:37 memo read in full; the promotion checklist by hand; alpha's /health after the run; `grep` for the privacy component's includes. Layer: served quotes, served sha, source.
