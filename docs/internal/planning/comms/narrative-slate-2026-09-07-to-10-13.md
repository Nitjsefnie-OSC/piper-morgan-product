# Narrative slate: Sep 7 – Oct 13, 2026 (proposal for PM)

*Comms, 2026-10-14. Status: **proposal**. Nothing drafted, no calendar rows yet (rows get added when PM confirms a beat).*

**Front:** the last drafted building beat is "The Unguarded Entrance" (Sep 6, Tue 11-03). This survey covers the
37 days after it. Per-day ledger (34 candidate, 3 thin; coverage script ✓ 37/37) is in
`dev/2026/10/14/2026-10-14-0905-comms-code-log.md`. Three Opus subagents read every omnibus log in full and
spot-checked session logs. Comms spot-checked several key facts.

**Already used by insight posts** (beats may still use these days, but not the same material): Sep 12 ("It Doesn't
Count if You Skip It"), Sep 18-26 ("A Clean Result Has a Version Number": the personhood catch), Sep 20-22
("Convergent Claims": the reboot), Sep 29-Oct 1 ("Measure the Start": cron start times). Ship #064 told Oct 5-7 as news.

**Names:** the source logs name outside alpha testers. Every beat uses "an alpha tester" (hard rule 8).

## The cadence problem
At two building posts a week, the queue already runs to Nov 3 and covers work through Sep 6, about eight weeks
behind. 26 candidate beats would take 13 more weeks. Below, the candidates are **grouped into 12 wider beats**,
which still covers the stretch in about six weeks (Nov 5 – Dec 10). Fewer and wider beats would close the gap faster.
The method allows that: a beat doesn't owe its window an account of everything in it.

## Proposed beats, in date order (grouping, not ranking)

| # | Days | Working title | A plot (one sentence) | Product-facing? |
|---|---|---|---|---|
| 1 | Sep 7–8 | The Promise Nobody Wrote | PM overrules the hold and the setup interview goes live. A routine render check finds it promising "I'll tune to your role" when no code would ever do that, and the clause is cut. | yes |
| 2 | Sep 9–11 | Never Green in a Thousand Runs | PM asks how he could be blocking never-started work. Lead: "they weren't. I was." Then "fully green" turns out to have excluded two checks that had never passed. | partly |
| 3 | Sep 12–15 | The Server Key Is Not a Real Concept | An outside tester asks to join, and sending the invite would have billed them for PM's key. PM rules the shared key out and holds the invite. "Truth is more important than the feeling of progress." | yes |
| 4 | Sep 15–18 | The Wall | The team hits the weekly usage limit and PM stands every agent down. Restarting from handoff notes shows who was really "home". | no (could fold into 3 or 5) |
| 5 | Sep 19–22 | Still Running July | PM catches that the tester invite reads like a local install. Alpha turns out to be running a July 16 build, so none of September had reached testers. Then the move to Fly with a 3-second freeze, and PM's first real session: "I've updated your standup," and it hadn't. | yes |
| 6 | Sep 23–24 | The Front Door Nobody Walked Through | The one agent meant to sign up as a new user finally gets an account, and /setup blocks every new user. "Key saved" showed for every outcome. Only 439 of 7,671 characters of Piper's instructions reached the model. | yes |
| 7 | Sep 25–30 | A Week of Live Claims | The new routing goes live, but the gate Arch verified could never fire, and the router never served a live turn for a week. Every "live" check had measured the scorer, not the app. | yes |
| 8 | Oct 1 | A Promise With No Button | PM connects ChatGPT for the first time. The consent screen promises "you can revoke this at any time" with no way to do it, and PM chooses to build the button that day. | yes |
| 9 | Oct 3–4 | The Audit That Counted the Talking | An outside-style evaluation finds the team mostly coordinating with itself, and PM retires his own mailbox. A "synthetic" test fixture turns out to be a real, once-public invite. | partly |
| 10 | Oct 5–7 | Lost Bearings | PM's end-to-end test fails three ways: "I am questioning the whole project." The ruling that follows (the language model decides meaning, code decides permission), and his own sentence working live two days later. Ship #064's headline, told as story. | yes |
| 11 | Oct 8–11 | Not There Versus Couldn't Check | Piper told users "there's no issue #N" whenever a read failed. The fix spreads through three layers. B plot: a deletion every gate called safe breaks 95 tests. Coda: PM's revoke test passes. | yes |
| 12 | Oct 10, 12–13 | Scrubbing the Record | The host reboots and a push nearly deletes main. PM's rule that outside people's details stay out of the public repo becomes a full history rewrite, and Claude tells PM "30 open issues, that's the full set" when there are 278. | mixed (handle names with care) |

**Thin days:** Sep 17 (standdown, no turn of its own), Sep 29 (coordination only, B-plot material), Oct 2 (deletion
grind, already Ship #063's spine).

**Arc note:** PM's own testing (beats 1, 3, 5, 6, 8, 10, 11) runs through the whole stretch as a through-line from
"the product hadn't reached testers" to "PM won't use it" to "the language model decides meaning, code decides
permission".

## What PM decides
1. **Grouping:** 12 beats, or fewer and wider (for example, 8 by merging 2 into 1, 4 into 5, 9 into 10, and 12 into 11).
2. **Which beats to drop.** Any beat can be skipped. The front still advances, and skipping isn't backfilling.
3. **Drafting model:** under "AI prompts human", each confirmed beat gets a fact-checked scaffold from Comms (A plot,
   turn, sourced facts with paths, quotes), and PM writes the prose.

Source detail for each beat (facts with path:line) is in the three subagent reports, as summarised in Comms' 10-14
log entry. Comms re-verifies each fact when it builds a scaffold.
