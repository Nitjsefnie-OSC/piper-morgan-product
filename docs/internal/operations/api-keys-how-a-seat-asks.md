# API keys: how a seat asks for one

Source: xian, 2026-10-13, relayed by Pard. The kept record (which org is which, budget, every key's
name, consumer and expiry) is `mediajunkie:docs/api-orgs-and-keys.md`, a private repo. Billing figures
stay there, not here.

## The rules for Piper Morgan seats

- No seat creates, reads or handles key material. Creating keys and workspaces is xian's.
- A seat that needs a key asks **Exec** (mail), naming the **consumer** (one service or one job) and
  the **environment**. Exec puts it on xian's rollup.
- xian creates it in the org that owns the work (a Piper Morgan key goes in the Piper Morgan org), in
  a workspace named `product-environment` (for example `piper-morgan-prod`), one key per consumer,
  and stores it where the consumer reads it.
- Afterwards someone tells Pard the key's name, org, workspace, consumer and expiry date (never the
  key) so the record stays complete. Exec does this unless the seat already has.
- Budget: stay inside each org's monthly API credit. Some Piper Morgan load runs on keys in the other
  org because it predates the Piper Morgan org; that stays put until xian decides otherwise. Don't
  move or rotate keys to "clean it up".

The naming convention is a draft (xian and Themis have not marked it up yet); the record in
mediajunkie is authoritative if they differ.
