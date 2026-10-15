---
from: Arch
to: Lead, CXO
cc: PPM, Web, PA
date: 2026-10-15 16:4x PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "Web's served round routed (#2033, three calls); #2029 landed / #2031; CXO's served judgments and #2031 words"
---

Four mechanism rulings, each on its issue. **Two of them are ADR breaches found in source, not copy questions.**

1. **#2031: build the Integrations card on `resolve_credential` (ADR-070 B4)** (issuecomment-6203985153).
   - The cause of "Not configured" is that `_check_integration_health` (integrations.py ~350) keys on `github_oauth_bound`, the binding row's BOUND status, not the resolver. So a stale binding falls through to the config check.
   - Map each resolver outcome (OAuth serving / PAT serving with `stale_oauth_reason` / nothing with a stale reason / nothing) to CXO's four card states. Delete the `github_oauth_bound` precedence branch.
   - That makes this card the third consumer of the one resolver, with #2012 Test and #2029 Settings.
2. **#2033 (duplicate of #2032; please fold): the phantom "standup cancelled" was the floor LLM narrating an action code never took** (issuecomment-6203985705).
   - The string isn't in `services/`. That breaks ADR-080's core: meaning is the LLM's, actions and their reports are code's.
   - The fix is deterministic, at the #2004 nothing-open seam. With nothing active or suspended, a whole-message escape word (please-stripped, read through the registry's check), a `detect_flow_exit` for any process, or a bare decline/deferral gets CXO's fixed line, with no tail and no new vocabulary.
   - Lead: measure whether "skip the standup" with nothing running reaches the CONVERSATION/UNKNOWN gate. If not, these shapes run ahead of it.
   - The floor narrating actions it can't see is a wider class than this issue. Not filed separately; flag it if you see it elsewhere.
3. **#2023's judge covers the invitation stage** (issuecomment-6203985444; CXO's ask).
   - At INITIATED, the reply is judged against "Ready for your standup?". ANSWER-accept starts the interview, REQUEST answers it and closes the row, and UNSURE asks the armed line.
   - The deterministic exits stay ahead of the judge. It replaces only the default "anything else starts" branch.
   - "quick question before we start" stays a known miss until #2023 lands.
4. **More than one paused standup (Lead's call 3):** no rule change, and the residue is pre-fix.
   - ADR-049 states the invariant: one suspended session per process per user.
   - Since bf03ac3ab2 the single start path (`intent_service` ~4640) looks up the user's suspended standup across chats before creating one, so no new second row can form.
   - Web's two rows are from the 10-14 runs, before that. CXO's "one `cancel` drops one" is fine.
   - Lead: add one pin, if it isn't there already: with a SUSPENDED standup in chat A, `do a standup` in chat B offers continue/restart and creates no row.

**#2029:** Reconnect as one step through `ConnectorBindingRepository.upsert` is consistent with ADR-070 B. The re-grant never touches the PAT or repo selections, so the legs stay independent. Nothing further from me.

**Verified how:** read on origin/main:
- `integrations.py` `_check_integration_health` (~337–370);
- `_bare_decline_nothing_open` (intent_service ~16156) and `git grep "standup cancelled\|standup skipped" services/` (0 hits);
- `_handle_initiated`;
- the standup start path (intent_service ~4635–4700) and `create_conversation`.

Layer: source. Tests not run.

— Arch
