"""#2101 — the calendar adapter's Google HTTP runs off the event loop.

googleapiclient is synchronous HTTP: ``events().list(...).execute()`` and
``Credentials.refresh(Request())`` block the loop for the whole round trip when called
directly from a coroutine (the shape the loop watchdog exists to catch). They now run in
``asyncio.to_thread``.

LAYER: the adapter (constructed, no network) with a fake service that records the calling thread.
DENOMINATOR: the range read (the week-calendar and agenda path); the thread is not the loop's.
"""

from __future__ import annotations

import threading
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, patch

import pytest

from services.mcp.consumer.google_calendar_adapter import GoogleCalendarMCPAdapter


class _Svc:
    def __init__(self):
        self.thread = None

    def events(self):
        return self

    def list(self, **kwargs):
        return self

    def execute(self):
        self.thread = threading.current_thread()
        return {"items": []}


@pytest.mark.asyncio
async def test_range_read_executes_on_a_worker_thread():
    adapter = GoogleCalendarMCPAdapter(user_id="u-2101")  # the constructor touches no network
    svc = _Svc()
    adapter._service = svc
    adapter._circuit_open = False
    adapter._calendar_id = "primary"
    now = datetime.now(timezone.utc)
    with (
        patch.object(
            GoogleCalendarMCPAdapter, "_get_user_timezone", new=AsyncMock(return_value="UTC")
        ),
        patch.object(GoogleCalendarMCPAdapter, "_now_user_local", new=AsyncMock(return_value=now)),
    ):
        events = await adapter.get_events_in_range(now, now + timedelta(days=7), user_id="u-2101")
    assert events == []
    assert svc.thread is not None, "the list was never executed"
    assert svc.thread is not threading.current_thread(), "execute() ran on the loop's thread"
