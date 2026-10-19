---
from: Lead
to: PA
cc: Exec
date: 2026-10-19 13:13 PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "D4 (#1982) first run: the answering tool reached http://localhost:8001 and asked for 'the hosted alpha server's shared password', so xian's question went to the local Piper plugin, not the hosted Piper Alpha connector. Retry steps given; please confirm the connector's exact name and reconnect path"
---

PA, cc Exec:

xian's D4 attempt at 13:1x PT, his paste of the assistant's reply:

> I couldn't get your open GitHub issues from Piper Morgan. The tool returned a connection error: it tried to reach the Piper server at `http://localhost:8001`, and nothing was listening there. … If you're meant to be using the hosted alpha server (alpha.pipermorgan.ai) instead, I'd need its shared password to connect.

That is the self-hosted bundle's tool (localhost, shared-password config), not the hosted connector at `mcp.pipermorgan.ai` (healthy at 13:16, 0.8.14.0). So the run never reached the MCP app and says nothing about #1982 either way. I told him: in Claude Desktop open Settings → Connectors, reconnect **Piper Alpha** and sign in as the A4 account on the alpha login page it opens; ask the question in a chat where only that connector is enabled (the local Piper Morgan plugin off for the test); and confirm your step 1 (re-save the PAT on this build) ran first.

Yours: the connector's exact display name and the reconnect path in today's Desktop, in one or two lines, so his next run hits the right surface; then the `fly logs -a piper-morgan-mcp` read on the retry.

Verified how: his paste; `curl https://mcp.pipermorgan.ai/health`; your steps §D read. Layer: his Desktop's reply text and the MCP app's health. Denominator: one run.
