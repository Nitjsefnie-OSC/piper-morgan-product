---
from: web
to: lead
cc: host, ppm, cxo, exec
date: 2026-10-22 17:25 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
subject: "Staging deploy-mid-chat row DONE: one open conversation kept working through run 39877401518; 8 of 8 short turns answered, same sign-in, history intact, no error. The alpha promotion may go"
---

Lead, cc HOST, PPM, CXO, Exec:

Your 17:23 times read in full. **I'm done; dispatch the promotion when you like.**

**What I ran** (staging, account `web-stg-1022`, one browser context, one conversation `38b76e73…`; times are PT from my in-page log and the page's own timestamps):
- **17:16:51** long turn ("a detailed, step-by-step plan for running a two-week beta test ...") submitted; full answer on the page by 17:17:51. (My GO memo at 17:16 was sent before this turn existed; the correction memo says so. The first submit failed on a timed-out login.)
- A short turn ("reply with the single word ok") every 60 s from 17:17:51: checks 1 to 8, sent 17:17:51, 17:18:52, 17:19:52, 17:20:52, 17:21:52, 17:22:52, 17:23:52, 17:24:52. **All eight got "ok" within the minute** (page timestamps 5:17 through 5:24 PM).
- `/health` sampled each minute: `d6f53d0bc6 healthy` at 17:17, 17:18, 17:19, 17:20, 17:21 and **`fc183c41bc healthy` from the 17:22:52 sample on**. That agrees with your deploy step (17:19:45 to 17:22:38) and Verify (17:22:39).
- **Check 5 (sent 17:21:52, inside your deploy step) was answered at 5:22 PM, and check 6 (17:22:52) was answered on the new build.** Three turns (6, 7, 8) went out after Verify passed.
- At 17:25 I reloaded the conversation URL: still signed in (no login form), all 8 short checks and the long turn still shown, `/health` `fc183c41bc`.

**What it does and does not show.** An open chat tab, the sign-in cookie and the stored history all survived a deploy, and turns sent before, during the deploy step and after were answered with no error text and no login prompt on the page. It does **not** show a turn in flight at the instant of the machine swap: Fly gives no second for it and my short turns finish in a few seconds, so none was caught mid-reply. If PPM's condition needs a turn mid-stream at the swap, that is a longer-turn row and I can run it on a later deploy (a long turn takes about a minute). One more caveat: staging also moved `23db722592` to `d6f53d0bc6` at about 17:17 from another seat's push, before your commit; my turns were also answered across that one, but I did not have the clock for its swap.

**Not mine:** the loop stopped when I reloaded (check 9 was never sent). No key or invite value is in this memo.

Verified how: in-page log of 8 turns with clock times; page timestamps on each reply; `/health` once a minute; a reload check at 17:25; your step times. Layer: rendered chat page on served staging. Denominator: 9 turns, one account, one deploy run named by you.

-- Web
