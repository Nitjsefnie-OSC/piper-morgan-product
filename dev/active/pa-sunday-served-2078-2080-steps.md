# Sunday served checks: the wizard sign-up (#2078), the add-project chain (#2080), the greeting (#2079), the MCP PAT read (#1982)

**Owner**: PA (steps and the judgement relay). **Written** 2026-10-17 18:49 from main (`d82b5ce4b3`, `86f938bf8d`,
`ebd29ecef7`) and CXO's 18:32 acceptance. **Run on**: Sunday's first promotion. Before starting, check alpha `/health`
names a sha that contains all three (plus `92f723e5b0`, the split decline, and `797ab61a11`, #2079) (PA does this when Lead's sha memo arrives).

**Who runs what.** Both checks have to go through the page in a real browser. Web's API lane misses #2078 by
construction.
- **#2078 needs a fresh invite**, and PA never holds one (invite codes are bearer credentials). So it's run by whoever
  holds the invite HOST mints: xian, or Web in an isolated browser context. PA writes the steps and relays the result.
- **#2080** runs on any account with no project called "Piper Morgan". Lead suggested xian's A4 account, in a fresh
  chat. Web can run it on a test account if xian isn't at the keyboard.

About 10 minutes for both.


## Status, 10-19 11:21 (alpha `f9fb8b750b`, Monday promotion 1 of 2, 11:17; contains every fix below plus #2082 and #2067. The prod DB was down 05:25–09:52 and is back; read `/health` `services.database` before any run)

| Row | State |
|---|---|
| B: #2080 chain | **CLOSED** (CXO 10-18 11:34, on Web's quoted chain and decline). Step 6 as I wrote it was unreachable by design (my spec error). |
| C: #2079 greeting | **CLOSED** (CXO 10-18 12:32, on Web's morning and afternoon quotes). |
| A: #2078 wizard | Not run. **xian minted ten codes** into `~/.piper-shared/xian-invite-bank-credential-20261018.txt` (HOST's shape). The 10-17 A4 file is spent (HOST's roster). The runner is xian (card D2), or Web if he hands one code over. Steps below stand. |
| D: #1982 MCP PAT read | Not run. On xian's card as **D4** (v82, after D2; Lead 10:0x). His hand; PA reads the MCP logs when he runs it. |
| #2077 | **CLOSED** (Lead 10-19 12:34): xian's own Chrome profile with the saved Piper password, `token` length 0 (card D1). |
| #2072, #2076, #2069, #2051 | Closed by CXO on Web's rows. |

## A. #2078: a fresh invited sign-up through the wizard (must-close)

Before: the build is `47ba746bee` (served 06:42 10-18, contains `d82b5ce4b3`; PA checked). **The invite:** HOST's file
`~/.piper-shared/xian-a4-pat-test-credential-invite-20261017.txt` is **probably spent**. xian's 10-17 16:09 sign-up
(the A4 account, the one #2078 stranded) used it; the file is timestamped 16:10. That's an inference, not
redeemed. If step 3 says "invalid or already used invite token", that's not a #2078 fail: mint one more
(`scripts/mint_prod_invite.sh --apply` on Amber, saved under a `-credential-` name), then redo step 3. Best to
mint first and save the retry.

1. Open `https://alpha.pipermorgan.ai/setup` in a browser that **isn't** signed in to alpha (a private window works).
2. Step 1 (System), then step 2 (Connect Your AI): enter a real LLM key and Continue.
3. Step 3 (Create Your Account): enter the invite code, a username, an email and a password, then **Create Account**.
   **Pass**: it moves on to step 4. **Fail**: any "Setup Failed", or the button stuck on "Creating…" (the 10-17 16:09
   bug).
4. Step 4 (Your Projects): add one project (any name), then continue.
5. Step 5. **Pass**: "Setup Complete", "You're all set. You're signed in, and Piper is ready to help." and an
   **Open Piper** button. Quote it. If it shows a toast titled "Account created, setup did not finish" instead, quote
   the toast and stop. That's #2078's failure path, worded honestly, and it means the key wasn't stored.
6. Click **Open Piper**. **Pass**: you land at `/` signed in, with no login page.
7. Open Settings → LLM API Keys. **Pass**: the key from step 2 shows as stored. Then open My Projects. **Pass**: step
   4's project is there.
8. **`setup_complete` isn't visible on any page** (the home template reads it only for a disabled orientation modal).
   It needs a database read, which is xian's hand, not PA's. xian's C1 count on 10-17 was 10 users, 5 with
   `setup_complete`. After this run it should be 11 and 6. If xian would rather skip the read, steps 5–7 are the
   served evidence and the count is the database layer. Say which was done.

Optional (CXO): force the key step to fail (for example, a key that saves but a network drop at step 3). Quote the
toast and that the button resets. Skip it unless CXO asks; it's hard to force on alpha.

Quote for CXO: step 5's words (or the toast), the landing at `/`, and steps 7 and 8.

## B. #2080: the add-project chain in a fresh chat

1. Start a **new chat**. Type `list my projects`. Quote the reply. It should offer to add one if there are none.
2. Reply `Yes`. Quote it. It should ask for the name.
3. Reply `Piper Morgan`. **Pass**: the reply is exactly one question, `Add a project called "Piper Morgan"? (yes/no)`,
   with no second question. Quote it.
4. Reply `Yes`. **Pass**: a reply saying the project was added. On 10-17 this said "I don't have a confirmation that
   the project was created". Quote it.
5. Open My Projects. **Pass**: "Piper Morgan" is listed.
6. **The decline.** In another fresh chat, repeat steps 1–3 with a different name that reads as a question (for
   example `What's next`), then reply `no`. **Pass**: "Okay, I won't add that project. If you meant to ask me
   something, go ahead." Quote it. Then check that no such project exists. (CXO 10-17 evening: split the constant. If Lead's split is on the build, the other confirm arm, for an ambiguous reply, says `Okay — I won't add a project called "X". Nothing has been changed.` instead. Either line is right for its own arm; quote whichever appears and say which arm it was.)
7. **The floor offer (CXO).** If any turn in the chain says "want me to create…" (or similar) when it can't perform
   the write, that's a FAIL. Quote it whole. This is the 10-17 shape: two yeses and no project.

Quote for CXO: every turn of 1–4 and 6, and step 5's list.

## C. #2079: the standup greeting (optional, alongside B)

On an account that has signed in through `/login` (xian's A4 account qualifies), after noon: type `give me a standup`.
**Pass**: the first word of the reply is "Good afternoon!" or "Good evening!", matching the page header above it.
A wizard-created account that never used `/login` reads "Hi!"; that's right (CXO). Quote the first line and the
header. Fix `797ab61a11`, plus `92f723e5b0` for B6's split decline.

## D. #1982: the MCP app reads a PAT-only account's GitHub (PA's lane; xian's hand)

**Why:** the PAT dual write (`15dba249c8`, on `47ba746bee`) stores a PAT saved in Settings under the GitHub
context too, so the MCP app can read it. Before this, a PAT-only user got `CONNECT_REQUIRED` from the MCP app.
PM's own account is OAuth-only (A1, 10-17: no PAT), so the account to use is **xian's A4 PAT-only account**.

1. **Re-save the PAT on this build.** A4's PAT was saved on `118241587e`, before the dual write, so the MCP app
   can't see it yet. On alpha, signed in as the A4 account: Settings → GitHub → paste the same PAT → **Update**.
   **Pass**: it still reads "Connected". (The alternative is runbook step 2b's backfill script, which is xian's hand
   on alpha. Re-saving is simpler for one account.)
2. **Connect the MCP connector as the A4 account.** In Claude Desktop (or claude.ai), add or reconnect the Piper
   Alpha connector, and sign in **as the A4 account** on the alpha login page it opens. Your usual connector is
   bound to your main account, which is OAuth and doesn't test this.
3. Ask: **"What are my open GitHub issues in Piper?"** **Pass**: real issue titles that match GitHub, with the
   total stated (A4's PAT saw 274 on 10-17). **Fail**: "connect GitHub", `CONNECT_REQUIRED`, or an empty list.
   Screenshot it.
4. PA reads the MCP app's logs for that call (`fly logs -a piper-morgan-mcp`, a read): `EncryptedDBCredentialStore`,
   no decrypt error, no degrade.
5. Afterwards, switch the connector back to your main account if you use it day to day.

Not covered: other PAT-only accounts saved before the dual write (Web's `web-pat-test`, any tester's). They need the
2b backfill (dry run, then `--apply` with a snapshot), which is xian's hand. Until then the MCP app reads them as
not connected.

## After

PA relays the quotes to CXO for #2078 and #2080, and comments on both issues with `Verified how`. #2078 closes on
CXO's judgement (must-close). #2080 closes on PA's served chain against CXO's acceptance.

Verified how: code reads on main this fire. The wizard markup and step-5 copy are in `templates/setup.html`; the
decline constant is in `services/intent_service/add_project_clarify.py` (`_add_project_confirm_decline`); the
`setup_complete` read is in `web/api/routes/ui.py`. Not served yet.
