---
type: briefing
title: BRIEFING-CURRENT-STATE.md - Where We Are Right Now
valid_from: "2025-09-30"
last_updated: "2026-10-15"
last_verified: "2026-10-12"
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

- **Alpha (live)** *(Lead, 2026-10-15 06:41 PDT, `curl https://alpha.pipermorgan.ai/health`)*: healthy, **v0.8.14.0**,
  git_sha `5e5f3366c4` (promoted 10-14 20:55 by Lead on xian's word, run 38678103509; code-equal to the 17:24 READY build `f8b2d15e52`).
  Serves the 10-13 and 10-14 landings (#1943 first-N, #1843, #1771+#2007, #1783, #2008, data-model.md). Promote gate widened 3153ab903a
  (Tests-run-head list ∩ rev-list walk) and test.yml queues on main (3b92152c14), so a docs push no longer threatens a dispatch and a
  code push only queues a Tests run. `origin/main` builds; the droplet and `origin/production` are gone (09-29).
- **Version** *(CIO, 2026-10-08, `git tag`)*: latest tag **v0.8.14.0** ("On Your Clock", 09-23). 0.9.0 is
  reserved for beta.
- **MVP gate** *(Docs, 2026-10-12 10:1x PDT, `sprint-truth.py`, live board pull of 1,815 items)*:
  **13 not done** (2 Sprint Backlog, 2 In Progress, 1 In Review, 8 Product Backlog), 1,238 done. The MVP milestone **is**
  the beta gate. **Dates: design partners Fri 10-23, hard stop Fri 10-30** (baseline 10-05; slips are logged in
  `docs/internal/planning/beta-gate-standard.md` and only PM moves either date). Read the ledger, not this line, for slips.
- **Engineering focus** *(Lead, 2026-10-15 11:10 PDT, from the 10-15 Lead log)*: 20 landings on main today, each re-run at merge:
  the seven-branch held batch (#2011 census, ANALYSIS margin, #1965+#2012, #2009/#2013/#2014 with three migrations, #2010 on Arch's
  offer_hint census ruling), #2020, #2017, #2019's one-item delete cap (xian's 10-14 ruling), #1771 in six units with the #888 escape-word
  map (END cancel/quit/exit; PAUSE stop/never mind; skip advances the interview; an unstarted standup never suspends), #2026, #2027's
  17 dead suggestion lists, the CI Concept lines. Tests green on `f76a307ecb`; two reds today were test fixtures, fixed within the hour.
  **Step 0 READY on the card (v38)** once staging redeploys past the known-broken guard; promotion only on xian's word. xian (10:48 via
  PPM) admitted #2017/#2018 to MVP; #1943 → Production. Open: #2024 (census copy hardening) and a seventh #1771 unit (politeness at
  the hatch, "skip the standup"). Held: #1982 (xian), PAT dual-write (#1983/#1995), #2005 paused, `lead-1943-clear-todos-resolver`.
- **PM's open asks** *(Exec, 2026-10-09 06:4x PDT)*: on Exec's attention rollup at
  `claude.ai/artifact/719UZ4h1NELjEwWZbDCceT` (its own header line carries the current version; do not pin one here, it was v90 at 04:2x and v95 by 06:4x). Do not copy the list here: it goes stale within hours.
- **Usage** *(CIO, 2026-10-15 10:1x PDT, last row of `dev/heartbeats/usage-per-account.tsv`, read 09:23)*: the pipermorgan.ai
  weekly meter is at **77%** and resets **10-15 22:00 PDT** (05:00Z). The stop line is **95%** of the weekly meter (PM-approved 10-06).
  xian's run-hot window also ends Thu 22:00.
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
