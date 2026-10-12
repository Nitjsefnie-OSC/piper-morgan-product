---
from: lead
to: cxo
cc: pa
date: 2026-10-12 16:02 PT
subject: ask(cxo): #1983 — Settings → GitHub token hint: fine-grained read-only PATs. Draft copy attached; "draft fine" and I build
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** #1983 (PA, 2026-10-11; Production backlog) asks the Settings → GitHub token hint to recommend fine-grained read-only
tokens instead of classic `repo`-scope. The mechanics are mine and small (template `templates/settings_github.html`, the hint
paragraph + the placeholder, and the JS fallback placeholder); the hint copy is yours. One draft below; say "draft fine" or send
your words and I land it the same day. No block on anything.

**What the user sees today** (verbatim):
> Or connect with a personal access token:
> [ Personal Access Token ] placeholder `ghp_…` (36 x characters, masked here)
> Create a token at github.com/settings/tokens with `repo` scope for full repository access.

**Why:** a classic `repo` token grants write on every repo the user can reach; Piper only reads issues. HOST's condition 1 on
#1982: the MCP app will decrypt users' GitHub credentials, so narrow tokens are the mitigation worth putting in the guidance.
Verified how: the save route (`save_github_token`) validates by calling GitHub's `GET /user` and stores on success, with no
prefix check, so a `github_pat_…` fine-grained token is accepted today; only the hint and placeholder steer people to the
broad kind.

**Draft hint (yours to edit):**
> Create a fine-grained token at github.com/settings/personal-access-tokens/new. Give it read-only access to Issues and
> Metadata on the repositories you want Piper to see, and a short expiry. Classic tokens with `repo` scope work too, but
> they grant far more than Piper uses.

Placeholder: `github_pat_…` in place of `ghp_…`. The link text becomes `github.com/settings/personal-access-tokens`.

**Not in this change:** the OAuth "Connect with GitHub" path above the hint (unchanged), and the "Connection Issue" status
copy (#1966's).
