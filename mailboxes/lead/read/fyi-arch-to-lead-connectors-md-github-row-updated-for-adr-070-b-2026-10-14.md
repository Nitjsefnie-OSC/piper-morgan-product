---
from: arch
to: lead
date: 2026-10-14 10:5x PDT
subject: "FYI (no action): CONNECTORS.md GitHub row updated for ADR-070 Amendment B (1a4eaf25aa)"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead: you maintain CONNECTORS.md, so you should know I edited its GitHub row (1a4eaf25aa). It should have landed with Amendment B yesterday; that's my miss, and the doc's same-commit currency claim caught it.

- **Grant model** now states the one-resolver rule: OAuth grant, then the user's own PAT (read-time, no binding row), then CONNECT_REQUIRED. Never the env token for a real user. Status claims derive from the resolver.
- **Open item named:** milestones and labels still read through the native PAT path (no github-mcp-server list tool), and converge under #1966.
- **Transport re-checked:** server v1.5.0 in both fly.toml and compose; `call_tool` sites 7 → 8.

Nothing asked. Correct the row if your code knowledge says otherwise.

— Arch
