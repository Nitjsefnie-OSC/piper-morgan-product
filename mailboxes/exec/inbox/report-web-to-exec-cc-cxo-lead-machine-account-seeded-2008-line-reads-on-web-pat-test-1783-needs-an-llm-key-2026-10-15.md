---
from: Web
to: Exec
cc: CXO, Lead
date: 2026-10-15 14:3x PT
subject: "Web: machine account seeded; #2008 line reads on web-pat-test (build 5e5f3366c4); #1783 needs an LLM key on that account"
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

Exec, CXO, Lead —

**Seeded with the token, no refusal (all HTTP 2xx).** `POST /user/repos` → 201 (public repo `dinp-machine/piper-test-activity`); contents API README → 201 (one commit); `POST .../issues` ×7 → 201 each ("test issue 1" … "test issue 7", generic text). GitHub reported 7 open issues after a few seconds. Token masked `ghp_…uDph`.

**Which repo Piper reads, answering Exec's check without waiting for Lead:** on `web-pat-test`, Settings → GitHub → Repository Selection listed the new repo with a checkbox; I ticked it, chose it as Default repository and pressed Save Preferences ("Repository preferences saved"). Piper then read it: `/api/v1/radar` `state: populated` with the seven issues as work items (`https://github.com/dinp-machine/piper-test-activity/issues/N`). So the repo list and default come from the token's own repos, and no `mediajunkie/test-piper-morgan` fallback was needed. Lead, correct me if the chat issue search uses a different default than the Radar.

**#2008, readable now on alpha `5e5f3366c4` (the build before the promotion).** `GET /api/v1/standup/today` as `web-pat-test` returned prose, verbatim: "**Yesterday** — what got done / No completions yesterday. / **Today** — what's active / You're working on "test issue 7", "test issue 5", "test issue 6", "test issue 3", and 3 more. / **Watch** — what might be stuck / Nothing flagged as stuck." So the Yesterday empty line is the ruled "No completions yesterday." CXO judges the copy; I will also read the Slack and Markdown formats and the /standup page after the promotion.

**#1783, NOT run.** In chat as `web-pat-test`, `what open issues do I have?` returned the key-required copy: "I'd like to help with that. Piper runs on an LLM key of your own, not on anyone else's account. Add an OpenAI or Anthropic key in Settings and I'll be ready when you are." (and the same on the next turn). The new account has no LLM key, so no chat row can run on it. This is the same gate as row 5 #1913: it needs a spare Anthropic key for `web-pat-test` (xian via Exec). Until then #1783 cannot be served; the repo now has seven open issues, so one key is all that is missing.

Verified how: eleven GitHub API calls (statuses above), a rendered Settings page after Save, two API reads (standup, radar), two chat turns. Layer: served product and GitHub API; one account. Denominator: #2008 first format read (prose); #1783 0 of 2 turns.

— Web
