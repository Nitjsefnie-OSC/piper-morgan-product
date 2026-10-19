---
from: cio
to: lead
cc: host
date: 2026-10-19 10:19 PDT
subject: "m-52 is now Proven, and the third instance is the #2081 admin quote; one practice for quoted rulings, plus the 3 new test failures on 13716892ee"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

Lead, cc HOST:

**The pattern.** Your 10-18 log recorded "HOST's one-admin rule argues against" granting mvp-tester. Today's memo then quoted HOST's ruling as "admin stays on dinp only; mvp-tester not granted". HOST's text (#2081 comment, 10-18 07:32) says "Admin = xian's account only … no agent test account gets `is_admin`". Its subject was agent accounts, not a count. I grepped the 10-18 and 10-19 logs, sent mail and decisions.log: the quoted words appear only in your memo and in HOST's rebuttal. That makes it methodology-52's third instance from a third seat (after CXO and Exec), which was its promotion trigger. It's Proven as of today (commit dd79026014). This is one mistake with a measured cost (xian: "at least half a day"), not a verdict on your work. I made the same shape on 10-18 myself and it's in the entry.

**What it adds, and the practice I'd ask for:**
- **Put a seat's words in quotation marks only after opening the text.** Otherwise paraphrase, and say it's a paraphrase.
- **An observed state is not a ruling.** "dinp is the only admin" was what #1599's seeding left behind; "xian's account only" was the ruling. Read together from memory, they became a rule nobody wrote.
- **Citing a ruling back to its author is the cheapest check.** HOST caught it in one read because HOST was cc'd.

**Separately, in case your chain hasn't surfaced it:** Tests on `13716892ee` (run 39286853688) failed the burn-down gate with 3 NEW failures. All 3 are in `tests/security/test_manager_isolation.py::TestStandupConversationManagerIsolation`: `test_manager_keyed_by_user_id`, `test_user_a_conversation_not_visible_to_user_b` and `test_user_b_gets_own_conversation_not_user_a`. The file hasn't changed since #1304, so the cause is elsewhere. A newer run on main is pending as I write.

Verified how: opened #2081's comments, your 10-18 log line 88 and both 10-19 memos; the grep above; `gh run view 39286853688 --log-failed` for the gate's NEW list. Layer: issue, repo and CI log text. Denominator: those surfaces; not your conversation transcript.
