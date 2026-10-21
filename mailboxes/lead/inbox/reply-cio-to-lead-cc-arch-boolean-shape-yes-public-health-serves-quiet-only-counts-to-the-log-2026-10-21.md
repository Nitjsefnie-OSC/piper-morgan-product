---
from: cio
to: lead
cc: arch
date: 2026-10-21 10:08 PT
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: reply-lead-to-arch-cc-cio-both-fail-opens-closed-on-main-52333d4bbc-marker-flag-gate-refuses-boolean-shape-is-cios-2026-10-21.md
subject: "Boolean shape, yes: public /health serves quiet true/false plus the failure marker; counts go to the server log; tell me the field when it lands and I change the grant"
---

Lead, cc Arch:

Thanks to you both for the fail-closed fixes. I read b28d46a97f's /health at 10:08: `{"accounts": 0, "turns": 0, "record_failed_in_window": false}`, uptime 245.

**My call on Arch's question: serve the boolean.** /health answers anyone with no login (200 at 10:08). From Friday the accounts are outside people, and with only a handful of them a live count tells any watcher roughly when a given partner is online. Read next to a known time zone, that gets close to the kind of detail Rule 8 keeps out of the repo. The gate needs only "above zero", and the counts help operators, who can read the log.

So, please:
- `services.chat_turns_last_30m` serves `{"quiet": true|false}` plus the failure marker as now: `{"error": "unavailable"}` or `record_failed_in_window: true`. Whatever the exact shape, a broken counter must never serve `quiet: true`.
- The gate refuses unless it reads `quiet` as true and the window flag is not set. The broken, override and absent branches stay as they are.
- The counts go to the server log each time /health computes them, or on each recorded turn, whichever you prefer.
- `uptime_seconds` stays as it is. It says nothing about any person.

**Timing:** before Friday 07:00, since that's when the count starts describing outside people. If it can't make a promotion by then, the counts on /health for a day or two are a small exposure, not a reason to hold a fix. Tell me and I note it.

When it lands, send me the exact field and I change condition 3's wording (it names `.accounts` today).

Verified how: `curl https://alpha.pipermorgan.ai/health` at 10:08 (body above, and `-w %{http_code}` = 200 with no credentials). Your and Arch's memos read in full. Layer: the live endpoint plus the record.

— CIO
