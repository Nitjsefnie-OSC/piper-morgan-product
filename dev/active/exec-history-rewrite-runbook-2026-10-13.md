# History rewrite (depth A): runbook

**Owner:** Exec. **Go:** xian, direct in Exec's session, 2026-10-13 12:02 PDT ("yes do the history re-write"). **Kit:** Themis, designinproduct `docs/agents/themis/deliverables/pm-history-clean-private/` (private; never copy here). **Proposed window:** tonight 23:00–24:00 PDT, after the 22:xx fires. Reviewers before the window: CIO (hooks, control plane), Pard (LaunchAgents), Themis (kit), HOST (fleet notice).

## The one danger

Every seat on Amber shares one git store (`~/Development/piper-morgan-product/.git`). After the force-push, any seat that runs its usual `git merge origin/main` and `git push origin HEAD:main` from an old branch pushes a merge that **fast-forwards the new main and brings the whole old history back**. Every step below exists to stop that.

## Steps

0. **Backup (done before the window):** full mirror plus a verified bundle of every ref at `~/Development/backups/piper-morgan-product-pre-rewrite-2026-10-13.{git,bundle}` (local; a second copy off-machine is xian's call). Old main at runbook time: `13e52a8dab`.
1. **Guard (CIO, before the window):** add to the shared `.git/hooks/pre-push` a refusal of any pushed commit that has an old-history commit as ancestor (sentinel: an old main sha; `git merge-base --is-ancestor`). Test it on a scratch clone. It covers every Amber seat and PM's checkout. It is advisory and bypassable (`--no-verify`), so steps 2 and 6 still apply.
2. **Freeze (T-15 min):** Exec mails every seat (v3 and v4) and Janus: no commits, no pushes, no mail-send until the "unfrozen" mail. Pard pauses the LaunchAgent fires for the window. Each seat replies with `git log --oneline origin/main..HEAD | wc -l` = 0 (or pushes first, before T-0).
3. **Final run (Themis, T-0):** `05-final.sh` on a fresh mirror taken after the freeze; checks pass (refs equal, 0 rule strings, file counts equal at every tip, independent re-application on main).
4. **Exec checks the rewritten head:** `python -m pytest tests/unit/scripts/test_prod_user_lookup.py` on a checkout of the rewritten main; spot-check 3 changed files; compare ref counts.
5. **Push (Exec):** force-push branches and tags only (`refs/heads/*`, `refs/tags/*`; GitHub refuses `refs/pull/*`). Then fetch from a fresh clone and re-run the rule search: 0.
6. **Each seat resets (no merge):** in its own worktree, `git fetch origin` then `git reset --hard origin/main` on `claude/{role}-cycle` (safe: 0 unpushed was confirmed in step 2). Report "reset to <new sha>". **Never `git merge` an old branch.**
7. **PM's checkout (xian's hand, any time later):** it holds uncommitted edits, so no agent touches it (CLAUDE.md rule 1). His steps: save `git diff` to a file, reset `main` to `origin/main`, re-apply the file. Until then `sync-pm-local.sh` will refuse to fast-forward, which is harmless.
8. **Unfreeze:** Exec mails "unfrozen"; Pard resumes fires. Watch the next 24 hours for a push carrying old history (the guard's log, and `git merge-base --is-ancestor <old sha> origin/main` = false at each Exec fire).
9. **Outside reach, after:** the two forks (the advisor re-forks; xian's yes), PR refs, old issue revisions (xian's clicks), other machines' clones (xian's laptop, Desktop worktrees: re-clone).

## Abort

Before step 5, anything failing stops the run with nothing changed. After step 5, the bundle restores every ref (`git push --force` from the backup mirror).
