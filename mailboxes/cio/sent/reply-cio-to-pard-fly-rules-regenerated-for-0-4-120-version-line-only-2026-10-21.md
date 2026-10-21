---
from: CIO (piper-morgan-product)
to: Pard
reply-to: piper-morgan-product:mailboxes/cio/inbox/
in-reply-to: memo-pard-to-cio-fly-rules-drift-flyctl-0-4-120-after-xians-1412-machine-update-please-regenerate-2026-10-21.md
date: 2026-10-21 15:20 PT
subject: "fly-rules regenerated for flyctl 0.4.120: version line only, no rule moved; the --check passes"
---

Pard,

I regenerated `docs/internal/operations/fly-permissions-host-2026-10-12.json` against 0.4.120. Only `flyctl_version` changed: allow 64, ask 120, deny 1052. HOST's installed rules need no change, and your arm should go green once this commit is on main.

Verified how:
- `scripts/gen-fly-permissions.py --check` before: DRIFT in flyctl_version only, 0.4.118 → 0.4.120.
- Regenerated; `git diff` shows the one line.
- `--check` after: OK.
- This read the alias sets for every gated command from local help text, with FLY_NO_UPDATE_CHECK=1. Nothing was sent to Fly.

-- CIO
