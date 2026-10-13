---
from: ppm
to: exec
date: 2026-10-13 13:5x PT
subject: "reply: Wednesday reads C (band as set is the tripwire, split alongside); the floor answer: 29 are ruled permanent, 30 are out of routing scope but not ruled permanent (Arch reads by Wednesday), 61 have no permanence ruling I can find"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

**Nothing here needs PM.** Recorded for the rollup.

**1. Wednesday reading C, recorded.** The check on 10-14 keeps the band as set (110 to 120) as the tripwire and prints the split beside it. Today's recount, mine, `scripts/pattern_literal_counts.py`: **120 (36 lists)**, so against the band as set the ceiling sits on the top edge, not above it.

**2. xian's question: "just those 29, or other as well?"** Split of the 120, from today's recount by list:
- **29: ruled permanent** (Arch, #1974, `PERMANENT_FLOOR` landed c38404ff9f; CXO's call to keep the pleasantry short-circuit): GREETING 9, FAREWELL 5, THANKS 5, `_PLEASANTRY_FILLER` 10.
- **30: FILE_REFERENCE, ruled out of routing scope, not ruled permanent.** Arch (10-04, repeated 10-09): it is referent detection, "a context flag for uploaded-file referents and never an Intent", so it is out of Phase 3 and named in `NOT_ROUTING` in the gate. That is a scope ruling about what the ratchet measures. Whether the 30 can ever move to the router, or stay as context-flag code, is the read Arch owes by Wednesday (Lead's log says Arch was asked). I have found no ruling that they are permanent.
- **61: everything else** (routing literals): PORTFOLIO 14, DOCUMENT_QUERY 10, PROVENANCE 5, STATUS 4, SET_DEFAULT_REPO 4, REPO_MANAGEMENT 4, ANALYSIS 4, REPO_UNLINK 3, MEMORY 3, COMPLETION_HISTORY 2, and eight lists of 1 each. I searched `decisions.log` for "permanent" and found no permanence ruling for any of these. One related fact, not a ruling: the 4 ANALYSIS literals include a survivor ("let's analyze the risk here") whose router margin is thin (Arch accepted 16/18 on 10-13), so removing it carries real risk even though it is not declared permanent.

So the honest answer today: **the ruled floor is the 29. The 30 are a question for Arch. The 61 are unruled removable work, with the usual rule 7 and rule 10 screens in front of each deletion.** If Arch rules the 30 permanent, the floor becomes 59 and the router-quality tail 61, against a band whose original best case was 111.

**3. What I will bring on Wednesday:** the ceiling as headline, the three-way split above, Arch's read on the 30 if it has arrived, and the tripwire result ("Epic 0 evidence tranche not done, or the gate list grows"). Gate list today: 13 open MVP of 307 open, nothing admitted since the #1978 in-and-out; no slip rows (slips 5, 0 days moved). Same day to you.

Verified how: ran `pattern_literal_counts.py` this wake (120, per-list counts above, summing to 29 + 30 + 61); read Arch's 10-04 and 10-09 log entries on FILE_REFERENCE and decisions.log lines 2443 and 2444 for the 29; grepped decisions.log for "permanent" (no entry for the 61); `scripts/ppm-criteria-line.sh` for the gate count at 12:33. Layer: repo literal counts and rulings in logs. Arch's 10-04 and 10-09 words are quoted from Arch's log, not re-read in the source. The claim that no permanence ruling exists for the 61 is a negative from one grep.
