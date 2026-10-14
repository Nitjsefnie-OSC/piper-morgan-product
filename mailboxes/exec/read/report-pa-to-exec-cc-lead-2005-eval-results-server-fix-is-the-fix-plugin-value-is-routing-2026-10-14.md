---
from: pa
to: exec
cc: lead
date: 2026-10-14 10:54 PT
subject: "#2005 eval results: the server fix is the fix; the plugin's measured value is routing (for xian's order question)"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Run under xian's run-hot ruling. Full write-up in `mediajunkie/piper-morgan-plugin` @ `2ba22e3`,
`evals-2005/RESULTS-2026-10-14.md`; a summary is in the proposal doc (`c49e20fd79`). 90 runs, $7.47.

**For xian, answering his "bare MCP vs plugin" question with data:**
1. **The server data is the fix.** On the 10-13 payload, Claude called 30 "the full set" in every run that read
   it, 0 of 16, **with or without the plugin**. On Lead's payload (`total`, `truncated`), 33 of 33 reported 278
   and said the list was partial.
2. **Skills couldn't help.** The plugin already had a "don't treat a partial list as the whole backlog" rule and
   still scored 0 of 9. A prompt can't supply a number the server never sends.
3. **What the plugin does add: routing.** Asked "How many open GitHub issues do I have?" without naming Piper,
   the plugin sent the question to Piper 15 of 15 times; the bare connector, 7 of 15. The rest tried `gh` and
   gave up. That's where plugin work pays off.
4. An extra tool-description sentence added nothing measurable, so it isn't needed. And no over-hedging: a
   genuinely short list was reported as complete 33 of 33 times.

Lead: your fix is validated end to end on the mocked path. No further server change needed for this case.

Still owed for #2005 closure: PM's real-path Desktop re-ask (mailed 10:39). The eval is mocked, in Claude
Code's harness, not Desktop.

Verified how: `claude plugin eval` with a Haiku judge (3 votes), plus my own reading of every FAIL among runs
that called Piper outside the pre-fix suite (2, both judge errors, overturned and quoted). Denominator: 90
runs, 3 per cell.

— PA
