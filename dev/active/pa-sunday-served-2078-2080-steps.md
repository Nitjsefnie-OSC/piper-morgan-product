# Sunday served checks: the wizard sign-up (#2078) and the add-project chain (#2080)

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

## A. #2078: a fresh invited sign-up through the wizard (must-close)

Before: the run builds on `d82b5ce4b3`. HOST has minted one invite; the runner has it from the
`~/.piper-shared/` file HOST names (masked form only in mail).

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

## After

PA relays the quotes to CXO for #2078 and #2080, and comments on both issues with `Verified how`. #2078 closes on
CXO's judgement (must-close). #2080 closes on PA's served chain against CXO's acceptance.

Verified how: code reads on main this fire. The wizard markup and step-5 copy are in `templates/setup.html`; the
decline constant is in `services/intent_service/add_project_clarify.py` (`_add_project_confirm_decline`); the
`setup_complete` read is in `web/api/routes/ui.py`. Not served yet.
