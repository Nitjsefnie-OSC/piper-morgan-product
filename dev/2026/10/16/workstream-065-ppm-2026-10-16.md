# Workstream Review — Ship #065 (PPM)

**Window**: Friday 09 October → Thursday 15 October 2026
**Filed**: 2026-10-16 09:3x PDT

## One paragraph, if that's all PM reads

The beta gate went from 14 open MVP issues to 6 across the window. That came from 12 closures, most of them on served readings of alpha, against 5 admissions and 1 un-admission. Every move is a ledger row. The dates did not move: design partners Fri 10-23 and hard stop Fri 10-30 held all week, and all seven slip entries so far moved 0 days. The Wednesday tripwire closed on the number, with no slip: 90 pattern literals, 29 of them a ruled permanent floor. What is left on the gate is the GitHub recovery path (#2017/#2018), two honesty items (#1913, plus #2048 from today), the Epic 0 epic (#1595) and the close-out gate (#1386).

## What moved

- **The gate, 14 → 6.**
  - **Closed (12):** #1969, #1951, #1978, #1886, #1623, #1579, #1860, #1843, #1771, #1965, #1889, #1783.
  - **Admitted (5):** #1969 and #1978 (each admitted and closed within the day); #2012 (Class 3, Test reported "successful" on a revoked grant); #2017 and #2018 (Class 4, a GitHub user with a dead grant cannot recover from the UI).
  - **Un-admitted (1):** #1943, to Production once xian held the `clear_todos` flip.
  - **Arithmetic:** 14 + 5 − 12 − 1 = 6, matching the criteria line on 10-15 21:33.
- **Slips, 3 → 7, 0 days moved.**
  - Entries 4 to 7: #1969, #1978, #2012, and #2017/#2018.
  - xian ruled on 10-12 that an in-and-out admission does not count against the 10-09 hold.
  - Every admission carried his word, through Exec, through Janus, or directly on 10-15.
- **The ceiling, 127 → 90 (35 lists).** These are my own recounts after each landing. The FILE_REFERENCE deletion (30 literals, ruled inert by Arch) took it from 120 to 90 on 10-13. The Wednesday 10-14 reading:
  - 29 literals are the ruled floor (#1974);
  - 61 are router-quality, and Lead's Option 3 run found none that misroute a day-one turn;
  - xian ruled Option 1 plus Option 3. No slip.
- **Product rulings carried to xian and recorded:**
  - **Bulk delete:** hold the flip, soft delete as the fix (#2021, which I filed, with a 7-day undo), and one item at a time as the interim cap (#2019).
  - **#888 escape words:** END and PAUSE split; `skip` is not an escape word (decisions.log).
  - **MCP, plugin and BYOC** are not on the MVP critical path (#2005 placed Production).
  - **The LLM-narration class:** filed #2042 when it reached its second served instance. Arch concurs: track the class, gate the instances. xian ruled it on 10-16.
- **A new placement practice, written into the gate standard on 10-16.** A child issue that blocks an admitted MVP parent goes on Production, "gated through" the parent, rather than being admitted twice. I used it four times on 10-15 for the GitHub recovery path (#2029, #2031, #2039 under #2018; #2037 under #2012).
- **Placement.** About 60 new issues placed with milestone and board entries as filed, among them #1975–#1994, #1995–#2005, #2007–#2023 and #2024–#2044. No open issue was left unmilestoned at any day's close.
- **Smaller pieces:** the PPM role card (10-13); the Production-vs-MVP and known-issue-disclosure practice note for HOST (10-13); the five-skills concept page for CIO (10-14).

## What didn't move

- **The dates.** They held; that is the intent, not a stall.
- **#1913 and the epic #1595.** They are open on the gate. I have not verified a closing proof for either.
- **Lead's Monday 10-12 reconfirm of main.** I owe a rule (c) ledger row against it, and it never arrived.

## Progress toward milestone status, not activity

- **Instrument:** `scripts/ppm-criteria-line.sh` at each day's close, and `gh issue list --milestone MVP --state closed` for the 12 closes.
- **Net:** 8 fewer open MVP issues. Unlike last week's fall from 28 to 14, which was mostly triage rulings, this week's fall is mostly closures on served or source evidence:
  - four served on alpha after the 10-15 promotion (#1771, #1965, #1889, #1783), plus #1843 on a served reply on 10-14;
  - the rest on Lead's and Arch's acceptance criteria.
- **Whose work:** the closing work was Lead's, Web's (served runs), CXO's and PA's (judgments), and xian's (S5). Mine was the admissions, the ledger, the placements, and putting the decisions to xian.
- **Caveat:** I did not rerun any served check myself.

## What I'd want PM to know that isn't in a bullet above

- **Two fires did not run** (10-10 21:33 and 10-11 06:33). I wrapped 10-10 late and told Exec. The cause was never investigated by me.
- **Two stale claims of mine, corrected the same day:**
  - 10-13: I said a floor ruling was still pending when Arch had already ruled. I had written from an old sync, and now re-fetch before writing "pending".
  - 10-15: I said #2014's counts were still owed when you had run them on 10-14 (0/0).
- **One silent tool failure.** A BSD `sed` insert into the ledger failed with no error (10-12). I caught it by reading back, and now insert with python.
- **One denied write.** On 10-14, my GitHub write to admit #2012 on a Janus relay was refused by the permission classifier. I did not work around it; Exec made the write on your word.
- **Relay latency.** Your 13:18 promotion approval on 10-15 reached Lead about 2h12m after I mailed it. Mail wakes are not fast enough for a time-critical word. The standing promotion grant now in force (10-16) removes most of that.

## What a user can do this week that they couldn't last week

Nothing from my lane directly. The user-visible changes behind this week's closes were Lead's, with copy by CXO; Web and PA served-checked them on alpha `6f2916d10f`. Examples:
- the standup offers to come back later instead of abandoning (#1771);
- GitHub-backed standup and radar say when a source failed, instead of rendering empty (#1965/#1889);
- a long issue list is capped with "show me the rest" (#1783).

## Next week (10-16 to 10-22, the week before design partners)

- **Intend to land:**
  - ledger every served close after today's promotion: #2048, then #2017/#2018 when S5 and the recovery path pass;
  - place everything filed the same fire;
  - a gate readiness read for 10-23, stated as which classes are open, and sent to Exec. I propose no date.
- **Blocked on (all xian, via Exec):**
  - the #2054 admission (Class 2, cross-user principal; asked 10-16);
  - S5 for #2031's no-token card.

*Corrected 2026-10-16 09:5x (Exec): an earlier version listed the machine account's GitHub login as blocked. xian created it on 10-15, Web built both alpha test accounts that afternoon, and S5's OAuth leg passed on it. My carried deferral was stale.*

**Verified how:**
- **Method:** read the day arcs of my seven PPM logs (10-09 through 10-15); the slip-ledger rows and paragraphs in `beta-gate-standard.md` for the window; and `gh issue list --milestone MVP --state closed --search "closed:2026-10-09..2026-10-16"`, which gave 14 rows, 12 inside the window plus #2040 and #2012 on 10-16.
- **Layer:** my logs, the ledger and the tracker. No fresh probe of alpha.
- **Denominator:** 7 of 7 logs; 12 of 12 window closures named.
- **Not re-measured:** Lead's, Arch's and Web's figures are quoted.
