# Proposal: privacy-policy MCP section + a support page

**Author**: PA, 2026-10-05, at PM's request. **Status**: proposal for PM's review. The voice pass goes to
Comms, and the website edit is Web's to make once PM approves. **Nothing here is live.**

Why now: every directory we plan to list in asks for a privacy-policy URL and a support contact. The
live `pipermorgan.ai/privacy` ("Last updated: May 2026") never mentions MCP, connectors, ChatGPT or
Claude, and `pipermorgan.ai/support` is a 404.

Every factual statement below was checked against the code on 2026-10-05; the source is noted in brackets.
**If the server changes, this copy must change with it.** (Same lockstep rule as the consent page.)

---

## A. New privacy-policy section (insert after "Data Sharing and Third Parties")

### Using Piper from ChatGPT, Claude and other AI assistants

You can connect Piper to an AI assistant you already use, such as ChatGPT or Claude, through Piper's
connector at `mcp.pipermorgan.ai` (built on the Model Context Protocol, "MCP"). Here is what that
connection does and doesn't do.

**What the assistant can read.** With your approval, given on a Piper sign-in page, the assistant can
read:
- your Piper profile: organization, active projects and stated priorities;
- the things Piper has confirmed with you about how you work;
- your open GitHub issues, read through the GitHub account you connected to Piper.

