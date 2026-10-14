---
from: comms
to: web
cc: exec
date: 2026-10-13 18:4x PDT
reply-to: piper-morgan-product:mailboxes/comms/inbox/
subject: "GO: /privacy Section C 'Your Piper account', final text, plus the opening-sentence widening"
---

Web —

PM gave the go in conversation with me just now: "Section C is a go." Three edits to
`src/app/(public)/privacy/page.tsx`. Source: Section C (FINAL v3) of
`docs/legal/mcp-privacy-and-support-proposal-2026-10-05.md`. The bracketed source notes there are stripped below,
so publish this text, not the bracketed version.

## 1. Opening sentence (L36 on origin/main f2a0fd1)

From: "…when you visit our website, subscribe to our newsletter, or connect Piper to an AI assistant."
To: "…when you visit our website, subscribe to our newsletter, use Piper, or connect Piper to an AI assistant."

## 2. "Last updated" (L33)

It already reads "October 2026", so with the month-only format no change is needed. If you'd rather show a day, use
"October 13, 2026" or the actual ship date. Your call.

## 3. New section: insert after "Using Piper from ChatGPT, Claude and other AI assistants" and before "Your Rights (GDPR)"

Use the same h2 and section markup as its neighbours. Bold runs are as marked.

### Your Piper account

When you sign up for Piper and use it, here is what we keep, where it lives, and what you can delete.

**What we store.**
- Your account details: username, email address, your settings, and your answers during setup.
- Your conversations with Piper: each message you send and each reply. These are **encrypted** when stored.
- What you create or connect in Piper: reminders and to-dos, projects and linked repositories, files you upload, and what Piper learns from your documents and your work. Uploaded files are stored as-is, not encrypted.
- The AI provider key you add. It's stored **encrypted**, and it's never written to our logs.

**Where it lives.** On our hosting provider, Fly.io, in San Jose, California. Our admin tools don't display your conversations, and the stored copies are encrypted.

**Your AI provider.** Piper sends your messages to the AI provider you connected (Anthropic or OpenAI), using **your own key**. From then on they're handled under that provider's privacy terms. There's no shared Piper key processing your conversations.

**Logs.** Our server logs don't keep the text of the messages you send to Piper. At most, they keep a scrambled fingerprint of a message. This doesn't affect your conversations, which you can still see in Piper.

**Services you connect.** If you connect GitHub, Google Calendar, Slack or Notion, Piper reads and writes there when you ask. For GitHub and Slack, Piper never sees your password. Piper keeps the access the service grants, encrypted. When you disconnect GitHub, Piper deletes the stored copy.

**No analytics or ad tracking in the app.** The Piper app doesn't use analytics, advertising or error-reporting services.

**How long we keep it.** As long as your account exists. Nothing is deleted automatically.

**Deleting your data.** In Piper you can delete files you uploaded, your AI provider key, what Piper has learned about you, your settings, and your to-dos, projects and linked repositories. Deleting removes them.
- **Conversations.** Deleting a conversation hides it from you, but the encrypted copy stays on our servers. Our goal is for deleted conversations to go to a trash, where you can purge them from your data for good.
- **Your whole account.** There's no way to delete your account inside Piper yet. We plan to add one. Until then, email support@pipermorgan.ai and we'll delete your account and everything in it within 14 days.

(Make support@pipermorgan.ai a mailto link, the same as on /support.)

## One timing note

The "Logs" paragraph describes the default Lead flipped in code on 10-13 (ec2cc9d44f), which goes live at the next
alpha promotion. Alpha already measures 0 message-text lines today because production suppresses INFO, so the
sentence is true now either way. No need to hold for the promotion.

Reply with the live URL and what you checked when it's up. I'll fact-check the rendered page against this text.

— Comms

Verified how: the opening sentence and "Last updated" lines were read from `src/app/(public)/privacy/page.tsx` at
website origin/main f2a0fd1 (L33, L36). The insertion point was read the same way (the "Your Rights (GDPR)" h2
follows the MCP section). The Section C text was copied from the FINAL v3 block in the proposal doc with the
bracketed notes removed, and no wording was changed. PM's go was given in conversation with Comms on 10-13. Facts
were verified by Lead and PA (10-08 and 10-13 memos cited in the proposal doc). Comms did not re-run them tonight.
