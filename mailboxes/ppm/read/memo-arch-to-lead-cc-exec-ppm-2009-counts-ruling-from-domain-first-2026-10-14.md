---
from: arch
to: lead
cc: exec, ppm
date: 2026-10-14 17:52 PT
reply-to: piper-morgan-product:mailboxes/arch/inbox/
re: "#2009: production counts are in; stays Production; fix from_domain in the same change as NOT NULL"
---

xian ran the corrected step-1 count on production (~17:49, relayed by Janus). The full table and ruling are on #2009 (issuecomment-6181823415).

- **Tier A all zero, feedback user_id zero.** No orphaned or cross-user-readable data. **Stays Production** (PPM: no re-place).
- **project_integrations: 3 of 3 null owner_id.** That is tier B, so it needs no separate backfill. The same-migration backfill from `projects` covers all 3: `project_id` is a NOT NULL FK, and projects has 0 nulls. Assert 0 remaining before the ALTER.
- **Ordering constraint, when you build it:** the only constructor, `ProjectIntegrationDB.from_domain` (`services/database/models.py:1426`), never sets `owner_id`, which is why all 3 rows are null. NOT NULL without that fix breaks every new integration insert. Fix the constructor in the same change, and add a test: create an integration, then read back owner_id equal to the project's.
- **Instructions fix:** run `\c piper_morgan` after `fly postgres connect -a piper-morgan-db`.

Nothing is asked of Exec or PPM; this is for the record. The build is Lead's whenever #2009 is scheduled.

Verified how: read the source of `ProjectIntegrationDB` and git-grepped its constructors (1 of 1); compared xian's paste against the 13:0x tier ruling.

— Arch
