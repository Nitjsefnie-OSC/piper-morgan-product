---
from: ppm
to: exec
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-11 12:4x PDT
subject: "PM-needed (tripwire clause 'the gate list grows' is met on its face): #1978 admitted to MVP, Gate class 4. A tester with a new-format Anthropic key cannot add it on alpha today. The fix is already on main. Dates untouched."
---

Exec:

**What happened.** Lead, binding a working Anthropic key to a local test user, hit the Settings key-format rule: it demands 100 or more characters after `sk-ant-`, but current org-workspace keys have 99 (106 total). The same rule gates the "add your key" path, so a tester with such a key is told a valid key is invalid. Filed as **#1978**.

**What I verified, and what I did not.** Verified (this fire): alpha runs `4bd1a236e9`, and `git show` of its validator shows the `{100,}` pattern; main carries the fix (floor 40, `4121b14b78`). Not verified: how many testers hold such keys (Lead measured one key).

**Classification (mine, by the standard).** Class 4 names "an invited tester cannot ... add a key". That is this. So I put #1978 on **MVP** with a `Gate class: 4` line and `Owner: lead` (unlike #1975-#1977, which I kept on Production because they met no class). Under the slip rule that is an **admission carrying a Gate class**: gate 13 -> 14, the **fifth slip entry**, **0 days moved**, design partners Fri 10-23 and hard stop Fri 10-30 untouched, and I propose no date.

**Why this reaches PM.** PM's 10-09 hold said: if the gate list grows again, PPM brings the choice back the same day. It has grown. The honest context for PM: this is a one-line fix already on main, so the entry should close when the fix is promoted and a served add-key check passes, taking the gate back to 13. PM decides whether a same-day, already-fixed admission counts against the hold; I am not asking for anything today beyond that call, and nothing needs to change for the fix to ship.

**Open PM questions, unchanged:** what Wed 10-14 reads against (band as set, re-based for the 29-literal permanent floor, or other), and whether #1977 is admitted. Ceiling is 121 (my recount); Lead's #1977 step 2 is served on a local server with the flag flip next.

Verified how: method: `gh issue view 1978`; `git show 4bd1a236e9:services/security/provider_key_validator.py` and the same path on main; `curl .../health` for alpha's sha (4bd1a236e9); `gh issue edit/project item-add/item-edit/comment` each returned; criteria line. Layer: issue state, source at two shas, alpha's reported sha; no served add-key attempt. Denominator: 1 issue; 1 key shape measured by Lead.
