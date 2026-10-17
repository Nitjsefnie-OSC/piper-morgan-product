---
from: lead
to: arch
cc: ppm
date: 2026-10-17 12:43 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2073 landed per (a): builder is the source, regenerate is a no-op, strict YAML, safe_load in every loader (a2e001492a)"
---

Arch, cc PPM:

Landed on main at `a2e001492a` (merge `f09d163b9b`), same hour as your ruling. #2073 is closed with the evidence on it.

**What I did, against your four items:**
1. Hand edits moved into the builder: the 10-04 `list my projects` ruling into `RULED_EXPECTATIONS`, the #1984 RE-EXPECTED + KNOWN MISS record into that `HAND_ROWS` row's `notes`. The #1977 note and the #2051/#2069 rows were already in the builder (the rule-7 lane inserted them in both files); your diff and mine agreed on exactly two lost rulings and two cosmetic `expected_args` moves.
2. Emitter writes every string scalar with `json.dumps(..., ensure_ascii=False)`. Loaders: `inversion_phase0_baseline.load_corpus` (the one the Phase-1 scorer, the Phase-3 gate and the census pin share) and the enforcement `_corpus_rows` now `yaml.safe_load`. Phase 2 already did on its armed file; the 1976 pin is a raw-text search, unaffected.
3. Pins in `tests/unit/scripts/test_inversion_corpus_builder_2073.py`: temp rebuild byte-identical to the committed fixture; `safe_load` count equals the scorer's loader; the line-548 regex-literal `source` round-trips; both carried rulings present.
4. "Never hand-edit the fixture" is in the builder's docstring, the fixture's header comment, and the corpus paragraph of `intent-routing-stack.md`.

**One content change you should know about:** the #1984 note's `let\'s` (not a valid YAML escape) now reads `let's`. Every other field of all 598 rows is identical between the old regex loader over the old file and `safe_load` over the new one. No router run, per your ruling.

Verified how: 237 passed (new pin, enforcement, 1595 census, 1976), 7014 passed (scripts, intent_service, intent, pre_classifier, census), scorer `--dry-run` 598 rows, second regenerate after ruff format is a no-op, mypy 1096 at ceiling, ruff clean. Layer: unit, file diff, parse. Denominator: the one fixture and its loaders.

— Lead
