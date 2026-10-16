#!/usr/bin/env bash
# test-owed-scan.sh — fixture tests for scripts/owed-scan.py (#1967). Run from the repo root.
set -u
here="$(cd "$(dirname "$0")" && pwd)"
t="$(mktemp -d)"; trap 'rm -rf "$t"' EXIT
mkdir -p "$t/dev/2026/10/16" "$t/dev/active"
log="$t/dev/2026/10/16/2026-10-16-0900-exec-code-log.md"
pass=0; fail=0
check() { # check <name> <want rc> <grep pattern>
  out=$(python3 "$here/owed-scan.py" --root "$t" --today 2026-10-16); rc=$?
  if [ "$rc" = "$2" ] && printf '%s' "$out" | grep -q -- "$3"; then pass=$((pass+1)); else fail=$((fail+1)); echo "FAIL $1 (rc=$rc)"; echo "$out"; fi
}
printf 'Drain: OWED[key: a; to: lead; by: 2026-10-20]: ship it\n' > "$log"
echo "key: a" > "$t/dev/active/exec-standing-items.md"
check "T1 documented form parses, has a row" 0 "1 OWED markers, 0 closed, 1 open · 0 flags · 0 markers not parsed"
printf 'Drain: OWED[key: a; to: lead; by: 2026-10-20].\n' > "$log"
check "T2 no ]: is counted, not skipped" 1 "UNPARSED 1 in dev/2026/10/16"
printf 'OWED[key: a; to: lead; by: 2026-10-20]: one OWED[key: b; to: cio; by: 2026-10-21]: two\n' > "$log"
check "T3 two markers on one line both parse" 1 "2 OWED markers"
check "T3b the second one is seen (b has no row)" 1 "NO-ROW   exec   key=b"
printf 'OWED[key: a; to: lead; by: 2026-10-20]: one; OWED-CLOSED[key: a]: done\n' > "$log"
check "T4 a close on the same line is a close" 0 "1 closed, 0 open · 0 flags · 0 markers not parsed"
printf 'example: `OWED[key: x; to: y; by: z]` in prose\n' > "$log"
check "T5 inline-code example is ignored" 0 "0 OWED markers, 0 closed, 0 open · 0 flags · 0 markers not parsed"
echo "test-owed-scan: $pass pass, $fail fail"
[ "$fail" -eq 0 ]
