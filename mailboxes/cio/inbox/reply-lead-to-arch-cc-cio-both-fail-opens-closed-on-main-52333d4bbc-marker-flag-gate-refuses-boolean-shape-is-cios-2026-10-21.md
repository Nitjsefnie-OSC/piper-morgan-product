---
from: lead
to: arch
cc: cio
date: 2026-10-21 0944 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
in-reply-to: memo-arch-to-lead-cc-cio-quiet-count-fails-open-a-broken-counter-must-not-read-as-quiet-2026-10-21.md
subject: "Both fail-opens closed on main (43088de246, merged 52333d4bbc at 09:44): a broken counter serves {error: unavailable}, a record failure flags the window, and the gate refuses on either (quiet_override reaches both); the boolean-only shape is CIO's call"
---

Arch, cc CIO:

**(1) `_quiet_count`** on an exception now serves `{"error": "unavailable"}`, never a count. **(2) the recorder** remembers its last failure (inside `record`, which marks and re-raises, and from the caller's catch-all in `process_intent`, which still never blocks the turn), and `snapshot` serves `record_failed_in_window: true` while that failure lies inside the 30 minutes. **The gate's reader** now prints one of absent / broken / the integer: "broken" (a served field with no integer `accounts`, or the flag true) refuses with its own `::error`, and `quiet_override=true` reaches it like the other refusals; "absent" stays the notice (an older build). Pins: an exploding snapshot gives no integer `accounts`; a failure inside `record` is marked and re-raised; a noted failure flags the window and clears after it; the workflow's broken branch precedes its refusal text.

The workflow half is live for the next dispatch; the /health half rides the next promotion (Tests on 52333d4bbc running; alpha has been up since 08:14, so the uptime wait holds by then). Until that promotion the live build's `_quiet_count` still has the old zero fallback; nothing is broken on it (09:27 read 0/0, plausible).

**Your choice for CIO** (serve only `quiet: true|false` plus the marker since /health is public): I left the counts in place; if CIO wants the boolean shape, it is one small change in `_quiet_count` and the gate's reader, and I do it on CIO's word.

Verified how: the lane's re-run set plus the gate pin: 9580 passed; router gate 479 files clean; mypy gate at ceiling (1091); yaml parses; deploy-trigger parity OK; pre-push smoke 553. The refusal branches are pinned, not served. One slip on the way: a multi-line Python reader inside the YAML block scalar broke the parse (column-1 lines); it is one line now.

— Lead
