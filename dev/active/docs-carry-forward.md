# Docs Carry-Forward

**Updated**: 2026-10-12 19:2x PDT (19:12 fire). DONE 10-12: 10-10 + 10-11 omnibuses, Weekly Audit #1994 closed, BRIEFING-CURRENT-STATE refreshed, How to Report edit pushed (xian approved), Ship #064 row set by Comms and view rebuilt. Known fault: bare `gh` hung on Amber after the 10-10 reboot (Pard); prefix `GODEBUG=netdns=go` until Pard confirms the fix. History in session logs (`dev/2026/10/{04..12}/*docs-code-log.md`), not here.

## Done this fire (04:12)
- 10-09 omnibus (`adba285845`, 540 lines, 15 logs, 1128 commits, 574 comparable) + 15 activity rows (`a0906091be`, 2865 to 2880). Nudged HOST (10-09 log lacks DAY-CLOSED, `8e927d29ef`).
- **"No Undo" PUBLISHED** (insight): website `d3246f3`, live at https://pipermorgan.ai/blog/no-undo/ (body phrase "sprint options" + image 200, verified after the deploy lag). Calendar row `published`, blogURL/blogPath set, `canonicalSite` empty, draft + jpg archived, validator 0 errors, 0 of 470 draftPaths unresolvable.
- Notice to Exec that the crosspost is owed (`afdcc5345`).

## OWED (PM's hand)
- Nothing for "It Doesn't Count if You Skip It": FULLY DISTRIBUTED 10-11 (LinkedIn + Medium URLs from PM, row `distributed`, `canonicalSite` `distributed`).
- `published` with an empty pubDate: "15 Sessions, Fast Recovery" (outside Step 1f's window, age unverified).

## Unclosed logs / awaiting
- HOST 10-09 log: no DAY-CLOSED (nudge sent). Spec's 10-08 log unclosed, no Spec 10-09 log, seat looks dormant. Re-check at the next START (Step 1d).
- Roadmap v19.0 fold LANDED (`aca130a366`). I re-audited it and **closed #1644** (05:3x). Reply to PPM filed (`114a882b5`). Enterprise milestone date (GitHub 2028-10-30 vs decisions.log 2027-10-30) is PM's via Exec, PPM routed it, nothing owed from Docs. Exec (cc, read 05:4x) will relay PM's 2027/2028 answer to PPM and Docs; no Docs edit unless asked.

## NEXT (named triggers)
- **Giving It Away**: PUBLISHED 10-13 (website `d1f39f2`). Medium crosspost DONE 10-13 (row `distributed`).
- **10-12 omnibus**: drafted by a Sonnet subagent 10-13, commit plus activity rows pending in the 04:12 fire log. Exec and CIO 10-12 logs unclosed (nudged).
- **Wed 10-14 04:12 fire**: PUBLISH Ship #064 "Weekly Ship #064: Code Decides Permission" (`ready-for-docs`, Comms memo received, pre-flight and dry-run done 10-13). Real publish from the website worktree: `--draft .../weekly-ship-064-draft-2026-10-12.md --slug weekly-ship-064-code-decides-permission --category ship --work-date 2026-10-02` (no image flag, reuses piper-ship.webp). Re-fetch first. Live URL is under `/shipping-news/`. Then row `published` with blogURL/blogPath, archive the draft, LinkedIn-only reminder to Exec.
- **Thu 10-15 04:12 fire**: PUBLISH "The Overzealous Cleanup Routine" (`ready-for-docs`, Comms memo received, pre-flight and dry-run done 10-13). `--draft .../the-overzealous-cleanup-routine.md --image .../the-overzealous-cleanup-routine-waiter-carries-away-untouched-dinners.png --slug the-overzealous-cleanup-routine --category building --work-date 2026-08-14`. Re-fetch first. Then archive draft and png, row `published` with `draftPath` to `drafts/published/`, Medium-only reminder to Exec.
- **Mon 10-19**: next weekly audit. **~11-30**: glossary 60-day re-verify.

## Held on PM (via Exec)
- `git rm` of `dev/active/covapitchdeckv2.pptx` and `dev/active/Treatment`. #1909's two open boxes.

## Seat facts
- LaunchAgent-only (cron `12 4,7,10,13,16,19,22 * * *`), no session cron to re-arm. START opens every fire.
