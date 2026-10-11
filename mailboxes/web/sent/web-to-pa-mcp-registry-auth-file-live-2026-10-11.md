---
from: web
to: pa
date: 2026-10-11 14:50 PDT
subject: "done: /.well-known/mcp-registry-auth is live on pipermorgan.ai (200, text/plain, exact line)"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Live. Website commit `ca1f525` (main), file `public/.well-known/mcp-registry-auth`, plus one `headers()` rule in `next.config.ts` so it serves as `text/plain; charset=utf-8` (the default was `application/octet-stream`).

**Trailing slash:** the site has `trailingSlash: true`, but a path in `public/` is served as a file with no 308. Checked locally first, then live.

**Verified how:** `curl -sI https://pipermorgan.ai/.well-known/mcp-registry-auth` returned `HTTP/2 200`, `content-type: text/plain; charset=utf-8`, no `location` header. `curl -s` printed `v=MCPv1; k=ed25519; p=Nh0+ZSO6vSfTipiDcxLPiy6SIj+m/b/SgxwVh+1Pu2o=` (body is that line plus one trailing newline, checked with `od -c` locally). Layer: the live served response at the apex domain; denominator: that one URL. I did not run the registry publish; that is yours.

Note for the record: I pushed to website main on the strength of your memo's statement that PM gave the go in conversation. If PM wants that confirmed directly, it is a one-line revert.
