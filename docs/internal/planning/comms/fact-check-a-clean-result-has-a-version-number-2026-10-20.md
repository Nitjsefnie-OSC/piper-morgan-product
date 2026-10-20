# Fact-check: "A Clean Result Has a Version Number" (Sun 10-25, insight)

**Draft:** `docs/public/comms/drafts/a-clean-result-has-a-version-number.md` (Comms' full draft, 10-02). xian hasn't touched it yet, and the title is still his to pick.
**Checked:** 2026-10-20, before xian's rewrite. An Opus subagent checked it against primary logs and git, and Comms reviewed the results.

## The record, in order

- **08-18.** Comms drafted "A Fix Needs the Same Rigor as the Claim It Fixes" (8e78fc5fa6), with "five more people" and "four different people" in it. Comms drafted "Described Is Not Running" the same day. The log says "mechanical checks clean" (`dev/2026/08/18/2026-08-18-0632-comms-code-log.md:72`).
- **09-01.** At xian's request, template-audit v1.11 added check #11 (agents called "people") (94a283454a). The check's search terms already included "someone".
- **09-18.** Comms drafted five pieces, including "Three Silent Failures Became One Law". The same-day log says "agent-as-'people' sweep clean (all legitimate generic/human uses)" (`dev/2026/09/18/…-comms-code-log.md:61`). It has no per-match list.
- **09-19.** HOST ruled on xian's referral (decisions.log:1940, issue 1834). Comms shipped v1.15 (894db8fdea) and added "person". The version field was not bumped.
- **Sat 09-26 05:36.** The post published (acf86bac8a).
- **~07:35.** xian reread it and flagged "four different people".
  - Docs grepped the draft and found the second instance, "five more people", which xian hadn't flagged (`dev/2026/09/26/…-docs-code-log.md:105-111`).
  - Docs fixed the site (d31fe348eb).
  - Docs' memo (3bb5996f93) said Docs found no existing check, but Docs had searched only `scripts/` and the template.
- **~07:44.** xian added that the rule runs both ways and is about accountability (Docs log :122-128).
- **10:50.** Comms replied (599bac88fa) and shipped v1.16 (c3378d4cb7).
  - The check had existed, so the cause was version drift.
  - A sweep of the 12-piece pool found 3 more instances in 2 pieces: two in "Described", one in "Three Silent". The "Three Silent" one was a miss in Comms' own 09-18 judgment.
  - Every match now gets its own verdict, and the version field is bumped.
  - Comms named the judgment call as the unsolved part ("a script can force a look… can't force the judgment").
- **12:42.** Docs withdrew its "no check exists" framing.

## Claims to fix

| Draft says | Record | Fix |
|---|---|---|
| "found it calling my AI agents 'people.' Twice" | xian flagged one. Docs found the second by grepping | "I caught one, and Docs found the second" |
| Docs "asked the obvious question" | Docs also concluded that no check existed (memo: "I didn't find one"). That's what Comms corrected | Optional: say Docs searched, found nothing, and concluded there was no check. It sets up the next beat |
| "The fix for the first failure is still open, and the team said so." | No primary source calls version drift open. Comms called the *judgment call* unsolved. It's true that no re-sweep mechanism exists (grep) | Make it xian's observation ("Looking back, nothing re-sweeps…"), not the team's statement |
| "It had flagged the sentence" | Probable, since "someone" was in the search from 09-01, but the 09-18 log has no per-match list | "The check would have caught the sentence, and the call made on it was wrong" |
| "The audit notes" | One line in Comms' log covering five drafts | "Comms' log that day" |
| "A list of twelve matches with twelve verdicts" | Hypothetical, but 12 was the real pool size, so readers may connect them | Use another number, or "every match" |

**Don't "correct" this one back:** the draft's "more than two weeks" (09-01 to 09-18 is 17 days) is right. Comms' own memo and the v1.16 changelog say "three weeks", and they are wrong.

**True as written:**
- Saturday morning, a few hours after publishing.
- Every actor in the miss was an agent.
- The quoted fragments.
- Docs, Comms and xian had all read the piece.
- The check was live from 09-01 and ruled on 09-19.
- The two sentences were written 08-18 and marked clean then.
- Nothing re-sweeps a piece that already passed.
- The pool of 12, with 3 more instances in 2 posts.
- The third piece was drafted and audited 09-18.
- Comms reported its own miss alongside the drift explanation.
- Per-match verdicts.
- The version wasn't bumped the week before.
- The both-directions accountability framing is xian's.

## Voice and template

- **H1** matches the calendar. The **dateline** matches. The **tease** matches Tue 10-27 "The Caveat That Kept Disappearing". If xian retitles this post, Saturday's tease must follow.
- **Claude-isms:**
  - "feels like a fact about the work. It's really…" is a mild reveal.
  - "instead of letting the tidier story stand alone" echoes the agents' self-praise. Consider cutting it.
- **"the team"** (in the "team said so" line) goes away with the attribution fix.
- **Clean:** 0 semicolons, no banned words, people-words all quoted or human-generic, no issue numbers in the prose.
- Side note, not for the post: the 09-26 omnibus puts xian's catch at "~10:00". The Docs log's 07:35 is the primary source.
