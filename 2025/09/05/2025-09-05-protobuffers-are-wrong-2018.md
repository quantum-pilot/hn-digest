# Protobuffers Are Wrong (2018)

- Score: 243 | [HN](https://news.ycombinator.com/item?id=45139656) | Link: https://reasonablypolymorphic.com/blog/protos-are-wrong/

### TL;DR

This 2018 polemic argues Protocol Buffers have an ad hoc, non-composable type system: special rules constrain maps, repeated fields, `oneof`, and presence, while default values can erase the distinction between absent and explicitly set data. It says permissive compatibility shifts validation throughout applications and generated wire types contaminate domain code. Commenters accept many ergonomic flaws but contest the conclusion, emphasizing rolling deployments, schema evolution, linters, unknown-field preservation, and real systems such as Chrome Sync where those compatibility properties are valuable.

### Comment pulse

- Defenders say wrappers handle several cited restrictions, though at the cost of additional schema ceremony.
- Alternatives mentioned include Typical, ASN.1, versioned migrations, and JSON schemas with explicit cross-release tests.

### LLM perspective

- View: The critique exposes type-design costs, but understates how compatibility across independently deployed versions constrains cleaner abstractions.
- Impact: Protobuf trades local elegance for operational evolution; whether that pays depends on deployment topology and domain-model separation.
- Watch next: Presence semantics, compatibility tests, unknown-field behavior, generated-code boundaries, and whether a simpler format meets actual rollout needs.
