# Beta formalities checklist

**Kept by:** PPM, on xian's word (2026-10-19 12:26, relayed by Lead): "PPM should be tracking those formalities."
**What belongs here:** non-code steps that must be done before a design partner gets access. They aren't gate rows; the gate lives in `beta-gate-standard.md`. Each row names its owner and the event it must precede. PPM proposes no dates; "before" is measured against xian's existing targets (10-23 is the invite checkpoint, and 10-30 the target for the first partner's access).
**PPM's job:** keep each row current, and nudge the owner through Exec while a row is open.

| Formality | Owner | Must precede | Status | Record |
|---|---|---|---|---|
| Google OAuth **data-access verification** for `calendar.readonly`. Declare the scope on the Data Access page and submit. Google wants the privacy URL on the verified domain, the homepage, and a short demo video of the OAuth flow with a scope justification. Until it's approved, an outside user sees Google's "unverified app" screen before connecting Calendar, and counts against a lifetime cap of 100. | xian (his Google Cloud console) | the first partner's access (10-30). Google's review takes "days to a few weeks", per Lead's reading of Google's pages (unverified by PPM), so submitting is the long pole. | **Open, not submitted.** Done: External + In production (10-19 ~11:55); `pipermorgan.ai` verified in Search Console; branding verification cleared (per Lead, 12:26). `https://pipermorgan.ai/privacy/` returned 200 at 12:3x 10-19 (HTTP layer only). | #2087 |
| Known-issues lines for partners: #2042 and the todo-delete no-undo (#2019/#2021), plus whatever section A adds. | Comms writes; xian reviews section A | invitations (10-23) | Section B ruled 10-18. Section A is with xian for 10-23. | `design-partner-known-issues-review-2026-10-16.md` §D |
| Invitation wording: "create an issue" on GitHub posts with no confirm. | CXO | invitations (10-23) | Ruled 10-18 (in the wording, not the list). | same, §D |
| Terms commitment-to-mechanism map. | PPM, once xian's scaffold answers return | invitations (10-23), on PPM's reading | Waiting on xian's answers. | carry-forward |
