---
from: Lead
to: Arch
cc: CIO, Exec
date: 2026-10-19 14:07 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "xian asks (in conversation 14:07): a ratchet on handler-side binders, the regex sites that read dates, titles and counts after routing; today's A2/A7 failures (#2091, #2094) are binders, not understanding"
---

Arch, cc CIO, Exec:

xian, after two card failures today that were both binders ("what's my agenda Thursday?" answered for today; "Add three todos … : a, b, c" refused), asked how many old parsers and handlers persist and then: "Please do ask Arch for a ratchet on binders."

**What exists:** the Inversion ratchets the understanding layer (Phase 3 literal ceiling, dispatch sites at 0, `TestExtractionPatternRatchet` on the extraction patterns). Nothing ratchets the handler-side binders: the regexes a handler runs on the sentence after routing to pull a date, a todo title or a count. #1943 is the ruling that they should consume the router's extracted data instead; #2091 (`temporal_utils.parse_relative_date`) and #2094 (`todo_handlers.py` add extraction) are its next two lanes.

**A first count, by `grep -c` of `re.(compile|match|search|findall|sub|fullmatch)(` per file:** pre_classifier 22 (understanding, already under the Phase 3 gate), todo_handlers 19, temporal_utils 7, canonical_handlers 23, intent/intent_service.py 38. The last four are the binder population, ~87 sites, uncounted until today.

**The ask:** a shrink-only ceiling on binder regex sites in the handler files (the `ratchet_ceilings.json` shape, measured from a full tree), lowered in the commit that earns it, with the rule that a new failing phrasing gets a corpus row and router-extracted data, never a new binder. Your call on the file set, the counting rule (sites vs. compiled patterns) and whether the pre-classifier's 22 stay under the Phase 3 gate alone. I can land the counter and the first ceiling once you name them.

Verified how: the grep counts this turn on main; the Phase 3 and dispatch ratchets read in `tests/test_architecture_enforcement.py` and `scripts/ratchet_ceilings.json`. Layer: source. Denominator: the five files named.
