"""Name-free count of accounts with a chat turn in the last 30 minutes (the quiet count).

xian's ruling (2026-10-20, via Exec and Janus): design partners are worldwide, so no
clock hour is quiet; a promotion should wait for a quiet 30 minutes instead. CIO
wrote it into the promotion grant (condition 3): the 20:00-21:00 PT window holds
until alpha's own /health serves this count and the promote gate refuses while it
is above zero.

What is kept: for each principal that sent a chat turn, a one-way hash of the id
and the time of its last turn; plus the times of recent turns. No id, no name, no
text. Process-local: alpha runs one machine, so the process is the deployment; a
second machine would need a shared store, which this module does not pretend to be.
"""

from __future__ import annotations

import hashlib
import threading
import time
from collections import deque
from typing import Deque, Dict, Optional

WINDOW_SECONDS = 30 * 60


class TurnActivity:
    """A rolling window of chat-turn activity, counted without names."""

    def __init__(self, window_seconds: int = WINDOW_SECONDS) -> None:
        self.window_seconds = window_seconds
        self._last_turn_by_account: Dict[str, float] = {}
        self._turns: Deque[float] = deque()
        self._lock = threading.Lock()

    @staticmethod
    def _token(principal: str) -> str:
        return hashlib.sha256(principal.encode("utf-8")).hexdigest()[:16]

    def record(self, principal: Optional[str], now: Optional[float] = None) -> None:
        """Record one chat turn. A turn with no principal counts as a turn, not an account."""
        ts = time.time() if now is None else now
        with self._lock:
            self._turns.append(ts)
            if principal:
                self._last_turn_by_account[self._token(str(principal))] = ts
            self._prune(ts)

    def _prune(self, now: float) -> None:
        cutoff = now - self.window_seconds
        while self._turns and self._turns[0] < cutoff:
            self._turns.popleft()
        stale = [k for k, v in self._last_turn_by_account.items() if v < cutoff]
        for k in stale:
            del self._last_turn_by_account[k]

    def snapshot(self, now: Optional[float] = None) -> Dict[str, int]:
        """``{"accounts": N, "turns": M}`` for the window ending now."""
        ts = time.time() if now is None else now
        with self._lock:
            self._prune(ts)
            return {"accounts": len(self._last_turn_by_account), "turns": len(self._turns)}


#: The one process-wide instance: the intent service records into it, /health reads it.
TURN_ACTIVITY = TurnActivity()
