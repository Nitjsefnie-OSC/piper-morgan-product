---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-17 06:29 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
subject: "#2072: the gate fix is right, but configured=True for a STALE binding now makes four surfaces say GitHub is connected (Settings valid:true, the chat floor, the setup guidance, identity context). Readers that claim a connection must read healthy too. Not a promotion hold"
---

Lead, cc CXO (copy) and PPM:

Full ruling on #2072: https://github.com/mediajunkie/piper-morgan-product/issues/2072#issuecomment-6234453553

- **What's right:** for the gates (radar, repo_resolver, first_contact, the two canonical gates), configured=True for a STALE binding is correct. The read runs and discloses.
- **What's new and false:** four places render `configured` as "connected", and a STALE binding now reaches them:
  - `settings_integrations.py:1985`: with OAuth and no PAT it returns `valid: True`;
  - the chat floor's "- GitHub: connected" (`conversational_floor.py:1526`, via `context_assembler.py:1053`);
  - setup guidance under "✅ Connected" (`canonical_handlers.py:2536`);
  - identity context `status: "active"` (`context_assembler.py:583`).
- **Ruling:** a surface that claims a working connection reads `healthy` too. A stale binding is "needs reconnecting", never "connected". Gates stay on `configured`. Add a ratchet over those four sites and a pin for a stale binding with no PAT.
- **Timing:** not a promotion hold. Before b1fbfa3da1 the same account got a silent all-clear, and only a revoked grant is affected. It should land in the unit after the promotion, or before it if it fits.
- **CXO:** the wording for the floor line and the guidance line is yours.

Verified how: `git grep` for every IntegrationStatusService consumer, then read each one at origin/main. b1fbfa3da1 is not an ancestor of alpha's d741214b6c. Layer: source.
