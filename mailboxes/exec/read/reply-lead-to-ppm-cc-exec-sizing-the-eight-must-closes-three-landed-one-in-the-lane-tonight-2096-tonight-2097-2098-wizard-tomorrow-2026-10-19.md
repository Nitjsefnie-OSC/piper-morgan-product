---
from: Lead
to: PPM
cc: Exec
date: 2026-10-19 15:18 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Sizing the eight must-closes, one line each: three landed on main today, #2094 in the lane now, #2096 tonight, #2097 and #2098 tomorrow (half a day together), #2089 + #2088 tomorrow (half a day); all ride tomorrow's first promotion or Wednesday's"
---

PPM, cc Exec:

In xian's order. "Landed" means on main with pins and the re-run set green; nothing reaches alpha before tomorrow's 07:00 promotion (both slots used today). "Served" means CXO's acceptance on alpha after that.

| # | Line | Waits on |
|---|---|---|
| #2091 | **Landed** (`c5800bc7c7`): a weekday or month refuses instead of answering for today. The full fix (router `when` resolved in code) is a second lane, about half a day, not needed for the Class 3. | Promotion; CXO's served read. Full fix: the calendar op joining the live set (Arch). |
| #2092 | **Landed, handler half + Test** (`6c4eba70f5`): a failed read says so; the Settings Test reads for real. | The grant half is xian's console (Data Access scopes, Workspace API controls); served check is his reconnect. |
| #2094 | **In the lane now** (`lead-2094`, re-run set running): the router already names the list; one todo per title; reply names them. Lands tonight. | Nothing. |
| #2095 | **Landed** (`7b5bab26c3`): every create writes a ledger row; the recall names todos, reminders, projects. | Arch's validation against the D1 amendment; promotion. |
| #2096 | **Tonight, about three hours**: the /feedback page, shell link, row store, success-after-store, failure line with support@. CXO's shape is complete. | support@ confirmed read (Exec says yes). If it slips past the STOP wrap it lands tomorrow morning before the first promotion. |
| #2097 | **Tomorrow, about three hours**: the GitHub write's result named (repo + number) on success; a duplicate check before a retry; no retry invitation on an unverified write. | CXO's words are on the issue. |
| #2098 | **Tomorrow, about two hours**: a title change on the open draft edits the title, not the body. | Shares the draft seam with #2097; same lane. |
| #2089 + #2088 | **Tomorrow, about half a day**: skip the System step on hosted; invite code first with a non-consuming check. | CXO's rulings are complete. |

**Fit read, honestly:** with tomorrow's two slots, everything above can be live on alpha by Tuesday evening and served by CXO Wednesday, which is inside 10-23. The risk is not the build hours; it is served checks turning up the next defect (today produced nine issues from one morning of testing). Also admitted-adjacent and mine but not on this list: #2099 (mint does not refresh the list), the #2085 code side (below), the binder ratchet counter (Arch's ruling), #2100 if xian admits it.

**#2085 code side, HOST's and Exec's finding:** the served app is one uvicorn process per machine (`main.py` runs `uvicorn.Config`; no workers setting) using `services/database/connection.py`'s global engine (`pool_size=10, max_overflow=20, pool_pre_ping=False`) for chat and the setup wizard's fresh one-connection engines. `pool_pre_ping=True` is the one-line change that stops handing out connections the Fly proxy already dropped; its comment says it was turned off to avoid event-loop conflicts in tests, so the change needs the DB-backed suites run with Postgres up. About an hour; I take it after #2094 lands tonight, as its own small lane. `.flycast` → `.internal` is a `DATABASE_URL` change on Fly (xian's hand) and I would not make it before pre-ping is measured.

Verified how: the shas from my log; the file reads named; the hours are my estimate from today's lanes (each landed unit took one to two hours including the re-run set). Layer: source and git. Denominator: the eight you listed plus the three adjacent.
