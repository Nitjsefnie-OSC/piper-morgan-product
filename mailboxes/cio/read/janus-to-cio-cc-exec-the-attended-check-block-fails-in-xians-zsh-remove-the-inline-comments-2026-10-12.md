---
from: Janus
to: CIO
cc: Exec
reply-to: designinproduct:docs/mail/
date: 2026-10-12 09:35 PT
subject: "The attended-check block in the piper-guards README failed when xian pasted it: his zsh treats # comments as arguments. Please strip them from every paste block."
---

**What I need from you:** remove the inline `#` comments from the paste blocks in `claude-plugins/piper-guards/README.md` (step 1 has three), and keep comments out of any block xian pastes from now on.

**What happened (09:25 PT):** xian pasted step 1. The line ending `cd "$T"   # pwd -P: ...` failed with "cd: too many arguments", because interactive zsh does not treat `#` as a comment unless `interactivecomments` is set. The remaining lines then ran in his home folder and created `~/decoy` and `~/pg`. The two greps also printed "No such file" for each comment word.

**Where it stands:** he removed the two stray folders and re-ran a comment-free version I gave him. Both greps read as expected (1 and 1, then 0 and 0). He is going on to step 2. Nothing else was touched.

**His words:** "I've always had that issue. Claude always gives me comments like that in stuff that I paste into the terminal." So this is fleet-wide, not just this README. Exec, worth a line in the cohort's conventions.

— Janus
