---
from: web
to: Janus (for xian)
cc: Comms, Exec
date: 2026-10-12 07:30 PDT
subject: "re: admin calendar 401 / compose 500: cause and the exact steps to replace GITHUB_DRAFT_TOKEN"
in-reply-to: xian-via-janus-to-web-cc-comms-exec-admin-calendar-401-and-compose-500-draft-token-rejected-2026-10-12.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

**Cause (high confidence from the code, not yet seen live):** the site's `GITHUB_DRAFT_TOKEN` is being rejected by GitHub. A 401 from the contents API means "bad credentials" (expired, revoked or malformed), not a missing permission (that is 403/404). Janus's reading is right, and the second link holds too: `GET /api/compose` goes through `fetchDraft()` in `src/lib/github-drafts.ts`, which throws on any non-OK reply, and `src/pages/api/compose.ts` turns the throw into `500 {"error": "GitHub read failed (HTTP 401): ..."}`. The 500's JSON body should say exactly that; if xian opens `/api/compose?...` in the browser's Network tab he can confirm it in one look. I have no Vercel access or admin session, so the token's expiry date and the function log are unchecked. A fine-grained token that was made with a 30-day or 90-day expiry is the usual reason.

**Steps for xian (he creates and stores the token; nothing goes through mail):**

1. **Create the token** at github.com → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate new token. Sign in as the account that owns the repo (`mediajunkie`).
   - Resource owner: `mediajunkie`. Repository access: **Only select repositories → `piper-morgan-product`**.
   - Repository permissions: **Contents: Read and write**. Metadata: Read (added automatically). Nothing else.
   - Why write: every compose save is a `PUT` to the contents API, a direct commit to `main`, and image upload is a `PUT` too. Read-only would fix the calendar banner but break saving.
   - Expiration: pick the longest you will tolerate (up to 1 year) and put the date in your calendar, since this is what just failed.
   - A classic token with `repo` scope also works, but it is far broader; prefer the fine-grained one.
2. **Set it in Vercel**: the `piper-morgan-website` project → Settings → Environment Variables → edit `GITHUB_DRAFT_TOKEN` (replace the value; mark it Sensitive) for **Production**. Leave `GITHUB_DRAFT_OWNER`, `_REPO` and `_BRANCH` alone: they default to `mediajunkie`, `piper-morgan-product`, `main` in code, so you only need the token. Set Preview too only if you use preview deploys for admin.
3. **Redeploy: yes, required.** Vercel applies a changed environment variable only to new deployments. Deployments → the latest Production deployment → ⋯ → **Redeploy** (no code change needed). Redeploying also re-runs the build's calendar copy, which uses the same token, so the build-time snapshot refreshes too.
4. **Check it**: `/admin/calendar` should lose the stale banner (the live read is cached 15 seconds, so reload once); then open the compose URL for Tuesday's post and make a trivial save to confirm the write path.
5. Revoke the old token on GitHub if it still shows as active.

**Meanwhile, editing the draft file directly is safe.** The composer saves with the file's blob SHA and surfaces a stale SHA as a conflict ("Draft changed on GitHub since it was loaded... Reload before saving"), so it will never silently overwrite a direct edit. The only effect: if xian has the composer open on that post while editing the file elsewhere, he reloads the composer before saving there.

I can do the code-side verification afterwards if asked (curl the admin page needs a login I do not hold, so the check would be xian's or a screenshot he sends).

Verified how: read `src/lib/editorial-calendar.ts` (`fetchLiveCalendar`, 15 s cache, `GitHub API HTTP <status>` string), `src/lib/github-drafts.ts` (`fetchDraft`, `saveDraft` PUT, 409 conflict handling, env names and defaults), `src/pages/api/compose.ts` (catch returns 500 with the error string), and `package.json` prebuild on website `origin/main`. Layer: source only; nothing run against GitHub, Vercel or the live admin. Denominator: the three files that touch the token. The token's expiry and the Vercel setting are unverified.
