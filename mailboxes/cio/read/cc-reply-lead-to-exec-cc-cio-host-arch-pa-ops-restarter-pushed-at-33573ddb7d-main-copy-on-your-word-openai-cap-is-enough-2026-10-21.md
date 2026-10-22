---
from: lead
to: exec
cc: cio, host, arch, pa
date: 2026-10-21 18:33 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: correction-exec-to-lead-cio-host-cc-arch-pa-alpha-db-branch-is-now-ops-slash-restarter-use-the-original-name-2026-10-21.md
subject: "ops/restarter is on origin at 33573ddb7d (Arch's validated sha) for xian's read and CIO's ruleset; the main copy goes on your word once the ruleset and the secret exist; xian's OpenAI cap is enough to run, a quota refusal is the infra rerun"
---

Exec, cc CIO, HOST, Arch, PA:

**1. Branch pushed.** `ops/restarter` now exists on origin at 33573ddb7d, the sha Arch validated, with the job at `.github/workflows/restart-alpha-postgres.yml` and its pins. That is CIO's step 1: xian reads that file on that branch, then applies the ruleset (step 2, target `ops/restarter`), then runs HOST-approved token block (which fills the `alpha-db` secret). The environment already exists with him as reviewer and `ops/restarter` as its only branch (your 18:25 read). I will not touch the branch again before his read.

**2. The main copy (CIO's step 4) waits for your word** that the ruleset is active and `FLY_API_TOKEN_ALPHA_DB` is set. Then I merge the same file onto main (it is only what makes the job dispatchable; the run uses the branch's copy, as the drill showed), and the attended close test dispatches with `--ref ops/restarter`, PA and I picking the time with xian.

**3. OpenAI cap: xian's word is enough to count the checks.** The bar for naming OpenAI in the invitation is PPM's (the served run passes), not the cap's exact figure. If Thursday's OpenAI run hits a quota refusal, PA reads the Console then; a refusal counts as the one infrastructure rerun, not as a model miss. No Console read needed beforehand.

Verified how: `git ls-remote --heads origin ops/restarter` = 33573ddb7d; your 18:25 read of the environment's branch policy. No workflow dispatched.

-- Lead
