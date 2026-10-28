# Call classifier

Two questions per call: is it a sales call, and if so, which type. Answer both from the conversation, not the calendar title.

"You" below means the person whose calls are being coached.

## Question 1: sales or not

### Tag `sales` when you see

- Price or budget mentioned by either side
- Scope or deliverables being defined ("we'd need this for our 12 people")
- A timeline or start date being discussed
- Decision criteria asked or stated ("how do you compare to X")
- Other people on their side being named ("I'd need to bring our COO to the next call")
- You qualifying intent ("what made you book this call", "what would success look like")
- An inbound prospect describing their pain in the first 5 minutes without being asked
- Any of your offers (from your context) discussed as something they might buy

### Tag `client_delivery` when

- The other side already pays you (an active client, customer or student)
- The call is about doing the work: kickoff, working session, support, check-in, recap

### Tag `peer_or_network` when

- Both sides are operators or founders swapping notes, with no buying intent on either side
- Podcast or interview conversations
- A friendly intro from a mutual contact with no specific ask

### Tag `internal` when

- Everyone is on your own domain, or you are on with a single trusted collaborator
- (Rare, since step 1 already filters for at least one outside attendee)

### Tag `unclear` when

- The summary and the first 5 minutes don't give a confident read
- The call mixed delivery for an existing client with a new sale (possible: an upsell)

Default to `unclear` rather than guessing. You will correct it, and the correction can be added here.

## Question 2: which type of sales call

Only when Question 1 = `sales`.

### `discovery`

The first real conversation about a problem. You ask, they describe. No price or scope yet. Goal: understand the pain and decide if there's a fit.

### `intro_inbound`

A 15 to 30 minute call from someone who found you (content, referral, website). Often vague ("we want to grow faster"). Half discovery, half qualification. Different from discovery because they often haven't formed the problem yet.

### `scoping`

They're in. Now you define together what the work looks like. Often several people from their side, more structured, longer (45 to 90 minutes).

### `demo_or_pitch`

You're showing your product, plan or approach. A walkthrough, a demo, a sample session. Talk ratio flips: you talk more than they do.

### `proposal_or_close`

The price is on the table. The talk is about decision process, contract, start date, who signs.

### `objection_or_negotiation`

Late stage. Pushback on price, scope or timing, or a competing vendor.

### `follow_up`

Anything after an earlier call in the same deal that doesn't fit above. Usually short. Goal: keep momentum or unblock.

## How the type is used

The type picks the framework in `frameworks.md` and sets the talk ratio target in `coaching-rubric.md`. Discovery and intro calls expect you to listen more. Demo and pitch calls expect you to talk more.

If a call shifts type midway (common: an intro that turns into scoping in the last 10 minutes), tag the main mode and call out the shift in the coaching.
