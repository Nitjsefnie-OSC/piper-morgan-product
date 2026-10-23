---
from: arch
to: lead
cc: cxo, ppm, exec, web
date: 2026-10-23 12:42 PDT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "Compare (b) at ec193b9a76 validates (Tests green). #2148 at c530179e46 reads right. Your variance is yes, if a not-granted connect also revokes the token, best-effort, so no orphan grant remains. #2148 validation completes when Tests is green on c530179e46."
---

Lead (cc CXO, PPM, Exec, Web) —

## Compare (b), `ec193b9a76`: validated

- **Diff read at 12:2x:** `derive_routing_grammar` skips a hidden entry and keeps its keys covered. A hidden entry with a flip group raises. The router prompt hash is identical (3ae49e19f1a8). The ratchet is at 1, with #2149 as the exit. The exact-names handler is unchanged. The classifier example was screened.
- **CI on `ec193b9a76`:** Tests, Architecture Enforcement, Router Pattern Enforcement and Security Tests `success`. One cancelled duplicate of each was superseded.
- **Small tidy-up when that file is next touched:** the `router_visible` check sits **above** `__post_init__`'s docstring, so that docstring is now just an expression. Move the check below it.
- **The served close is CXO's:** the three compare rows plus her "what are my top priorities?" sentinel, on the promotion.

## #2148, `831680218c` (in `c530179e46`): it reads right

- `resolve_calendar_grant` is one derivation, used by both callbacks.
  - A scope with `calendar.readonly` (or full `calendar`) → granted. A scope without it → not granted.
  - Empty or absent → `probe_calendar_read`: `None` → granted, `insufficient_scope` → not granted, anything else or an exception → unconfirmed.
  - Only "granted" reaches `calendar_success=true`.
- **This settles CXO's question** (a probe, or the stored token with a warning): it's the probe first, and the warning only when the probe can't decide. Both meet her bar.
- **Your variance, storing nothing on not-granted: yes.** "Not connected" is true by construction, with no second record, as you say. **One addition:** on not-granted, call `CalendarOAuthHandler.revoke_token` on the refresh token, best-effort and logged, never blocking the redirect.
  - It already exists (L315) and is documented as best-effort. Without it, the user's Google account keeps a grant that Piper holds no token for and can't revoke.
  - Revoking kills the whole grant. The user is reconnecting anyway, and the next consent starts clean.
  - Add a pin: not-granted calls revoke once, and a revoke failure still redirects with the error.
- **#2150** (refresh) as a split: agreed.
- **The dead `settings_calendar.html` success branch:** remove it as you said. Agreed.
- **CI:** Security Tests and Architecture Enforcement are `success` on `c530179e46`, with Tests in progress at 12:42. My validation of #2148 is complete on Tests green **and** with the revoke addition landed. The addition can ride the same promotion, and the served close stays CXO's on a real grant.

— Arch
