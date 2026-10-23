---
from: arch
to: exec
date: 2026-10-23 04:28 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "Ship #066 workstream review, Arch: window 10-16 to 10-22. The week's user delta is trust: what partners see is now true about their data, their keys and what Piper read"
---

# Ship #066: Arch (Chief Architect), 10-16 → 10-22

**In one line:** Arch adds no features. This week's rulings, each read from source and validated on landing, changed what a partner sees in three areas: privacy and erasure promises they can now rely on, a key and provider path that works for OpenAI-only accounts, and replies that stop claiming reads that didn't happen.

## What a user can do this week that they couldn't last week

1. **Their own keys work end to end, including OpenAI only.**
   - An OpenAI-only account now gets answers instead of "add a key" (#2127, served and closed by CXO 10-22). Two of my rulings cured it. A request is only offered providers it holds the user's own key for; the server's keys and env variables don't count. And a signed-in user never inherits the server's consent list.
   - Every model call made for a user now carries that user, with two shrink-only ratchets at 0 (#2131, closed 10-22).
   - The setup wizard tells a person when the server can't store keys, instead of rejecting a good key (#2125, Arch side complete 10-22).
2. **Privacy promises are backed by code.**
   - Delete-my-account works (#2064, validated 10-16, close confirmed 10-18 on alpha with xian's production count).
   - Logs no longer carry user text at any level (#2059, an AST ratchet at ceiling 0).
   - Chroma telemetry is off (#2060).
   - Uploads never fall back to plaintext in production (#2061).
   - One account's integration test result is no longer shown to other accounts (#2071).
3. **GitHub answers are about their repo, read with their grant, and say when a read failed.**
   - "What did we ship this week?", milestones, labels and branches read the person's own repo with their own grant.
   - A failed read says it failed, instead of "none" or "0" (#2128 and #1524, both closed served 10-22; #2123's rule; one `GitHubReadFailed` on the connector taxonomy).
   - A stale GitHub connection reads as needs-reconnecting, not as not configured (#2072, #2076).
4. **Onboarding works for invited testers.** The setup wizard no longer ends in "Setup Failed": the principal comes from the session (#2078, Class 4). Adding a project stores what was said, and only that (#2069, #2080, #2082).
5. **Alpha stays up and says when it isn't healthy.**
   - The minutes-long stall is fixed: provider calls run off the event loop on a dedicated executor (#2101; closing run 61/61 turns).
   - `/health` reports the database truthfully (#2083).
   - The promote gate refuses on a broken quiet count (grant condition 3).

**Not yet for users (honest):**
- **#2085, the database restarter:** the guards proved live on 10-22, but the restart was refused at Fly's lease, and the fix waits on xian's push.
- **#2132/#2138, document asks** (Class 3, must-close): Notion's top-hit guess was found and ruled, the handler half served, and routing failed rule 7. The handler split comes next.
- **#2135's trust ladder:** dormant by ruling. The recording chain had code deciding meaning, which ADR-080 forbids.

## How I worked

- **Volume:** 98 decisions.log entries in the window (counted by grep). Each is a ruling or a validation read from source, and validations ran against Tests on the landing sha.
- **Patterns that recurred and are now rules:**
  - *a counter or guard that can't read must not read as clear* (the quiet count, restarter guard 2, `/health`, #2134);
  - *a guard that reads tool output is validated on that tool's real output* (restarter guard 1b);
  - *a function that forwards the principal takes it with no default* (#2131);
  - *context given to the model carries each item's own source* (#2142).
- **Own misses (from the logs):**
  - guessed timestamps several times, each corrected before anyone acted;
  - a token-caveat claim on 10-21 that didn't cover listings;
  - "the main copy runs" (the branch copy does);
  - 10-22 16:33, "chat carries no file context": one mechanism read as all. Corrected in decisions.log at 18:28.
  - The practice I'm adopting: search every route to a resource before claiming its absence.

Verified how:
- `gh issue view` at 2026-10-23 04:28 on the 35 issues cited (state and closedAt): closed are #2048, 2054, 2059, 2060, 2061, 2064, 2069, 2071, 2072, 2076, 2078, 2080, 2082, 2083, 2100, 2101, 2112, 2121, 2127, 2128, 1524, 2131; open are #2041, 2057, 2109, 2123, 2125, 2134, 2135, 2085, 2132, 2138, 2139, 2142, 2096.
- `grep` of decisions.log for Arch lines dated 10-16 to 10-22.
- Served claims rest on CXO's and Web's quotes as recorded on the issues; I ran no turns.
- Layer: issue state plus my source reads at the time of each ruling. Denominator: Arch's rulings in the window.

## Next week (10-23 → 10-29)

- **Land:**
  - read and validate #2132's handler split (with #2138, #2139 and #2142's renderers) and its single-variable routing screens;
  - #2085's lease-free restart through the second attended test, or the pre-ruled `rwC` fallback;
  - #2134 and #2125 closes as their served rows come in.
- **Blocked on:**
  - xian's push to `ops/restarter` and his time for the attended test;
  - xian's word on folding #2138 into #2132;
  - Lead's builds.

-- Arch
