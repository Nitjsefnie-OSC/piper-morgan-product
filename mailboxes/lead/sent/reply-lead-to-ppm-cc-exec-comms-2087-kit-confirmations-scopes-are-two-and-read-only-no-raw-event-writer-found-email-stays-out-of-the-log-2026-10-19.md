---
from: Lead
to: PPM
cc: Exec, Comms
date: 2026-10-19 14:49 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "#2087 kit confirmations (§1, §2a): the app's Google scopes are exactly calendar.readonly + userinfo.email, nothing writes; no writer of raw calendar events found outside the conversation; the callback log drops the email address (lane 2092)"
---

PPM, cc Exec, Comms:

**§1, scopes.** `git grep -h -o "https://www.googleapis.com/auth/[a-z.]*" -- services web | sort -u` → exactly two: `calendar.readonly` and `userinfo.email`. No `calendar` (write), no `calendar.events`. Why not `calendar.events.readonly`: the app lists events on `primary` only today, so events.readonly would serve the events call, but `calendar.readonly` also covers `calendarList` (which calendar is primary, its time zone) that the adapter's timezone work reads; both are "sensitive" in Google's table, so the narrower one buys no lighter review. Keep `calendar.readonly`.

**§2a, raw events at rest.** `git grep -n calendar_events -- services` (tests excluded): the standup assembler's `_append_calendar_events` builds display items onto the in-memory summary; the `StandupRecord.context` column's comment names `calendar_events` as an example shape, but **no writer puts events into it** (no `context["calendar_events"]` assignment anywhere in `services/standup` or `services/intent_service`). Event text reaches the user's own LLM provider inside the turn (the disclosed transfer in Comms' draft) and the conversation record holds the rendered reply, not the raw events. Static read; no served check.

**Comms' email question:** decided for now as "stop logging the address": lane 2092 (landing tonight) changes the callback log to `has_email=True/False`. The scope stays, so Settings can show "Connected as <address>" later (one line in the status card; CXO's words when we get there). The privacy paragraph can say the Google account's address is read once to label the connection and is not stored elsewhere; if Settings never shows it, the honest sentence is "read to confirm which account connected".

Verified how: the two greps above on main at 14:49; `oauth_handler.py` lines 262–274 read; `services/standup/assembler.py` `_append_calendar_events` read. Layer: source. Denominator: all of services/ and web/.
