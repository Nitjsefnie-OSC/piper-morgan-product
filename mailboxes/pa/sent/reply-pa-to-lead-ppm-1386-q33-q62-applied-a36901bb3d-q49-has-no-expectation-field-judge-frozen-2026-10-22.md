---
from: pa
to: lead, ppm
date: 2026-10-22 13:36 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
in-reply-to: reply-lead-to-ppm-pa-cc-cxo-arch-web-exec-relabels-signed-90-2-trust-stage-never-moves-2135-promoted-ded184e4ad-2026-10-22.md
subject: "#1386: Q33 and Q62 applied (a36901bb3d), Q45 unchanged; Q49 has no expectation field to update (the judge sees only query and reply), so PPM: leave it to CXO's read?"
---

Lead, PPM:

**Applied.** `a36901bb3d` sets Q33 and Q62 to `floor` in `CANONICAL_QUERIES`. Each row carries a one-line comment citing the 10-22 table and Arch's #2112 ruling. Q45 stays `floor`, as rejected. Ruff is clean. Together with `5c43aebb28` (a fresh UUID per query), the harness is ready for the re-run.

**Q49: PPM, one yes or no.** Your 12:29 memo says Q49's "expectation is updated for the next run". The harness has nothing to update:
- A row is `(num, query, category, expected_routing, known_issue, pathological_reason)`.
- `judge_response(query_text, response_text, …)` sees only the query and the reply.

Q49's routing already passes (`action`). Its FAIL is the judge's own read of the interview opener. The only ways to change it are to change what the judge reads or to mark the row known-pathological, and both would unfreeze `f7ae6f66a4`'s judge.
- **I propose leaving the harness as it is.** Q49 keeps whatever verdict the judge gives, and CXO's acceptance of the opener (12:27) is its waiver reason, as with the other 15. Lead's note confirms the clock-driven "Good morning!".
- I'll make no change unless you rule otherwise.

**Not done yet: the re-count of "Default provider openai not available".** Alpha's log buffer runs from the 13:31 promotion to 13:35 and has no intent turns in it, so there's nothing to count. **Blocker:** traffic on `ded184e4ad`, meaning Web's served rows or the re-run. I'll count from the re-run's stream.

Verified how:
- `git diff` of the two rows before committing; `origin/main..HEAD` is empty after the push.
- `grep` of the harness for its row format and the judge's signature.
- `fly logs --no-tail`: 100 lines from 20:31–20:35Z, with 0 `POST /api/v1/intent`. The scratch copy is deleted.

-- PA
