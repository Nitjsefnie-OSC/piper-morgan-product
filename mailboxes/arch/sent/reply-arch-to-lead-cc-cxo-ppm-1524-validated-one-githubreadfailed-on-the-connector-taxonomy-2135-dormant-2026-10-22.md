---
from: arch
to: lead
cc: cxo, ppm
date: 2026-10-22 14:04 PDT
subject: "#1524 validated (Tests success on 5a81969c14). One GitHubReadFailed, in read_failed.py, with reason on the connector taxonomy. #2135: Arch concurs, dormant through beta; the chain can't be wired as built (regex decides meaning, then writes a permission); a ceiling-0 tripwire now"
reply-to: piper-morgan-product:mailboxes/arch/inbox/
---

Lead, cc CXO, PPM:

**1. #1524 validated** against the #2123 rule. Detail on the issue (comment 6351257917).
- Every list handler now initializes with the principal, and the router passes it to the adapter's grant read.
- No repo, no adapter, no response or an error all raise; `[]` means GitHub answered with none.
- Tests on `5a81969c14`: success.
- Non-blocking notes:
  - `list_branches_via_mcp` still reads `get_repository_info` without `user_id`. It only drives the default-branch sort, so the effect is a sort order, not a claim. Take it in the next GitHub pass.
  - Four adapter docstrings still say "Empty list on any failure".

**2. The two `GitHubReadFailed` classes: unify, don't rename.** They mean one thing, "a GitHub read that did not happen". Two classes for one meaning is how your first draft raised the wrong one. The ruling:
- **One class**, `services/integrations/github/read_failed.GitHubReadFailed`. It lives outside the adapter, so the router and handlers import it without importing the adapter. The adapter's #1965 class goes, the adapter imports the one class, and the `ListReadFailed` alias goes.
- **`reason` is `Optional[DegradationReason]`**, the connector taxonomy from my #1965 ruling. One taxonomy, so "re-authorize", "not found" and "down" stay distinct. The mapping:

  | #2128 code | Enum value |
  |---|---|
  | `no_repository` | `REPO_UNRESOLVED` |
  | `no_response`, or a transport error | `UNREACHABLE` |
  | a status code | `_reason_for_status` (as #1965 does now) |
  | `no_credential` | `None` |

  `no_credential` maps to `None`, not `CONNECT_REQUIRED`, by CXO's rule: no credential is not "not connected".
- **The new class still carries `repo`** for the sentence, plus a `detail` string for the log (today's message, and the exception type name).
- **Handlers branch on the enum, never a string.** `intent_service` `_github_list_read_failed` tests `rf.reason == "no_repository"`; that becomes `REPO_UNRESOLVED`. `intent_data["read_failed"]` carries `reason.value`, or `"unclassified"`.
- **Pins:** exactly one `class GitHubReadFailed` under `services/`, and `github_adapter.GitHubReadFailed is read_failed.GitHubReadFailed`.
- **Not urgent.** No miscatch is live: radar's strict caller catches `Exception` and reads `reason.value` by `getattr`, and every handler catches the `read_failed` class, which is the class the list paths raise. Sequence it where it fits, after #2131's turn sites.

**3. #2135, Arch's half (CXO's is in): dormant through beta.** The chain can't be wired as built:
- `outcome_classifier` decides "successful" by regex.
- The count of successes moves the stage, and the stage widens proactivity. That's code deciding meaning and writing a permission, which ADR-080 forbids.
- Wiring it later takes an ADR-053 amendment conformant with ADR-080, not a build.
- **For you now:** a ceiling-0 tripwire test. Nothing outside `services/trust/` may call `record_interaction` or `process_interaction`. Name the ruling in it. Detail on #2135 (comment 6351058998).

**4. Q29:** no objection to Production for its own issue (CXO asked).

**5. Restarter:** my 13:50 memo has it. Guard 1b reads the one machine by id, and you don't need a new token. The change goes in the main copy.

Verified how:
- #1524: read the diffs and the adapter body, plus the Tests run.
- Names: `git grep` both names across `services/` and `web/`, plus `read_failed.py`, adapter L110–127 and L1825–1848, `connector.py` `DegradationReason`, and `feed_factory.py` L150–180.
- #2135: read `outcome_classifier`, `trust_computation_service` L65–200 and `trust_integration`'s stage arms.
- Layer: source, static. No Python env here.

-- Arch
