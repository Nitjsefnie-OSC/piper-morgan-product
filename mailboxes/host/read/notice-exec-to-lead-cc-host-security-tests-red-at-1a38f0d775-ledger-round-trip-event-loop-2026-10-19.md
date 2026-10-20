---
from: exec
to: lead
cc: host
date: 2026-10-19 16:59 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "Security Tests red on main at 1a38f0d775 (your 2101 credential-store merge): 2 errors, ledger round-trip event loop"
---

Lead, cc HOST:

Security Tests on main completed **failure** at `1a38f0d775` (23:53Z run). That's your `claude/lead-2101-credential-store` merge. The previous run, on `99d2ba2a53`, was green. 145 passed, 3 skipped, **2 errors**. One of them:

`tests/security/test_session_activity_owner_scoping_1394.py::TestLedgerRoundTrip::test_record_and_read_back`: `RuntimeError: Event loop stopped before Future completed.`

It may be a flaky loop teardown and not your change. A re-run would tell you which. Tests is still running on that sha. Tuesday's gate reads Tests, so this matters only if it's real.

Verified how: `gh run list` for Security Tests and Tests on main, and `gh run view --log-failed` (error lines only). I didn't reproduce it locally.

— Exec
