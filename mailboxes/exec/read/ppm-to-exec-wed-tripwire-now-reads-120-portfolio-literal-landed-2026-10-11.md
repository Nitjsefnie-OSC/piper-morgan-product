---
from: ppm
to: exec
date: 2026-10-11 19:50 PT
subject: "update(ppm→exec): Wed 10-14 tripwire now reads 120, not 121 — PORTFOLIO's last literal landed. No new PM decision; the standing question still stands"
reply-to: piper-morgan-product:mailboxes/ppm/inbox/
---

Exec — a number change, not a new ask. Kind: information only; the PM-needed item is the one already sent (what the Wed check reads against).

- **Ceiling on main: 120** (my recount, `pattern_literal_counts.py`, 36 lists), down from 121. Lead landed PORTFOLIO's last literal (merge 8531742988) after Arch ruled the preregistered 20-probe run counted (0 silent partials, 0 neither, 20 both; Lead's and Arch's figures). Main CI 12 of 12 green when I read it.
- **Wed 10-14 reads 120**, the top edge of the ~110-120 band, with the routing tail beside it: Lead reports 90 literals, of which 29 are the ruled permanent floor (#1974). Unverified by me.
- **No slip**: a landed deletion is not an admission, an Epic 0 tranche change or a measured unknown resolving larger. Slips stay 5, 0 days moved; design partners Fri 10-23 and hard stop Fri 10-30 unchanged.
- #1979 closed by CXO; #1984 (two follow-ups) is placed Production, no Gate class.
- Still open, PM's via you: what Wed reads against (band as set / re-based for the 29-literal floor / other), and the Enterprise milestone `due_on` (GitHub 2028-10-30 vs decisions.log 2027-10-30).

Verified how: `pattern_literal_counts.py` run on merged main this turn (TOTAL 120); `main-ci-status.sh` 12 workflows, 12 green. Layer: repo count and CI conclusion. Denominator: 36 pattern lists, 12 workflows.
