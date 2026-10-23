# ops/

**`alpha-hold.md` (absent by default): an alpha promotion hold.** While this file exists on `main`, `fly-deploy.yml`'s promote job refuses, and prints the file. (CIO's proposal and Arch's conditions, 2026-10-23, after a promotion went into an attended test's hold that existed only in mail.)

- **To call a hold:** commit `ops/alpha-hold.md` to `main` with four lines:
  - who holds it;
  - why;
  - the condition that clears it;
  - who removes it.
- **To clear it:** the holder deletes the file in a commit when the condition is met. If a hold outlives its condition, Exec or xian removes it.

The promote step reads the file from `origin/main`, not from the dispatching branch, and it refuses if `origin/main` can't be resolved.
