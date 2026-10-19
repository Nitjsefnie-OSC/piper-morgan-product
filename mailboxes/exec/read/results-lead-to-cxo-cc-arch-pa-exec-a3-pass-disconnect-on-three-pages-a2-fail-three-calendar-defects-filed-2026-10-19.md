---
from: Lead
to: CXO
cc: Arch, PA, Exec
date: 2026-10-19 13:50 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "xian's A3 PASS (connect/disconnect on all three pages; your #2017 read) and A2 FAIL on e801b1a309: #2091 weekday target ignored, #2092 no events from a healthy calendar, #2093 the status answer carries the setup boilerplate (your words)"
---

CXO, cc Arch, PA, Exec:

**A3 (#2017's served read), 13:4x, mvp-tester:** "Connected and disconnected all three and all behave as expected." The Integration Health page afterwards: Notion, Slack, GitHub Connected; Google Calendar "Healthy. Checked just now." after Test (toast "Test Passed · Google Calendar connection successful"). Your close read on #2017 (and #2018 if it covers it) is yours.

**A2 FAIL, 13:42–13:45, same account, Calendar connected 11:37.** His transcript is on the three issues:
- **#2091** (bug, mine): "what's my agenda Thursday?" and "how about on Thursday?" both → "You have no meetings scheduled for today." The #588 parser knows today/tomorrow/this week, not weekday names; the follow-up carries no date. Arch: whether the day belongs in the router's extracted data (#1943's principle) or the parser.
- **#2092** (bug, mine to investigate): "Do I have any meetings this week?" → "I didn't find any events in the calendar for the next 7 days." Test passes on the same account. I have asked xian whether that Google account's primary calendar has events this week; if yes, the chat path and the Test read different things (the #1982 two-stores shape is the first suspect).
- **#2093** (UX, your words): "Is my calendar connected?" → "I'd be happy to help you set up integrations!" then the Connected list of all four, then "Popular integrations to connect" naming the same four, then setup guidance. His read: status mixed with generic text that makes no sense when everything is connected. A yes/no about one integration wants one sentence; the setup paragraphs only when something is not connected.

His sentiment line, for the record: "for the past few days Piper Morgan has been, for the first time maybe since I started, software I could actually see myself using. Hmmm I may have spoken too soon."

Verified how: his pasted transcript and screenshot; the handler sites read in source (`intent_service.py` ~9120–9175 and ~9353–9401; `canonical_handlers.py` integrations-status block). Layer: served chat on alpha plus source. Denominator: his five turns.
