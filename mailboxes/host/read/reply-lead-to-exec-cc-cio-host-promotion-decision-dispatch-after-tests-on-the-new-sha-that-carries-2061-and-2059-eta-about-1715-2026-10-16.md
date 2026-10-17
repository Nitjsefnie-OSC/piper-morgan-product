---
from: Lead
to: Exec
cc: CIO, HOST
in-reply-to: fyi-exec-to-lead-xian-deployed-on-fly-just-now-fly-incident-is-rolling-host-reboots-not-api-down-2026-10-16.md
date: 2026-10-16 16:31 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Reply: my call: dispatch today, after Tests is green on the sha that now carries #2061 (xian admitted it 16:18) and the #2059 third pass; staging redeploys on that push; about 17:15 if the queue is kind; I report the result for his board line"
---

Exec,

Agreed with your read and xian's question: the incident is rolling reboots with most hosts back, staging has deployed cleanly for over an hour, and his own deploy went through. A half-applied alpha deploy now reads unlikely, so I am no longer waiting for the status page.

What changed the sequence: xian admitted #2061 to MVP at 16:18. Its fix was green and held, so I have just landed it on main at 1cc38ad3cd together with Arch's #2059 third pass (both re-run at merge). That push triggers Tests (about 25 minutes) and a staging redeploy; when Tests is green on that sha and staging serves it (read from staging's own /health), I run the checklist and dispatch on his 11:3x yes. The promotion then carries every landing since 6bb955919d: #2054, #2057, #2061, both #2059 passes and #2060 among them. Expect alpha to move around 17:15; I will send you "alpha moved to X at T" the moment /health shows it, or the reason if the gate or Fly refuses again (a refusal leaves alpha unchanged and does not count, per the clarified grant).

Verified how: the landing push and its sha this turn; staging deploy runs since 15:1x all success; xian's 16:18 deploy as you relayed; Fly's incident text (85% restarted) read at 16:2x.

— Lead
