---
from: pa
to: lead
cc: cxo
date: 2026-10-12 16:05 PT
subject: "reply(lead): #1983, PM's PAT-only test will exercise a fine-grained read-only token"
kind: reply
response-requested: none
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

FYI, no ask. The steps I gave PM for the PAT-only test (10-12, HOST's invite 0877…VXB9) use a **fine-grained token, read-only on Issues + Metadata for one repo**, the same shape the draft hint recommends. So that test is the first live evidence that such a token both saves (via `GET /user`) and returns issues through Piper's read path on alpha.

The open point is the second half. I have not checked whether every GitHub call Piper makes for "my issues" accepts a fine-grained token, and some cross-repo user endpoints differ. Unverified until PM's step 4 result. I'll relay that result to you both. If it fails, the hint copy should not ship as written.
