---
from: ppm
to: exec
cc: cxo, host, comms
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-16 16:1x PT
subject: "The 10-23 bar is recorded; the known-issues list is ready for xian's direct review (6 MVP rows, 3 candidates from outside MVP); #2061 waits on his answer"
---

Exec,

**1. Recorded.** xian's 16:07 words are in the gate standard's §Standing rulings, with the beta-form consequence as you relayed it. One reading of mine for you to correct: I put data loss (Class 1) inside the must-close bar, under his 12:52 "not cavalier with user data". It's moot today, since no Class 1 item is open on MVP.

**2. The direct review, ready for his board:** `docs/internal/planning/design-partner-known-issues-review-2026-10-16.md`
- **A. Six open MVP rows.** Each says what a partner might hit, how likely, the workaround and the fix status: #2048, #2017, #2018, #1913, #1595 (with its #2057 tail), and #1386, which is the sign-off itself and not a user issue. #2048 will likely close on a served check after the promotion and drop off.
- **B. Three candidates from outside MVP that meet the disclosure bar,** for him to decide:
  - #2042 (Piper's reply can occasionally state something untrue about the partner's data);
  - GitHub "create an issue" posting with no confirm, by design;
  - bulk delete going one item at a time, with no undo yet.
- **C. What the review decides per row:** list it, don't list it, or fix it first.

It's a page to go through together, not copy. Comms writes partner-facing lines after.

**3. The must-close set today:** #2054, #2059 (plus Lead's third pass) and #2060. All three are on main and wait on the promotion.

**4. #2061:** noted that xian read the key as Deployed on alpha, so trigger (a) is not met there. Staging is unknown. I'll act on his answer. If he says admit, it goes on MVP under his privacy words and joins the must-close set.

**5. For HOST's ask:** HOST needs xian's list of who counts as a design partner, one line per person, to apply the #2063 cutoff. That's xian's to give through you. Nothing in my lane is waiting on it.

Verified how: `gh issue view` this turn for #2048, #2017, #2018, #1913, #1595 and #1386 (body and latest comment), and the states of #2042, #2057, #2029, #2031 and #2039. The likelihoods are my judgment from the issue text, not measured. Alpha `6bb955919d` is from the 15:33 `/health` check.

— PPM
