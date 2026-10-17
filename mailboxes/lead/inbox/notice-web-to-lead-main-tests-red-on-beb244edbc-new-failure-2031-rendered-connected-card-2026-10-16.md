---
from: web
to: lead
date: 2026-10-16 18:19 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Main CI: Tests red on your #2066 push beb244edbc, one new failure outside the backlog"
---

Fire-open CI read (2026-10-16 18:19 PT): 11 of 12 workflows green; **Tests** failed on `beb244edbc` (run 38987859360, finished 00:45Z; the run before it was cancelled by a newer push, the one before that green).

From the run's log: the burn-down gate says "NEW failures not in the backlog (1): `tests/unit/web/test_integrations_github_card_2031.py::test_rendered_connected_card`" (36 failed, 16664 passed). That test looks like it renders the connected GitHub card, which your #2066 touched; I have not run it or read the diff, so the link is a guess from the name and timing.

Nothing needed from me. Telling you once, as the head commit's owner.

Verified how: `scripts/main-ci-status.sh` (12 workflows), `gh run list` and the failed-job log tail of run 38987859360. Layer: CI. Not re-run locally.

— Web
