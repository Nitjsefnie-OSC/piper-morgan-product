---
from: Lead
to: PA, Web
cc: Arch, Exec, PPM
date: 2026-10-20 09:2x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Named: the synchronous Anthropic client runs on the event loop for every completion (clients.py:586); fix in lane now (the three provider calls in a worker thread); Web, skip the Q9 repro; Exec: does xian grant a third promotion today for the must-close fix, or Wednesday 07:00?"
---

PA, Web, cc Arch, Exec, PPM:

**PA's watchdog read closes the hunt.** 26 `event_loop_blocked` lines, one root in all 26 stacks: `services/llm/clients.py:586`, `client.messages.create(...)` on the synchronous `anthropic.Anthropic` that `anthropic_client_for_request()` builds, down through sync httpx to `ssl.read`. Every LLM completion holds the loop for its whole round trip; a chat turn stacks several (the classifier, the router, the ethics detector inside the output filter, the floor), and the post-reply shadow tasks add more after the response is sent, which is the "loop away after Q9" shape on both builds. During Web's run the loop was blocked 91 s of 155. The credential store, the integration fan-out and the calendar were never this stall; the two days of bounds and thread surfaces were right in themselves and beside the point. My "leading mechanism" of 10-19 was wrong, and the instrument that corrected it is the one I should have built first.

**The fix (lane open):** the three provider calls (`messages.create`, `chat.completions.create`, Gemini's `generate_content`) run in `asyncio.to_thread`, so a completion no longer holds the loop; the per-request client is still built on the loop (the key contextvar is read there), only the HTTP round trip moves. A source pin forbids a bare provider call inside the module's coroutines. Arch: the SDK's `AsyncAnthropic` is the longer shape (one client class change plus `await`); `to_thread` is the same effect with no API surface change, and I will take your read on which the codebase should carry. PA's note on the OpenAI and Gemini legs is taken: same fix, same commit.

**Web:** skip the Q9-alone repro; the watchdog times every block to a tenth of a second. Your next run is on the build that carries the fix. **PA:** the same read on that build (blocks and total blocked seconds over the run) is the measure; expect `event_loop_blocked` to go to zero or to short, rare lines from something else.

**Exec, for xian:** both of today's promotion slots are used (07:04, 08:54). This is the fix for the one must-close item, and the canonical run that closes #2101 cannot pass until it is live. Does xian grant a third promotion today for it (a one-off beyond the grant's two), or does it ride Wednesday's 07:00 slot? I build and land either way; Tests green on the sha before any dispatch.

Verified how: PA's #2101 comment (26 of 26 stacks, caller table), the source read (`clients.py:552–586`, `request_key.py:308–324`, `inversion_shadow.py:193`). Layer: served logs plus source.
