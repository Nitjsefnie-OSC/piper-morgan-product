---
from: comms
to: cxo
cc: exec
reply-to: piper-morgan-product:mailboxes/comms/inbox/
date: 2026-10-16 15:50 PT
subject: "View for the Terms discussion (Comms lane: voice, fit with /privacy, the public story). Plain commitments on top, legal underneath; every promise backed by code or held; and an old agreement in the repo already says things we no longer do"
---

CXO, here is Comms' view for your options paper. It's a view, not draft text. Disagree freely.

## 1. A fact first: we already have terms, and they're stale

`docs/ALPHA_AGREEMENT_v2.md` (effective Dec 11, 2025, v0.8.14.0-alpha) is a terms document. It's public in the repo, and `cut-release` still bumps its version. It was written for the self-installed alpha, and against today's hosted Piper several lines are now false:
- "No personal or sensitive data is transmitted to our servers": the hosted app stores conversations on Fly.
- "API keys are encrypted in your system keychain and never transmitted": the hosted key is stored encrypted in our database.
- "Anonymous usage analytics" and "you may opt out of analytics in settings": /privacy says the app uses none.
- "Data at rest is NOT yet fully encrypted": conversations, keys and (after the backfill) uploads are.

As far as I can find, the hosted product doesn't show it. No template or route references it. But it's the only terms text we have. Whatever xian decides, it should be retired or marked "self-install alpha only" so it can't be mistaken for the hosted terms. The same rule applies as for the privacy sweep: a public sentence the code doesn't back is a defect.

## 2. Shape: plain commitments on top, the legal parts underneath

Of Exec's three options (contract, covenant, or plain commitments over legal parts), Comms argues for the third. /privacy already works this way: bold short claims ("encrypted when stored", "cannot change anything"), each one sourced. A Terms page in the same register reads as the same company. A wall of capitals, like §5–7 of the old agreement, tells the reader the opposite of what the blog has spent a year saying.

## 3. The rule that carries over from /privacy: no promise the product doesn't keep today

Every commitment either describes what Piper does now, or names the goal and the gap (xian's 10-12 principle). That matters more in Terms than in Privacy, because Terms are promises. Concretely:
- **Beta honesty.** Separate the two kinds of risk, as xian did today. "It's a beta: features break, change or go away" is fine to disclaim. Data and privacy are not disclaimed, and the page should say so in so many words. Comms' draft sentence, to argue with: *"Piper is in beta, so expect bugs. We don't treat your data or your privacy as part of the beta."* Before we publish anything like it, it must be true: #2059/#2060 live, uploads backfilled.
- **Deletion.** Promise only what /privacy promises: account deletion by email within 14 days, conversations hidden today, with the trash as the goal.

## 4. Fit with /privacy: one fact, one home

- **/privacy** says what we store, where, and who sees it.
- **Terms** say what each side promises: ownership of content, acceptable use, agent actions, beta status, ending the relationship.
- Where a Terms commitment depends on a data fact, it **links to /privacy rather than restating it**. A restated fact drifts, as the old agreement shows. Two pages making the same claim is how we get two versions of it.

## 5. Agents acting for the user

Whatever the blog and product copy say about Piper confirming before it acts, and what the confirmation flows actually do, should be one claim, said once in Terms and true in code. If an action can happen without confirmation, Terms must not imply otherwise. That's a fact for Lead or PA to state per action type before any wording exists.

## 6. What not to copy

- Indemnification of us by the user (§7 of the old agreement). It sits badly with a product whose pitch is trust.
- "Access may be revoked at any time without notice", without a data-export or deletion path alongside it.
- "Any feedback you provide may be used without compensation" in its broad form. Narrow it to product feedback, never the user's work content.
- The all-caps disclaimers, unless counsel says the law requires capitals. Then put them underneath, not on top.

## 7. Who signs

xian's call. From the voice side: the plain layer should be written by xian (AI prompts human), with Comms checking every claim against code. The legal layer underneath is the part where counsel's review matters. Name that split in the paper so neither layer gets written by the wrong hand.

**Verified how:** I read `docs/ALPHA_AGREEMENT_v2.md` on main this turn (sections 1–11). `git grep` finds no reference in `web/` or `services/`, so it isn't shown in the product (denominator: repo templates and routes, not the hosted build). /privacy claims are from the website's `privacy/page.tsx` on origin/main, read today.

— Comms
