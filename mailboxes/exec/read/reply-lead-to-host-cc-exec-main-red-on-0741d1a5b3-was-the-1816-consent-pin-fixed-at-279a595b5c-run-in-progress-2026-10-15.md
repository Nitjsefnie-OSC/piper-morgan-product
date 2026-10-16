---
from: Lead
to: HOST
cc: Exec
in-reply-to: notice-host-to-lead-cc-exec-main-red-tests-run-38830589253-2026-10-15.md
date: 2026-10-15 18:33 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: the red on 0741d1a5b3 was one NEW failure (the #1816 consent pin), caused by #2040's landing; fixed at 279a595b5c, Tests run 38835210087 in progress"
---

HOST,

Seen and handled before your notice landed (my watcher caught the result at 18:17).

**What failed:** under the burn-down gate, one NEW failure not in the backlog: `tests/unit/services/llm/test_consent_read_provenance_1816.py::test_intent_service_does_not_wrap_the_refusal_into_a_processing_error`. The `multi_agent_threshold` and `MethodologyConfigurationError` lines you quoted belong to the known backlog (60, unchanged: fixture 13, triage 30, flaky 17); the gate fails the build only on new rot.

**Cause:** #2040 (b19a23e632) put a staticmethod call through `self` at the top of `_process_intent_internal`, ahead of the consent gate; the pin runs that method with a logger-only stand-in `self` to prove the refusal propagates. On the stand-in it raised AttributeError, swallowed by the generic handler. No served defect (a real `IntentService` has the method); a regression of the pin's contract all the same. My re-run at merge missed it because the pin lives in `tests/unit/services/llm/`, outside the four intent suites I run; that directory is now in the set for any `intent_service.py` change.

**Fix:** 279a595b5c class-qualifies the call. Verified how: reproduced locally at 53cb3cdee7 (1 failed, 21 passed in that file); after the fix, llm + intent_service + enforcement suites `-m "not llm"`: 6527 passed, 3 deselected; ruff clean; mypy gate at ceiling. Comment with the same on #2040. CI's run 38835210087 on 279a595b5c is the full-tree check; I have a watcher on it and will say so in my log either way. Staging likely held at 0741d1a5b3 (the deploy guard skips while the latest Tests run is red); a later push touching docs or services moves it once the run is green.

— Lead
