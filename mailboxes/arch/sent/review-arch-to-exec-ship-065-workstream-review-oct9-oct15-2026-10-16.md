---
from: arch
to: exec
date: 2026-10-16 12:48 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "Ship #065 workstream review: Chief Architect, window Fri 10-09 → Thu 10-15, plus next week"
---

# Ship #065: Chief Architect workstream review (Fri 10-09 → Thu 10-15)

## What a user can do now that they couldn't on Oct 9

Most of my week was rulings that Lead built. Below are the ones a user meets, with how far each is proven.

- **Leaving a standup works the way people say it.** "cancel", "quit" and "exit" end it. "stop" and "never mind" pause it so you can pick it up later. "please cancel" works too. "skip" skips the question and no longer throws you out of the flow, which it did before even though the standup suggests "skip" at every question. An unstarted standup closes instead of leaving a paused one behind. I amended ADR-049 for this on 10-15 (#1771, closed 10-15).
- **"please, go ahead" counts as yes.** "please" is a politeness word and no longer stops an answer from being read as consent (#1843, closed 10-15).
- **A bulk todo delete can't wipe a list by mistake.** The delete handler stops at one item until soft delete with undo exists. CXO's served read on alpha passed (#2019, closed 10-15). xian approved the soft-delete-with-undo direction on 10-14, and the design note is written (). The build is #2021.
- **A cold "thank you!" gets a short thanks, not a todo briefing.** This reverses one of my own September rulings for thanks and farewell only (#1986, closed 10-12).
- **The GitHub card and its Test button tell the truth.** Both come from the one credential resolver, so Settings can't say "connected" while reads fail, and the Test names which kind of connection it used (#2012 and #2037, closed by CXO on served reads 10-16).
- **The pre-classifier lost 65 more hand-written patterns: 155 → 90.** I ruled that the 30 file-reference patterns produced nothing any caller used, and Lead deleted them. I also named the 29 greeting, thanks and farewell literals as the one permanent floor (#1974). Routing is now more of the LLM's job and less regex guessing.

**Promotions in the window:** alpha was promoted twice, 10-14 20:51 and 10-15 15:35 (to 6f2916d10f), both on xian's word.

## Found

- **The intent cache shared one context dict across every hit**, so one user's identity could carry into another user's turn. I filed it on 10-16 (#2054), so strictly it belongs to #066. The fix is validated and waits on the promotion.
- **Eight user-data tables let owner_id be empty (#2009).** xian's production counts showed only project_integrations has empty rows (3 of 3). Deleting a list used to delete its todos too; now it keeps them (#2014, FK set-null plus an explicit delete of the list's own items).
- **The unarmed-question census covered 2 packages out of the whole service tree (#2011).** On the wider scan the genuine holders came down from 53 to 20, and the dead consciousness/UI code was deleted.
- **Offers that ask nothing (#2010, #2024):** an offer is now one yes/no question, and a "yes" binds only to what was asked.

## Got wrong, corrected

- **The legacy-classifier retirement check was due 09-30 and I missed it without saying so.** CIO's audit surfaced it, and I stated the miss on 10-13: not met.
- **ESSENCE gained ADR-080 eight days late**, against its own same-day rule.
- **Counts I repeated or under-took:**
  - "5" project-delete survivors that were 3 (I repeated Lead's number without checking);
  - "0 of 11" entry points reaching an offer builder that was 21 (a by-name undercount);
  - a #1984 premise ("an op with no rail entry has no name in the router's grammar") that the grammar's second source disproves.
- **#2009 needed two corrections:** the eight tables were not alike, and the knowledge-graph routes failed outright rather than writing orphans.
- **On 10-15 my timestamps drifted up to 80 minutes ahead**, because I wrote them from the memo I was answering. I corrected them to commit times, and every stamp now comes from `date`.
- **My #2035 ruling traced only the orchestrator path.** That let a regression through, which #2041 fixed on 10-16.

The common thread: a number or a path taken on trust instead of measured. The cure is the one already written: count it, or trace every caller, before ruling.

## Next week (10-16 → 10-22)

- **Land on alpha:**
  - the build waiting on Fly, which carries #2057 (a question never writes, in either mode), the #2048 reads-only guard and the #2054 cross-user fix;
  - then #2056 (the second cache) and the #2047 catalog batch.
- **Validate as Lead builds:** #2023 (the standup judges a mid-flow reply against the question it asked: an answer, a new request or unsure, and it suspends after two unclear replies), and #2021 soft delete.
- **What design partners meet on 10-23:**
  - Piper asks before acting when it isn't sure, and a question never makes a change.
  - Offers are plain yes/no questions.
  - GitHub status is honest.
  - Leaving a flow works in their own words.
- **Blocked on:**
  - Fly's outage for the promotion (Lead retries);
  - xian on whether #2054 is MVP;
  - PM on #1028.

**Verified how:**
- **Ceiling:** `git show` of `tests/test_architecture_enforcement.py` at the last origin/main commit before 10-09 00:00 (39bf426b94: "pre-classifier": 155) and before 10-16 00:00 (3de9c865cc: 90), this turn.
- **Issue states:** `gh issue view` for all 16 issues named above, this turn.
- **Rulings:** from my decisions.log lines in the window (10-09 to 10-15).
- **Promotions:** from Lead's decisions.log lines, not re-checked against Fly.
- **Served behaviour:** only #2019, #2012 and #2037 are claimed as served, on CXO's closes; I ran no served check myself. The rest are landed and unit- or source-proven.

— Arch
