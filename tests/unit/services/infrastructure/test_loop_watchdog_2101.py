"""#2101 — the event-loop watchdog names the call that blocks the loop.

LAYER: the watchdog's checker step against a pinned clock, a real blocked loop in a thread,
and the startup phase's start/stop. DENOMINATOR: no stall while the heartbeat moves; one
announcement per stall with the blocked thread's stack; resume logged with the total; a
real sync block inside a coroutine is seen and named by file and function; startup and
shutdown wire it.
"""

from __future__ import annotations

import asyncio
import threading
import time

import pytest

from services.infrastructure import loop_watchdog as mod
from services.infrastructure.loop_watchdog import LoopWatchdog, format_thread_stack


class TestCheckerStep:
    def test_no_stall_while_the_heartbeat_moves(self, monkeypatch):
        now = [100.0]
        monkeypatch.setattr(mod, "_clock", lambda: now[0])
        wd = LoopWatchdog(stall_seconds=3.0)
        wd.beat()
        now[0] = 102.0
        assert wd.check_once() is None
        assert wd.blocks_seen == 0

    def test_one_announcement_per_stall_then_resume(self, monkeypatch):
        now = [100.0]
        monkeypatch.setattr(mod, "_clock", lambda: now[0])
        seen = []
        wd = LoopWatchdog(stall_seconds=3.0, on_block=lambda age, stack: seen.append((age, stack)))
        wd.beat()
        now[0] = 104.5
        assert wd.check_once() == pytest.approx(4.5)
        now[0] = 105.5
        assert wd.check_once() is None  # same stall, not announced twice
        assert wd.blocks_seen == 1
        assert len(seen) == 1 and seen[0][0] == pytest.approx(4.5)
        assert isinstance(seen[0][1], list)
        now[0] = 110.0
        wd.beat()  # the loop came back
        now[0] = 110.5
        assert wd.check_once() is None
        assert wd._blocked_since is None
        now[0] = 115.0
        assert wd.check_once() == pytest.approx(5.0)  # a second stall announces again
        assert wd.blocks_seen == 2


class TestStackSampling:
    def test_format_thread_stack_names_the_sampled_frame(self):
        def _inner_marker_2101():
            return format_thread_stack(threading.get_ident())

        lines = _inner_marker_2101()
        assert lines, "the current thread has frames"
        assert any("_inner_marker_2101" in line for line in lines)
        assert all(" in " in line and ":" in line for line in lines)

    def test_unknown_thread_has_no_stack(self):
        assert format_thread_stack(-1) == []


class TestRealBlockedLoop:
    def test_a_sync_block_inside_a_coroutine_is_seen_and_named(self):
        """Run a loop in a worker thread, block it with time.sleep inside a coroutine
        (the #2101 shape), and let the watchdog thread catch it."""
        seen = []
        ready = threading.Event()

        def _blocking_call_2101():
            time.sleep(1.2)

        async def main():
            wd = LoopWatchdog(
                stall_seconds=0.4,
                check_seconds=0.1,
                heartbeat_seconds=0.1,
                thread_id=threading.get_ident(),
                on_block=lambda age, stack: seen.append((age, stack)),
            )
            wd.start()
            await asyncio.sleep(0.3)  # heartbeat running, no stall yet
            ready.set()
            _blocking_call_2101()  # the loop is away for 1.2 s
            await asyncio.sleep(0.3)  # resumed; the watchdog logs the total
            await wd.stop()
            return wd.blocks_seen

        worker = {}

        def run():
            worker["blocks"] = asyncio.run(main())

        t = threading.Thread(target=run)
        t.start()
        t.join(timeout=10)
        assert not t.is_alive()
        assert worker["blocks"] == 1
        assert len(seen) == 1
        age, stack = seen[0]
        assert age >= 0.4
        assert any("_blocking_call_2101" in line for line in stack), stack


class TestStartupPhase:
    @pytest.mark.asyncio
    async def test_phase_starts_and_stops_the_watchdog(self):
        from types import SimpleNamespace

        from web.startup import LoopWatchdogPhase, StartupManager

        app = SimpleNamespace(state=SimpleNamespace())
        await LoopWatchdogPhase.startup(app)
        wd = app.state.loop_watchdog
        assert isinstance(wd, LoopWatchdog)
        assert wd._thread is not None and wd._thread.is_alive()
        await LoopWatchdogPhase.shutdown(app)
        assert wd._thread is None
        assert StartupManager.__init__ is not None
        assert LoopWatchdogPhase is StartupManager(app).phases[-1]
