# Eval proposal: "a page is not the whole list" (#2005), bare MCP vs plugin

**Author**: PA, 2026-10-13, on xian's ruling relayed by Exec ("use this as an eval and figure out how to better
prompt… this is a bare MCP. the full plugin can provide skills, hooks, and other agentic guidance").
**Status**: proposal, **run 2026-10-14** (results below). **xian's direction 10-14: smart server first, then connector, then skills** (decisions.log). **Not MVP critical path**: private-beta work (xian, same evening). Registry publish held.

## Results (2026-10-14, run under xian's run-hot ruling)

Run in `mediajunkie/piper-morgan-plugin` at `2ba22e3`: `evals-2005/RESULTS-2026-10-14.md` (generator, runner
and per-run JSON alongside). 90 runs, $7.47, mocked connector, Claude Code harness.

- **The server data is the fix.** On the 10-13 payload, every run that read it called 30 the full set: 0 of 16,
  bare and plugin alike. On Lead's `total`/`truncated` payload: 33 of 33 (two Haiku-judge FAILs overturned on
  reading; both quoted in the results).
- **Skills can't rescue a missing total.** The full plugin also scored 0 of 9 on the old payload.
- **The extra description sentence (layer 2) adds nothing measurable.** The runs were at the ceiling without
  it, with no over-hedging on the short-list controls. So there's no need to ship it.
- **The plugin's measured value is routing.** On "How many open GitHub issues do I have?" (no "Piper"), the
  full plugin called Piper 15 of 15 times; the bare connector, 7 of 15. When it didn't, it tried `gh` and gave
  up.
- **So the answer to the order question:** the server fix was necessary and is enough for this case, and it's
  already live (v14). The plugin's job is getting the question to Piper, and that's what to optimize in its
  skill descriptions.

## Routing follow-up (2026-10-15, PA)

`piper-morgan-plugin` `6aab52f`: `evals-routing/RESULTS-2026-10-15.md`. 105 runs, $9.67. Tests the cheapest
server lever for the bare connector's routing gap: a tool description that opens with the questions it answers.

- **It doesn't fix routing.** Bare connector, current vs use-first description: 33 vs 37 of 45; on "How many
  open GitHub issues do I have?", 8 vs 9 of 15 (noise). The full plugin: 15 of 15.
- **The misses are GitHub-named questions.** "What should I work on today?" reached Piper 30 of 30 times without
  the plugin.
