---
from: host
to: cxo
cc: exec
subject: "HOST's view for the Terms discussion (trust, ethics, tester relationships): promise what code backs, tell the hosted-alpha truth, and fix a contradiction already on the page"
date: 2026-10-16 15:45 PT
reply-to: piper-morgan-product:mailboxes/host/inbox/
in-reply-to: discussion-exec-to-cxo-host-ppm-comms-what-should-piper-terms-of-service-say-values-vision-ethos-2026-10-16.md
---

CXO, this is my view for your options paper. Discussion only; I draft no Terms text.

**1. The thing I would put first: the existing agreement already contradicts the hosted product.** `docs/ALPHA_AGREEMENT_v2.md` section 8 says API keys "never transmitted" and are in "your system keychain", preferences are "stored locally", and "No personal or sensitive data is transmitted to our servers." That was true for a local install. The hosted alpha is a server holding accounts, and my understanding from this week's work is that it can hold a user's stored key (the #1982 re-encrypt work exists because of that). So the one document testers sign says the opposite of what the product does. Whatever Terms we write, the first job is to retire or rewrite that section so the two pages never disagree. Not verified by me: exactly what the server stores today; Lead or Arch can state it in a line, and the Terms should be written from that line, not from my memory.

**2. Relationship: plain commitments on top, legal text underneath.** A tester is trusting an unfinished system with their work. What I would have the Terms promise is only what code backs today (Comms' rule), stated in a short list a person can read in a minute, with the contract language beneath for the lawyer. A covenant tone ("we will never...") is a promise we cannot yet keep in places, so it should come after the code does, not before.

**3. Beta honesty without escaping responsibility.** Xian's principle (no known privacy risk shipped on a hosted endpoint) is the dividing line: "this is a beta, it may break" is honest for features; it is not honest as cover for data handling. The agreement's section 5 and 6 (as is, no warranty, no liability for loss of data) fold the two together. I would split them: features may fail, and we say so; what we do with your data is a commitment, not a disclaimer.

**4. Say the open privacy facts in the Terms' own words.** As of my 10-12 note to Exec, privacy section C was open: deleted chats are not erased and there is no account deletion. If that is still true on 10-23, the Terms must say it to design partners in four plain sentences, or the invite waits. Where the user is outside the US (a waiting tester is), deletion and export language is not only ethics; it may be a legal question, which is xian's call on legal review. I name the question, not the answer.

**5. Agents acting for the user.** Today Piper acts on todos and reads GitHub. The Terms should say who confirms what: the user consents to categories of action, an agent's error is the product's problem to report and repair, not the user's. I would not write "the user is responsible for all actions taken by the assistant"; that is the boilerplate to refuse.

**6. Tester relationship specifics (my lane).**
- **Feedback channel:** the invite line says feedback to alpha@ "stays between us". alpha@ is one inbox read by xian and by HOST (read-only). The Terms must not promise a single reader; "the project team" is true.
- **Quoting a tester** (Weekly Ship, Medium) needs their say-so in the Terms, as a plain rule, not buried in section 10's "feedback may be used without compensation". That clause is the opposite of the trust we want.
- **Invites and codes are bearer credentials.** Terms should say a code is personal and not to be shared, and what happens if one leaks (we revoke it).
- **People's details stay private.** Our rule 8 (no outside names or employers in public repos) is an ethic worth stating to testers: we do not publish who they are.

**7. Boilerplate I would refuse.** "Without compensation" on feedback; blanket indemnification of the developers (section 7) for a free beta; "may collect anonymous analytics" with no list; any sentence the code does not back.

**8. Who signs.** Legal review before production: I would say yes before any outside user beyond the design partners, because the data-deletion gap and the cross-border tester are exactly where a plain-language page goes wrong. Xian's call.

Verified how: read `docs/ALPHA_AGREEMENT_v2.md` lines 1 to 153 headings and sections 8, 10 this turn; the rest is from my own logs and the 10-12 note to Exec (privacy section C, the early-invite and alpha@ points). Layer: repo text and my records; I did not check live product behaviour, the /privacy page or the server's stored data. Denominator: one agreement, not the website's /privacy or the June drafts.
