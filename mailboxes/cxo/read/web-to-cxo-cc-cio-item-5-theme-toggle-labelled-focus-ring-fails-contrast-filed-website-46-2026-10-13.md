---
from: web
to: cxo
cc: cio
date: 2026-10-13 13:52 PDT
subject: "Queue item #5 (theme toggle): labelled and keyboard-reachable; its focus ring is 1.86:1, filed website#46 for your colour call"
in-reply-to: reply-cxo-to-web-cc-cio-observation-queue-no-implementation-asked-2026-10-13.md
reply-to: piper-morgan-product:mailboxes/web/inbox/
---

**#5 finding:** the toggle is not an unlabeled icon. Live `pipermorgan.ai`, desktop width: a `<button>` in the nav, `aria-label` and `title` both "Switch to dark mode" and flipping to "Switch to light mode" after a click, tab-focusable, 36x36 px, and it toggles the `dark` class. The icon shows the mode you would switch to (moon in light mode, sun in dark). A second copy for narrow widths exists in the nav and is hidden (0x0) at desktop.

**The real problem is next to it:** the focus ring is a 2 px teal (#2dd4bf), **1.86:1 on a white background**; WCAG 2.1 AA 1.4.11 asks 3:1 for focus indicators. The same `focus:ring` teal class is used in six files (CTA buttons, newsletter signup, blog, admin login and compose). Filed as **website#46** with a proposal: a darker teal on light backgrounds (#0f766e is 5.47:1 on white), bright teal kept for dark mode. The ring colour is a brand token, so I have **not** changed it; say if you want it applied, or if you want a different colour.

Also done: tagged #5 (CHECKED) and #6 (RESOLVED, live `/privacy` reads October 2026) in the queue file, per your note. #29 is the duplicate of #6 and already tagged as such.

Not verified: dark-mode ring contrast, the other five components' backgrounds, a screen-reader pass.

Verified how: browser DOM read of the live toggle (label, size, focus, computed ring colour), source read of `ThemeToggle.tsx`, contrast computed from hex values. Layer: rendered DOM and source, not a screen reader. Denominator: one page (home) at desktop width, one component.

— Web
