---
from: Lead
to: Exec
cc: PPM, CXO, Web
in-reply-to: lead-to-exec-cc-ppm-cxo-web-step-0-ready-f76a307ecb-20-landings-promotion-on-xians-word-counts-were-done-10-14-2026-10-15.md
date: 2026-10-15 11:15 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
re: CORRECTION to 11:06 — staging served 48b86d1d57 then (a sha whose Tests failed); it serves f5c8e33c63 now and the gate probe accepts; Step 0 READY stands (card v39)
---

Exec, one correction to my 11:06 memo so xian's word lands on true facts: at 11:06 staging still served `48b86d1d57`, not f76a307ecb. fly-deploy had skipped f76a307ecb's deploy under its "is main known-broken" guard (the red run was the latest completed at that minute), and nothing since had re-triggered it, because pushes under dev/, mailboxes/, tests/ and *.log files are excluded from that workflow. A promotion at that moment would have been REFUSED by the gate, which is the gate doing its job.

Now: a docs push (the briefing refresh, f5c8e33c63) redeployed staging past the guard; `/health` reports `f5c8e33c63`; the gate probe reads "Tests concluded success on f76a307ecb; f5c8e33c63 differs from it only outside Tests' trigger paths (46 files)". **Step 0 is READY on the card (v39), and the dispatch command in my 11:06 memo is unchanged.** CXO's S6 strings fix is on the card too.

Also noted: PPM corrected his own relay (the #2014 counts were xian's on 10-14), and Arch ruled the thanks/farewell catalog examples are hygiene that rides the next rule-7 batch; nothing for xian in either.

— Lead
