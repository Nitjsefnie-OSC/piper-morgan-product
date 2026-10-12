#!/usr/bin/env python3
"""r6-slim-swap.py — R6 step 5: replace CLAUDE.md with the probe-tested slim ruleset. FOR XIAN TO RUN, attended.

CIO's seat was refused this edit by auto mode ([Self-Modification], 2026-10-12 08:46 PDT); CIO did not retry.
Run from CIO's worktree:   cd ~/Development/piper-morgan-worktrees/cio && git pull -q origin main && python3 dev/2026/10/12/r6-slim-swap.py
It: (1) refuses if CLAUDE.md changed on main since the candidate was built (re-check needed then);
(2) appends extraction #8 with the full old text to claude-md-history.log; (3) writes CLAUDE.md from the candidate,
minus its "CANDIDATE ONLY" comment; (4) commits and pushes to main. Revert: git revert <the commit>.
"""

import subprocess
import sys
from pathlib import Path

BUILT_ON = "a2ce30228c"  # last CLAUDE.md commit the candidate was rebased onto
CAND = Path("dev/2026/10/12/r6-slim-CLAUDE-candidate.md")
HIST = Path("docs/internal/architecture/decisions/claude-md-history.log")
git = lambda *a: subprocess.run(
    ["git", *a], capture_output=True, text=True, check=True
).stdout.strip()

last = git("log", "-1", "--format=%h", "origin/main", "--", "CLAUDE.md")
if not git("rev-parse", last).startswith(git("rev-parse", BUILT_ON)[:10]):
    sys.exit(
        f"STOP: CLAUDE.md changed on main ({last}) after the candidate was built on {BUILT_ON}; tell CIO."
    )
old = Path("CLAUDE.md").read_text()
c = CAND.read_text()
new = c[c.index("# CLAUDE.md") :]
blob = git("rev-parse", "HEAD:CLAUDE.md")
HIST.write_text(
    HIST.read_text().rstrip("\n")
    + f"""

2026-10-12 (CIO; applied by xian) -- EXTRACTION #8: CLAUDE.md replaced by the slim ruleset (R6 step 5).
Spec's 2026-10-03 D-propose rewrite, rebased onto the 10-12 file ({CAND}). PM gate (2026-10-04: every probe
scenario at or above baseline) met: candidate 57/60 after judge fixes (all FAIL transcripts read), b re-run on a
neutral premise 6/6 for both files; 10-08 baseline 56/60 (dev/2026/10/12/r6-slim-probe-results.md).
Size {len(old):,} -> {len(new):,} chars (~{len(old)//4:,} -> ~{len(new)//4:,} tokens, chars/4). Rationale and incident
history for each rule stay in the earlier entries of this log. Old file: blob {blob}. Full removed text follows.

--- removed: CLAUDE.md before extraction #8 ---
{old}
--- end extraction #8 ---
"""
)
Path("CLAUDE.md").write_text(new)
git("add", "CLAUDE.md", str(HIST))
subprocess.run(
    [
        "git",
        "commit",
        "-q",
        "-m",
        "R6 step 5: slim CLAUDE.md (extraction #8; probe gate met)\n\nApplied by xian from dev/2026/10/12/r6-slim-swap.py.",
    ],
    check=True,
)
subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], check=True)
print(f"done: CLAUDE.md {len(old):,} -> {len(new):,} chars; pushed. Tell Exec/CIO.")
