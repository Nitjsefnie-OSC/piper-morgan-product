#!/usr/bin/env bash
# pre-commit-ship-synthesis-gate.sh — PreToolUse hook for `git commit*` (PROPOSED; CIO to review and register)
#
# Blocks a commit that ADDS a new Weekly Ship draft (docs/public/comms/drafts/weekly-ship-NNN-draft-*.md)
# unless that Ship's internal synthesis exists and xian has discussed it:
#   docs/internal/planning/comms/ship-reviews/ship-NNN-week-review.html  containing  <!-- discussed: YYYY-MM-DD -->
#
# Why: the draft-weekly-ship skill's Step 2c (synthesis for xian, discussed before any draft) was skipped
# for #054 and again for #066 (2026-10-23), both times by an Exec working from habit, not the skill. A rule
# in prose was read past twice; this makes the shortcut fail at the commit with the reason and the fix.
# xian approved the two-part fix 2026-10-23 (this gate plus the status line in scripts/ship-kickoff.sh).
#
# Exit 0 = allowed (no new Ship draft staged, or the gate is satisfied). Exit 2 = blocked, message on stderr.
# Only ADDED draft files are checked, so edits to an existing draft (Comms, xian's admin saves) pass.

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$REPO_ROOT" || exit 0

ADDED=$(git diff --cached --name-only --diff-filter=A 2>/dev/null | grep -E '^docs/public/comms/drafts/weekly-ship-[0-9]{3}-draft-.*\.md$')
[ -z "$ADDED" ] && exit 0

STATUS=0
while IFS= read -r f; do
  n=$(basename "$f" | sed -E 's/^weekly-ship-([0-9]{3})-draft-.*/\1/')
  syn="docs/internal/planning/comms/ship-reviews/ship-${n}-week-review.html"
  if [ ! -f "$syn" ]; then
    echo "BLOCKED: $f adds Ship #${n}'s draft, but its synthesis ($syn) does not exist." >&2
    echo "  Run the draft-weekly-ship skill from Step 2c: synthesis for xian first, then the discussion, then the draft." >&2
    STATUS=2
  elif ! grep -qE '<!-- discussed: [0-9]{4}-[0-9]{2}-[0-9]{2} -->' "$syn"; then
    echo "BLOCKED: Ship #${n}'s synthesis exists but has no '<!-- discussed: YYYY-MM-DD -->' marker." >&2
    echo "  The draft follows xian's discussion of the synthesis (process guide step 7). Add the marker the day he discusses it." >&2
    STATUS=2
  fi
done <<< "$ADDED"
exit $STATUS
