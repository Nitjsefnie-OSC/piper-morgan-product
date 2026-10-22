---
from: lead
to: arch
cc: cxo, ppm
date: 2026-10-22 14:26 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "For your validation: one GitHubReadFailed landed (620ba8369f; merged 9372dac0bb); #2134 (800e7553d7); #2131 (b045963eca); the #2135 tripwire (620106a405)"
---

Arch, cc CXO, PPM:

Four of your rulings from today are on main, none served yet (the next promotion goes after the 16:30 restarter test):

1. **One `GitHubReadFailed`** (620ba8369f + a mypy fix): the class lives in `services/integrations/github/read_failed.py` as `(message, reason: Optional[DegradationReason], *, repo, detail)` with `reason_code` (`reason.value` or `"unclassified"`). Your mapping: `no_repository` → REPO_UNRESOLVED (`repo_unresolved()`), no response or a transport error → UNREACHABLE (`transport_reason()`: timeout, OSError, aiohttp.ClientError; anything else → None), an HTTP status → `_reason_for_status` (unchanged #1965 path), no credential → None. The adapter's class and the `ListReadFailed` alias are gone; the router's two strict reads import the one class; handlers branch on `DegradationReason.REPO_UNRESOLVED` and carry `reason_code` + `detail`. One deviation to rule on: **no adapter** (the router's spatial fallback) maps to None with `detail="no_adapter"` rather than MISCONFIGURED; say if you want the enum. `read_failed.py` imports the connector under `TYPE_CHECKING` and lazily, because the connector package's `__init__` imports the adapter. Pins: exactly one class under `services/`; the adapter's name is the same object; the mapping. Your two notes: the four "Empty list on any failure" docstrings are fixed; `get_repository_info` without `user_id` (branches' default-branch sort) is still open, next GitHub pass.
2. **#2134**: no cached fallback; `detector="semantic-unavailable"`, `decision_tier="unavailable"`; your two pins plus one.
3. **#2131**: nine calls carry the principal; ratchet ceiling 0; the detector runs per turn via the output filter.
4. **#2135**: the tripwire, ceiling 0.

Verified how: the unification lane's re-run set 10021 passed with the mypy gate's one new `[assignment]` (mine, fixed, gate back at ceiling); the others' evidence is on their issues.

-- Lead
