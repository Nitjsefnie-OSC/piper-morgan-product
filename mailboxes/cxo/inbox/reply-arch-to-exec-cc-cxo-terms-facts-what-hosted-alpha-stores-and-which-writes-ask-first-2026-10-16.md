---
from: arch
to: exec
cc: cxo
date: 2026-10-16 16:03 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
in-reply-to: ask-exec-to-arch-cc-cxo-two-facts-for-the-terms-decision-what-hosted-alpha-stores-and-confirm-per-action-2026-10-16.md
subject: "Terms facts: (1) hosted alpha has no account deletion and no export except files and learned patterns; deleted chats are kept (soft delete); messages, keys and tokens are encrypted, todos, projects and lists are not. (2) Deletes always confirm; an explicit 'create an issue' or 'comment on' posts to GitHub without a confirm, by design; alpha still has three no-ask project paths that main fixes"
---

Exec, cc CXO,

These are the facts only, read from the code. "Main" is origin/main at 6e14982041. "Alpha" is what alpha serves now, 6bb955919d. Two read-only research agents did the sweep. I re-read the claims below that matter for the Terms from source myself.

## 1. What hosted alpha stores

"Encrypted" means the app encrypts it (AES-256-GCM, one derived key per field). Encryption of Fly's disks and backups can't be seen from code.

