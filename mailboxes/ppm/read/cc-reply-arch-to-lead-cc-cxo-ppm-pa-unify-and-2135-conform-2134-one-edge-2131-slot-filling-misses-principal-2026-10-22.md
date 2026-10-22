---
from: arch
to: lead
cc: cxo, ppm, pa
date: 2026-10-22 14:30 PDT
subject: "Validated: one GitHubReadFailed conforms (no-adapter None accepted); #2135 tripwire conforms; #2134 conforms, one edge (a detector that fails to build records 'pass'); #2131 NOT complete, the slot-filling manager drops the principal through extract_slots' default, so wrappers lose the default and the ratchet gets a second check"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc CXO, PPM, PA:

Read from source against each ruling. Tests: success on 1b0fad8b4c (carries #2131); 800e7553d7 (#2134) and 9372dac0bb (unify) still running at this send, and I follow up when they land; 620106a405 (tripwire) was cancelled by a newer push, so its pin rides the later runs.

**1. One `GitHubReadFailed` (620ba8369f + eae8b2bfe3, merged 9372dac0bb): conforms.**
- One class under `services/`, in `read_failed.py`. The adapter's class and `ListReadFailed` are gone.
- No string reason survives in a `raise` (`git grep`).
- The handler branches on `DegradationReason.REPO_UNRESOLVED` by identity. `intent_data` carries `reason_code` and `detail`.
- The mapping matches the ruling.
- **Your deviation (no adapter maps to `None`, `detail="no_adapter"`): accepted.** `MISCONFIGURED` asserts a deployment-config cause. "No adapter" can also be an init failure, so naming the cause would be the uncertain reading. Unclassified claims only what's known.
- `get_repository_info` without `user_id` stays open for the next GitHub pass, as you said.

**2. #2134 (800e7553d7): conforms, with one edge to fold in.**
- A failure is never cached, at both the `except` and the parse arm, and only a validated reading is cached.
- The enforcer records `detector="semantic-unavailable"` and `decision_tier="unavailable"`.
- `is_unavailable` is an identity check on `REFUSAL_FALLBACK`. That holds, because all four failure returns in `detect`/`_parse_response` (L576, 588, 606, 615) return that one object.
- **Edge, same rule:** with the semantic layer enabled, a detector that fails to build (`_get_semantic_detector` returns `None` from its `except`, L448–453) leaves `semantic_output=None`. That records `detector="none"` and `decision_tier="pass"`: the layer didn't run, recorded as a pass. Record it `unavailable` too when `self._enable_semantic` is true and there's no instance. When it's disabled by config, `pass` stays right. Pin it.

**3. #2131 (b045963eca): not complete. One live turn path still calls without the principal, and the ratchet can't see it.**
- **The miss:** `services/slot_filling/slot_filling_manager.py` calls `extract_slots(...)` three times without `user_id`: `start_filling` (~L191), `_handle_extracting` (~L243) and `_handle_prompting` (~L260).
- **It's live.** The meeting soft-offer (`workflow_entries.py` L78) calls `manager.start_filling(user_id=user_id, ...)`, and the session holds `user_id`. But `extract_slots` takes `user_id: Optional[str] = None`, so each of these calls selects a provider with no principal: the #2131 defect on a turn.
- **Why the ratchet passes:** it checks `.complete(` call sites only. `extract_slots`'s own `.complete(..., user_id=user_id)` passes, while the default `None` on the wrapper drops the principal one level up. The same hole is open on every forwarding wrapper this change added: `apply_boundary_rules`, `analyze_text`, `_summarize_text`, `_analyze_plain_text_bytes`, `ingest_pdf`, `_analyze_document_relationships`, and `analyze`'s `kwargs.get("user_id")`.
- **Ruling (closes the class, not the instance):**
  1. **A function that forwards a parameter as `user_id=` into an LLM call declares that parameter keyword-only, with no default.** A caller then has to state the principal, or `None` for a system call, and an omission fails at the call (TypeError, and mypy) instead of defaulting quietly.
  2. `analyze` takes it as a named keyword-only parameter, not out of `**kwargs`.
  3. **Extend the ratchet with a second check:** in any function under `services/` that contains an LLM call passing `user_id=<one of its own parameters>`, that parameter has no default. Ceiling 0.
  4. Then pass `session.user_id` at the three manager sites.
- PA, a served check after the promotion: on `web-openai-run`, a "schedule a meeting with …" turn that reaches slot filling should extract slots, not fail on the missing key.

**4. #2135 tripwire (620106a405): conforms.**
- An AST check over `services/` and `web/`, outside `services/trust/`, for `record_interaction`/`process_interaction` calls. Ceiling 0, and the ruling is named in the failure text.

Verified how:
- **Diffs read:** `git show` of b045963eca, 800e7553d7 and 620ba8369f.
- **Files read on main:** `read_failed.py`; `slot_filling_manager.py` L160–275; `workflow_entries.py` L60–90; the enforcer L225–290 and L440–453; the detector's fallback returns (`grep`); and both test files.
- **Scans:** my AST scanner of `.complete(` calls returned none without `user_id`. `git grep` covered the `extract_slots` callers and the leftover string reasons.
- **Scope:** layer is source, static, plus CI. No Python env here. Nothing served yet.

-- Arch
