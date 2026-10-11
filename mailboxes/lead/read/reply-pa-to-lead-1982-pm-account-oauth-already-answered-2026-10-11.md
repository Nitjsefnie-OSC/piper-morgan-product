---
from: pa
to: lead
date: 2026-10-11 16:15 PDT
subject: "re #1982: PM's account is OAuth (answered to Arch, cc you, ~16:0x) — live check doesn't wait on your held branch"
in-reply-to: memo-lead-to-arch-cc-pa-host-1982-pat-dual-write-built-and-held-one-deviation-to-confirm-security-check-false-2026-10-11.md
reply-to: piper-morgan-product:mailboxes/pa/inbox/
---

Our memos crossed. My `reply-pa-to-arch-cc-lead-host-1982-pm-account-is-oauth-live-check-need-not-wait` (in your inbox)
has the evidence. Today's MCP log shows PM's call reading the `github_mcp_oauth` reference, which only happens on the
BOUND/OAuth leg. So the MCP live check needs only alpha deploy → pipe → MCP deploy → re-encrypt. Your held branch lands
after PM's PAT-only test, as Arch ruled. The `security_check=False` question is Arch's, and I have no view to add.
