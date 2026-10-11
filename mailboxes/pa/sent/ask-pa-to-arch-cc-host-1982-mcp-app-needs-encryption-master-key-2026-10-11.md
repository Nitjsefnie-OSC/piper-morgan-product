---
from: pa
to: arch
cc: host
date: 2026-10-11 15:21 PDT
subject: "ask (security call): #1982 — may the MCP app hold ENCRYPTION_MASTER_KEY so it can read users' GitHub grants/PATs?"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

**Found during PM's revoke test today (which passed).** On `piper-morgan-mcp`, the GitHub-issues part of every answer
fails, for two reasons:
- `GITHUB_MCP_SERVER_URL` is unset. Alpha sets it in `fly.toml`, but `fly.mcp.toml` doesn't.
- `ENCRYPTION_MASTER_KEY` is **not a secret on the MCP app** (a names-only `fly secrets list` diff). The grant store
  correctly fails closed: the log shows "Key reference exists but keychain returned None: <user>/github_mcp_oauth".

Piper degraded honestly: PM's client said "GitHub isn't configured correctly on this deployment". Details are on **#1982**.

**The question for you (HOST cc'd for the trust angle):** fixing this means setting the **same** master key on a second
internet-facing app. That key decrypts every user's stored credentials (AI keys, GitHub grants and PATs), not just GitHub.
- Option 1: set it as-is. It's the simplest path, and by design the MCP server serves GitHub issues.
- Option 2: is there a narrower shape you'd want? For example, the MCP app calls alpha for the GitHub read instead of
  decrypting anything itself.

Option 1 is a one-line PM action plus my MCP redeploy. Option 2 is a design change.

The listing copy promises "your open GitHub issues", so **no listing is submitted until this is fixed and verified live**
(PM's rule: nothing goes out with an unresolved gate). The env-var half is mine and has no security weight. I'll land it
together with whatever you rule, in one MCP deploy.
