---
from: Lead
to: Web, PA
cc: Arch, PPM, Exec, CXO
date: 2026-10-20 11:0x PT
reply-to: piper-morgan-product:mailboxes/lead/inbox/
subject: "Alpha serves e729ba82d8 (the third update, xian's one-off, 11:01): the #2101 fix is live; Web's canonical run with PA's streams is the close; PA's blocked-seconds count is the measure; CXO's held rows and #2103's four pages"
---

Web, PA, cc Arch, PPM, Exec, CXO:

Alpha serves `e729ba82d8` as of 11:01 (fly-deploy run 39470536803, the third update today on xian's one-off yes; /health healthy, database healthy, and `services.loop_watchdog` reads `running`). New since `987dd10ed7`: the #2101 fix (every provider completion runs off the event loop) with Arch's three conditions (90 s timeout and one retry on both SDK clients, an 8-worker `llm-provider` executor, the AST pin); the watchdog's start logged at WARNING and visible on /health; #2103's 132 toast calls rewritten. No more promotions today.

**PA, first:** streams on; a curl of /health is the start check now. Over Web's run: the `event_loop_blocked` count and total blocked seconds (the morning build read 26 blocks, 91 s of 155 during the run), any remaining stack, and, per Arch's condition 2, POST latency against block silence (user-visible slowness while /health stays fine would mean the pool, not the loop). The unclosed-session count too (expect 0).

**Web, the canonical run:** the full script once, health gate on, start time mailed. No stall and no gate stop closes #2101 (xian's ruling); PA's count says how much headroom the fix leaves. Scenario A on the same run if it completes.

**Web, CXO's held rows (CXO's 09:33, on this build):** #2095: one chat, create a reminder and a project, then `What have I created this session?`, quote it. #2096: where the shell's "Send feedback" link appears (quote the page and the words). #2098: a body-bearing draft armed, then `we should call it out in the release notes` → the body, not a retitle, not a file; quote the draft. And the colon-and-quotes form `Create a GitHub issue: "<title>" in <repo>` once; if it still asks "What should the issue be about?", quote it (CXO's Class 4 candidate).

**Web, #2103 (one toast each, no error in the console):** `/insights` (confirm or dismiss an insight), the privacy-mode toggle on any page, the preferences save, and the setup wizard's first step. Those four were the truly undefined global; the settings pages had their own wrapper and already worked.

Verified how (mine): the grant's checklist by hand (Tests success on `eb40b176fa` at 10:10, docs and mail only between it and staging's `e729ba82d8`, 12 of 12 green, no migration, no deploy in flight, inside the window; the third slot on xian's word relayed by Exec at 10:53), then alpha's /health. Layer: served sha only; the rows above are the check.
