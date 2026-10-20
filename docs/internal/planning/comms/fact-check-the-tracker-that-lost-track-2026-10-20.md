# Fact-check: "The Tracker That Lost Track" (Thu 10-22)

**Draft:** `docs/public/comms/drafts/the-board-that-stopped-matching-reality.md` (Comms' full draft, 2026-09-18). xian hasn't touched it yet.
**Checked by:** Comms, 2026-10-20, before xian's rewrite. On the Phantom Feature, the facts reached xian too late. This one gets checked first.
**Primary sources:**
- Lead's 08-16 log, `dev/2026/08/16/2026-08-16-0642-lead-code-log.md`, the entries from ~22:2x to ~23:0x.
- The evening fire headings in all 08-16 session logs.

## The record, in order (what xian can write around)

1. **21:47 to 22:27, Sunday 08-16.** Six agents closed their day as quiet:
   - Lead (21:47, "quiet WATCH, day closed")
   - Web (21:52 STOP)
   - PA (22:12 STOP)
   - CXO (22:17)
   - PPM (22:22 STOP, "Six clean fires")
   - Docs (22:27 day close, "genuine idle")

   That is more than half of eleven.
2. **~22:2x.** xian sent Lead the MVP board as a TSV (60 items) and asked three questions. Lead's log doesn't record what the questions were.
3. **Nine closures.** Each one rested on "PM's own live-transcript evidence *or* direct code verification":
   - **On xian's transcripts:**
     - 1411 (his own "#109" close ask)
     - 1190 (the same flow is the gate end-to-end test)
     - 1605 (the verb flow passed test rounds 1 and 2)
     - 1566 (reminders surfacing, "relentless")
     - 1491 (reminders surface live)
     - 1562 (clock-honesty pass)
   - **On a deploy or code:**
     - 1603 (the v51 deploy, which "Marked 4 done" exercises)
     - 1557 ("[BUILT] verified in code today")
   - **On an answer:** 1569 (product question answered and shipped)
4. **Board hygiene.** Ten shipped items were still in Backlog. Lead moved them to In Review one item at a time, using the safe per-item mutation. The items were 1617, 1622, 1623, 1625-1628 and 1630-1632.
5. **The backlog wave.** **Lead** dispatched five agents on unstarted, unblocked items:
   - 1544: todos wrongly shown as empty
   - 1567: the repo-answer dead end
   - 1534: the integration-status claim
   - 1597: the live-verification backlog
   - 1615: first-contact polish
6. **~23:0x, first results.**
   - **1544:** the floor prompt's own anti-fabrication examples had seeded xian's misframe word for word. The prompt was rewritten.
   - **1534:** already fixed under 1547. It was verified, not rebuilt.
   - **1615:** the bullets were already fixed on 08-14. That was verified, and the tense half was built.
   - **1278:** **xian closed it mid-turn on his word.** 56 releases had been served, "hosting is the workhorse".
   - **xian** ordered a deploy, a tracker and a test plan once the last lanes landed, and said he would test in the morning.
7. **~23:0x, the last lanes.**
   - **1597:** three old fixes were verified live (1518, 1532, 1529). Inside the **same** lane, 1480 was split: its login-bounce branch failed live. Unit tests had mocked the state, so they could never catch it. It was filed as #1640 with a strict-xfail pin.
   - **1567:** the repo dead end became a bound conversation, with 49 tests including xian's transcript. The uncovered call sites were filed as #1641.
   - **Close of the night:** v57 deployed. The 13-item morning tracker was republished.
   - **Day totals:** 13 closures, 12 board corrections, 10 lanes merged, 3 issues filed, 51 MVP items open.

## Draft claims that are wrong or overstated

| Draft says | Record | Fix |
|---|---|---|
| ¶3 Each of the nine closures was "grounded in something I could point to directly", "evidence sitting in my own memory" | Six rested on xian's transcripts. The rest rested on code, a deploy or an answer that Lead checked | "Most on what I'd seen myself, the rest on Lead checking the code" |
| ¶4 "I dispatched a wave of five items" | Lead dispatched the agents | "Lead dispatched five agents…" |
| ¶4 "walked through the whole board live" | xian sent a TSV and three questions. Lead answered with actions | Fine if xian remembers it as live. Otherwise "sent Lead the board and three questions" |
| ¶6 "What happened after I logged off… Lead kept working the five lanes through the night" | xian was still there mid-turn (he closed 1278 and ordered the deploy). Everything landed within about an hour, by ~23:0x | Drop "after I logged off" and "through the night" |
| ¶6 "while a fourth found one branch of a login flow" | The login-bounce split (1480 to #1640) was inside the 1597 lane, the same lane as the "three old fixes". The fourth and fifth lanes were 1567 (repo dead end) and 1615 | Fold the login finding into the third lane. Name 1567 if a fourth is wanted |
| ¶6 "genuinely live in production" | "verified live" on the hosted alpha | "live" |
| ¶3 "quietly stalled… because nobody had gone back to update status" | The cause isn't recorded | Drop the cause, or mark it as xian's read |
| ¶5 "about forty minutes" | ~22:2x to ~23:0x for the first batch. The deploy came in the same hour | Roughly right. "Under an hour" is safer |
| ¶5 "It outproduced most of the rest of the day" | The daytime work was a merge (1624), a disposal (1633) and the memory-index packing. Most of the 13 closures came in the evening. Team-wide output isn't measured | xian's call. True for closures |

**True as written:**
- The quiet-evening framing, with more than half of eleven agents.
- The sixty-item board.
- Ten Backlog items moved to In Review, one at a time.
- Nine closures in the first pass.
- The five lane descriptions.
- 1544's prompt seeding the misframe.
- 1534 already fixed elsewhere.
- Three old fixes verified live.
- The login branch that unit tests had mocked around, its own issue, and the test pinning it.
- xian closing 1278 on his word with 56 releases.
- The new release and the tracker.
- Thirteen issues closed, about a dozen board corrections, and five stalled threads moved.

## Voice and template items for xian's rewrite

- **Title.** The calendar title is "The Tracker That Lost Track" (xian, 10-19). The draft H1 still reads "The Board That Stopped Matching Reality".
- **Footer tease is stale.** It teases "A Bounded Search Reported as a Total". The 10-24 row is now titled "Mistaking the Inset for the Map". The tease needs the new title.
- **Banned words:** "quietly" (¶3) and "keep it honest" (¶6).
- **Claude-isms (not-X-but-Y reveals):**
  - "not because anything was wrong, but because I hadn't actually looked"
  - "Not what the board said. What I knew"
  - "drifts because checking it takes longer than trusting it, not because anyone means for it to"
  - "What stays with me"
- **Gnomic:** "not the count" in ¶8 doesn't parse.
- **Agents as people:** none. "someone asks it to" refers to a user, and "nobody"/"anyone" are generic.

## Knock-on, fixed today

The Phantom Feature's footer tease (publishing 10-20) said "six hours after most of the team called it a quiet Sunday." The quiet closes ran 21:47-22:27, and xian sat down ~22:2x, so it was minutes, not six hours. Changed to "late on a Sunday night, just after most of the team had called it a quiet day".
