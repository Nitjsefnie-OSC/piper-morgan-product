# Piper Morgan plugin: directory listing copy (DRAFT)

**Author**: PA, 2026-10-06. **Status**: draft for Comms' voice pass, then PM approval. Nothing submitted.
**For**: the Claude directory portal (name ≤100 chars, one-liner ≤200, description ≤2000, 1–5
categories) and the OpenAI plugin submission (icon, short and long description). Limits are from the
portal docs read 2026-10-05.

**Truth constraint (same rule as the consent page, #1911):** every claim below must match what v0.1.0
actually does. It is read-only, has three skills, and comes from one hosted connector. Re-check this copy
whenever the plugin's skills or the server's tools change.

## Name (≤100)

Piper Morgan

## One-liner (≤200), 145 chars (counted)

A product-management colleague who knows your priorities and open issues, and turns them into a daily
standup and a ranked to-do list. Read-only.

## Description (≤2000)

Piper Morgan is a product-management colleague. Connect Piper once and your assistant can see what Piper
knows about you: your organization, active projects and stated priorities, what Piper has confirmed
about how you like to work, and your open GitHub issues.

Three skills put that to use:

- **What Piper knows**: see your profile, priorities and open issues in one place, including what
  Piper *doesn't* know yet.
- **Morning standup**: a plan for today, short enough to read in thirty seconds, tied to your stated
  priorities and to specific open issues.
- **Prioritize my issues**: your open issues sorted into do first, next, and defer or drop, each with
  one line of reasoning, plus the biggest judgment call it made, so you can overrule it.

**Clear about what's missing.** Piper reports empty as empty. They don't invent progress they can't
see, and they label their own inferences. In our tests against sample data, each skill does this where
the same assistant without the plugin doesn't.

**Read-only.** The connector can't change anything in Piper or GitHub, and it can't see anyone else's
data. You approve access on a Piper sign-in page.

Piper Morgan is in invitation-only alpha. You need a Piper account at pipermorgan.ai.

*(≈1,150 chars. ⚠️ Add "Revoke anytime in Settings → Connected apps" only after the Revoke fix is live
on alpha and seen working.)*

## Categories (1–5), proposed

Productivity · Project management · Developer tools (for GitHub issues)

*(Exact category names come from the portal's picklist; map these at submission time.)*

## Still needed before submission (not copy)

- ~~Icon~~ RESOLVED 10-06 (PM): `pm-logo-color` → plugin repo `assets/icon.png` (2000px) + `icon.svg`.
- Support contact (PM; see `docs/legal/mcp-privacy-and-support-proposal-2026-10-05.md`).
- Privacy-policy MCP section live (same proposal).
- A reviewer test account (an alpha invite through the real invite flow).
- The Revoke fix live (`87e8bc9c49`) before any "revoke" sentence anywhere.

## Sources and changes (Comms, 2026-10-06, per PM)

- **Piper takes they/them** (PM 2026-10-06: they/them for Piper in product copy too, not "it"). The connector stays "it".
- **"short enough to read in thirty seconds"**: source is `piper-morgan-plugin/skills/morning-standup/SKILL.md`
  step 2 ("short enough to read in thirty seconds"). That's a **design target** in the skill, not a measured
  property, so the copy now says it as a target.
- **"In our tests against sample data… doesn't."** was "In our evals, each skill does this reliably…". Source is
  the plugin README ("all three skills score 1.00 with the plugin and 0.00 without") and
  `evals/results/` (gitignored, 6 runs 2026-10-06 13:49–13:54Z, mocked connector, 3 trials per arm). The
  saved runs are partial (1–2 cases each) and earlier ones include with-plugin scores of 0.5 and 0.67, so
  **"reliably" isn't shown yet**. PA: if one complete run reproduces the README's 1.00/0.00 across all
  cases, cite it here and "reliably" can come back.
  - **PA, 2026-10-06 ~13:0x: condition met.** One complete run on the final suite: `piper-morgan-plugin` `evals/RESULTS-v0.1.0.md` + `.json` (`f22d064`): `partial: false`, all three skills 1/1/1 with vs 0/0/0 without, unrelated case correct, $1.46. The earlier 0.5/0.67 came from a since-removed regex grader that misread the standup's own disclaimer. "Reliably" is sourced if Comms wants it back; the wording stays Comms'.
- **"can't see anyone else's data"**: PM 2026-10-06. Data separation is a **release requirement**, not a
  copy hedge ("I will not release software that doesn't offer clear data separation"). So the claim stays,
  and the gate is release readiness (cross-caller isolation, #1458) before any listing goes live.
  - **PA, 2026-10-06: gate already MET.** #1458 CLOSED 2026-10-05 22:52Z (two-caller interleaved test through the real app, pinned `user_context_service` store test with a mutation check, AST rule that every MCP handler resolves the caller; MCP v10 `e3dde4b26f`). CXO retired the re-check trigger 10-05 16:30.

---

## v2 DRAFT (PA, 2026-10-11): for PM's one review pass, after Comms' voice pass

**Why a v2 (PM, 10-11: "for at least some users… a first impression and may set longer-term expectations"):**
(1) v1 sells to people who can't get in: invite-only came last, with no way to ask. (2) One copy was headed
to listings that ship different things: only the **plugin** carries the skills. Smithery, the MCP Registry
and a plain connector listing get the **server alone** (one tool, three read-only data sources). (3) There's
no frame for "early probe" vs "the product", so the narrow scope could read as thin. (4) Small fixes:
"Piper… They" read as the skills; the revoke line (pending PM's revoke test); the Registry one-liner should match.
Invitation route: **support@pipermorgan.ai** (PM, 10-11: lighter than a dedicated page). Written as plain text, not a link, so it works in listing fields that don't render links.

### A. Plugin listing (Claude directory plugin bundle; OpenAI plugin)

**Name:** Piper Morgan

**One-liner:** A product-management colleague who turns your priorities and open GitHub issues into a daily standup and a ranked to-do list. Read-only.

**Description:**

Piper Morgan is a product-management colleague. Connect Piper once and your assistant can see what Piper knows about you: your organization, your active projects and stated priorities, what Piper has confirmed about how you like to work, and your open GitHub issues.

**What Piper knows comes from you.** Piper knows only what you've set up in your Piper account at pipermorgan.ai, including the GitHub account you connect there. With a new account, Piper knows little, and says so.

Three skills put that to use:

- **What Piper knows**: your profile, priorities and open issues in one place, including what Piper *doesn't* know yet.
- **Morning standup**: a plan for today, short enough to read in thirty seconds, tied to your priorities and to specific issues.
- **Prioritize my issues**: your open issues sorted into do first, next, and defer or drop, each with one line of reasoning, plus the biggest judgment call behind the ranking, so you can overrule it.

**Clear about what's missing.** When something is empty, Piper says so. The skills don't invent progress, and they label inferences as inferences. In our tests against sample data, each skill did this in every trial, and the same assistant without the plugin didn't.

**Read-only, and yours to switch off.** The connector can't change anything in Piper or GitHub, and it can't see anyone else's data. You approve access on a Piper sign-in page, and you can remove it any time in Piper under Settings → Connected apps. *(Last clause gated on PM's revoke test.)*

**An early release.** This first version reads and suggests. It doesn't act for you yet. Piper Morgan is in invitation-only alpha, and you need a Piper account to use it. To request an invitation, email support@pipermorgan.ai.

### B. Server-only listing (Smithery, MCP Registry, Claude connector directory)

**One-liner:** Read-only access to what Piper Morgan, a product-management colleague, knows about you: priorities, projects, working style and open GitHub issues.

**Description:**

Piper Morgan is a product-management colleague. This connector lets your AI assistant read what Piper knows about you, so it can plan and prioritize with real context:

- your organization, active projects and stated priorities
- what Piper has confirmed about how you like to work
- your open GitHub issues, through the GitHub account you connected to Piper.

**What Piper knows comes from you.** Piper knows only what you've set up in your Piper account at pipermorgan.ai, including the GitHub account you connect there. With a new account, Piper knows little, and says so.

Ask "What does Piper know about me?" to see all of it in one answer, empty parts included. Piper reports empty as empty and doesn't fill gaps with guesses.

**Read-only, and yours to switch off.** The connector can't change anything, and it can't see anyone else's data. You approve access on a Piper sign-in page and can remove it any time in Piper under Settings → Connected apps. *(Last clause gated on PM's revoke test.)*

**An early release.** Piper Morgan is in invitation-only alpha, and you need a Piper account. To request an invitation, email support@pipermorgan.ai. For a daily standup and issue ranking built on this, see the Piper Morgan plugin.

**MCP Registry `server.json` description** (Registry limit 100 chars): `Read-only access to what Piper Morgan, a product-management colleague, knows about you.` *(87 chars; the 100 limit is the schema's `maxLength`, checked 10-11.)*

**Counted 10-11 (python `len`), recounted after Comms' pass:** A one-liner 136/200, A description ~1,450/2,000, B one-liner 147/200, B description ~950/2,000. Registry 87/100 unchanged.

### What changed from v1, line by line
- Invite-only moved from a closing aside to a closing call to action, with a link.
- New "An early release" line: says what this version does *not* do yet, so the scope reads as deliberate.
- "Clear about what's missing / Piper reports empty as empty. They don't…" → "Honest about what's missing. When something is empty, Piper says so. The skills don't…" (the subject is now unambiguous).
- "In our tests… each skill does this where…" → "did this every time" (sourced: `RESULTS-v0.1.0`, complete run, 1/1/1 vs 0/0/0; "every time" rather than "reliably" to avoid implying a large sample). Comms' call.
- Revoke clause added, gated on the test.
- A server-only variant that promises no skills.

### Comms' voice pass (2026-10-11), changes made in place above
- A one-liner: "a colleague **that** turns" → "**who** turns" (Piper is they/them, and v1 had "who").
- "Honest about what's missing" → "**Clear** about what's missing". PM flags "honest" as a Claude-ism, and v1 used "Clear".
- "did this every time" → "did this **in every trial**". It's the same sourced claim (`RESULTS-v0.1.0`, 1/1/1 vs 0/0/0), and it names the unit, so it doesn't sound like a large sample.
- "plus the biggest judgment call made" → "the biggest judgment call **behind the ranking**" (the bare passive had lost its subject).
- A: "The connection can't change" → "The **connector**", to match B and the "connector is it" rule.
- "you need a Piper account to use this" → "to use **it**".
- "reads and suggests; it doesn't act" → two sentences, and the B bullet list lost its semicolons (no semicolons in public copy).
- **Left for PM, not changed:** "It doesn't act for you **yet**". "Yet" is a quiet promise about a later version. It's true to the plan, but it sets the kind of expectation PM named. Keep it or drop it, PM's call. `[INVITE LINK]` and the gated revoke clause are untouched.

### PA, after Comms' pass (2026-10-11, PM's question: "does the write-up address that Piper can only know things about you if you have set up an account already?")
- It didn't. "You need a Piper account" was there, but not *why*: everything Piper reports comes from the Piper account (setup answers, what you've confirmed with Piper, the GitHub account connected there). Added the paragraph **"What Piper knows comes from you."** to A and B, right after the opening, so a stranger knows up front that a new account knows little. "Piper will say so" is they/them-safe and avoids "honest".
- `[INVITE LINK]` → "To request an invitation, email support@pipermorgan.ai." (PM leaned to support@; PA agrees, see the session log.)
- Recounted (python `len`, bold marks and gating note stripped): A description 1,781/2,000, B description 1,279/2,000. One-liners and the Registry line unchanged.
- Comms' open question ("yet") is still PM's.

### Comms, on PA's new paragraph (2026-10-11)
- Kept the paragraph and its place. Shortened it in A and B: the opening paragraph (A) and the bullet list (B) already name the same four things (priorities, projects, working style, GitHub), so the new paragraph doesn't repeat the list. It now says only where the knowledge comes from and what a new account means.
- "Piper only knows" → "Piper knows **only**" (it scopes the knowledge, not the verb). "A new account knows little" → "With a new account, **Piper** knows little" (an account doesn't know things, Piper does).
- The support@ line reads fine as is.


### PM's review (2026-10-11 15:07 PT, in conversation with PA)
- "Good update to the draft. That helps contextualize it a lot."
- **"Yet" stays** ("Keep the 'yet' in").
- **Revoke clause stays out until PM's revoke test, and nothing is submitted until that's resolved.** If the test passes, the clause goes in as gated text, then submission. If it fails, the clause stays out and the fix comes first.
- First-time user setup and config: "can wait". Filed as #1981 (no milestone; placement is PPM's).
