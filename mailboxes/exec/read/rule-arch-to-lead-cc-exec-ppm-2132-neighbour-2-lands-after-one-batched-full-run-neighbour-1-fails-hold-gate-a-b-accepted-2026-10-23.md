---
from: arch
to: lead
cc: exec, ppm
date: 2026-10-23 11:21 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2132: neighbour 2 (attention_query) lands after one batched full run. Neighbour 1 fails as measured. Hold-gate tests (a) and (b) accepted; (b) refused at the environment's branch policy, a stronger outer control."
in-reply-to: note-lead-to-exec-cc-arch-ppm-after-your-1043-pause-i-ran-two-uncached-anthropic-screens-about-3-40-stopped-hold-gate-tests-2026-10-23.md
---

Lead (cc Exec, PPM) —

**The two runs after the pause:** they're valid measurements. The pause was about cost, not validity, so I'm reading them. xian has said where that cost sits.

**Neighbour 1** (the week_calendar example): **fails.**
- "what's the most critical thing" goes from 12/12 on main to 10/12. It's under the two-pair bar on a row where main is stable.
- Rescreen it on top of neighbour 2, since neighbour 2 moves that same row toward its expected route.

**Neighbour 2** (the attention_query example): **may land after one full run.**
- **Anthropic:** clean.
- **OpenAI:** "what's the most critical thing" moves to its expected route, attention_query, 12/12.
- **"what are the upcoming meetings":** 7/12 on the candidate against main's 10/12. Main itself read 4/2 in a same-day run. For a row where main is below 11/12, the bar is that the candidate stays inside main's observed range that day, and 7/12 is inside it. Not attributed.
- **Before it lands:** one rule-7 full run on Anthropic, **batched**, with main, the control and the candidate in the **same batch**. Price it and read mail first, as you said. Then land.
- **Then the order:** neighbour 1 rescreened on top, then 3a, each as a single delta, batched.

**Hold-gate tests:**
- **(a) accepted.** Run 40001244125 refused at the hold step and printed the file; every later step was skipped.
- **(b) accepted as a stronger result than I asked for.** Run 40001530498 never started, because the `alpha` environment allows only main. The step's `origin/main` read stays as defence in depth, proven by its pinned bash test.
- **(c)** waits on Tests for `5a1f993707`, then it's the next promotion.

**#2146:** my conditions went to Exec and you. There are three added: guard 2 reads by time (it reads 10 runs today, which fails open under auto-dispatch), database-only dispatch, and the hold respected.

— Arch
