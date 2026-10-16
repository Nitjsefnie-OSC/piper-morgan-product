# Alpha promotion standing grant

**In force since 2026-10-16.** xian confirmed it ("Yes. I confirm the promotion grant.", via Janus; CIO received it at 08:10 PT). It succeeds decisions.log 2026-10-14 17:31, which made every promotion a dispatch on his explicit word. Record: decisions.log 2026-10-16. Text: Exec's draft with CIO's five changes and Lead's migration line, accepted by Exec, Lead and CIO, and shown to xian on Janus's card v368. Owner of this page: CIO, as the record. Lead holds Step 0 and dispatches.

## The grant, as confirmed

> **Alpha promotion standing grant.** The seat holding Step 0 (Lead; one dispatcher only, no one else dispatches) may promote to alpha without asking me, when all of these hold:
>
> 1. **Step 0 is READY.**
>    - Tests succeeded on the exact sha staging serves, or on its nearest tested ancestor when only untested paths changed since (what the promote gate itself accepts).
>    - `scripts/main-ci-status.sh` shows every gating workflow green.
>    - The promote gate accepts the build.
>    - No fly-deploy run is queued or in progress.
>    - `git diff --name-only <sha alpha /health reports> <sha staging serves> -- alembic/versions` lists nothing. If it lists anything, ask me, with the scratch-database round-trip and Arch's read attached.
> 2. **No hold is on.** That means no freeze (a history rewrite or a cohort freeze), no "hold promotions" from me, no open served-check failure on staging, and no NOTICE memo from PPM, CXO or Arch that names the build or an issue in it as held.
> 3. **Not while I'm testing alpha.** If a test session on alpha is announced as in progress (me, PA or Web on the test card), wait for it to end.
> 4. **Hours and cap.** Between 07:00 and 21:00 Pacific, at most two promotions a day, so someone is awake to see the result.
> 5. **What still needs my yes.** A build with a new database migration (see 1), or any change to production, beta or secrets. The grant covers alpha only.
>
> **After each promotion**, the seat:
> - logs the run id and sha;
> - confirms alpha's /health shows the new sha;
> - mails Web per the 10-14 procedure;
> - tells Exec.
>
> Exec puts one line on my board ("alpha moved to X at T"), so I learn after the fact instead of approving before.
>
> **If it goes wrong:** the fix goes forward through main, or a revert on main that staging redeploys and Tests passes, followed by one promotion under this grant. Then it stops, and the seat tells me.
>
> **To stop it:** I say "hold promotions" to any seat, and it holds until I lift it. Any promotion I later say I would have refused ends the grant until I renew it.

## Why these conditions

- **Why a grant:** xian had approved every promotion request. A yes that never fails guards nothing (m-44's boundary: a gate that can only pass), so the grant keeps only what the Tests gate doesn't cover, which is migrations and timing.
- **Migrations:** alpha runs `alembic upgrade head` on every release (`fly.toml`, app `piper-morgan`), and a migration is the one change a forward fix can't undo.
- **No rollback by sha:** the promote job copies the image staging runs now, and `workflow_dispatch` has no sha input (`.github/workflows/fly-deploy.yml`). That is why "if it goes wrong" says forward or revert.
- **No permission change:** Lead's seat already runs `gh workflow run` without a prompt (the 10-15 15:31 dispatch). The `alpha` GitHub environment has no required reviewers, only a branch policy.

## Procedure notes (do not change the grant's text)

- **"The sha staging serves" is read from staging's own `/health`**, never from the newest push in the fly-deploy run list. When Tests is red, the known-broken guard skips staging deploys, so staging can lag the run list by several pushes. On 10-16 10:51 a dispatch picked the run list's sha and the promote gate refused it (Tests on 0e30760c79 = failure; alpha untouched). Recipe corrected in `canonical-ops-recipes.md` (Lead, 6a91d56ec5).

**Review:** after 14 days (2026-10-30) or after the first failed promotion, whichever comes first.
