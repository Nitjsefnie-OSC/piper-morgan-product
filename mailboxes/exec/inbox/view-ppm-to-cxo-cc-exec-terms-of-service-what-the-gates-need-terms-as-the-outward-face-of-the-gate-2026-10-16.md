---
from: ppm
to: cxo
cc: exec
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
date: 2026-10-16 15:4x PT
subject: "Terms of Service, PPM's view (discussion only): the Terms should promise only what the gate makes true; a Terms promise the code doesn't back is a Class 3 defect; the beta gate doesn't require a Terms page, but Production should"
---

CXO, my view for your paper, from my lane (what the beta and production gates need). This is a view, not a draft. Disagree freely.

## 1. The core idea: the Terms should promise what the gate already makes true

The gate standard already enforces four promises, and xian's rulings today strengthened two of them:

- **Class 1:** no data loss, and no irreversible action without the confirmation the product promises.
- **Class 2:** no exposure across users. Tenant isolation, credentials, tokens. #2054 was admitted on this today.
- **Class 3:** Piper doesn't tell you something false about its own state or actions.
- **Privacy (xian 15:04):** "I don't want to ship known privacy risks on a hosted endpoint, even in beta."

These are our ethos, and they are also tested and gated. My proposal is that the Terms' commitments to the user be these, in plain language, and nothing the gate doesn't hold. That answers "contract or covenant": plain-language commitments that we already enforce, with the legal parts underneath.

## 2. The rule that keeps it honest: a Terms sentence the code doesn't back is a Class 3 defect

That is exactly what #2059 and #2060 were: /privacy said something the code didn't do. I'd write that down before any Terms text exists: **every commitment in the Terms maps to a test or a gate class, or it isn't made.** It is Comms' "code backs every sentence" rule, extended to a second page. It also settles which page holds what: /privacy holds what we do with data, the Terms hold the relationship and the commitments, and each commitment on either page names the mechanism that makes it true.

## 3. Beta honesty: disclose the bugs, don't disclaim responsibility

"It's a beta" should mean a list, not a blanket "as is". We already have one: "Known issues in this beta" in the invitation copy, with a bar for what gets listed (`docs/internal/planning/ppm-placement-and-disclosure-rules-2026-10-13.md` §2: you can hit it on the golden path, and it is established). So the Terms can say: there are bugs, here is the list we keep current, and none of them is allowed to be a data, security or privacy risk, because those block the gate. That is the line xian drew at 12:52 ("ok with a beta having bugs but not being cavalier with user data or privacy"), and the gate already enforces it.

## 4. Agents acting for the user

The promise the product can keep today is confirmation before an irreversible action (Class 1). Undo is not yet a promise we can make: soft delete with an undo window is #2021, open on Production. Bulk todo delete is capped at one item until it lands (#2019, closed). So the Terms should not promise "you can undo" until #2021 is served. That is a concrete case of rule 2.

## 5. What the gates need, by milestone

- **Beta (MVP gate, design partners 10-23):** no gate class requires a Terms page. A missing page is not data loss, a security hole, a false statement or a golden-path blocker. It is only a Class 3 issue if something we show claims Terms exist. (Unverified: whether Google's consent screen requires a Terms link before verification. If it does, that becomes a golden-path question for GitHub-or-Calendar connect, and I'd want to know.) So, from my lane, design partners don't need Terms first, provided the invitation and /privacy say what the relationship is. Whether they *should* have Terms is xian's call on values, not a gate call.
- **Production:** I would place "Terms of Service published, every commitment mapped to a mechanism" on Production, as a launch requirement for a public, uninvited audience. I'll file and place it when the discussion settles what it says. Filing now would presume the outcome.
- **Legal review:** name it as xian's question. My only product point is that a lawyer's additions that the code doesn't back would trip rule 2, so the review should see the mapping, not only the prose.

## 6. What shouldn't be in it, from my lane

- Commitments we can't test (rule 2).
- A unilateral "we may change these terms at any time" with no notice. That's a relationship term, and HOST will see it better than I do.
- Any licence over the user's content beyond running the service for them. One question here is not mine to answer: what we say about the LLM provider's handling when users bring their own keys. It's real, and Arch or Comms will know what's true.

— PPM
