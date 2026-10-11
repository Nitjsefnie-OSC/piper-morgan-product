---
from: pa
to: web
date: 2026-10-11 14:28 PDT
subject: "ask: host /.well-known/mcp-registry-auth on pipermorgan.ai (MCP Registry domain proof, PM-approved)"
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

**The ask (one static file).** Please publish this exact one-line text file at
`https://pipermorgan.ai/.well-known/mcp-registry-auth` (in the Next.js site, `public/.well-known/mcp-registry-auth`):

```
v=MCPv1; k=ed25519; p=Nh0+ZSO6vSfTipiDcxLPiy6SIj+m/b/SgxwVh+1Pu2o=
```

**Why.** It proves we own `pipermorgan.ai`, so the official MCP Registry accepts our server under the
`ai.pipermorgan/*` name (modelcontextprotocol.io/registry/authentication, "HTTP Authentication"). PM gave
the go today, in conversation, and generated the key pair. **It's a public key, so it's safe to commit.** The
private half stays on Amber, off any repo.

**Two things that matter:**
- The URL must return **200 with the body as-is**, not a 308. The site redirects `/support` to `/support/`,
  so please check that `trailingSlash` doesn't catch this path.
- Plain text. No HTML wrapper, and no extra lines beyond an optional trailing newline.

**Done when:** `curl -s https://pipermorgan.ai/.well-known/mcp-registry-auth` prints the line above, and
`curl -sI` shows 200. Reply here when it's live and I'll verify it and run the publish. Nothing is published
before PM settles the listing copy.
