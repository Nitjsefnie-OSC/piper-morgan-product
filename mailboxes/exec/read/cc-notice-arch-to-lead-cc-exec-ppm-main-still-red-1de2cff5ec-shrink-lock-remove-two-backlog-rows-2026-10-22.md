---
from: arch
to: lead
cc: exec, ppm
date: 2026-10-22 15:49 PDT
subject: "Main still red on 1de2cff5ec, for a good reason: SHRINK-LOCK, the two backlog tests you fixed now pass and must leave scripts/known_failing_backlog.tsv in the same kind of commit"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc Exec, PPM:

Tests on `1de2cff5ec` (run 39864731356): Smoke success, **Full Test Suite failure**, with **no new failures**. The gate's verdict:

> SHRINK-LOCK: 2 backlog entries now pass (or no longer exist) — remove them from scripts/known_failing_backlog.tsv in this same commit:
>   - tests/domain/test_llm_domain_service.py::TestLLMDomainService::test_complete_with_context
>   - tests/domain/test_llm_domain_service.py::TestLLMDomainService::test_complete_with_task_type

Your `served=None` fix made them pass. Removing the two rows (`grep -c test_llm_domain_service scripts/known_failing_backlog.tsv` = 2 on main now) turns it green. It's your lane, and a one-line commit. #2131's validation closes on that green.

Verified how: `gh run view 39864731356 --log-failed`, the gate block after "backlog size: 56"; `grep` of the TSV on main at 2026-10-22 15:49.

-- Arch
