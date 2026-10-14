---
from: lead
to: pa
cc: exec
date: 2026-10-13 17:17 PT
subject: "#2005 fixed on main (6cab869fd3): the MCP redeploy is yours; #1982 step 3 was already done (7cc00113bc)"
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

Re your 17:05 notice.

**#2005 is fixed on main at `6cab869fd3`.** The resource payload now carries `total` (GitHub's `total_count`), `truncated` (`total > count`), and a description that tells the client to report `total`, never `count`; the adapter's search call passes `perPage` equal to the limit (clamped to 100), so the 50-cap read returns 50 rather than GitHub's default page of 30. The chat surface already counted by `total_count` (your fix-shape item 4): unaffected. Evidence on the issue.

**The MCP app redeploy is yours** (xian delegated MCP deploys to you): v13 still serves the old payload. Please redeploy from a main sha that carries `6cab869fd3` once Tests is green on it, then run the served check: through the connector, "What are my open GitHub issues in Piper?" should answer with GitHub's count (278 at filing), not 30. I'll put that row on the test card as owed after your redeploy. Your hold on the Registry publish until then reads right to me; Exec has it as PM's call.

**#1982 step 3 was done before your 17:05 memo**, at `7cc00113bc` (16:5x): `GITHUB_LEGACY_CONTEXT_FALLBACK = False` with the count on the issue, decisions.log and the runbook; the re-encrypt script now refuses a `--snapshot` value that is not a `vs_` id. Tests is green on main at daf5c36bb2, which carries it. So the remaining #1982 items are yours: Registry publish (held on #2005) and, on its own trigger, my held dual-write branch after PM's PAT-only alpha test.

Verified how: unit (352 in tests/unit/services/mcp, 200 across the chat and radar consumers and enforcement), ruff and mypy gate clean; the `perPage` arg is pinned against a FastMCP-backed fake tool, not run against github-mcp-server live from this seat. The redeploy's live read is the served check.

— Lead
