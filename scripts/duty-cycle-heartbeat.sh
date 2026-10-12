#!/usr/bin/env bash
# duty-cycle-heartbeat.sh v2.0 (CIO 2026-07-28; v2.0 2026-10-12: R3 step 1 done — STORE ONLY, NO GIT)
#
# ★ v2.0 (2026-10-12, CIO; Exec confirmed 3 of 3 readers on the store; xian approved the edit in session):
# this script writes ONLY the non-git store ($PIPER_HB_STORE, default ~/.local/state/piper-heartbeats; read
# with scripts/hb-store.py). It no longer commits, fetches, merges or pushes anything, so it no longer ships
# your cycle branch (#1980 is gone with it) and makes no hb(...) / hb-last-invoked(...) commits on main.
# `--if-quiet` and `--no-push` are still accepted, as no-ops, so callers don't break. The git-era text below
# (`dev/heartbeats/...`, refinements, retries) describes the surface that existed until 2026-10-12; that
# directory is history now. The old git code is in git history (this file before 2026-10-12).
#
# WHY THIS EXISTS
# The freeze-watchdog inferred liveness from WORK OUTPUT — commits and session-log updates. But the
# duty-cycle skill tells agents NOT to produce work output on quiet fires ("don't commit a
# near-duplicate entry each fire"; "trivial/quiet-hold fires don't need an entry"). So a CORRECTLY
# EXECUTED quiet fire left no trace on origin/main and was invisible to the belt BY CONSTRUCTION —
# we were alerting on compliance. lead was flagged 3x on 2026-07-27 while alive and working.
#
# ⚠️ HOW TO READ THIS SURFACE — 2026-08-05, added after its own author misread it.
# This file is APPEND-PER-FIRE, so a role has one row per fire that day. Reading it without filtering
# gives a DIFFERENT ANSWER depending on which row you grab, and the error is not random:
#
#   ⭐ IT SELECTIVELY HITS THE MOST ACTIVE ROLES. A role that fired once has no later row to misread;
#      a role that fired three times does. So a naive read reports the roles that emitted MOST as the
#      ones performing WORST. The measurement error correlates with compliance. (PA, 2026-08-05: I
#      published host as +203 and pa as +210 when they were +24 and +30 — they had 3 rows each; ppm
#      was the one I got right, purely because it had a single row.)
#
# For per-fire latency, FILTER ON THE FIRE TYPE — column 3 exists for exactly this:
#     awk -F'\t' '$3=="START"' dev/heartbeats/YYYY-MM-DD/{role}.tsv | head -1
# Prefer this over `head -1`: a role that never emitted a START returns EMPTY (a visible, correct
# signal) rather than silently handing you its 10:00 WORK row as if it were the morning fire.
#
# No threshold reconciles "detect a stall fast" with "tolerate legitimate quiet" when the only
# evidence is whether work happened. Widening trades false positives for latency, and for
# low-frequency roles the trade is unacceptable (exec fires 2x/day → a 25h threshold). The fix is to
# stop inferring liveness from work at all: emit a signal that means "I woke up", nothing more.
#
# HOST'S THREE REFINEMENTS, all implemented:
#  (a) COST IS PER QUIET FIRE, NOT PER FIRE. On a fire that does work, the work commit already IS a
#      heartbeat — it carries role and timestamp on origin/main. Only fires that would otherwise
#      leave no trace need this. Busy agents pay ~zero. See --if-quiet.
#  (b) SIZE DISCIPLINE ON DAY ONE. We have watched this exact append-only shape fail twice this month
#      (MEMORY.md byte truncation, then its line ceiling underneath). Rotation is structural here:
#      one file per role per day, so no file grows without bound and nothing needs pruning logic to
#      stay correct. It also removes write contention entirely — each role owns its own path, so ten
#      agents can never conflict on a shared append.
#  (c) SILENCE MUST BE DIAGNOSTIC (G6). A broken heartbeat WRITER looks exactly like a quiet cohort —
#      the file simply stops growing. So the reader side (duty-cycle-freeze-check.sh) distinguishes
#      "this role is missing" from "NOBODY wrote today", and reports the latter as a writer fault
#      rather than as N independent stalls. This file's job is to make that distinguishable; see
#      HEARTBEAT-WRITER-SILENT there.
#
# NOT A LOGGING SURFACE. This is machine-readable liveness, not a record. The session log remains the
# single canonical record (PM 2026-06-12). What the skill forbids is a near-duplicate PROSE entry
# polluting institutional memory — which is why the same line REQUIRES one-line WATCH/START entries.
# A TSV append was never in scope of that prohibition (HOST concurring, 2026-07-28).
#
# USAGE
#   scripts/duty-cycle-heartbeat.sh <role> [fire-type]      # always writes
#   scripts/duty-cycle-heartbeat.sh <role> [fire-type] --if-quiet
#       ↳ writes ONLY if this role has no commit on origin/main since its last heartbeat window,
#         i.e. only when the fire would otherwise be invisible. This is the form the skill calls.
#   scripts/duty-cycle-heartbeat.sh <role> [fire-type] --if-quiet --no-push
#       ↳ added 2026-09-22 (fire-zero recursion incident fix, second defect): commits the marker
#         locally but does NOT fetch/merge/push. For a caller (specifically the post-commit hook)
#         where a push-from-this-context would race the belt or, worse, be the delivery mechanism
#         for a runaway recursion. Delivery then rides the caller's own next real push. Safe to
#         combine with --if-quiet or use alone; order of flags doesn't matter.
set -uo pipefail

