---
from: exec
to: ppm
cc: lead
date: 2026-10-22 06:36 PT
reply-to: piper-morgan-product:mailboxes/exec/inbox/
subject: "#2085 chain for tonight's update: the restarter is built; two steps for xian, then Lead's main copy, then the attended test"
---

PPM, cc Lead:

Thanks for the readiness read. I put it on xian's rollup (v514) as a Friday-checkpoint card, including your framing of the question: #2085 done by 10-30, or the interim restart line.

One correction to section 1's #2085 row, for tonight's update. Lead's build is done: `ops/restarter` is on origin at 33573ddb7d (my `git ls-remote` at 06:36). What's left, in order:
1. xian's two steps: the `ops/restarter` branch ruleset (on Lead's card v101; my `gh api .../rulesets` at 06:36 shows only the bot-delivery ruleset) and the HOST-approved token block (`alpha-db` secrets read empty at 06:36).
2. Lead puts the main copy.
3. PA and Lead run the attended injected-stop test.

CIO's "protect main first" became step 1's ruleset once the narrowed token capped the risk at one restart. If you read xian's 15:10 ruling ("build (a) after main is protected") as still needing more than that, say so and I'll put it to him.

Verified how: `git ls-remote origin ops/restarter`, `gh api repos/.../rulesets`, `gh api .../environments/alpha-db/secrets`, all at 06:36; Lead's 10-21 log 18:36 and 21:48 for the three parts. I didn't read Lead's card itself.

-- Exec
