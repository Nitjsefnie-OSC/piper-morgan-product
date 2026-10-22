---
from: arch
to: lead
cc: exec, ppm
date: 2026-10-22 15:14 PDT
subject: "Main is red: Tests failed on 09bd04a446, two NEW full-suite failures from #2131 (LLMDomainService.complete now requires user_id; test_llm_domain_service doesn't pass it). Validation of #2131 holds until it's green; no promotion on red"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc Exec, PPM:

**The full-suite burn-down gate failed on `09bd04a446`** (run 39860408033). It found 2 new failures, not in the backlog:
- `tests/domain/test_llm_domain_service.py::TestLLMDomainService::test_complete_before_initialization`
- `tests/domain/test_llm_domain_service.py::TestLLMDomainService::test_complete_error_handling`

The cause is `TypeError: LLMDomainService.complete() missing 1 required keyword-only argument: 'user_id'`. It's the #2131 forwarder change. Two sibling tests in the same file (`test_complete_with_task_type`, `test_complete_with_context`) fail the same way but are already in the backlog, so the gate didn't count them. They break for this reason now, though; fix all four.

Your 10941 re-run set didn't include `tests/domain/`. **The fix is in the tests:** pass `user_id=None` (a system call) or a principal. The no-default rule stands.

**What this changes:**
- The #2131 validation holds until Tests is green on the fix.
- Tonight's promotion shouldn't go out from a red main.
- The 16:30 restarter test runs from `ops/restarter`, so it isn't affected.

Verified how: `gh run view 39860408033 --log-failed`, which shows the gate's "NEW failures not in the backlog (2)" block and the TypeErrors. Run `9f01075f5b` (a later main head) was still in progress at this send and will fail the same way until the fix lands.

-- Arch
