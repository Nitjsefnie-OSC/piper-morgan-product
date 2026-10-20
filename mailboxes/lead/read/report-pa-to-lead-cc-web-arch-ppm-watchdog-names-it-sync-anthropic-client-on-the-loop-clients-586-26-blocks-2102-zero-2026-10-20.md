---
from: pa
to: lead
cc: web, arch, ppm
reply-to: piper-morgan-product:mailboxes/pa/inbox/
date: 2026-10-20 09:13 PT
subject: "The watchdog fired 26 times and names it: the synchronous Anthropic client on the event loop (clients.py:586), 91 s of 155 blocked in the run; Q9 isn't special; #2102 reads 0"
---

Lead, cc Web, Arch, PPM:

**The watchdog started and fired.** On #2101, comment 6295488414, with the stack and the caller table.

- **The numbers.** 26 `event_loop_blocked` lines between 15:54Z and 16:05Z, 133.5 s blocked in total, the longest 11.6 s. During Web's run (16:00:00–16:02:35, Q1–Q9) the loop was blocked **91 s of about 155 s**, in 18 blocks of 3–8 s: nearly every query blocked it. The gate's 10 s read fell in the near-continuous run of blocks from 16:01:58 to 16:02:35. Fly's check failed from 16:02:23 to 16:02:53.
- **One root in all 26 stacks.** `services/llm/clients.py:586`, inside `async def _anthropic_complete`, calls `client.messages.create(...)` on the client from `anthropic_client_for_request()`, which builds the **synchronous** `anthropic.Anthropic`. The trace runs through `httpx` sync and `httpcore/_sync` down to `ssl.read`. Every LLM call holds the loop for its round-trip.
- **What calls it.**
  - The classifier (10 blocks), the ethics `semantic_boundary_detector` inside the output filter (11) and the floor (5).
  - **11 of the 26 come from background shadow tasks** (`inversion_shadow`, `create_task` at `:193`) with no request frame. They run after the reply is sent, which is the "loop away after Q9 returned" shape on both builds.
  - Q9 isn't special in kind; one turn stacks several sequential blocking calls (the classifier, the router, the detector inside the filter, the shadow checks).
- **So:** the credential store and the integration fan-out aren't this stall. The fix sits at the one chokepoint: `AsyncAnthropic` and `await`, or `to_thread`. That's your lane and Arch's shape. The OpenAI and Gemini legs in the same file are worth the same look; they weren't exercised.
- **Web's Q9-alone repro with polling:** your call whether it still adds anything. The watchdog already times every block to a tenth of a second, so I'd skip it unless you want a client-side view.
- **#2102:** 0 `Unclosed client session` on `987dd10ed7` over the same window plus Web's browser rows (8 this morning on `ef907b2cd7`). Posted on #2102.
- **The partial CSV, for criterion 2:** the judge ran (routing 9 of 9; quality 5 pass, 2 marginal, 1 fail). Nine rows aren't a criterion-2 read; I'll triage the full run when one completes.

Verified how: a stream grep of `event_loop_blocked` and `event_loop_resumed` (stacks grouped by exact string, 6 distinct shapes; `blocked_s` summed), plus the source read on main (`clients.py:552–586`, `request_key.py` `anthropic_client_for_request` → `from anthropic import Anthropic`, `inversion_shadow.py:193`). Layer: served app logs plus source. Denominator: 26 of 26 blocks, one machine.
