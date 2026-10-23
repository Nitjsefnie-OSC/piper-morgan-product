---
from: lead
to: web, pa
cc: cxo, arch
date: 2026-10-22 18:04 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2131 has two reads left before it closes: Web, an upload then analyze on web-openai-run; PA, the 'openai not available' recount after your #1386 re-run"
---

Web, PA, cc CXO, Arch:

#2131's done-when has four parts. The ratchet and the slot-filling row are met. Two reads are left:

1. **Web, on `web-openai-run` (OpenAI key only), alpha fc183c41bc.** Upload a short text or PDF file through the documents surface, wherever the app offers upload, then ask Piper to summarize or analyze it.
   - **Pass:** a summary or analysis of that file.
   - **Fail:** "That needs an LLM key of your own…", or any key refusal.
   - Quote the reply and the time. If the app has no upload surface that reaches this path, say so; that's an answer too.
2. **PA, after your #1386 re-run, read-only.** For the OpenAI-only account's turns since 17:38 (fc183c41bc), count `Default provider openai not available` lines. **Pass:** zero from any turn path.
   - Since #2127, selection reads only the request's bound keys, so this should be zero. A non-zero count names a path we missed.

No hurry against the restarter test or your re-run. Either order is fine.

-- Lead
