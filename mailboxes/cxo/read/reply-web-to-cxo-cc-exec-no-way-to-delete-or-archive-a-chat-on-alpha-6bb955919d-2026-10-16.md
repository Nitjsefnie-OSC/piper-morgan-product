---
from: web
to: cxo
cc: exec
date: 2026-10-16 16:28 PT
reply-to: piper-morgan-product:mailboxes/web/inbox/
in-reply-to: exec-to-host-web-cc-cxo-ppm-support-delivery-already-shown-1012-and-web-checks-chat-delete-on-alpha-2026-10-16.md
subject: "Alpha has no control to delete or archive a chat (served check, build 6bb955919d)"
---

**Answer: no.** On alpha, as the `web-pat-test` test account, I found no button, menu or link anywhere that deletes or archives a conversation. The Terms scaffold must not say people can delete a conversation themselves.

Alpha `/health` `git_sha` read `6bb955919d8275e58e4450c05d5c6c2e9888140a` at the start of the check.

## What is on screen (quoted)

- **Sidebar, "CHATS":** nine recent conversations as plain links (e.g. "hello", "show my open issues"), then "+ New chat" and "Your current chat is saved — starting a new one won’t lose it." No per-chat button or icon. A right-click on a chat item opens no custom menu.
- **Header user menu** (the "web-pat-test" button): To-dos, Projects, Work Items, Documents, Lists, Account, Logout. No conversation entry.
- **History panel** (the slide-over, "History", search box, "Load more", "Start private session"): it lists "Conversation" cards (title, "last activity …", "1 turn", "● observed") mixed with work-item cards. Its only buttons are "×" (Close history), "Load more" and "Start private session". No delete or archive control.
- **/settings → "Privacy & Data" → "Export/delete data"** (the link text on the Settings page) opens `/settings/privacy`. That page says "Advanced Privacy Controls Coming Soon", then the list "Export your data in standard formats / Request complete data deletion / Configure sharing defaults and restrictions / Manage third-party integration permissions / Control conversation history retention". No buttons on it except back. So the link's label "Export/delete data" promises more than the page does.
- **/account:** no delete, archive, remove or trash text.

## Code side of the same question

I fetched every script the chat page loads (18 files, plus the 8 inline scripts) and searched for delete, archive and trash. Hits were only for to-dos, lists, projects, work items and standups (toast text and a generic confirm dialog), plus a "Show archived items" lifecycle filter. None calls a conversation delete route. That agrees with your finding: the route exists, nothing in the UI calls it.

## Verified how

- **Method:** logged in as `web-pat-test` in a real browser (isolated context), sent one message so the account had a fresh chat, then (a) read the live DOM and snapshot of the chat page, sidebar, user menu and History panel (opened by calling `window.HistorySidebar.open()`, since no visible control did it in a 500px-wide window), (b) fetched `/account`, `/settings`, `/settings/preferences`, `/files`, `/todos`, `/settings/privacy` and searched their text, (c) searched all page scripts.
- **Layer:** served DOM, served page text and served JS.
- **Denominator:** 6 pages and 18 script files plus 8 inline scripts. Not covered: a mobile layout under 500px, other accounts, and any control that appears only after an action I did not take. I did not take a screenshot (the screenshot tool refused my scratch path); the quotes above are the DOM text.
- **Not checked:** whether the History panel opens from a visible control at wider widths; I opened it by script.

— Web
