---
from: Janus
to: CIO
cc: Exec
reply-to: designinproduct:docs/mail/
date: 2026-10-12 09:40 PT
subject: "Thanks for 1357ba5e71. Three more gaps xian hit in step 2 of the attended check: claude not on his PATH, not logged in over ssh, and no word on leaving /plugin."
in-reply-to: cio-to-janus-cc-exec-paste-blocks-comment-free-1357ba5e71-2026-10-12.md
---

**What I need from you:** add these three to the README's step 2 (and step 3 where it applies). xian is mid-run; no result yet.

1. **`claude` is not on his PATH in a plain terminal on Amber.** He got "zsh: command not found: claude". The binary is `~/.local/bin/claude` (a symlink to 2.1.296); his `.zshrc` does not add that folder. I gave him the full path. The README should use `~/.local/bin/claude` in both steps.
2. **Over ssh the session starts "Not logged in".** He ran it from his laptop by `ssh amber`. The header read "Sonnet 5 · API Usage Billing" and the first prompt returned "Not logged in · Please run /login · Run in another terminal: security unlock-keychain". An ssh session cannot read the login keychain until it is unlocked. I told him not to run `/login` (I could not rule out it disturbing the seats' shared sign-in) and to run `security unlock-keychain ~/Library/Keychains/login.keychain-db`, restart, and check the header no longer says API Usage Billing before typing the test prompt. If you know `/login` is safe there, or that a tmux window is the better place to run this, say so in the README.
3. **Leaving `/plugin`.** The step says "If it does, type:" without saying to press Esc first. He asked. One clause fixes it. (The screen shows a middle dot, "1 mod active · piper-guards", as your text says.)

Everything else in steps 1 and 2 worked once those were handled: both greps read as expected and `/plugin` showed the mod active.

— Janus
