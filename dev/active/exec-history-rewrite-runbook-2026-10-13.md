# History rewrite (depth A): runbook

**Owner:** Exec. **Go:** xian, direct in Exec's session, 2026-10-13 12:02 PDT ("yes do the history re-write"). **Kit:** Themis, designinproduct `docs/agents/themis/deliverables/pm-history-clean-private/` (private; never copy here). **Window:** freeze 22:30 PDT (Themis: rewrite plus checks run over an hour); push when xian is at the keyboard (see step 5). Pard's hold covers 22:55 to 04:00 and lifts on "unfrozen". Reviewers before the window: CIO (hooks, control plane), Pard (LaunchAgents), Themis (kit), HOST (fleet notice).

## The one danger

Every seat on Amber shares one git store (`~/Development/piper-morgan-product/.git`). After the force-push, any seat that runs its usual `git merge origin/main` and `git push origin HEAD:main` from an old branch pushes a merge that **fast-forwards the new main and brings the whole old history back**. Every step below exists to stop that.

## Steps

0. **Backup (done before the window):** full mirror plus a verified bundle of every ref at `~/Development/backups/piper-morgan-product-pre-rewrite-2026-10-13.{git,bundle}` (local; a second copy off-machine is xian's call). Taken 12:03 PDT: 196 refs, bundle 1.22 GB, `git bundle verify` passed. **Refresh both at the freeze** (`git remote update` in the mirror, new bundle) so the backup holds the last pre-rewrite pushes. Old main at runbook time: `13e52a8dab`.
1. **Guard (CIO wrote it, e6d75bbe5, 9 of 9 tests; Pard installs by 21:00, or xian pastes `cp scripts/git-hooks/pre-push "$(git rev-parse --git-common-dir)/hooks/pre-push"`):** dormant until a sentinel file exists. Original plan: add to the shared `.git/hooks/pre-push` a refusal of any pushed commit that has an old-history commit as ancestor (sentinel: an old main sha; `git merge-base --is-ancestor`). Test it on a scratch clone. It covers every Amber seat and PM's checkout. It is advisory and bypassable (`--no-verify`), so steps 2 and 6 still apply.
2. **Freeze (22:30):** Exec mails every seat (v3 and v4), Janus, Themis and Pard with HOST's notice text: stop now, including anything half-finished; a mail wake during the freeze is not a work order. **One allowed action:** a single reply by 22:45 giving `git status --short | wc -l` and `git log --oneline origin/main..HEAD | wc -l` (push or save first if either is not 0). Then nothing: no commit, push, mail-send, merge, `git clean`, `git stash`, `git reset` or `git checkout`. Pard's hold stops new LaunchAgent fires from 22:55. Exec's own 22:38 cron fire only logs.
3. **Arm the guard (Exec, T-0, after a fetch):** `git rev-parse origin/main > "$(git rev-parse --git-common-dir)/piper-old-history-sentinels"`. From here every push from Amber is refused, so the freeze is mechanical; xian's push comes from Themis's mirror, a separate git folder.
3a. **Final run (Themis, after the replies):** results go privately to designinproduct `docs/mail/`; the rewritten bare mirror stays at Themis's scratch path, unmodified until the push is verified; Themis writes "do not push" if any stop condition fails. `05-final.sh` on a fresh mirror taken after the freeze; checks pass (refs equal, 0 rule strings, file counts equal at every tip, independent re-application on main).
4. **Exec checks the rewritten head:** `python -m pytest tests/unit/scripts/test_prod_user_lookup.py` on a checkout of the rewritten main; spot-check 3 changed files; compare ref counts.
5. **Push (xian's hand):** every seat, Exec included, is denied `git push --force` by rule, and no agent works around that. xian runs the one push command, typed as `! …` in Exec's session, from a clone of Themis's mirror: branches and tags only (`refs/heads/*`, `refs/tags/*`; GitHub refuses `refs/pull/*`). Then fetch from a fresh clone and re-run the rule search: 0.
5a. **Widen the sentinels (Exec, after step 5):** append every branch tip in the shared store that is not an ancestor of the new main (CIO's loop, 12:17 memo); prune after the 24-hour watch.
6. **Each seat resets (no merge; CIO confirmed `--keep` allowed on all 11 seats and tested on a rewritten history; an untracked file that does not collide, like HOST's Fly backup, is kept):** `git reset --hard` is denied on every seat (Pard), so: `git fetch origin`, check `git status --short` is empty, then `git reset --keep origin/main` (it refuses if any local change would be lost; CIO to confirm it is allowed on every seat). Reply "reset to <sha>" with `git log --oneline -1`. Never merge an old branch, `stash pop`, or check out an old sha. Report "reset to <new sha>". **Never `git merge` an old branch.**
7. **PM's checkout (xian's hand, any time later):** it holds uncommitted edits, so no agent touches it (CLAUDE.md rule 1). His steps: save `git diff` to a file, reset `main` to `origin/main`, re-apply the file. Until then `sync-pm-local.sh` will refuse to fast-forward, which is harmless.
7b. **Before unfreeze (CIO):** one `mail-send.sh` from a scratch clone of the rewritten main (the heartbeat writes only to its store, no git; confirmed).
8. **Unfreeze:** Exec mails "unfrozen"; Pard resumes fires. Watch the next 24 hours: CIO's loop over every sentinel ("OLD HISTORY BACK" must never print) plus the guard log. Tick skill v1.52 also stops a seat that missed the reset mail from merging. No one dispatches `scope-guard.yml` tonight (its retry rebases onto main).
9. **Outside reach, after:** the two forks (the advisor re-forks; xian's yes), PR refs, old issue revisions (xian's clicks), other machines' clones (xian's laptop, Desktop worktrees: re-clone). **xian must not push from the laptop until it is re-cloned**: an old-history merge on top of the new main is a fast-forward and GitHub would accept it.

## Open for xian

- When he can be at the keyboard for step 5 (tonight after about 23:45, or another night).
- Whether to expire the shared store's reflogs and garbage-collect old objects afterwards (irreversible; the bundle would be the only copy). Exec's lean: not now; revisit in a week once nothing has gone wrong.
- The backup holds what the rewrite removes: only xian and Exec read it; no agent copies from it into any repo.

## Abort

Before step 5, anything failing stops the run with nothing changed. After step 5, the bundle restores every ref (`git push --force` from the backup mirror).
