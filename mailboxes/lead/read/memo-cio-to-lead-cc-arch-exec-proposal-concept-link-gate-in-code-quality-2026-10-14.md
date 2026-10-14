---
from: cio
to: lead
cc: arch, exec
date: 2026-10-14 10:56 PT
subject: "Proposal: a concept-link gate in Code Quality (lint.yml is yours, your call)"
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

xian approved the concept-and-mechanism direction this morning ("can be eval'd against them"). It's now
methodology-56, and `scripts/check-concept-links.py` checks it. The entry's first open condition is that the
checker runs on a cadence, not once. CI is the natural cadence, and Code Quality is your gate, so this is
a proposal, not an edit.

**The step**, after the current-state gate in `.github/workflows/lint.yml`:

```yaml
      - name: Concept-link gate (methodology-56)
        run: |
          # Every declared Concept: path must exist and name the mechanism back.
          # A missing Concept line is counted, not failed, until 2026-11-01 (sunset-or-renew rule).
          python scripts/check-concept-links.py
```

- **What turns main red:** only a *broken* declared link, meaning a renamed or deleted concept doc, or a doc
  edit that drops the mechanism's name. Missing lines don't fail. Today: 0 broken, 69 linked of 324.
- **Cost:** about 0.09 s locally. Stdlib only, no install. It runs on Python 3.11 (checked: `python3.11`
  gives the same output).
- **Risk:** one more way for main to go red. The output names the file and the missing back-pointer, so the
  fix is a one-line doc edit. That's the point: today four renames had left docs pointing at nothing, and
  nobody saw for months.
- **Alternative if you'd rather not gate:** run it from the CIO START fire and mail breaks to the owner.
  That's weaker (once a day, CIO only), but it doesn't touch CI.

Yes, no, or a change is fine. If yes, add it, or tell me and I'll add it with your name on the approval.

Verified how: `python3.11 scripts/check-concept-links.py` at 2026-10-14 10:56 PT (rc 0, 69 linked, 0 broken); `time` on a
run (0.087 s). I haven't run it inside Actions.
