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
> 4. **Hours and spacing.** Between 07:00 and 21:00 Pacific, so someone is awake to see the result. No daily count: after a promotion, the next one waits until the Alpha Health Watch (`.github/workflows/alpha-health-watch.yml`) has run green once on it, so a break is pinned to one build before another lands on top. *(2026-10-20: replaced "at most two promotions a day". xian via Janus, relayed 11:08: "In this pre-beta period I am comfortable with a readiness based process and no limit to number of deploys per se." On CIO's recommendation of 10:54; the cap's original reason, CIO's 10-16 draft, had gone stale: it was used up every day 10-17 to 10-20 and held the #2101 fix. decisions.log 2026-10-20.)*
> 5. **What still needs my yes.** A build with a new database migration (see 1), or any change to production, beta or secrets. The grant covers alpha only.
>
> **After each promotion**, the seat:
> - logs the run id and sha;
> - confirms alpha's /health shows the new sha and its body `status` reads `healthy` (since #2083 the body carries `services.database`; a `degraded` body with the right sha means the image is live but the database is not answering, which is "If it goes wrong", not a promotion to report as done);
> - mails Web per the 10-14 procedure;
> - tells Exec.
>
> Exec puts one line on my board ("alpha moved to X at T"), so I learn after the fact instead of approving before.
>
> **If it goes wrong:** the fix goes forward through main, or a revert on main that staging redeploys and Tests passes, followed by one promotion under this grant. Then it stops, and the seat tells me.
>
> **A dispatch that leaves alpha unchanged is not a promotion and has not gone wrong.** That means alpha's /health still shows the previous sha, healthy, whether the gate refused it or Fly failed before the deploy. It isn't a promotion for the spacing rule. The seat fixes the cause or waits out the outage, then may dispatch again within the grant's hours, and mentions it in its line to Exec. *(2026-10-16: added at 11:44 as a gate-refusal-only line, confirmed by xian via Janus after a 10:51 gate refusal was read as the grant's stop; that reading came from wording in CIO's superseded first draft. Widened at 15:04 to any dispatch that leaves alpha unchanged, xian via Exec ("Yes, wider-version of grant is acceptable."), after Lead's 11:33 dispatch failed at Fly's image query during Fly's partial outage. A deploy that half-applied, leaving alpha changed or unhealthy, still falls under "If it goes wrong".)*
>
> **To stop it:** I say "hold promotions" to any seat, and it holds until I lift it. Any promotion I later say I would have refused ends the grant until I renew it.

## Why these conditions

- **Why a grant:** xian had approved every promotion request. A yes that never fails guards nothing (m-44's boundary: a gate that can only pass), so the grant keeps only what the Tests gate doesn't cover, which is migrations and timing.
- **Why no count (10-20):** a count holds back fixes as readily as features, and it batches changes so a break is harder to pin to one build. Each promotion already passes the Tests gate and reaches xian's board as "alpha moved to X at T". The spacing rule keeps one build per health-watch window. The watch checks liveness and the database only, not behaviour; served checks and testers cover that, as they did under the cap.
- **Expected next shape, not a rule (xian, 10-20):** "Once we enter beta and start to have users active on hosted system we'll probably move to something like nightly deploys from staging to production but will continue to allow relative free deployment to staging." Recorded as a direction to revisit at beta, not as a condition.
- **Open (PPM's and CXO's call):** whether a deploy drops a tester's open chat is unverified. Once design partners start (10-23), quiet windows for outside testers' sessions may be needed; that would widen condition 3, not reinstate a count.
- **Migrations:** alpha runs `alembic upgrade head` on every release (`fly.toml`, app `piper-morgan`), and a migration is the one change a forward fix can't undo.
- **No rollback by sha:** the promote job copies the image staging runs now, and `workflow_dispatch` has no sha input (`.github/workflows/fly-deploy.yml`). That is why "if it goes wrong" says forward or revert.
- **No permission change:** Lead's seat already runs `gh workflow run` without a prompt (the 10-15 15:31 dispatch). The `alpha` GitHub environment has no required reviewers, only a branch policy.

## Procedure notes (do not change the grant's text)

- **"The sha staging serves" is read from staging's own `/health`**, never from the newest push in the fly-deploy run list. When Tests is red, the known-broken guard skips staging deploys, so staging can lag the run list by several pushes. On 10-16 10:51 a dispatch picked the run list's sha and the promote gate refused it (Tests on 0e30760c79 = failure; alpha untouched). Recipe corrected in `canonical-ops-recipes.md` (Lead, 6a91d56ec5).

**Review:** after 14 days (2026-10-30) or after the first failed promotion, whichever comes first.
