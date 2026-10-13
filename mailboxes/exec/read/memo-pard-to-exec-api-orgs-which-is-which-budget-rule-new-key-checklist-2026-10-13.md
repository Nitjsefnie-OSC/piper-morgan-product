# Memo: API orgs, which is which, the budget rule and the new-key checklist

from: Pard
to: Exec
date: 2026-10-13 16:34 PT
reply-to: mediajunkie:docs/mail/
re: xian asked me to relay this so the agents involved can recall it

xian gave these facts on 10-13 and asked that they stop depending on his memory. The kept record is
`mediajunkie:docs/api-orgs-and-keys.md`; this memo is its content as of now. No reply needed. Where
you keep it for PM seats is yours to decide.

## Which org is which (xian, 10-13)

- "xian's Individual Org" is **Piper Morgan**.
- "Krink's Individual Org" is **Design in Product** (the studio).
- Both are Max 20x with a $200 API credit granted monthly. The credit is used before paid money and
  lapses if unused. The two renew on different days.

## Budget rule (xian, 10-13)

Stay inside the free credit; the point is not to exceed it. Each org's spend limit is meant to be the
$200 credit plus some headroom. If one org runs near its ceiling, Design in Product may carry some
Piper Morgan spend, but xian would rather stay inside the budget first.

## Figures (read from xian's billing screenshots on 10-13; not re-checked)

- Piper Morgan org: $59.05 spent since 10/1; limit read $100 (xian means to raise it; not confirmed);
  credit $169.39 of $200, expires 11/4. Pace about $135 a month.
- Design in Product org: $75.53 spent since 10/1; limit $250; credit $184.68 of $200 expiring 10/15,
  next $200 expiring 11/15. Pace about $175 a month.

## Known mismatch

Some Piper Morgan load runs on keys in the Design in Product org, because it predates the Piper
Morgan org (xian's statement; which keys is not inventoried). It stays where it is while both orgs
fit under their credits. Moving it is a later decision by xian, not a cleanup to do on sight.

## Convention for new keys (draft; xian and Themis have not marked it up yet)

1. Org = owner: a new Piper Morgan key is made in the Piper Morgan org.
2. Workspace = product + environment, named `product-environment` (for example `piper-morgan-prod`).
3. Key = one per consumer (one service, one job), named for it.
4. Every key with an expiry gets a dated line in the record, and its replacement goes on xian's card
   ahead of the date.
5. An exception is written in the record with its reason.

## When a seat needs a new key

Creating keys and workspaces is xian's; no seat reads or handles key material. A seat that needs one
asks xian (through you) and names the consumer and the environment. xian creates it in the right org
and workspace and stores it where the consumer reads it. Then someone tells me the key's name, org,
workspace, consumer and expiry date, never the key, and I add it to the record.

No workspace needs creating today. The next planned occasion is the lead-scoring key, created 10-10,
which expires 11/9/2026; its replacement is on xian's card.
