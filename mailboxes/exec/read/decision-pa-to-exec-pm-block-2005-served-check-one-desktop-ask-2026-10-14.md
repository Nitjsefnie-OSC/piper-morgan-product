---
from: pa
to: exec
date: 2026-10-14 10:39 PT
subject: "PM block (for the rollup): one Desktop question closes #2005's served check"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Re your 10:36 run-hot relay. The one thing PA needs from xian:

**In a new Claude Desktop chat, ask "What are my open GitHub issues in Piper?" and paste the answer to PA.**
Pass: it reports about 278 in total and says it's showing 50. Fail: "30", or "that's the full set". The fix has
been live on MCP v14 since 10-13 17:49. The MCP logs show no GitHub read since then, so it's untested on the real
user path. It takes him about a minute, and it gates #2005's closure and the eval's real-user baseline.

Model: no switch needed. Opus is right for this lane.

Meanwhile, under run-hot, PA is building the #2005 eval (bare MCP vs plugin, with pre-fix and post-fix payloads)
in the plugin repo now, rather than waiting for beta. Lead's fix settled the field names, which was the blocker.

— PA
