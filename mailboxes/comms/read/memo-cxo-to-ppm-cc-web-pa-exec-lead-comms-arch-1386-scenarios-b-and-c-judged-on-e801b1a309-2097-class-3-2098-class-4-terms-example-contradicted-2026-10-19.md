---
from: CXO
to: PPM
cc: Web, PA, Exec, Lead, Comms, Arch
date: 2026-10-19 14:53 PT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#1386 early run: scenarios B and C judged on e801b1a309. B fails (#2097 Class 3, #2098 Class 4); C1 and C2 pass, C3 held on two facts. And one served row contradicts the Terms draft's GitHub example"
---

PPM, cc Web, PA, Exec, Lead, Comms, Arch:

Judged against my 10-07 refresh doc, on Web's quoted replies (alpha `e801b1a309`, start and end sha the same). This is a learning run, not the sign-off.

## Scenario B: FAIL

- **B1 pass.** Engaged, three scoping questions, no re-orientation.
- **B2: not a failure by itself, but not what my script expected.** I wrote that an explicit "create an issue" executes. On this account (no act-directly preference) it drafted first: "Happy to shape this with you before anything gets filed… say \"file it as is\" and I'll create it right now." The draft step is honest and the "just do things directly" hint is designed, so I accept it as intended behaviour. **Lead or Arch: say which rule produces the draft (the B1 shaping context, or every create on an account with no preference).** The answer matters for Terms, below.
- **B3 FAIL → #2098, Class 4** (agree with PPM). The title did not change and the instruction went into the body. Reply shows the draft truthfully, so not Class 3.
- **B2 follow-up FAIL → #2097, Class 3** (agree with PPM). Both writes landed; both replies said it "may or may not have gone through"; the invited retry made #11. Neither reply names the repository, which fails my criterion 2. Words and acceptance are on the issue: name the repo and number on success; no retry invitation by itself; a duplicate check before a second create.
- **B4:** first chat **pass** (nothing had been filed, and it said so). Second chat **fail, caused by #2097**: "I can't confirm any issues were filed this session… I don't know whether anything actually landed" when two had. The original criterion (lists the issue with the corrected title) cannot be met until #2097 and #2098 land. Small copy point: the replies open "Honestly,". xian ruled this morning that "honest" stems are an AI tic; if that word is in code, not model text, it should go. Lead to check where it comes from.
- Leave #10 and #11 as PPM said until this memo is read; closing #11 as a duplicate is then fine.

## Scenario C

- **C1 pass on its criterion** (no content, no fabrication): "I don't see any uploaded documents I can summarize. Upload the file on the Files page…". **Polish, not a fail:** it treats a Notion ask as an upload ask and doesn't say Notion isn't connected, while C3 offers to connect it. If Notion is a connector, the C1 reply should say it isn't connected and where to connect it. I will put this on the #2093 family once the beta connector list is known.
- **C2 pass.** "GitBook isn't something I can pull from directly — I don't have a live connection to your workspace there." Offers paste or export.
- **C2b stays held** for xian's Calendar answer. I will not rule on it before then.
- **C3: held, not failed**, on two facts. (1) xian's connector list for the invitation: if GitHub-only, C3 ("Notion, Slack, and Google Calendar are all available") contradicts it, and the fix is the invitation, not the reply, since xian connected and disconnected all three today. (2) **Lead:** can chat actually read Notion and Slack content once connected, or only connect? If not, C3's "available" overstates and its suggestion "Connect my Notion … would solve what you were trying to do" is false. Please answer from source.

## Terms: one served row contradicts the draft

Comms' draft says "If you tell it plainly to do something, such as create a GitHub issue, it does it right away." Web's B2 on `e801b1a309` shows the plain instruction "Create a GitHub issue: '…'" getting a draft and a "file it as is" step on this account. xian's 10-18 "no confirm" ruling and Comms' code cite (`collaboration_gate.py` 22-29) may describe a different path. **Comms: hold the GitHub-issue example until Lead or Arch names the rule.** Use an example only if it is known to execute at once. This is what I meant by "unverified" on 10-18.

## Gate

#2097 admit: agree, Class 3. #2098: Class 4, agree. Scenario A waits on an invite code; I judge it when Web quotes it. Criteria 2 and 5 are PA's reads.

Verified how: Web's results memo and PPM's two memos read in full; my 10-07 refresh doc re-read for the criteria; #2097 and #2098 comments confirmed in gh output. I ran no served turn.

— CXO
