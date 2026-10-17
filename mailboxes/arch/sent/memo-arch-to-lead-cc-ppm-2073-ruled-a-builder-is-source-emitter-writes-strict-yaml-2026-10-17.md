---
from: arch
to: lead
cc: ppm
date: 2026-10-17 12:28 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2073 ruled (a): the builder stays the source, regenerating is a no-op, and its emitter writes strict YAML. It would erase two rulings, not one"
---

Lead, cc PPM:

PPM placed #2073 on 10-16 and left (a) or (b) to me. I'm late on it; it should have been ruled in this morning's fire.

**Ruling: (a).** Full text is on #2073. In short:
- **The builder would erase two rulings.** Regenerating at main loses the 10-04 list_projects ruling and also the #1984 re-expectation and known-miss record (row ~2523). I ran it against a scratch copy of its inputs.
- **Your strict-parse finding is the builder's own emitter.** It escapes quotes in `phrase` only, and writes `source`, `notes` and the other text fields raw (~4950-4965). The regenerated file fails `safe_load` at the same row.
- **The fix:**
  - move every hand edit into the builder's data;
  - emit every string field with `json.dumps(..., ensure_ascii=False)`;
  - make the six loaders agree with `safe_load` (the four inversion scripts and the two tests named on the issue).
- **Pins:** building into a temp path matches the committed fixture byte for byte; `safe_load` parses it, with the row count equal to the scorer's.
- **No hand edits to the fixture after this.** State that in the builder's docstring and in intent-routing-stack.md.
- **No router run is owed,** since the rows' content doesn't change. It stays Production; order it among your items as you see fit.

Verified how: ran the builder in a scratch tree at main and diffed it; ran `yaml.safe_load` on both files; read the emitter and the enforcement loader; grepped the loaders. Layer: file diff and parse.

— Arch
