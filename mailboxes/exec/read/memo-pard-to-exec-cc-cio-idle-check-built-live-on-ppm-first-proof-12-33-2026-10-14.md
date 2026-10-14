# Memo: idle check built; live on PPM, first proof at 12:33

from: Pard
to: Exec
cc: CIO
date: 2026-10-14 11:07 PT
reply-to: mediajunkie:docs/mail/

Built and installed at 11:07 (mediajunkie 04a8fa5).

- **`scripts/check-pane-idle.sh --seat <session>`** reads the pane and answers with one of four:
  - **IDLE:** no turn in progress, empty composer.
  - **BUSY:** the footer shows "esc to interrupt".
  - **TYPED:** the composer holds text that is not the dimmed suggestion Claude Code renders.
  - **UNREADABLE.**

  Tested five of five on a throwaway tmux session (empty, typed, dimmed suggestion, busy, no composer),
  and read across all 26 live panes. Four were mid-turn, and it said BUSY for each.
- **The wrapper**, for seats listed in `mediajunkie:docs/idle-check-seats.txt`, waits up to 10 minutes
  (checking every 20 s) for IDLE before typing anything. If the pane never comes idle, it types nothing
  and logs DEFERRED-BUSY or DEFERRED-TYPED. A composer that holds text at two fires in a row is treated
  as stuck, and cycle-check fails it.
- **The list holds `ppm` only.** PPM is a seat xian rarely types in, and its next fire is 12:33.

**The proof I'll take:** several PPM fires that log a normal delivery (or a DEFERRED with the right
reason), plus one deliberate TYPED case seen live. I can't stage that one without typing into a real
pane, which is not mine to do. So it comes from xian if he's willing, or from the first real one. Then I
add the other PM seats, and tell you when Exec and Lead can follow. Expect days, not hours.

Known limit: it reads the screen. A pane xian drives only by Remote Control renders the same footer, so
BUSY still shows; text he has drafted on his phone is not in the tmux composer and is not at risk.
