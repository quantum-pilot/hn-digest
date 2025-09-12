# Protobuffers Are Wrong (2018)

- Score: 243 | [HN](https://news.ycombinator.com/item?id=45139656) | Link: https://reasonablypolymorphic.com/blog/protos-are-wrong/

TL;DR
The essay argues Protocol Buffers are an ad‑hoc, non-compositional schema language whose type system and presence semantics leak into application code. Defaulted scalars and pseudo‑optional message fields obscure unset vs. set‑to‑default; oneof desugars into fragile mutually exclusive fields, breaking algebraic guarantees and complicating generic transforms. “Compatibility” is reframed as permissiveness that decentralizes validation and optimizes for Google’s scale. HN counters that protobuf’s backward‑compat guarantees and linters enable rolling deploys; time‑compat constraints drive trade‑offs; unknown‑field preservation is valuable in systems like Chrome Sync.

Comment pulse
- Backwards‑compat + linters enable rolling upgrades across mixed versions → fewer deploy constraints — counterpoint: permissive defaults mask bugs and push validation throughout the codebase.
- Design space constrained by cross‑version compatibility; many limitations resolved by wrapping types in messages → awkward but workable ergonomics.
- Unknown‑field preservation matters in practice → cited as essential to Chrome Sync; some teams even forked protobuf to guarantee it.

LLM perspective
- View: Separate domain models from wire schemas; generate adapters to avoid leaking proto semantics into business logic.
- Impact: Pick tech by constraints: rolling deploys and small payloads → protobuf; strong algebraic types → alternatives with explicit presence.
- Watch next: Track proto3 presence/optional improvements, better schema‑diff linters, and competing DSLs (ASN.1, Cap’n Proto, Typical) with real compositional unions/maps.
