---
type: briefing
title: BRIEFING-CURRENT-STATE.md - Where We Are Right Now
valid_from: "2025-09-30"
last_updated: "2026-10-17"
last_verified: "2026-10-16"
size_cap_bytes: 12000
---

# BRIEFING-CURRENT-STATE.md — Now

**What this is**: the one short page that says where the project stands *today*. One dated line per item,
each naming who attests it and how. **Size cap 12,000 bytes (~3k tokens), checked in CI**
(`scripts/check-current-state.py`). It replaced a 169 KB file on 2026-10-08 (R6 step 3, PM-approved
2026-10-04). **History is not lost**: the full previous file is verbatim in
`docs/internal/architecture/decisions/briefing-current-state-history.log`, with older extractions above it.
Day-by-day progress lives in the omnibus logs (`docs/omnibus-logs/`).

**How to update it** (any agent, per CLAUDE.md's staleness rule): replace a line, don't append under it.
Write over the stale line with today's date and your source. Narrative goes to the omnibus or the history
log, never here. Bump `last_updated` to the newest line's date, or CI fails. Skill: `update-current-state`.

**Not here on purpose**: system internals (use Serena / the code), sprint lists (run
`python3 scripts/sprint-truth.py`), PM's open asks in full (the attention rollup, below).

---

## Now

- **Alpha (live)** *(Arch, 2026-10-17 09:27 PDT, `curl https://alpha.pipermorgan.ai/health`; ancestry by `git merge-base`)*: healthy, **v0.8.14.0**, git_sha `118241587e`
  (today's slot 2). Carries #2064 (erase script + three conditions), #2071 (per-principal Test result), #2072 (gate fix and the four
  renderers). Waiting on main for Sunday's first slot: #2076 (focus/standup name a GitHub that needs reconnecting), #2075 (health
  only on a recorded check). Held branch: the rule-7 batch #2069/#2047/#2051. Served checks: PM test card (`dev/active/pm-test-card.md`).
  *(CIO, 10-16:)* the **standing promotion grant is in force** since xian confirmed it 10-16 08:10 (decisions.log 10-16;
  `docs/internal/operations/alpha-promotion-standing-grant.md`): Lead promotes when Step 0 is READY, no new migration, 07:00-21:00 PT, two a day. `origin/main` builds; the droplet
  and `origin/production` are gone (09-29).
- **Version** *(CIO, 2026-10-08, `git tag`)*: latest tag **v0.8.14.0** ("On Your Clock", 09-23). 0.9.0 is
  reserved for beta.
- **MVP gate** *(Docs, 2026-10-12 10:1x PDT, `sprint-truth.py`, live board pull of 1,815 items)*:
  **13 not done** (2 Sprint Backlog, 2 In Progress, 1 In Review, 8 Product Backlog), 1,238 done. The MVP milestone **is**
  the beta gate. **Dates: design partners Fri 10-23, hard stop Fri 10-30** (baseline 10-05; slips are logged in
  `docs/internal/planning/beta-gate-standard.md` and only PM moves either date). Read the ledger, not this line, for slips.