The assistant **cannot change anything** in Piper through this connection, and it **cannot see
another person's data**. [The server exposes three read-only resources and one read-only tool; every
request is tied to the account that approved it; per-user isolation is tested (#1458).]

**Where your data goes.** When your assistant reads from Piper, that information goes to the assistant's
provider (for example OpenAI or Anthropic) as part of your conversation. From then on it's handled
under **that provider's** privacy terms, not ours. No AI model runs on Piper's side of this
connection. [PDR-006: a pure tool server, no server-side LLM.]

**What Piper keeps about the connection.**
- A record of each connected assistant app: the name it registers with and its sign-in callback
  addresses. [`mcp_oauth_clients`: `client_name`, `redirect_uris`]
- Access credentials, **stored only as one-way hashes, never in readable form**. [`identity.py`:
  SHA-256 `hash_credential`] Access tokens expire after one hour; the longer-lived token that renews
  them expires after 30 days. [`oauth_provider.py`: `ACCESS_TOKEN_TTL`, `REFRESH_TOKEN_TTL`]
- When each connection was created and last used. [`last_used_at`]
- Standard technical request logs (time, address requested, result), kept for security and
  troubleshooting.

Piper **does not receive your conversations** with the assistant. It only receives the specific
requests your assistant makes to read the items listed above.

**Turning it off.** You can remove an assistant's access at any time in **Settings → Connected apps**
in Piper. Access ends right away. Removing Piper from your assistant's own settings also stops
the assistant from using it. ✅ *Gate cleared 2026-10-11: PM's revoke-then-ask test, the next call refused
(401, `reason=revoked`) and the token refresh refused, per PA's notice. "Access ends right away" replaces the
held "It stops working immediately" (the "It" was ambiguous). Handed to Web 10-11.*

---

## B. A support page: `pipermorgan.ai/support`

**Piper Morgan support**

**Contact**: `<SUPPORT ADDRESS — PM to choose>`. We read every message. During the beta, expect a reply
within <N> business days. *(PM: pick a real, monitored address. Directory reviewers and users will write
to it, so it must be watched.)*

**Connecting Piper to ChatGPT or Claude**
- Add a connector with the URL `https://mcp.pipermorgan.ai/mcp`.
- You'll be sent to Piper to sign in and approve read-only access.
- Then ask your assistant: "What does Piper know about me?"

**Something isn't working**
- *"No tools" or "action discovery failed"*: remove the connector and add it again, so your assistant
  picks up Piper's current tools.
- *The assistant says it has no access*: you may have revoked it, or it may have expired. Reconnect from
  your assistant.
- *Parts of the answer are empty*: that's expected, not broken. Piper only reports what's actually
  there, and a new account doesn't have much yet.

**Removing access**: You can revoke access in Settings → Connected apps in Piper, and access ends right away.
You can also remove Piper from your assistant. *(10-11: gate cleared, handed to Web. Only the Piper-side revoke was
tested, so the timing claim stays on that one.)*

**Privacy**: see [our privacy policy](/privacy).

---

## C. Your Piper account (FINAL v3, Comms 2026-10-13, PM's answers in; from Lead's cited facts)

*Status: draft for PM. Facts from Lead's 10-08 memo (`mailboxes/comms/read/facts-lead-to-comms-…-2026-10-08.md`),
each cited there to code on `origin/main` = alpha `e8ecd10d5a`. Bracketed notes are sources and get stripped at
publish. Insert after Section A.*

*v2.1 (10-13): PM answered GOAL 2 (trash, then purge), GOAL 3 (plan to add, manual deletion via support@ meanwhile)
and N = 14 days, in conversation with Comms. GOAL 1 (logs), later the same morning: "keep only fingerprints of logs."*

*v2 (10-12), PM's principle via Janus: "We must always honestly say what the product does now. If we plan to do
something different we should acknowledge the goal and the current gap." So every sentence below states what
Piper does today, and the three gaps now read as "today X, our goal is Y". **PM fills four blanks, marked ⟦PM …⟧:**
three goals (each one a short phrase, or "none", which drops that goal sentence) and one turnaround in days. No
other decisions are left in this section.*

### Your Piper account

When you sign up for Piper and use it, here is what we keep, where it lives, and what you can delete.

**What we store.**
- Your account details: username, email address, your password (stored only as a one-way hash, never in readable form), your
  settings, and your answers during setup. [`database/models.py:141` `password_hash`; `routes/setup.py:872` bcrypt at signup.
  10-16: the earlier note "no password is stored" was wrong. Fix 1, xian OK 10-16, handed to Web.]
- Your conversations with Piper: each message you send and each reply. These are **encrypted** when stored.
  [AES-256-GCM per field, `field_encryption.py`]
- What you create or connect in Piper: reminders and to-dos, projects and linked repositories, files you upload,
  and what Piper learns from your documents and your work. Uploaded files are stored as-is, not encrypted.
  [Lead: uploads on a Fly volume, not encrypted at rest; learned patterns encrypted except one routing field]
  ⚠ 10-16: WRONG per code. `file_context/storage.py` encrypts uploads (AES-256-GCM) when ENCRYPTION_MASTER_KEY is set;
  legacy files plaintext until the #1306 backfill. Waiting on xian's two prod reads (key set? backfill remaining?) via Exec.
- The AI provider key you add. It's stored **encrypted**, and it's never written to our logs.
  [`user_api_key_service.py:205-226`; `field_encryption.py:14-16`]

**Where it lives.** On our hosting provider, Fly.io, in San Jose, California. [`fly.toml`: region `sjc`]
Our admin tools don't display your conversations, and the stored copies are encrypted.
[`web/api/routes/admin.py`. NOT claimed: "no one can read them". The decryption key is a server secret.]

**Your AI provider.** Piper sends your messages to the AI provider you connected (Anthropic or OpenAI), using
**your own key**. From then on they're handled under that provider's privacy terms. There's no shared Piper key
processing your conversations. [#1812, `provider_selection.py`]

**Logs.** Our server logs don't keep the text of the messages you send to Piper. At most, they keep a scrambled
fingerprint of a message. This doesn't affect your conversations, which you can still see in Piper.
[⚠ 10-16: false on one path until issue 2059 promotes (classifier WARNING logs a 50-char prefix); Lead's lane is fixing it,
no copy change if it promotes before 10-23. PM 10-13: "keep only fingerprints of logs." Lead 10-13: knob default flipped to off in code at every text-logging
site (`services/utils/utterance_log.py`, ec2cc9d44f, 27 pinning tests), live at the next promotion. Alpha measured
today: 0 lines with message text (INFO is suppressed in production). Fly app-log search keeps 7 days. "At most"
because in production even the fingerprint lines are below the log level. NOT claimed: a retention period (a log
drain outside fly.toml is unverified).]

**Services you connect.** If you connect GitHub, Google Calendar, Slack or Notion, Piper reads and writes there
when you ask. For GitHub and Slack, Piper never sees your password. Piper keeps the access the service grants,
encrypted. When you disconnect GitHub, Piper deletes the stored copy.
[GitHub: PA 10-08, `connector_grant_store.py` (AES-256-GCM, same store as the AI key), `disconnect.py:93` deletes
it. Slack: Lead 10-08, keychain service → encrypted DB on the hosted app, and it refuses to save rather than store
plaintext (#1382). NOT claimed: Calendar and Notion storage (untraced); Slack's disconnect path (untraced);
that disconnecting revokes the grant at GitHub (only Piper's copy is seen deleted). PENDING PA/Lead if PM wants
those covered.]

**No analytics or ad tracking in the app.** The Piper app doesn't use analytics, advertising or
error-reporting services. [Lead: none found by a code-wide grep (GA, Mixpanel, Segment, Sentry). This covers
the app only, not this website. ⚠ 10-16: the in-app Chroma client may send anonymized telemetry (posthog); Lead's lane
is setting anonymized_telemetry=False]

**How long we keep it.** As long as your account exists. We don't automatically delete your conversations, files or account.
[10-16: two daily jobs delete expired sign-out records (`BlacklistCleanupJob`) and 90-day safety-audit rows
(`EthicsAuditCleanupJob`), never user content (`web/startup.py:422, 515`). Fix 2, xian OK 10-16, handed to Web. Session tokens: 30 min, refresh 7 days]

**Deleting your data.** In Piper you can delete files you uploaded, your AI provider key, what Piper has learned
about you, your settings, and your to-dos, projects and linked repositories. Deleting removes them.
- **Conversations.** Deleting a conversation hides it from you, but the encrypted copy stays on our servers.
  Our goal is for deleted conversations to go to a trash, where you can purge them from your data for good.
  [`conversations.py` sets `lifecycle_state="deleted"`.]
- **Your whole account.** There's no way to delete your account inside Piper yet. We plan to add one.
  Until then, email support@pipermorgan.ai and we'll delete your account and everything in it within 14 days.
  [Lead: promise "on request" only if someone will act on requests. support@ is PM's address (live on /support).
  The person who carries out a deletion is PM's call, and it isn't written into the policy.]

---

## Decisions for PM
1. **The support address.** It's the one blocking choice.
2. Approve section A's facts (they're code-checked, but it's your policy), then route to Comms for voice
   and Web to publish. Bump the policy's "Last updated" date.
3. The "Turning it off" sentence waits for the Revoke fix to be live and seen working.
4. **Section C (your Piper account), v2 2026-10-12.** Rewritten to PM's "say what it does now, plus the goal and
   the gap" principle. GOAL 2, GOAL 3 and N (14 days) answered 10-13. GOAL 1 (logs) answered 10-13: "keep only fingerprints", done in
   code by Lead and measured on alpha the same day. **Section C is final (v3, 10-13). PM's go 10-13 (in conversation with Comms); handed to Web the same evening with the opening-sentence widening.**
   Opening sentence for Web: "…when you visit our website, subscribe to our newsletter, use Piper, or connect Piper
   to an AI assistant." Then
   Comms gives Web the final text. When Section C ships, the policy's opening sentence widens to cover using Piper
   (Comms rewords it in the same hand-off).
5. ~~One check only PM can run~~ **No longer needed for the privacy claim** (PA 10-08 09:5x traced GitHub's no-key
   path: like Slack, it fails closed, so the access is encrypted in the DB or the connect is refused, never
   plaintext). `fly secrets list -a piper-morgan` now only tells PM whether connecting works on alpha. That's a
   function question, not a policy one.
