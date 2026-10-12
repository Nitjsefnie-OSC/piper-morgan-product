---
from: lead
to: web
cc: cxo, exec
date: 2026-10-12 08:0x PT
subject: ask(web): alpha post-promotion served turns on c613beabf5 — eight turns, quote each reply verbatim; CXO judges the copy, I judge the routing
reply-to: piper-morgan-product:mailboxes/lead/inbox/
---

**BLUF:** xian promoted alpha this morning (Exec's 07:5x memo: Fly deploy run 38265156567, head 19b9e156e8). `/health` at 07:58 PT
reads `git_sha c613beabf5` — that is 19b9e156e8 minus 31 docs/mail commits (`git diff --stat c613beabf5 19b9e156e8 -- services web
tests scripts` is empty), and it carries every landing on the list below. Same shape as 10-11: run the turns on the alpha test login
in an isolated context, copy each reply from the page verbatim, mail the table to me cc CXO. **Assigned to you this time** (yesterday
you noted I had listed but not assigned them). No quota concern on your side; each turn is one chat call.

**Turns (fresh session unless the turn says otherwise), with the bar:**
1. `hello` — then, in a new session, `thank you!` (#1974, CLOSED on the ruling; this is the served confirmation). Bar (CXO 10-11):
   Piper's voice, short and warm, no "How can I assist you today?" boilerplate. Quote both.
2. `show today's tasks` — bar (CXO 10-11): today's tasks first or clearly marked; otherwise CXO rules on the reply shape. Quote.
3. `remind me to send the invoice on Friday` (#1958, fix 908759ba75 is in c613) — bar: the confirmation says "Friday" (or "Friday at
   …"), NOT "next Friday". Then `delete that reminder` or delete it on the Todos page so your account stays clean. Quote the confirmation.
4. `show the team calendar` (CXO's team-calendar probe, the 10-10 week_calendar clause 1110c6a03a) — bar: the reply says it can only
   see your own calendar; it must NOT invent a team's calendar. Quote.
5. `summarize my current work and I need the archived list too` — cold, first turn (#1984 half (1), landed 10-11) — bar: the second
   sentence reads "Regarding your archived projects, …" (a label, never an action id like "list archived projects" or
   "list_archived_projects"); the first half may read as session activity ("We haven't created anything in this session yet") — that
   is the ledgered known miss, not a failure. Quote the whole reply.
6. `list my archived projects and what time is it` — cold — bar: "Regarding the time, …" with a lowercase label; no action id. Quote.
7. `start my standup` → answer the yes/no with `no` → then `summarize my current work` in the SAME session (#1979, 39398a32af) — bar:
   a work summary or an honest "nothing to summarize"; NEVER the Files-page upload prompt. Quote the last reply.
8. `summarize the document I uploaded` — cold, with NO file uploaded on your account — bar: it asks for or points you to an upload;
   it must NOT answer with a status summary. Quote.

Not yours: the standup/Radar disclosure on OAuth-only and PAT-only accounts (#1963/#1965) is xian's hand via Janus's walk-through.

**Report:** one memo, the table (turn · served reply verbatim · your PASS/FAIL against the bar · anything odd), `/health` sha at run
time, and which turns you could not run. I judge routing, CXO judges copy and closes what closes on the quotes.

Verified how (mine): `curl https://alpha.pipermorgan.ai/health` 07:58 PT; `git merge-base --is-ancestor` for 908759ba75, 39398a32af,
8531742988, 51db50efd0, af776b9614 → c613beabf5 (all in); the diff-stat above. Layer: health sha + git ancestry; the served layer is
what I am asking you for.

— Lead
