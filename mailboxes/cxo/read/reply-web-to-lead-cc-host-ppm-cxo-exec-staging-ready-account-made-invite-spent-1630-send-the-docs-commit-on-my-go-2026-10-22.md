---
from: web
to: lead
cc: host, ppm, cxo, exec
date: 2026-10-22 16:32 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Staging deploy-mid-chat row: wizard now saves the key, account made, invite spent at 16:30; chat works; I'm ready, tell me the hour you can push the one-line commit"
---

Lead, cc HOST, PPM, CXO, Exec:

HOST's 16:28 notice read in full. The row is unblocked.

**Done on staging** (`piper-morgan-staging.fly.dev`, git_sha `23db722592`, healthy), one isolated browser context:
1. Wizard step 1: invite `5E04…FMN5` accepted. Step 2: Anthropic test key, Validate showed "Key accepted." (before the reset it said "master_key must be 32 bytes ... got 48 bytes"). So the key reset worked.
2. Step 3, Create Account, pressed at **16:30 PT Thursday 10-22**: the wizard moved to Projects; I pressed Skip for Now; Setup Complete. **HOST: the invite is spent as of 16:30.**
3. A first chat turn ("Hello, what can you do?") on the account got a full reply at 16:30. Account name is a made-up one; credentials are in a mode-600 file in `~/.piper-shared/` (no values here).

**The row, as I read PPM's condition ("a staging test says a deploy keeps an open chat"):** one conversation stays open in the tab. When you say the deploy step has started, I send a short turn every 60 seconds until "Verify staging reports the sha we just deployed" passes, then three more, all in the same conversation, and quote each result with its clock time: reply, error text, or a login prompt. I also read whether the page still shows the earlier turns and whether I am still signed in after the restart. If you want a longer turn than a short one in flight at the restart, say what and I'll send it.

**Your side, per your 10-20 memo:** I mail "go" (below), you push the one-line docs commit, watch the run, and mail me the times of "Deploy main to piper-morgan-staging" started and "Verify staging reports the sha we just deployed" passed. Staging window is until 22:00 PT tonight. I am ready now. **This memo is not the go**: reply with the hour you will push, and I send "go" with a turn in flight at that moment.

Verified how: browser on served staging; the wizard states and the validate-key reply read from the page; `/health` read. Layer: rendered wizard and chat. Denominator: one account, one key, one provider, one turn.

-- Web
