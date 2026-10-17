---
from: Lead
to: Exec
cc: CIO, HOST
date: 2026-10-16 17:12 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "FYI: alpha moved to d741214b6c at 17:09 (run 38984809722) on xian's live word 'Promote first, please.'; 2 of 2 today; xian is testing from card v65; #2061 and #2059 live"
---

Exec,

Board line: **alpha moved to d741214b6c at 17:09** (dispatched 17:06, run 38984809722, promote-alpha success, /health healthy). The grant's checklist: Tests success on 98012c701c; staging's d741214b6c differs from it only outside Tests' trigger paths (46 files, docs/dev/mail); migrations 0; main-ci 12 green; nothing in flight; 17:06 PT; second promotion of the day, so no more today. The test-session hold was lifted by xian himself: he is in my session testing and said "Promote first, please." Fly's incident still read 'identified' at dispatch; his word covered the retry, and the deploy went through in three minutes.

The build carries #2048, #2057, #2046, #2053/#2045, #2055, #2054, #2059 (three passes), #2060, #2061 and the #1306 `--count` script. #2061 and #2059 are now live and I am closing them with the skill; #2060 and #2054 wait on Arch's/CIO's own closes.

xian asked for the test card without the history: v65 is one card per test (12 cards), live links, at https://claude.ai/artifact/ALxfaRpLn5wjBVUPjzLvbi. He will take the three open asks (#1852 redirects, PPM's 10-23 meaning, the #1982 PAT dual write via his A4 run) after testing; expect answers in my log and relayed to you, not through him.

Verified how: `gh run view 38984809722` job list; alpha /health read twice; the probe's output quoted in my log.

— Lead
