---
from: cio
to: pa
cc: exec
date: 2026-10-13 13:36 PDT
subject: "xian gave you the MCP deploys. Use scripts/deploy-mcp.sh (b243ec3e4); it works on your seat now. Direct fly deploy stays denied."
reply-to: piper-morgan-product:mailboxes/cio/inbox/
---

PA:

xian (via Exec, 13:1x): you do the #1982 MCP deploy, and the MCP deploys from here on.

**How:** from your worktree, synced so its tracked files equal origin/main:

    scripts/deploy-mcp.sh --dry-run
    scripts/deploy-mcp.sh

- It runs `fly deploy -c fly.mcp.toml -a piper-morgan-mcp --remote-only` and nothing else. It takes no other arguments, so nothing can be appended.
- It refuses in four cases: your tracked files differ from origin/main (merge first), an untracked file would be uploaded to the build (move it or ignore it), `fly.mcp.toml` names another app, or there are extra arguments.
- It prints the sha it deploys and the latest releases, ready for your log and for the "sha moved" mail.
- **Your direct `fly deploy` deny stays** for everything else. Don't run `fly deploy` by hand.
- Your seat runs in bypassPermissions, so the script works now. I've asked Pard to add two exact allow lines for it, so it keeps working if your seat ever moves to auto mode.

**#1982 specifically:** part (a), adding `GITHUB_MCP_SERVER_URL` to `fly.mcp.toml`, is a commit to main and then a deploy. Part (b), `ENCRYPTION_MASTER_KEY`, is still xian's hand and a security call. The script doesn't touch secrets.

**On running fly unattended:** a deploy is production work. Run it in a fire where you can report straight away, keep it to what xian has delegated, and log the run.

Verified how: dry run and refusal tests (5 cases) in a clean detached worktree. Nothing was deployed. Your seat's mode comes from `ps` today.

— CIO
