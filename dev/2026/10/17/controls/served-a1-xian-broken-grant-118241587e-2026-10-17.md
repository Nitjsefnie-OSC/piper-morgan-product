# Card A1 served readings: xian's own account, alpha `118241587e`, 2026-10-17 15:16–15:2x PT

Recorded by Lead from xian's console paste and screenshots in chat. Layer: served alpha, real browser, xian's own account (the binding that failed on 10-16 with `degraded []`). Judge: CXO (words), PA (comments on #2031, #2072).

## Step 1: read snippet after the revoke (the one read nobody had run on this build)

**PASS.** Console output verbatim (prose fields):

```
degraded ["your GitHub work items"]
today {"prose":"Your GitHub connection needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up.","summary":{"yesterday":[],"today":[],"watch":[],"degraded_sources":["your GitHub work items"],"degraded_details":[{"label":"your GitHub work items","reason":"stale_token","connector":"GitHub"}]},"disclosure":"Your GitHub connection needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up."}
slack  standup: "*Morning Standup* :sunrise:\n_2026-10-17 3:16 PM PDT_\n\n_Your GitHub connection needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up._\n"
markdown standup: "# Morning Standup\n*2026-10-17 3:16 PM PDT*\n\nNote: your GitHub connection needs re-authorizing, so I can't put together a standup. Reconnect it in Settings and I'll pick back up.\n"
```

Note for readers of the steps file: `degraded` carries the user-facing label ("your GitHub work items"); the `stale_token` reason and `connector: GitHub` are in `degraded_details`. On 10-16 (`d741214b6c`) this same read gave `degraded []` and an all-clear standup. #2072's gate fix is seen working on the account that showed the failure.

## Step 2: the pages (screenshots in chat)

- **Integrations** (`/settings/integrations`, "Last updated 3:17:09 PM"): GitHub card **⚠️ Needs reconnecting**, "GitHub no longer accepts your connection.", one **Reconnect with GitHub** button, no Test button. **PASS.** Headline: **Needs attention**, "0 of 2 connected integrations working" (Google Calendar shows "Connected", "Not checked yet. Press Test."). Observation for CXO: an untested Calendar counts as not working in that headline; no card fail, filed as a note.
- **Settings → GitHub** (`/settings/integrations/github`): **Needs reconnecting**, "GitHub no longer accepts your connection, so I can't read your GitHub right now." Fix Connection: "Reconnect to give me access again. Nothing else on your account changes." + **Reconnect with GitHub**; below, the PAT form ("Or connect with a personal access token", a masked field, Reconnect / Disconnect). **PASS** on the words. Open question for PA: the masked field reads as a placeholder; the card did not say "Connected via your personal token", so no PAT is inferred.

## Step 3: Reconnect with GitHub

Clicked. GitHub's own screens followed: account chooser (xian is signed into two GitHub accounts), the authorize page (repositories public and private, two org grants, "Fewer than 10 GitHub users", redirect to alpha.pipermorgan.ai), then GitHub's sudo-mode confirm. Those screens are GitHub's, not Piper's. Result on alpha: **pending xian's last screenshot.**

## Step 4: read snippet after reconnect

Pending.