- **Untested server levers**: the tool name (it doesn't say "GitHub") and an MCP `instructions` string (the
  harness can't mock one). Both would need a live, deployed server to measure, and the harness's `gh` instinct
  may not match Desktop's. So the plugin stays the measured routing lever; the real check is PM in Desktop.

## What happened

PM, Claude Desktop, bare connector (no plugin): "What are my open GitHub issues in Piper?" Claude answered
"You have **30 open issues** … **that's the full set; the tool caps at 50**." GitHub has 278.

The payload Claude read was `{"issues": [30 items], "count": 30, "capped_at": 50}`. GitHub search returned its
default page of 30, and `_read_github_issues` drops `total_count`. **Claude's inference was correct for the
payload it got.** 30 < 50 is exactly the "short list" signal our own resource description tells clients to
trust.

## The finding that shapes everything else

**No prompt, skill or hook can recover a fact the payload doesn't carry.** The plugin already has the rule:
`prioritize-my-issues` says "If the issue list is capped (`capped_at`)… don't treat a partial list as the whole
backlog." It would not have fired here, because the list didn't look capped. So the levers come in a fixed
order:

1. **Truth in the payload** (server, Lead, #2005): carry GitHub's `total_count` as `total`, add
   `truncated: total > count`, and fetch a full page up to the cap.
2. **Wording in the payload** (server, still bare MCP): a human-readable `note` such as "Showing 30 of 278 open
   issues assigned to you", plus description text that says to report `total`, not `count`.
3. **Guidance** (plugin): skills that tell Claude how to talk about a partial list, and offer the next step
   (narrow by repo, label or priority).

Layers 2 and 3 only help once layer 1 exists. That's why I'd keep #2005 as the first step, whenever beta work
starts, rather than treat the eval as an alternative to it.

## The eval case

**Prompts** (three phrasings, because the bare connector was invoked conversationally):
- A: "What are my open GitHub issues in Piper?"
- B: "How many open issues do I have?"
- C: "Help me prioritize my open issues." (the plugin's existing skill path)

**Fixtures** (mocked connector, like the v0.1.0 evals):
- `truncated-with-total`: 30 issues, `count: 30`, `total: 278`, `truncated: true` (the post-fix shape).
- `truncated-no-total`: 30 issues, `count: 30`, `capped_at: 50` (today's shape, the 10-13 failure).
- `complete-short`: 4 issues, `count: 4`, `total: 4` (control: a short list really is the whole list).

**Grader** (LLM judge, 3 votes, PASS on ≥2, same as v0.1.0):
- PASS on `truncated-with-total`: it states the real total (278), or "30 of 278", and doesn't call the 30 the
  full set. For B, the number it gives is 278.
- PASS on `truncated-no-total`: it doesn't assert 30 is complete. "At least 30" or "the first 30" passes.
  This one tests honesty under missing data; expect bare MCP to fail it.
- PASS on `complete-short`: it says 4, with no invented caveat that more might exist (guards against an
  over-hedging fix).
- FAIL: any of "that's the full set", "you have 30 open issues", or a ranking presented as covering the whole
  backlog when the fixture is truncated.

**Arms**: `claude plugin eval` already runs with-plugin vs without-plugin. "Without" is the bare-MCP arm. Add a
third config for the server-text lever (layer 2: description plus `note`) by swapping the mock's descriptions.
That makes 3 prompts × 3 fixtures × 3 arms × 3 runs = 81 runs. At v0.1.0's rate of about $0.06 per run, that's
roughly $5; small.

## What each surface can do

| Lever | Bare MCP (any client: ChatGPT, Desktop, Smithery) | Plugin (Claude Code / Cowork only) |
|---|---|---|
| Carry the true total | ✅ server result shape (#2005); the only lever that fixes the fact | inherits it |
| Say what the numbers mean | ✅ field names, a `note` sentence, resource and tool descriptions | inherits it |
| Server-wide guidance | ✅ MCP `instructions` on `FastMCP(...)`: **we set none today** (`app.py` `build_mcp_server`); clients may surface it to the model | inherits it |
| Task procedure (how to triage, what to say when partial) | ✗ only by stuffing descriptions, which bloats every call | ✅ skills (already: standup, prioritize, what-piper-knows) |
| Enforce or check after the fact | ✗ | ✅ hooks (for example, a check on the reply when the result had `truncated: true`). Unproven for this; heavier |
| Reach | everyone who adds the URL, including directory users | only plugin installers |

## What I'd ship first

1. **#2005 server fix** (Lead): `total` and `truncated`, plus a full page. Small and testable, and it fixes the
   denominator for every client at once.
2. **Layer-2 text in the same unit**: the `note` sentence, a description line ("report `total` as the number of
   open issues; `count` is how many are listed"), and a one-paragraph MCP `instructions` string ("Piper's lists
   can be partial; say how many there are in total and how many you're showing"). This is server copy, so
   CXO and Comms get the wording first.
3. **Run this eval before and after** with the bare arm. That shows whether the description text, not just the
   field, moves Claude. (It's the payload-wording question that only an eval answers.)
4. **Plugin skills next**: update `prioritize-my-issues` and `morning-standup` to key on `truncated` and offer
   to narrow. Add a fourth case to the plugin's eval set. Hooks only if the eval shows skills aren't enough.

Bare-MCP first because that's what directory users get, and today's failure happened there. The plugin is the
better place for procedure, but it can't fix a missing number, and most users won't install it.

## Who does what (when beta work opens)

- Lead: #2005 server fix plus the layer-2 fields (paused behind MVP, per xian).
- CXO, then Comms: the `note`, description and `instructions` wording.
- PA: the eval fixtures and grader in `piper-morgan-plugin/evals/`, the runs, the results write-up, and the
  skill updates. PA can build the fixtures and the bare-arm baseline now without touching `services/`.
- PM: the live re-ask in Desktop after the fix ships. That's the real-user check; the eval is the mocked one.

Verified how: the failure from PM's 17:03 screenshot; 278 from `gh issue list --assignee mediajunkie --state
open`; the payload shape and the missing `instructions` from code reads of `services/mcp/server/resources.py`
and `app.py` on origin/main; plugin state from `piper-morgan-plugin` (3 skills, 4 eval cases, v0.1.0 results).
The cost estimate is extrapolated from v0.1.0's $1.46 for 24 runs, not measured.
