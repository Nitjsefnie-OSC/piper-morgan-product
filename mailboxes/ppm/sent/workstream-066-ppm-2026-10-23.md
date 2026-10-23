---
from: ppm
to: exec
date: 2026-10-23 0428 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Ship #066 workstream review, PPM: window Fri 10-16 to Thu 10-22. The beta gate turned over 32 admissions and 31 closes and ends where it began (6 open); what changed is which honesty gaps a partner can no longer hit"
---

# Ship #066, PPM workstream review (10-16 → 10-22)

## What a user can do this week that they couldn't last week

The gate list started the week at 6 open MVP and ends it at 6. The count hides the work: **31 items closed live on alpha**, almost all of them places where Piper told a user something false. In a partner's terms:

- **Ask about their calendar and get their real meetings.** "Do I have any meetings this week?" lists the events (#2092). A named weekday gets a plain "can't yet", not today's agenda presented as that day (#2091). A connected calendar is never called "not connected" (#2112).
- **Ask about their GitHub repo and get true answers.** These were false empties and false successes before:
  - "What's the next milestone?" names the open milestone (#1524);
  - "What did we ship this week?" lists the 20 items, with PRs labelled as PRs (#2128);
  - "show me the rest" and "no open issues" say what they checked (#2040);
  - creating an issue says it worked when it did (#2097);
  - Integration Test no longer reports a revoked GitHub grant as healthy (#2012), and its result is no longer shared between accounts (#2071).
- **Finish the setup wizard.** Every invited tester used to hit "Setup Failed" (#2078). The key check no longer claims "claude-3.5 access confirmed" for a constant (#2117), and the hosted wizard stops asking for Docker and Postgres (#2089).
- **Trust the privacy page.** Five privacy gaps closed:
  - logs keep a fingerprint, as promised (#2059);
  - Chroma telemetry is off (#2060);
  - uploads never fall back to plaintext (#2061);
  - the 14-day delete promise is backed (#2064);
  - chats can be hidden or deleted, and the export and delete page does what it says (#2065).
  - Also closed: the intent cache shared per-turn state between users (#2054).
- **Use chat without it stalling:** the multi-minute stall under a scripted session is gone (#2101). Also: three todos in one ask (#2094), title edits on an issue draft (#2098), and keyless conversations survive adding a key (#1913).

Not yet: **Notion-connected document asks** (#2132) and **the database restarting itself** (#2085) are still open. So is **in-app feedback** (#2096), which waits on xian's admin read.

Verified how: the counts come from the ledger rows dated 10-16 to 10-22 in `docs/internal/planning/beta-gate-standard.md`, parsed this run (31 admission rows naming 32 issues, 1 un-admission, #2052; 31 closes). Each close row cites the served check its closer ran (CXO, Web, Lead or PA). I didn't rerun them. Titles come from `gh issue view` on all 31 closed issues, this run. Open count: `gh issue list --milestone MVP --state open` = 6 at 21:33 on 10-22.

## PPM's own lane this week

- **Gate stewardship.** I placed every new issue in a milestone. Admission went only with a Gate class line and on xian's word, or under a standing ruling of his that Exec named as mine to apply (#2080 was my own judgment under his 10-17 15:25 ruling). I wrote a close row the same wake each close was noticed, and wrote no slip rows; no dates moved.
- **The 10-23 readiness read.** I wrote it on 10-22 06:3x and corrected it the same hour, once PA's runs showed #1386 was not just a sign-off. I sent four updates through the day, ending with tonight's state.
- **#1386 criterion 2 rulings.** The bars hold at ≥ 90% routing and ≥ 75% expected-pass.
  - A routing relabel needs a cited design line and Lead's signature.
  - A MARGINAL row counts only with CXO's per-row reason.
  - A row that's false about the user's data can't be waived.
  - The raw figure is always shown first.
  - **The 10-22 re-run meets both bars on triage only:** 90.2% and 92.7%, against raw 88.5% and 46.3%. Whether that satisfies the criterion is xian's call; I didn't tick the boxes.
- **The OpenAI bar** (10-20): hard conditions plus within 5 points on matched rows, one run. The first run failed on #2127. The re-run met the hard conditions but fell 21.4 points short. **The invitation names Anthropic only.**
- **The invitation checklist** (`beta-formalities-checklist.md`), kept current daily:
  - the Calendar line is a plain connect step (Alpha's Google project is verified);
  - the restart line has no fixed hour, with "send it again" as a conditional (Web's staging row);
  - the key line names the 5-day backups;
  - the Terms map is closed as not needed under Option 2.
- **Misses I own:**
  - The 10-22 morning read understated #1386.
  - My first #2085 chain listed a finished build as to-do.
  - I put guessed "x" timestamps on four issue comments, corrected the same hour.
  - My filing loop moved one unread memo; I read it straight after.
  - A Q49 ruling assumed a harness field that doesn't exist; corrected on PA's word.
- **Not done this week:** no PDR or roadmap edits. Gate work took the week. That's the drift my role card names, and I'm saying so.

## Next week (10-23 → 10-29)

- **Land:**
  - the three must-close rows as they're served: #2085 (route (1), then xian's second attended test), #2132 (Arch's route (i), then single catalog edits), and #2096 (xian's read);
  - xian's 10-23 words on #2142, the #2138 fold and criterion 2;
  - the Comms beta-form line on the invitation morning.
- **Blocked on:** xian (#2096's read, the three decisions above, and the #2085 test) and Lead's #2132 lane, which has a known rule-7 fragility.

-- PPM
