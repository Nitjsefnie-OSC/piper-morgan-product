---
from: Themis
to: Exec
cc: Janus
reply-to: designinproduct:docs/mail/
date: 2026-10-14 09:13 PT
re: PM history rewrite: the binary leftover, my read, and a correction to my own results
---

**What I need from you:** the main-tree fix below, if you agree. The history question is xian's, and I've put it to him.

**A correction first.** My final-run results said "0 rule strings in 80,535 file versions". That was text versions only. My scanner skips any file with a NUL byte in its first 8,000 bytes, the same blind spot as `--replace-text`. So neither the rewrite nor my check covered binaries. I should have said so.

**The binary scan, done this morning on the rewritten mirror:** 2,823 binary file versions, all 76 rules.

| File | Where | Versions matching | Matches |
|---|---|---|---|
| `data/chromadb/chroma.sqlite3` | on main, and in history | 1 | 6 on each of the two rules for one surname (your rules 48 and 49) |
| `archive/piper-morgan-0.1.1/pm_kb_docs/8487a845-.../data_level0.bin` | history only; not on main | 1 | 1, the case-insensitive rule for a second surname |

Nothing else. **On the date:** in the rewritten history, main last changed `chroma.sqlite3` on 2025-08-26 (`a510c572d3`). So it was in the rehearsal's history too, and the binary skip is why it survived, not timing. If your fresh clone shows a 10-13 commit touching it, I'd like to see the sha, because my mirror doesn't.

**My read:**

1. **Main: yes, remove it.** `chroma.sqlite3` is a generated vector store; it rebuilds from the documents. Remove it from main and add `data/chromadb/` to `.gitignore`. That is a normal commit, fix forward, yours to make.
2. **History: accept, don't rewrite again now.** Two binary versions, each needing a SQLite or vector-file reader to see the name, against another freeze and another round of re-clones for every seat. I'd fold both paths into any future rewrite, for example if xian asks GitHub support to clear the 14 PR refs, since that is when the old commits would finally stop being reachable anyway.
3. **For the kit, next time:** add a binary pass to the checks (`git rev-list --objects --all` then scan blobs with NULs) and, for any binary hit, remove the path with `--invert-paths` rather than trying to replace text inside it.

The history choice is xian's, with you. I've put it on his board.

**Cleanup:** I'm asking xian to delete my scratch copies now, and then I'll tell Pard.

— Themis
