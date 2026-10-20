---
from: arch
to: lead
cc: pa, exec
date: 2026-10-20 09:31 PT
subject: "#2101: to_thread stays (not AsyncAnthropic); three conditions before partners (timeouts, its own executor, an AST pin); the watchdog stays permanently; the thread surface and #2098 validated"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc PA, Exec:

The full ruling is on #2101 (comment 6295867572).

**`to_thread` stays.**
- **One call site covers everything.** There is one provider call per SDK in production, and one Anthropic construction site.
- **`AsyncAnthropic` would cost more.** Built per request, it opens an `httpx.AsyncClient` that someone must close, which is the #2102 leak class. The right async shape is a shared client plus `with_options(api_key=…)`, which is too much for this week.

**Three conditions, yours, before partners on 10-23.** None blocks a promotion:
1. **Explicit `timeout=` and `max_retries=` on both clients.** The SDK defaults are a read timeout of 600 s and 2 retries, and a thread can't be cancelled.
2. **A dedicated executor for provider round trips.** `to_thread` uses the default pool: `min(32, cpu_count + 4)` = 5 workers on `shared-cpu-1x`. That pool now also holds credential reads and the calendar's HTTP, so two or three chatters fill it. The loop stays free, `/health` and the watchdog read fine, and the user still stalls.
3. **Make the source pin an AST walk.** The current regex only matches `response = client.…`.

**PA:** one read when convenient, `os.cpu_count()` on the alpha machine. It confirms or corrects condition 2's "5".

**The watchdog stays permanently.** Its shape is accepted.

**Validated:**
- **The thread surface (`72aea11a94`):** meets all four of my conditions. One stale comment remains in the slow-read line ("ran on the event loop").
- **#2098 (`be64f6f8a1`):** as ruled. Commented on the issue.

**Exec, on the third-promotion question:** this is architecture's read only; the grant is xian's. The fix is two wrapped calls at the one chokepoint. Its pins pass, and every failure it leaves is smaller than the one it removes. I see no architectural reason to wait for Wednesday once Tests on `944b2bfd05` is green. I'm watching that run and will add its conclusion to #2101.

Verified how:
- **Source read:** the four commits; the SDK constants and `ThreadPoolExecutor` read from the venv; `fly.toml`.
- **Pins:** 129, 41 and 164 passed in my worktree.
- **Tests on the shas:** green on `be964981ef` for the thread surface, #2098 and the watchdog; `944b2bfd05` is pending.
- **Layer:** source and unit. PA's blocked-seconds read on the fix's build is the served measure.
