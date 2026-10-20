"""#2101 — the bounds and the executor for provider round trips (Arch's conditions, 2026-10-20).

Every provider completion runs in a worker thread (the SDK clients are synchronous; called on
the loop they held it for the whole round trip, which was the alpha stall). Three bounds sit
here so both SDK clients and both call sites read the same numbers:

- ``PROVIDER_TIMEOUT_SECONDS`` / ``PROVIDER_MAX_RETRIES``: passed to ``Anthropic(...)`` and
  ``OpenAI(...)``. The SDK defaults (600 s read, 2 retries) would let a hung call hold a worker
  for half an hour; a thread cannot be cancelled from the loop, so the bound is what ends it.
- ``PROVIDER_EXECUTOR``: a dedicated pool for the round trips. ``asyncio.to_thread`` shares the
  loop's default executor (``min(32, cpu_count + 4)``, 5 workers on alpha's shared-cpu-1x),
  which also carries credential reads and the calendar's HTTP; two or three chatters would
  fill it and stall each other while the loop, /health and the watchdog stayed fine.
"""

from __future__ import annotations

import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, TypeVar

PROVIDER_TIMEOUT_SECONDS = 90.0  # a long floor reply with a large context runs tens of seconds
PROVIDER_MAX_RETRIES = 1  # one retry on connection errors / 429 / 5xx; never a silent third try
PROVIDER_EXECUTOR_WORKERS = 8

PROVIDER_EXECUTOR = ThreadPoolExecutor(
    max_workers=PROVIDER_EXECUTOR_WORKERS, thread_name_prefix="llm-provider"
)

_T = TypeVar("_T")


async def run_provider_call(fn: Callable[..., _T], /, *args: Any, **kwargs: Any) -> _T:
    """Run one synchronous SDK round trip on the provider executor and await it."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(PROVIDER_EXECUTOR, functools.partial(fn, *args, **kwargs))