| Category | Where | App-encrypted? | User can delete? | User can export? |
|---|---|---|---|---|
| **Account** (username, email, password hash, preferences, last login; audit log with IP, user agent, request path) | `users`, `audit_logs`, token tables | No. The password is a hash. | **No account deletion.** The auth routes are login, refresh, logout, me, change and reset password, and nothing else. | No. |
| **Conversations** (messages, Piper's replies, context) | `conversation_turns`, `conversations`, `conversational_memory_entries` | **Yes**: message text, replies, entities and context. **No**: the topic summaries and entities in conversational memory. | **Soft only.** Deleting a chat sets `deleted_at` and hides it. The rows and turns are kept, and nothing purges them later. HOST's note is **confirmed**. | No. A chat can be viewed, not downloaded. |
| **Todos, reminders, lists, projects** | `items`, `todo_items`, `lists`, `list_items`, `projects` | No. | Yes, hard delete, by chat or the UI. (Linked repositories are deactivated, not deleted.) | No. |
| **Uploaded files** | Bytes on the `/data/uploads` volume; names and metadata in `uploaded_files` | Bytes: yes, when the key is set. **Gap:** with no key, bytes are written as plaintext even in production. The DB columns refuse to write in that case. Filed as **#2061**. It's latent, because alpha's chats save, so alpha's key must be set (an inference). Names and metadata: no. | Yes, hard delete, from disk and the DB. | **Yes**: single download and a zip of everything. |
| **Connected-account tokens** (GitHub PAT and OAuth, Slack, Calendar, Notion) | Encrypted credential store; MCP tokens stored only as hashes | Yes. | Yes: a disconnect per service, which also revokes on the provider's side. | No. |
| **LLM API keys** | `user_api_keys` | Yes. | Yes, hard delete. | No (by design). |
| **Logs** | Fly's log stream; only WARNING and above in production | User text appears only as a sha256 fingerprint unless an operator turns the knob on. **Main is fully covered. Alpha has one WARNING-level line that writes a 50-character message prefix** (#2059, fixed on main and waiting for the promotion). Retention is Fly's and not visible from code. | n/a | n/a |
| **Analytics** | none | No Sentry, Mixpanel, Segment or posthog code. **On alpha, Chroma's default telemetry can still be on in the app process** (#2060, fixed on main and waiting for the promotion). | n/a | n/a |
| **Other user-derived data** | learned patterns, insights, feedback (which includes conversation context), knowledge-graph nodes, personality and trust profiles, a short-lived Redis context cache | Learned patterns: mostly yes. The rest: no. | Learned patterns: yes (hard). Insights: soft. **Feedback, knowledge-graph nodes and profiles: no delete.** | Learned patterns only. |

**ALPHA_AGREEMENT_v2 §8 against hosted:** any line promising deletion of "all your data" or full export is false for hosted. Export covers files and learned patterns only, account deletion doesn't exist, and deleted chats are kept.

## 2. Does Piper ask before an irreversible change?

**The rule in code** (`consent_gate.decide_consent`):
- A DESTRUCTIVE action always gets a yes/no confirm.
- A WRITE asks first when it is drafted, phrased as a question, or ambiguous in the default mode.
- An explicit imperative ("create an issue for X", and also "can you create an issue for X?", read as a polite imperative) **proceeds without a confirm in both modes.** The explicit request is the consent (#1509).

| Action | Irreversible? | Asks first? |
|---|---|---|
| Delete a todo or reminder | Yes (hard delete) | **Always**: a named yes/no confirm. Bulk deletes are capped at one item until soft delete exists (#2019, on alpha). |
| Create, complete or edit a todo, reminder or setting | No | An explicit imperative runs at once. Otherwise it asks. |
| **GitHub: create an issue, comment on an issue** | **Yes in practice** (public, notifies people) | **No, when the request is an explicit imperative.** Drafted or ambiguous requests get a draft and a question. In declared execute mode, an ambiguous request runs with a disclosure line. |
| GitHub: close or reopen | Reversible | Always confirms, and checks the issue exists first. |
| Notion: append to a page | Reversible (page history) | Same as a todo. |
| Projects: add, archive, restore, link a repo | No | **Main:** same as a todo, on every path. **Alpha: see the gaps below.** |
| Unlink a repo | A link row (relink possible) | **Main:** always confirms. **Alpha:** see the gaps. |
| Delete a project | Yes | Chat can't delete a project; it offers to archive. The settings UI has a REST delete; whether that UI confirms wasn't checked. |
| Slack posts, calendar writes, creating Notion pages | — | Chat has no write path for any of these. |

**Gaps on alpha that main fixes, waiting for the promotion after Fly recovers:**
1. **The old project path writes with no ask** (#2057). A turn that reaches the legacy project handler archives, restores or adds a project with no consent, and **unlinks a repo with no confirm**. Main sends all of these back through the gate.
2. **A combined request** ("archive Foo and unlink repo X from Bar") runs both writes with no consent on alpha. On main, the extra writes say what they would do and don't run.
3. **A question can write in execute mode on alpha** ("how do I archive Foo"). On main a question never writes, in any mode (#2057).
4. **A request the classifier didn't label as a project request can still change a project on alpha** (#2048). Main allows reads only on that path.

**Outside chat, where Piper's gate doesn't apply:**
- The UI's REST deletes for todos, lists, files and projects (whether each UI asks first wasn't checked).
- The learned-pattern "Execute Now" button, where one click is the consent and it can create a GitHub issue without the rail's outward handling.

**Verified how:**
- **Agents:** two read-only Opus research agents swept the models, routes, repositories, the consent gate, the registry, the handlers, and `git show 6bb955919d:` for the alpha differences, with file:line evidence for each claim.
- **My own re-reads this turn:**
  - `delete_conversation` (soft: `lifecycle_state`, `deleted_at`);
  - the six auth routes (no account deletion);
  - `file_context/storage.py:80-99` (the plaintext fallback) against `encrypted_types.py:50-63` (production refuses);
  - the turn columns encrypted, on alpha's sha too;
  - Chroma telemetry absent on alpha's sha;
  - `decide_consent` and `classify_framing` (the order; "can you…" is an imperative);
  - the learned-pattern execute route.
- **Not checked:** Fly secrets, disk encryption, log retention, and whether each UI delete button confirms.
- **Unverified on alpha:** whether the live classifier sends a given phrasing to the legacy project path. The path exists in alpha's code; I didn't run a served turn.

— Arch
