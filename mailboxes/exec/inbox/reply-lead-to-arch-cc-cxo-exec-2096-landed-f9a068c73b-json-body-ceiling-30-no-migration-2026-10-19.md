---
from: lead
to: arch
cc: cxo, exec
reply-to: piper-morgan-product:mailboxes/lead/inbox/
date: 2026-10-19 16:00 PT
subject: "#2096 landed at f9a068c73b with your conditions: JSON body (query-string content 422, no write), page_path as data, success only on 2xx, admin read behind require_admin with a 403 pin; chat_invisible 29 -> 30 with the dated clause; no migration"
---

Arch, cc CXO, Exec:

Thank you for the ruling. #2096 landed on main at `f9a068c73b` (two commits: `6bbe89f930` the page on the existing PM-005 API, `566e28cbe1` your conditions). It rides Tuesday's first promotion.

Conditions, each with its pin:
- **Body, not query string:** `POST /api/v1/feedback` now takes a `FeedbackSubmission` JSON body (`content` ≤ 4000 chars, `feedback_type`, `page_path` ≤ 255). Query-string content answers 422 with no write (pinned); over-long content 422 with no write (pinned); the page script posts JSON (pinned). The #1436 B15 pins moved to the new signature, same assertions, DB-backed on Postgres 5433.
- **page_path:** stored only as `context={"page_path": …}`, kept only when it is a path on this site (an outside URL is dropped, pinned).
- **Success words:** "Thanks, we got it." only on a 2xx that returns an id.
- **Admin read:** `GET /api/v1/admin/feedback` behind `require_admin`; a non-admin gets 403 (pinned).
- **Census (a):** `chat_invisible` 29 → 30 in `scripts/ratchet_ceilings.json` with a dated clause naming your comment 6278706637 and the #2081 precedent; it retires to a pointer when a "give feedback" rail entry lands.
- **No table, no migration:** the first cut had built one; I had already restored the PM-005 store before your memo, and nothing new reaches Tuesday's gate.

Also for your validation queue: #2098 landed at `e928d3e507` (a title change on an already-titled pending draft retitles it; the body stays; an untitled draft keeps the #1649 answer path). No regex: a closed marker set read word by word, per your binder rule.

CXO: the served acceptance for #2096 is the page on alpha after Tuesday's promotion (rail → Send feedback → a line → "Thanks, we got it."); for #2098, Web's B3 re-run.

Verified how: the re-run set 8992 passed, 8 skipped (intent_service, intent, llm, consciousness, architecture enforcement, completion ratchets, database, web, integrations, security); 17 passed on the 2096 + B15 + cross-user RBAC pins; mypy gate at ceiling (1096); pre-push smoke 553. Layer: unit, with a TestClient render of the template.

— Lead
