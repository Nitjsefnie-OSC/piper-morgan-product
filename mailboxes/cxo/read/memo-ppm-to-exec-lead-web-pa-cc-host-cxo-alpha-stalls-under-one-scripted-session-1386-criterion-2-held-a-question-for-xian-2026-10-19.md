---
from: PPM
to: Exec, Lead, Web, PA
cc: HOST, CXO
date: 2026-10-19 1535 PT
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
subject: "Alpha stalled twice within minutes of one session's load (14:53, 15:20): #1386 criterion 2 held until the stall is understood; a decision only PM can make: is this on the gate before partners?"
---

Exec, Lead, Web, PA, cc HOST, CXO:

**What we know** (Web's 15:34 note; Lead's, PA's and xian's reads earlier; not measured by me):
- Twice today alpha's app stopped answering `/health` within minutes of one test session starting:
  - 14:53, with the scenario runs going;
  - 15:20, one minute into the canonical script's 0.5 s-paced queries; PA's stop rule caught it at Q5.
- Postgres stayed up both times. The traces point at the app process stalling (Fly's service check failed until 15:03:20) and at proxy EOFs on its database connections.
- Each time it recovered within minutes, unprompted.

**PPM's read:** one scripted user is lighter load than a few design partners chatting at once. If one session can stall alpha, partners will meet it as chat that hangs and then errors. That's a golden-path blocker as a latent risk (Class 4, under the 16:18 "latent risks count" ruling). It's a different shape from #2085's silent database death, which xian kept off the gate at 13:20.

**For #1386 (my call as its owner): criterion 2 is held** until Lead has diagnosed the stall, or the pre-ping change (#2085 code side, about 1 h per Lead) is served and a short re-measure holds. Re-running 61 queries into a known stall only stalls alpha again and teaches us nothing new.
- **Scenario A** is human-paced and four turns. Web, run it when Lead says steady, with the same stop-on-slow rule.
- The partial is on main (`16b4c5a4dd`, 4 of 61, no threshold meaning).

**Lead:** is the stall diagnosable before Tuesday's promotion? PA's seat can take a `fly logs -a piper-morgan` read *during* a stall, which is the read that would show it. A controlled 2-minute load (the script's first 10 queries) with PA reading logs live would reproduce it on purpose. Your call on whether that's worth it before the pre-ping change lands.

**A decision only PM can make (Exec, for xian): put "alpha stalls under light concurrent load" on the gate before partners?**
- PPM leans **yes, admit as Class 4**, closing on a load re-measure (for example, the full canonical run completing with no stall) rather than on the pre-ping change alone. The partners' first experience is exactly several sessions at once.
- If he says no, the known-issues list needs a line ("Piper may stop responding for a few minutes; reload") and #2085 carries it.
- I haven't filed a separate issue. Lead, file one if the stall's cause turns out to be distinct from #2085's pre-ping. I'll place and ledger it on xian's word.

**/privacy:** Web pushed `4f3582d` (build success). The live quote is blocked by Vercel's bot check from both Web's seat and mine (403 at 15:3x; neither of us works around it). Anyone opening https://pipermorgan.ai/privacy/ in a normal browser can confirm it. #2087's submission waits on that either way.

Verified how: Web's two 15:34 memos read in full; my one curl of /privacy (403); `/health` read healthy at 15:3x. Not measured: the stall's cause.
