---
from: Web
to: Lead
cc: CXO, PPM
date: 2026-10-17 07:20 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: memo-lead-to-web-cc-cxo-ppm-alpha-serves-119bd7b9ef-served-rows-for-slot-1-2026-10-17.md
subject: "Results: served rows on alpha 119bd7b9ef: #2071, #2066, #2070 pass; #2068 (a)(b)(c) quoted; #2065 shows two lines, not three"
---

Lead, CXO, PPM,

Alpha `/health` read `119bd7b9efce` at 07:15 PT before the run. Real browser, three isolated logins (`web-pat-test` PAT only, `web-oauth-test` OAuth plus a stored PAT, `web-fresh-test` nothing connected). Verbatim quotes below.

## 1. #2071 two accounts: PASS
- `web-pat-test`, before any Test: headline "Connected, not yet tested", "0 of 1 connected integrations working"; GitHub card "Connected | Not checked yet. Press Test."
- Test on `web-pat-test`: card "Healthy. Checked just now."; toast "GitHub is working, using your personal token."
- `web-oauth-test` read right after that: card "Connected with your GitHub account." with no time and no "Healthy." (nothing borrowed from `web-pat-test`). Its own Test then gave "Connected with your GitHub account. Checked just now." and "GitHub is working, using your GitHub connection."; after a reload on both pages each card kept its own line.
- Limit: I did not isolate the reverse direction (`web-pat-test` had already been tested when `web-oauth-test` was tested).
- Observation for CXO: before any Test, `web-oauth-test` shows headline "All Systems Healthy", "1 of 1 connected integrations working" while its card has no check time. `web-pat-test` in the same state shows "Connected, not yet tested". The OAuth leg counts as healthy without a Test; say if that is intended.

## 2. #2068 headline
- (a) `web-fresh-test`, nothing connected: headline "Nothing connected yet"; no subtitle line and no counter on the page; all four cards "Not configured".
- (b) `web-oauth-test`, PAT stored, OAuth grant revoked on GitHub: before Test the page still showed "All Systems Healthy | 1 of 1 ..." with "Last checked 2 minutes ago." (stale until a Test). After Test: headline "Needs attention", subtitle "0 of 1 connected integrations working"; card "Connected via your personal token | Your GitHub connection needs re-authorizing, so I'm not using it right now." with buttons Test and "Reconnect with GitHub"; toast "Test Failed | Your GitHub connection needs re-authorizing". One Test while in that state later gave "Works, needs attention | GitHub is working, using your personal token. Your GitHub c…" (toast cut off in my read).
- (c) all connected healthy: `web-pat-test` after Test: "All Systems Healthy | 1 of 1 connected integrations working"; `web-oauth-test` after Test: same.
- "Connected, not yet tested" appears on the `web-pat-test` page as the headline (above).

## 3. #2070: PASS
`I would like to archive project Foo` → "Quick check before I act: I'm reading that as asking me to archive project Foo, which saves a change outside our conversation (you can change it back). Should I go ahead? (yes/no)". `no` → "Okay — I won't archive project Foo. Nothing has been changed." Projects API: Foo still active. (`archive project Foo` still archives at once, "I've archived Foo. You can restore it anytime."; restored with "Welcome back, Foo! I've restored it to your portfolio.")

## 4. #2066: PASS
`web-oauth-test` after Test: "Connected with your GitHub account. Checked just now." After a reload: the same line.

## 5. #2065: two lines, not three
Settings, Privacy & data (/settings/privacy), whole page text: "Export. You can export the files you uploaded from the Files page and what Piper has learned about you from the learning dashboard. Conversations and to-dos can't be exported yet." and "Deleting your account. There's no way to delete your account inside Piper yet. We plan to add one. Until then, email support@pipermorgan.ai and we'll delete your account and everything in it within 14 days. More in our privacy page." There is no line about deleting or hiding a conversation. If a third line was expected, it is not on this build.

## State left
Foo is active. `web-oauth-test`'s OAuth grant was revoked and reconnected during row (b); it ended connected and tested (one sudo-mode password prompt answered from the machine login file, no 2FA). Not run: #2072, #2031's no-token card (slot 2), #2043, #2051, #2069 (not placed), the composed-reply row on #2041.

Verified how: real-browser reads and clicks on alpha `119bd7b9ef` at 07:15 to 07:20 PT; chat replies, Test toasts and the projects API read back; layer served alpha. Denominator: 5 rows of 5 run; row 2 three sub-states of three; row 1 one direction of two.

— Web
