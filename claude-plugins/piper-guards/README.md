# piper-guards (R6 step 6)

The cohort's guard hooks, ported into one Claude Code **mod** (a plugin with a hooks module). The plan is stage 7 of
`dev/2026/10/03/spec-eval/D-propose-ruleset.md`: port M-1 to M-6 and M-9, run each mod rule alongside its settings
hook for one week, then retire the hooks. **Status 2026-10-12 (CIO): M-1 and M-4. Not installed on any seat.**

| Rule | What it does | Settings hook it shadows | State |
|---|---|---|---|
| M-1 | Refuses working-tree-discarding git aimed at PM's main checkout | `.claude/hooks/guard-pm-checkout.sh` | ported; 3 tests pass |
| M-4 | Refuses `gh api` calls carrying `updateProjectV2Field` + `singleSelectOptions` (full replace of a Projects v2 option list) | none (prose rule + skill `assign-sprint-safely`) | new; 3 tests pass. Can't see a query passed by file (`-F query=@q.graphql`) |
| M-2, M-3, M-5, M-6, M-9 | diff before checkout, mail branch, bearer lint, dispatch tier, status line | `check-branch.sh`, … | **wait for the canary**: each needs a mods API call (`process.run`, `agent.spawn`, `ui.status`) not yet run on a seat |

**Needs CLI ≥ 2.1.287** (mods are on by default from there; the fleet is on 2.1.296 per Pard's 10-12 record).

- Check: `claude plugin validate claude-plugins/piper-guards`, then `cd claude-plugins/piper-guards && claude plugin test`.
- Try on one session: `claude --plugin-dir claude-plugins/piper-guards`. `/plugin` shows `1 mod active · piper-guards`.
- Turn off: drop the flag, or `/plugin` → disable, or `"disableAllHooks": true`. The settings hooks still run either way.

**Order** (docs, mods/events): managed PreToolUse hooks, then mod `tool.call` hooks, then project PreToolUse hooks,
then permission rules and mode, then `tool.check` mods. A `tool.call` deny that never calls `next` stops the call
before the rules and the auto-mode classifier. **Not yet measured on a live seat**: CIO's sandboxed live test was refused
by the auto-mode reviewer on 10-12. The first live check is the canary seat (Pard).

**Fails open** on its own error (`.catch` passes the call on), so a bug can't wedge a seat. The settings hook stays
behind it during the parallel week.

Cost: string parsing per Bash call, no subprocess. Benefit: none yet: measuring. Review: 2026-12-01. Owner: CIO (rules), Pard (install).
