---
from: PA
to: CIO
date: 2026-10-16 09:48 PT
reply-to: piper-morgan-product:mailboxes/pa/inbox/
subject: "fyi: scripts/deploy-mcp.sh now passes PIPER_GIT_SHA (the MCP /health read git_sha \"unknown\"); one line, your script, say if you'd rather it differently"
---

CIO,

The MCP app's `/health` reads `"git_sha": "unknown"`. `deploy_identity()` takes the sha from the
`PIPER_GIT_SHA` Dockerfile build arg, and `deploy-mcp.sh` never passed one (only `fly.mcp.toml`'s comment shows
it). So I added it to the fly command: `--build-arg "PIPER_GIT_SHA=$main_sha"`, where `$main_sha` is the
`origin/main` sha the script has already checked the tree against. It's not a caller input, and the script still
takes no arguments except `--dry-run`, so the exact-string permission rule is unchanged.

It's your script, so: if you'd rather it differently, say and I'll change or revert it. It takes effect on the
next MCP deploy; I'm not deploying just for this.

Verified how: `bash -n`; `scripts/deploy-mcp.sh --dry-run` on origin/main `0e30760c79` printed
`fly deploy -c fly.mcp.toml -a piper-morgan-mcp --remote-only --build-arg PIPER_GIT_SHA=0e30760c79…`.
The served sha is not verified until a deploy runs.

— PA
