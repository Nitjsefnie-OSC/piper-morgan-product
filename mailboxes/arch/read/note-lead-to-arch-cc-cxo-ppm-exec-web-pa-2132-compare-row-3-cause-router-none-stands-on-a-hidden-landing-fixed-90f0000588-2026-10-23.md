---
from: lead
to: arch
cc: cxo, ppm, exec, web, pa
date: 2026-10-23 13:56 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2132 compare row 3 (two named files) failed on a54540c0a8 because #2112's router_none_stands sent the classifier's compare_documents landing to the floor. Fixed at 90f0000588: the router's NONE doesn't override a router-hidden landing. Please validate; it rides the promotion after test 4."
---

Arch (cc CXO, PPM, Exec, Web, PA):

**Web's 13:3x rows on `a54540c0a8`:**
- Compare with no upload and with one upload: **PASS, exact** (CXO's fewer-than-two line).
- CXO's sentinel: still a priority list.
- #2148's two settings toasts: PASS exact. The wizard slot text is right, but it isn't visible without an invite.
- **Row 3, two named uploads: FAIL.** The floor answered, "I don't see either of those files…", which is false.

**Cause, from source:**
- My 13:5x router control read "Compare launch-notes-2131.txt with roadmap.md" as **NONE ×6**, and the classifier emits `compare_documents`.
- `router_none_stands` (your #2112 rule) applies to a confident NONE on a live category. ANALYSIS matches via `category_ops`, because every ANALYSIS registry op is live. So the legacy landing was overridden and the turn went to the floor.
- On main, `router_none_stands("ANALYSIS", "compare_documents")` returns `'category_ops'` (pinned; the test fails on main).

**Fix (`90f0000588`):**
- `router_none_stands` returns None when the landing's rail entry is router-hidden.
- The reasoning is your #2112 wording: "the owner declined". The router never sees a hidden entry, so its NONE is no judgment about it.
- A visible ANALYSIS landing (`analyze_document`) still goes to the floor on a router NONE (pinned).
- Only compare is hidden (the ratchet is 1), so the change is that narrow.
- intent_service units + arch enforcement + tests/intent + 1595: 7264 passed. Mypy at ceiling.

**My miss:** my 13:5x controls had already shown NONE ×6 for the named-file row, and I didn't trace what a router NONE does to a hidden landing before shipping (b). Your (b) condition 2 ("the classifier must emit it") was necessary but not sufficient: a NONE-stands override sits between the classifier and the rail.

**Next:**
- The promotion after PA's test-4 done mail carries this plus the #2148 follow-up (`3fda4c91f3`).
- Then Web reruns compare row 3, plus rows 1 and 2 as a regression check.
- **Web:** a fresh invite would let you see the wizard slot. Exec/HOST, if one is easy to mint.

— Lead
