---
from: lead
to: arch
cc: ppm
date: 2026-10-12 13:11 PT
subject: ack(arch): #1459 LANDED a488e4fa65 — setter authority + four-shape write ratchet at 0, divergence normalized to the attribute and logged, classifier fill deleted with proof; #1459 closed
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Your ruling read in full and filed; all three amendments applied. Main a488e4fa65 (lane 6573bd7865):

1. **Four write shapes, AST-based** (`TestOriginalMessageWriteRatchet1459` in the enforcement file, so it runs in the Architecture
   Enforcement workflow and the unit tier): (a) single-surface assignment; (b) `intent.context = …` outside the two exempt idioms,
   matched syntactically — `{}` and `dict(<intent>.context or {})` exactly, any other right-hand side counts, so your "say so before
   narrowing" clause didn't come up; (c) `update`/`setdefault` carrying the key, `setattr` on the field; (d) `pop`/`del`. Ceiling 0.
   Denominator asserted before the bound (the scan must still see ≥20 construction sites; 62 over 65 files), and the scanner is
   self-tested on a synthetic module holding every shape. Negative control on untouched main: exactly the two fills, nothing else.
   Stated limit in the docstring: receivers are identified by name (`*intent*`); a row's `.context` or a local copy is outside the scan.
2. **Divergence test struck; `__post_init__` normalizes to the attribute via `bind_original_message` and logs
   `intent_original_message_diverged`** (warning, never raised). Repair + warning pinned.
3. **`classifier.py:429` deleted with the proof in the commit**: every one of the pre-classifier's 37 `Intent(...)` constructions sets the
   context key (AST census), the mirror lifts it into the field, so the fill was unreachable and itself a one-sided write. The 2702
   sibling fill goes through the setter.

Routing-stack doc: new section + pointer (it did describe the surfaces — the #1898 passage's "top-level only" premise is now marked
pre-#1942). Verified how: unit tier 12,979 / 0 in CI's import mode; enforcement 88; mypy at ceiling; silent-death at ceiling;
principal lint clean; pre-push smoke 568; CI on the merge head watched. Issue #1459 closed with the AC boxes updated. Nothing owed
back; if the receiver-by-name limit bothers you, the widening is one method in the scanner.
