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
- **Engineering focus** *(Lead, 2026-10-15 06:41 PDT, from the 10-14 Lead log and carry-forward)*: 10-14 closed four MVP issues
  (#1886, #1623, #1579, #1860) and landed nine units, now live on alpha 5e5f3366c4. Seven code branches held through the 10-14 promotion
  land this morning in order (#2011 census-b, #2010 list-projects offers, ANALYSIS margin example, #1965/#2012 OAuth-leg error, #2009
  owner NOT NULL migration, #2013 KG owner, #2014 items check). Then #1771 second seam, #2019 interim delete cap (xian approved PPM's
  recommendation 10-14 21:02: `clear_todos` flip HELD, #2021 soft delete first), #2020 strings, #2017 Disconnect; #2023 corpus rows first
  (Arch's ruling). Held: #1982 Registry publish (xian), PAT dual-write branch (#1983/#1995), #2005 paused as an eval, `lead-1943-clear-todos-resolver`
  (flip held). Next promotion only on xian's explicit word.
- **PM's open asks** *(Exec, 2026-10-09 06:4x PDT)*: on Exec's attention rollup at
  `claude.ai/artifact/719UZ4h1NELjEwWZbDCceT` (its own header line carries the current version; do not pin one here, it was v90 at 04:2x and v95 by 06:4x). Do not copy the list here: it goes stale within hours.
- **Usage** *(CIO, 2026-10-08)*: the weekly window reset Thu 10-08 21:59 PDT; stop line **95%** of the weekly
  meter (PM-approved 10-06). Readings: `dev/heartbeats/usage-per-account.tsv`.
- **Mail** *(CIO, 2026-10-08)*: v3 (`scripts/mail-send.sh`) for everyone. **Mail v4 pilot** (exec + cio,
  lead from 10-12) runs through `scripts/mail4.py` in the private `piper-morgan-mail` repo; see
  `docs/internal/operations/mail-v4-pilot.md`. No mail to PM: anything for PM goes to Exec (10-03).
- **Ruleset refactor (R6)** *(CIO, 2026-10-09)*: steps 1-4 done (guard + allow-list; sign-off; this page; 32 of 50
  defects). Step 5: probe baseline recorded (`dev/2026/10/08/r6-probe-baseline/`); the slim CLAUDE.md waits on PM
  decisions D-E/D-F. Step 6 (CLI upgrade + mods) waits on D-G.
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
