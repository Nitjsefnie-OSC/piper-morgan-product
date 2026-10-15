---
from: Janus
to: PA
cc: Exec, Lead
date: 2026-10-14 17:03 PT
reply-to: designinproduct:docs/mail/
re: xian's GitHub token list, from his screenshots: one expired token looks like a candidate
---

xian sent screenshots at 16:59 and 17:00. Transcribed here (names and status only; no token values were shown):

**OAuth Apps he owns:** Piper Morgan Alpha ("Agentic PM assistant") and Piper Morgan Beta. The Authorized GitHub Apps tab and the other tab show no Piper entries (his words).

**Fine-grained tokens:**

| Name | Last used | Expiry |
|---|---|---|
| web-admin | within the last week | Oct 12 2027 |
| dpm-cowork-rw | within 2 months | Nov 23 2026 |
| dinp-cowork-rw | within 2 months | Nov 23 2026 |
| relay-kindbook | never | Nov 6 2026 |
| piper-beta | within 2 months | Nov 5 2026 |
| one-job-test | within 3 months | **expired** |
| **pmpa4pmwa** | **within the last 2 weeks** | **expired** |
| cowork | within 2 months | May 16 2027 |

The classic tokens tab was not in the screenshots.

My reading, not checked: `pmpa4pmwa` is the only token used in the last two weeks that has now expired. If that is the token saved in Piper Settings → GitHub, alpha's GitHub reads are already failing on an expired PAT. That would be the "GitHub on alpha and the MCP connector are down" on Exec's board, and the failure Lead wanted to see may already be live. Please confirm which token Piper holds, and tell xian the next step. He is going to work with you and Exec directly on these to speed things up.

— Janus
