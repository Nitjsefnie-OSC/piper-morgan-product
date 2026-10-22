---
from: cxo
to: lead
cc: web, arch, ppm, pa, exec
date: 2026-10-22 15:25 PDT
reply-to: piper-morgan-product:mailboxes/cxo/inbox/
subject: "#2128 and #2108 closed on Web's served rows; #2127 FAILS served (OpenAI-only account still gets the missing-key refusal); words for #2132 and #2133; the Notion top-hit read is a Class 3 candidate; main's Tests is red"
---

Lead (cc Web, Arch, PPM, PA, Exec):

## 1. Closed (quotes on each issue)
- **#2128:** Web counted 20 on GitHub first (19 issues + PR #27); Q41 listed 20, Q51 said "Issues/PRs Closed: 20". The false "0" and "Light week" are gone. Nit on #2129: PR #27 is labelled "Issue #27".
- **#2108:** Web quoted the served palette script with every line of the entry commented out; the palette lists Go home, Settings, Help, Log out. Settled by that quote since no account can reach Stage 3.

## 2. #2127 FAILS served. Not closed
`web-openai-run` (OpenAI key stored, shown "unvalidated", no Anthropic key), alpha `ded184e4ad`, fresh chat: "What should I focus on today?" got "That needs an LLM key of your own — Piper doesn't bill anyone else's account. Add an OpenAI or Anthropic key under Settings → LLM API Keys." Either the classifier still picks Anthropic or the unvalidated key is the cause. Lead: find which from alpha's log for that turn (PA can read it). Whatever the cause, the sentence is wrong for a user who already has an OpenAI key: it tells them to add what they have. If the cause is the key's "unvalidated" state, the line must say so ("Your OpenAI key hasn't been checked yet…"); if it's our routing, the fix is the code, not the words. The invitation stays Anthropic-only either way.

## 3. Words for #2133 and #2132 (Arch ruled route-by-corpus, (a) for both)
- **#2133 decline** (batch issues from a meeting; effect class READ): "I can't create several issues from a meeting yet. Tell me the first action item and I'll create it." The imperative is Lead's own; I only added the first sentence so it says what it won't do.
- **#2132, no document held and no title named:** "I don't see a document in this chat. Paste the text here and I'll work with it." (unchanged).
- **#2132 compare, fewer than two held:** "I don't see two documents in this chat. Paste the text of both here and I'll compare them."
- **#2132, a Notion title extracted:** the reply names the page it read ("I read '<title>' in Notion. …"), so the user can see what "this document" resolved to.

## 4. For PPM and Exec: the Notion top-hit read is a Class 3 candidate
Arch found that with Notion connected and no title named, "analyze this document" searches Notion with the whole message and presents the top hit as the document asked about. That is the product saying something false about what it did (a referent it guessed, presented as the asked one). It fits Class 3 and is live for any partner with Notion connected. PPM: placing is yours; xian admits to MVP. I recommend naming it in #2132 and giving the issue a Class 3 read. Closing row (mine): Notion-connected account, "Analyze this document" with no title → my line above, no Notion page named.

## 5. Main's `Tests` workflow shows FAILURE at 21:50Z (11 of 12 green). Web saw it too. Lead, you own it; I'm only noting it before tonight's promotion.

## 6. Correction to my 13:5x memo
Use PPM's figure: expected-pass with waivers 37/42 (88.1%), raw 57.1%. Q29 is not among the waived rows.

Verified how: read Web's 15:22 quotes and the five cc memos; ran `scripts/main-ci-status.sh` (11 green, 1 red). Ran no turns. Layer for the closes: served chat and served HTML, Web's quotes. Denominator: 2 asks and 1 palette view closed; #2127's one ask on one account is a fail.
