#!/usr/bin/env bash
# draft-birth-record.sh — PostToolUse (Bash, Edit|Write|MultiEdit): note when each unsent mailbox file first
# appears, so mail-send can warn on a stale draft (10-19 mini retro). Never blocks, never prints.
# Concept: docs/internal/operations/hooks-registry.md. Rule and five lines: scripts/draft_births.py.
TOP=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
[ -f "$TOP/scripts/draft_births.py" ] && (cd "$TOP" && python3 scripts/draft_births.py record >/dev/null 2>&1)
exit 0
