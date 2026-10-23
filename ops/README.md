# ops/

**`alpha-hold.md` (absent by default): an alpha promotion hold.** While this file exists on `main`, `fly-deploy.yml`'s promote job refuses, and prints the file. (CIO's proposal and Arch's conditions, 2026-10-23, after a promotion went into an attended test's hold that existed only in mail.)

- **To call a hold:** commit `ops/alpha-hold.md` to `main` with four lines:
  - who holds it;
  - why;
  - the condition that clears it;
  - who removes it.
- **To clear it:** the holder deletes the file in a commit when the condition is met. If a hold outlives its condition, Exec or xian removes it.

The promote step reads the file from `origin/main`, not from the dispatching branch, and it refuses if `origin/main` can't be resolved.

Known gap (Arch, 2026-10-23, accepted): the step runs `git fetch origin main || true`. If that fetch fails, it reads the checkout's `origin/main`, which is a few seconds old, so a hold committed inside those seconds is missed. Commit a hold before you announce it.

Validated 2026-10-23:
- **(a) Refused.** Hold on main, dispatched from main: run 40001244125 refused at this step and printed the file.
- **(b) Refused earlier.** A dispatch from another branch (run 40001530498) never reached this step: the `alpha` environment's branch policy rejects non-allowed branches.
- **(c)** No hold: a dispatch from main proceeds to the next gate (the next promotion).

