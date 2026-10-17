# Design-partner known issues: for xian's direct review with PPM

**Prepared:** 2026-10-16 16:1x PDT by PPM, per xian's 16:07 bar (relayed by Exec): "privacy and security, the rest disclosed as known issues (pending our direct review of them)".
**Status:** a draft for review. Nothing here is partner-facing copy. Comms writes the wording after xian's review; the lines below are what a partner might hit, in plain terms, for deciding.
**Alpha served at drafting:** `6bb955919d`. Several items have fixes on main that ride the waiting promotion, and an item that closes on a served check before 10-23 drops off this list.

## The bar (recorded in `beta-gate-standard.md` §Standing rulings)

- **Must be closed and live on alpha before partners start:** every privacy and security item on MVP. As of 16:3x that was six; at 17:3x, two remain open (#2059 and #2061 closed live on `d741214b6c` at 17:14, #2054 and #2060 at 17:30):
  - #2054: one user's turn could carry another user's identity in the intent cache;
  - #2059: logs keep message text, against /privacy;
  - #2060: Chroma telemetry, against /privacy;
  - #2061: uploads are written as plaintext if the encryption key is missing (latent; admitted on xian's 16:18 word);
  - #2064: the 14-day account-deletion promise on /privacy has no erasure path in code;
  - #2065: Settings' "Export/delete data" page lists actions that don't exist, and /privacy says deleting a chat hides it, but no control does (admitted 16:3x).
  #2064 (176d66a53c) and #2065 items 1 and 2 (1e9d0f5809) are on main and ride tomorrow's first promotion. #2064 also needs xian's live count; #2065 also needs Comms' /privacy fix 4 (xian's OK).
- **Disclosed, after this review:** everything else open on MVP, below.
- **Also before the beta form:** the uploads backfill run with zero remaining (xian approved the four conditions, 16:18).
- **Data loss (Class 1):** none open on MVP today. I'd treat any new one as inside the must-close bar, under xian's 12:52 "not cavalier with user data", unless he says otherwise.

## A. Open on MVP: what a partner might hit

| # | What a partner might hit | How likely | Workaround today | Fix status |
|---|---|---|---|---|
| #2048 | On an account with no projects, "list my projects" gets "I don't have your projects list in front of me right now", which reads as a fault, not "you have no projects yet". | Likely on day one: a new account has no projects, and the phrase is on the onboarding card. | "show my projects" or "what projects do I have?" answers correctly. | **Closed 2026-10-16 18:32 PT** on CXO's served acceptance (alpha `d741214b6c`, 3 of 3 fresh chats plus a control). Drops off the list. |
| #2017 | The GitHub card's Disconnect button did nothing on 10-14. On 10-15 it worked for xian; whether it asks to confirm wasn't observed. | Only partners who try to disconnect GitHub. | Reload and retry; it worked on 10-15. | Partial served reading; Web's run of the confirm and the four settings pages is owed. |
| #2018 | If a partner's GitHub connection dies (they revoke Piper on GitHub, or the token dies), Settings may not show it, and recovering isn't obvious. | Low: only after a revoke or expiry on GitHub's side. | Disconnect, then Connect with GitHub (worked on 10-15). | Steps 1 and 5 passed (S5, 10-15). #2029 and #2039 closed. #2031 (the card says "Not configured" for a stale binding) is waiting on xian's S5. |
| #1913 | A chat started before adding an AI key can disappear from the sidebar once the key is added. The server keeps it (Lead, 10-02); the vanish is in the page. | Low if partners follow the invitation (key first). | Reload; per Lead's probe the chat is still listed. Unverified on alpha since. | Open; cause not yet found client-side. |
| #1595 | Piper sometimes misreads a phrasing: it answers a different question or gives a generic reply. Rephrasing usually works. | Likely, now and then. This is the understanding-layer epic. | Rephrase. | The epic's planned wave. Its tail: legacy project-write paths that acted without asking (#2057, fixed on main, waiting on the promotion; archive is reversible). |
| #1386 | Not a user-facing issue: the close-out sign-off itself (the canonical suite and three scenarios, re-run at MVP close). | n/a | n/a | Fires last. |

## B. Outside MVP, meeting the disclosure bar: xian decides whether to list them

The bar (`ppm-placement-and-disclosure-rules-2026-10-13.md` §2): a partner can hit it on the golden path or a setting they're told about, and it is established by a check or a served run.

| # | What a partner might hit | Why it might belong on the list |
|---|---|---|
| #2042 | Piper's reply can occasionally state something about the partner's data that the code didn't produce, such as a wrong count. | Served twice (#2033, #2040). Served instances that are false on a golden path get gated as found, but the class stays open. |
| (by design) | "Create an issue for X" on GitHub posts at once, with no confirm, because the explicit request is the consent (Arch 16:03, via CXO). Deletes always ask. | Not a bug, but a partner who expects a draft first would be surprised. CXO notes the Terms can't claim "confirms before anything it can't undo". |
| #2019 / #2021 | "Delete all my todos" deletes one at a time (the interim cap). There's no undo yet: soft delete is #2021. | A visible limit, and the reason the invitation mustn't imply undo. |
| #2067 (added 18:35) | After the 30-minute sign-in lapses, Test on the GitHub card prints "Token has expired" under GitHub, which reads as a broken connection. The words are Piper's session expiry, not GitHub's. | Likely: any partner who leaves Settings open half an hour. A false card statement, not privacy or security. Small fix (route a 401 to "sign in again"). |
| #2068 (added 18:35) | The Integrations headline reads "Multiple Issues" and "0 of 4 integrations healthy" when GitHub works and the rest are simply not connected. | Certain for any partner with fewer than four connected. A false headline; CXO has ruled the words, so the fix is small. |
| #2069 (added 18:38) | "Add a project called Baz with description …" saves the whole phrase as the name and replies as if it kept a description. | Plausible for a partner's first project. Correctable by rename. A false reply, not privacy or security. |

## C. What the review should produce

For each row: **list it** (Comms writes the line), **don't list it** (with the reason), or **must fix first** (it moves to the must-close bar, an admission on xian's word). PPM ledgers the outcome.
