"""#1943, the "first N" DELETE shape — the SERVED answer (Web's 2026-10-11 FAIL).

Web, alpha 4bd1a236e9: with five reminders listed, `delete the first two
reminders` armed ONE confirm naming the row whose text contained "two". The
#1666 gate's named-target leg fuzzy-bound "first two" before the
router-targets hook could run (fixed: a positional-only target is a
passthrough, test_delete_ordinal_not_a_name_1943.py).

Marked ``llm``: real app + DB + the served router (local flag includes
``delete_todo``, as alpha's does). Seeds Web's list shape through the REAL
write path — two due items first, then two upcoming ones whose titles carry
"one" and "two" — under the authenticated principal, and removes them after.

  turn 0 → "what reminders do I have?" shows the list NUMBERED
  turn 1 → 'Delete 2 reminders: "revise the pr" and "send the budget review
           to finance"? …(yes/no)' — the FIRST TWO of the numbered list,
           nothing deleted yet, never the "two"-titled row
  turn 2 ("yes") → exactly those two gone, the upcoming pair untouched
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

import pytest

from services.intent_service import inversion_live

pytestmark = pytest.mark.llm

FLAG = (
    "read_status,read_referent,read_synthesis,create_todo,create_reminder,"
    "read_strategic,read_temporal,delete_todo,read_floor,read_floor_2,"
    "read_canonical,read_portfolio,complete_todo"
)
DUE = ["revise the pr", "send the budget review to finance"]
UPCOMING = ["web check alpha one", "web check alpha two"]
TURN = "delete the first two reminders"


async def _seed(user_id: str):
    from services.todo.todo_management_service import TodoManagementService

    svc = TodoManagementService()
    now = datetime.now(timezone.utc)
    made = []
    for i, text in enumerate(DUE):
        when = now - timedelta(hours=len(DUE) - i)
        t = await svc.create_todo(
            user_id=UUID(user_id), text=text, priority="medium", reminder_date=when, due_date=when
        )
        assert t is not None and t.id
        made.append(t)
    for i, text in enumerate(UPCOMING):
        when = now + timedelta(days=1, hours=i)
        t = await svc.create_todo(
            user_id=UUID(user_id), text=text, priority="medium", reminder_date=when, due_date=when
        )
        assert t is not None and t.id
        made.append(t)
    return svc, made


@pytest.mark.skipif(
    not os.environ.get("PIPER_E2E_LIVE_HEADER_KEY"),
    reason="live probe: set PIPER_E2E_LIVE_HEADER_KEY (operator spend, deliberate)",
)
async def test_delete_the_first_two_reminders_asks_for_the_first_two_of_the_numbered_list(
    e2e_client, e2e_byoc_auth, e2e_test_user, monkeypatch, caplog
):
    monkeypatch.setenv(inversion_live.LIVE_CATEGORIES_ENV, FLAG)
    caplog.set_level("INFO")
    user_id = e2e_test_user[0]
    svc, seeded = await _seed(user_id)
    session_id = str(uuid4())
    try:
        r0 = await e2e_client.post(
            "/api/v1/intent",
            json={"message": "what reminders do I have?", "session_id": session_id},
            **e2e_byoc_auth,
        )
        assert r0.status_code == 200, r0.text[:300]
        reply0 = r0.json().get("message") or ""
        print(f"\n[turn 0] reply: {reply0.replace(chr(10), ' ⏎ ')[:500]}")
        assert (
            "1. **revise the pr**" in reply0
            and "2. **send the budget review to finance**" in reply0
        ), reply0
        assert (
            "3. **web check alpha one**" in reply0 and "4. **web check alpha two**" in reply0
        ), reply0

        caplog.clear()
        r = await e2e_client.post(
            "/api/v1/intent", json={"message": TURN, "session_id": session_id}, **e2e_byoc_auth
        )
        assert r.status_code == 200, r.text[:300]
        body = r.json()
        reply = body.get("message") or ""
        decision = [
            x.getMessage() for x in caplog.records if "inversion_live_decision" in x.getMessage()
        ]
        print(f"\n[turn 1] decision: {[d[:240] for d in decision][:1]}")
        print(f"[turn 1] reply: {reply.replace(chr(10), ' ⏎ ')[:500]}")
        assert (
            decision and '"route": "inversion"' in decision[0]
        ), "turn 1 not served by the Inversion"
        assert '"operation": "delete_todo"' in decision[0], decision[0]
        first_line = reply.splitlines()[0]
        assert first_line.startswith("Delete 2 reminders:"), reply
        assert (
            '"revise the pr"' in first_line and '"send the budget review to finance"' in first_line
        ), reply
        assert "web check alpha" not in first_line, reply
        assert first_line.rstrip().endswith("(yes/no)"), reply
        assert body.get("requires_clarification") is True
        still = [
            t
            for t in await svc.list_todos(user_id=UUID(user_id), include_completed=False)
            if t.text in DUE + UPCOMING
        ]
        assert len(still) == 4, [t.text for t in still]

        r2 = await e2e_client.post(
            "/api/v1/intent", json={"message": "yes", "session_id": session_id}, **e2e_byoc_auth
        )
        assert r2.status_code == 200, r2.text[:300]
        reply2 = r2.json().get("message") or ""
        print(f"[turn 2] reply: {reply2.replace(chr(10), ' ⏎ ')[:400]}")
        assert reply2.startswith("Deleted 2 reminders:"), reply2
        remaining = [
            t.text
            for t in await svc.list_todos(user_id=UUID(user_id), include_completed=False)
            if t.text in DUE + UPCOMING
        ]
        assert sorted(remaining) == sorted(UPCOMING), remaining
    finally:
        for t in seeded:
            try:
                await svc.delete_todo(todo_id=UUID(str(t.id)), user_id=UUID(user_id))
            except Exception:
                pass
