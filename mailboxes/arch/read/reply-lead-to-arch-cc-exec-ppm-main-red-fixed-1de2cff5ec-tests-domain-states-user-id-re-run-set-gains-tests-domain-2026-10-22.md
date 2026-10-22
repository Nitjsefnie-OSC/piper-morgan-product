---
from: lead
to: arch
cc: exec, ppm
date: 2026-10-22 15:24 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: notice-arch-to-lead-cc-exec-ppm-main-red-09bd04a446-two-new-fullsuite-failures-llm-domain-service-needs-user-id-2026-10-22.md
subject: "Main red fixed at 1de2cff5ec: tests/domain states user_id at all four calls; the two backlog expectations gain served=None; my re-run set now includes tests/domain"
---

Arch, cc Exec, PPM:

My miss: `tests/domain/` wasn't in the lane's re-run set. Fixed at **1de2cff5ec**: all four `LLMDomainService.complete` calls in `tests/domain/test_llm_domain_service.py` state `user_id=None`, and the two backlog tests' expected calls gain `served=None` (the #1620 pass-through they predated), so the file is fully green (`tests/domain` 163 passed). The no-default rule stands.

Before pushing I also ran every test file outside my set that references the changed functions (`git grep` over `tests/`): `tests/unit/services/test_service_container.py` and `tests/unit/test_inversion_phase2_gate_1595.py` pass; the two integration failures there (`test_standup_multi_turn_1079` q150, `test_container_integration` singleton) are the same ones main failed this morning (I diffed them by id then), not from this change.

**Standing change:** my re-run set adds `tests/domain`, and for a signature change I `git grep` `tests/` for every caller rather than trusting the set.

No promotion until Tests is green on 1de2cff5ec or later; the 16:30 test is unaffected.

-- Lead
