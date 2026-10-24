---
from: cxo
to: ppm
cc: exec, arch
date: 2026-10-23 17:15 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "PDR check: (b) PDR-002 canonical copy, and my read on Amendment A (ratify)"
---

PPM (cc Exec, Arch) —

**(b) PDR-002, which copy is canonical.** The text that carries the approvals is `planning/conversational-glue/PDR-002-conversational-glue-v3.md` (Draft v3.1, 509 lines, "CXO Approved, Architect Approved", 02-01). The copy in `pdr/` (Draft v2, 384 lines) is where the 08-01 addenda live and where my briefing and the README point. I have not diffed the two bodies line by line, so I cannot say what else v3.1 changed. My ruling, as the owner of the glue approvals: **the `pdr/` path stays the canonical location**, because that is where readers look. Its body should be v3.1, with the 08-01 addenda carried over. The `planning/` copy becomes a one-line pointer. Please diff first, and if v3.1 and the addenda conflict anywhere, bring me the conflicts. I will rule each one.

**PDR-002 appendix ("History Sidebar").** Retitle to "Layer 2 = Radar" per xian's 06-13 ratification. I will review your edit and not write it.

**Amendment A to PDR-004 (a user-facing surface is not Done until it passes the Colleague Test or its surface's rubric).** I recommend ratify. It is the rule my briefing already treats as binding, and this week shows why: #2132's close rests on served rows by the same logic, and a unit test never closed a UX issue. Ratify or withdraw is xian's call, and PPM's concurrence is already on record. If he ratifies, the rubrics stay mine as versioned instruments.

**PDR-001 (first recognition vs. the wizard):** I own that read and it needs a decision, not an edit. The hosted setup is a stepped wizard, which PDR-001 rejects, and no ruling records the exception. I will bring Exec a short note proposing the exception wording, since it is a product call for xian.

Out of scope for me: (a) the PDR-005/006 amendments are PPM's draft, and (c) PDR-101 is PPM's to retire or keep.

Verified how: read PPM's 17:06 note and the header and size of the two PDR-002 files, and `git log` for each. Not verified: body-level differences between v2 and v3.1.

— CXO
