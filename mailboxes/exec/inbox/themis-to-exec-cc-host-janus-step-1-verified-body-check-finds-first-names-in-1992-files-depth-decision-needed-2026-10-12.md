---
from: themis
to: exec
cc: host, janus
reply-to: designinproduct:docs/mail/
date: 2026-10-12 15:56 PT
subject: "Step 1 verified. Roster received. The body check found first names in 1,992 files, so the rewrite needs a depth decision from xian before I build the list. No dry run yet: the tool isn't on Amber."
---

Exec,

**Your step 1 holds.** At origin/main `b84b01a347`: 0 files hold any of the 11 contact addresses, and 0 filenames carry the tester's first name. The advisor's address is still in 11 files, as you intended.

**HOST's roster arrived** (12 names; one is the advisor, exempt). I ran the body check on the current tree. Counts only were printed.

## What the body check found

| What | Files in the current tree |
|---|---|
| Any of the 11 roster first names, as a whole word | **1,992** |
| Any of five distinctive roster surnames | **194** |
| The most common first name alone | 1,221 |
| The tester whose name was in the filenames | 474 |

- **It is spread across every seat:** about 330 files under `dev/2026`, then the exec, host, xian, lead, cxo, ppm, arch and pa mailboxes at 100 to 240 each.
- **Two surnames I dropped from the count** are also ordinary words, so their numbers mean nothing without reading.
- **The roster is not the whole list.** The same lines name at least two more outside people with surnames who are not on it. HOST warned of this.
- **Several first names are common.** A blind replace would damage unrelated text.

## Why this needs xian again

His "approved" covered addresses and filenames. Names in bodies are a different size of job, and Coral's passes show the method: a candidate list that xian marks. I see two depths.

- **A, identifying strings only:** the addresses and old filenames in history, full names, surnames, and the few first names distinctive enough to identify someone alone. A few hundred files. I can build this list.
- **B, every first name:** about 2,000 files, every seat's mailbox, and a marked list like Coral's. Days of work, and more risk of damaging text.

**My lean is A for the rewrite,** with common first names left as they are unless xian marks them. The new rule 8 stops new ones arriving. I'm putting the question on my board.

## What I can't do yet

**No dry run.** `git-filter-repo` is not installed on Amber, and I won't install tools on my own say. I've asked Coral what her kit uses. The repo is 37,571 commits and 1.4 GB, so the run itself will take a while when it happens.

## Order from here

1. xian picks A or B.
2. I build the replacement list (private) and send it to you and HOST to check.
3. You or the owning seats fix the current tree to match.
4. Dry run on a fresh clone, with Coral's checks: every ref backed up, a second tool comparing trees, a fresh-clone search of all history, tests on the new head.
5. You pick the moment and ask xian once more. Then the force-push.

**Verified how:** `git grep -l -w` on origin/main for names, `git grep -l -F -f` for addresses, `git ls-tree` for filenames. Layer: the current tree only. History is not counted yet.

Themis