ROLE=""; FIRE="work"; MODE=""; NO_PUSH=0
for arg in "$@"; do
  case "$arg" in
    --if-quiet) MODE="--if-quiet" ;;
    --no-push) NO_PUSH=1 ;;
    --*) echo "usage: $0 <role> [fire-type] [--if-quiet] [--no-push]" >&2; exit 2 ;;
    *)
      if [ -z "$ROLE" ]; then ROLE="$arg"; else FIRE="$arg"; fi
      ;;
  esac
done
[ -n "$ROLE" ] || { echo "usage: $0 <role> [fire-type] [--if-quiet] [--no-push]" >&2; exit 2; }

cd "$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "heartbeat: not in a git repo" >&2; exit 2; }

# R3 step 1 (dual-write 2026-10-08; git write removed 2026-10-12, CIO): the non-git heartbeat store, one
# record per invocation (the 10-05 per-fire-record ruling). Read with scripts/hb-store.py.
# Store: one directory on this host (the cohort runs on Amber). Columns: ts, role, fire, source (fire|hook),
# epoch. A store failure is now FATAL and loud (m-44): there is no git fallback, so a silent miss would read
# as a frozen role.
PIPER_HB_STORE="${PIPER_HB_STORE:-$HOME/.local/state/piper-heartbeats}"
_hb_ts="$(date '+%Y-%m-%d %H:%M:%S %Z')"; _hb_ep="$(date +%s)"
_hb_src="fire"; [ -n "${PIPER_IN_POST_COMMIT_HOOK:-}" ] && _hb_src="hook"
if mkdir -p "$PIPER_HB_STORE/$(date +%Y-%m-%d)" "$PIPER_HB_STORE/last-invoked" 2>/dev/null \
   && printf '%s\t%s\t%s\t%s\t%s\n' "$_hb_ts" "$ROLE" "$FIRE" "$_hb_src" "$_hb_ep" >> "$PIPER_HB_STORE/$(date +%Y-%m-%d)/$ROLE.tsv" \
   && printf '%s\t%s\t%s\t%s\n' "$_hb_ts" "$FIRE" "$_hb_src" "$_hb_ep" > "$PIPER_HB_STORE/last-invoked/$ROLE.txt"; then
  echo "heartbeat-store: $ROLE $FIRE ($_hb_src) recorded"
else
  echo "heartbeat-store: FAILED to write $PIPER_HB_STORE — the belts will read $ROLE as stale. Investigate now." >&2
  exit 1
fi
exit 0
