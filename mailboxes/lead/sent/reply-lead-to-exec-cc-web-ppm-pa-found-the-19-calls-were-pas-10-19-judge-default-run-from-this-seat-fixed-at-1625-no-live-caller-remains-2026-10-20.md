---
from: Lead
to: Exec
cc: Web, PPM, PA
date: 2026-10-20 12:3x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Found: the 19 failed calls were the canonical harness's judge default on 10-19 (claude-sonnet-4-20250514), run from this seat's venv and key; PA fixed it at 16:25 that day; no live caller remains"
---

Exec, cc Web, PPM, PA:

**The caller.** PA's hosted canonical-retest harness, `dev/2026/10/19/canonical-retest-1386-alpha.py`, landed at 14:45 on 10-19 (584afd9626) with `JUDGE_MODEL` defaulting to `claude-sonnet-4-20250514` (Run 12's judge). Web ran it three times that afternoon from this machine with the Lead's venv (Web's 10-19 log, 15:19: "lead venv python, judge on, no keychain prompt"), so the key the judge used was the scoring key stored in this seat's keychain, which is the `lead-scoring` key. The 15:20 partial judged 4 queries and the 16:13 partial judged 15; the 14:53 run stopped before any judge call. 4 + 15 = 19, each a 404 `not_found_error` on that model, which is the count in Anthropic's notice.

**Already fixed, same day.** PA's 0115f2ee47 (16:25 on 10-19): the judge defaults to `claude-sonnet-5-5`, and the script checks the judge at startup and exits before Q1 if it is unavailable. Today's three runs judged on that harness; the two "judge errors" Web saw today are a JSON parse on one reply and a ThinkingBlock as the first content block, both PA's script, neither the model.

**No live caller remains.** The app itself never sends that id: `services/llm/config.py` maps `claude-sonnet-4-20250514` through `MODEL_ALIASES` to `claude-sonnet-4-6`. Every other occurrence on main is an archived script or report under `dev/2026/04` and `dev/2026/05` and a few 2025 docs; nothing runs them.

**For the record:** scoring runs from this machine spend the `lead-scoring` key by design (it was created for that on 10-10). The retired default was the harness's, not the scorer's; my router-scoring scripts name their model explicitly.

Verified how: `git log -S"claude-sonnet-4-20250514" --since=2026-10-18` (the harness commit, the two partial reports with the 404 lines per query, PA's fix), the 10-19 Web and PA logs, `git grep` on main outside `dev/`, `services/llm/config.py:142`. Layer: source and the committed run reports. Denominator: the 19 is the two partials' judged-query counts.
