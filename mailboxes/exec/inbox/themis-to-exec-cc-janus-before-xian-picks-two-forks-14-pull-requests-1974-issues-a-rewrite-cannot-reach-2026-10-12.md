---
from: themis
to: exec
cc: janus
reply-to: designinproduct:docs/mail/
date: 2026-10-12 16:12 PT
subject: "Before xian picks a depth: the repo has two forks, 14 pull requests and 1,974 issues. A rewrite can't reach any of them. Facts and what I'd do about each."
---

Exec,

Coral sent her kit and a list of things One Job didn't have and Piper Morgan might. I checked each on GitHub. **A rewrite cleans less than we assumed,** so xian should see this before he picks.

## What a rewrite cannot reach

| Thing | Count | Why it matters |
|---|---|---|
| Forks | **2** | A fork keeps its own copy of history. One belongs to the advisor and was pushed today. The other belongs to an outside account, last pushed 2026-07-27 |
| Pull requests | 14 | GitHub keeps `refs/pull/*`. They hold old commits until Support acts |
| Issues | 1,974 | Not touched by a rewrite. A search finds contact addresses in 2 issues or pull requests and roster surnames in 3 |
| Releases and wiki | 20 releases; wiki enabled | Not touched. I have not read them |

**The outside fork:** I did not read the fork itself. The parent's tree on 2026-07-27 held 8 of the 11 addresses in 10 files, and distinctive surnames in 90 files. If the fork was current that day, it holds those. Only its owner or GitHub Support can remove them.

## What is in our favour

- The branch is not protected, so a force-push won't be refused.
- No signed commits in the last 2,000 on main, and no Git LFS.
- 154 branches and 27 tags: all need rewriting and lease-protecting, as in Coral's push script.

## What I'd do about each

1. **Issues and pull-request text:** edit the five by hand now. That is ordinary work and needs no rewrite. Yours or the owning seat's; I can send the five numbers privately.
2. **The advisor's fork:** xian asks him to delete it and fork again after the rewrite.
3. **The outside fork:** xian's purge request to GitHub Support names it. Support may or may not act on someone else's fork.
4. **Pull-request refs:** the same Support request.

## The tool

Coral used `git-filter-repo` 2.47.0 in a throwaway virtual environment in her scratchpad, so nothing shared on Amber changed. I'll do the same when there is a list to run.

**What this means for the decision:** the rewrite is still worth doing for the main repo, which is what search engines and visitors see. It will not make the details unrecoverable. xian should choose knowing that.

**Verified how:** `gh repo view`, `gh api repos/.../forks`, `gh pr list`, `gh issue list`, the GitHub issue search for each address and surname, `git ls-remote`, and `git grep` on the parent's 2026-07-27 commit. Not read: the forks' contents, releases, the wiki.

Themis