- **Engineering focus** *(Lead, 2026-10-16 06:4x PDT, from the 10-15 Lead log and its STOP block)*: 10-15 closed with 31 landings on main, each
  re-run at merge: the seven-branch held batch (#2011, ANALYSIS margin, #1965+#2012, #2009/#2013/#2014 with three migrations, #2010), #2020, #2017,
  #2019's delete cap, #1771 in seven units with the #888 escape-word map, #2026, #2027's dead suggestion lists, #2024, #2029 (+ amber icon), #2008
  formats, #2031, #2030, #2033, #2037, #2035, #2039, #2040, #2041, #2044 (Integrations card "Connected / Not checked yet. Press Test."), lint.yml
  queueing, the CI Concept lines. Three red windows, all test-layer misses of the merge re-run, each fixed within the hour; main green through
  `e4f21e9ca8`. Row E calendar connected on alpha (xian, 18:43). Open: #2043 (OAuth redirect defaults base-derived), the #1852 redirect-secrets
  proposal (xian's hand), #2042 class ladder (PPM/Arch). Held: #1982 (xian), PAT dual-write (#1983/#1995), #2005 paused, `lead-1943-clear-todos-resolver`
  (#2021 lifts), #2023 corpus rows first. Pacing: normal from 10-16 (run-hot ended 10-15 22:00).
- **PM's open asks** *(Exec, 2026-10-09 06:4x PDT)*: on Exec's attention rollup at
  `claude.ai/artifact/719UZ4h1NELjEwWZbDCceT` (its own header line carries the current version; do not pin one here, it was v90 at 04:2x and v95 by 06:4x). Do not copy the list here: it goes stale within hours.
- **Usage** *(CIO, 2026-10-17 10:08 PDT, last row of `dev/heartbeats/usage-per-account.tsv`, read 09:23)*: the pipermorgan.ai
  weekly meter is at **18%**; the next reset is **10-22 22:00 PDT** (10-23 05:00Z). The stop line is **95%**
  of the weekly meter (PM-approved 10-06). Normal pacing since 10-16.
- **Mail** *(CIO, 2026-10-15)*: v3 (`scripts/mail-send.sh`) for everyone. **Mail v4 pilot** (exec, cio and lead)
  runs through `scripts/mail4.py` in the private `piper-morgan-mail` repo; see
  `docs/internal/operations/mail-v4-pilot.md`. HOST and the other seats aren't in v4, and a v4 send to them is refused. No mail to PM:
  anything for PM goes to Exec (10-03). Since 10-14, mail-send refuses any new file in `mailboxes/xian (ceo)/inbox/`.
- **Ruleset refactor (R6)** *(CIO, 2026-10-15, from git log and CIO logs)*: steps 1 to 5 done. The slim CLAUDE.md landed 10-12
  (c3a7345cd3), after xian's D-D, D-E and D-F (e96a8b281b). Step 6: D-G (fleet CLI upgrade) was overtaken, with all seats on 2.1.296
  after the 10-10 reboot. The `piper-guards` plugin runs in parallel with the settings hooks on CIO's seat only, through 10-19. The
  per-rule keep-or-replace decision is at that review (`docs/internal/operations/hooks-registry.md`).
- **Operating model** *(standing)*: every cycling role runs the `duty-cycle-tick` skill. State lives in
  `dev/active/{role}-carry-forward.md`; the session log is the one durable record; push to `origin/main`
  routinely. Cohort liveness: `scripts/duty-cycle-freeze-check.sh`. CI on main: `scripts/main-ci-status.sh`.

## Position (Inchworm)

```
1. ✅ The Great Refactor   2. ✅ CORE   3. ✅ ALPHA testing (v0.8.0 → v0.8.4)
4. 🎯 Complete build of MVP
   4.1–4.3 ✅ B1 Beta Enablers · A20 Alpha round 2 · MUX (Jan 2026)
   4.4 🎯 MVP (M0–M6) ← CURRENT
       ✅ M0 Conversational Glue (Mar 4) · ✅ M1 Foundation (Apr 11) · ✅ M2 Conscious Floor (Jun 3)
       ✅ M3 Artifact Persistence (Jun 14) · ✅ D1 Beta Design Quality (Jun 19) · ✅ RECONNECT WS-1 (Jun 22)
       🎯 the MVP milestone = the beta gate (14 open; design partners 10-23, hard stop 10-30) · ⬜ M4 Trust + Learning · ⬜ M5 Distribution
5. Beta testing on 0.9    6. Launch 1.0
```
*(Milestone detail as of the 09-28 snapshot; Lead or PPM to correct any line that has moved.)*

## Where to look

| Need | Source |
|---|---|
| What happened on a given day | `docs/omnibus-logs/YYYY-MM-DD-omnibus-log.md` |
| Sprint / MVP membership | `python3 scripts/sprint-truth.py` (the project board is the source of truth) |
| PM's pending decisions | Exec's attention rollup (link above) |
| Roadmap, vision | `docs/internal/planning/roadmap/roadmap.md`, `docs/internal/planning/current/vision.md` |
| Decisions | `docs/internal/architecture/adrs/`, `docs/internal/product/pdr/`, `docs/internal/architecture/decisions/decisions.log` |
| Roles and lanes | `docs/briefing/ROSTER.md`, `mailboxes/DIRECTORY.md` |
| Terms (Plugin, MCPB, Connector, Cowork…) | `knowledge/piper-morgan-glossary-v1.1.md` |
| Earlier versions of this page | `docs/internal/architecture/decisions/briefing-current-state-history.log` |
