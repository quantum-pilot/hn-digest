# GraphQL: The enterprise honeymoon is over

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46264704) | Link: https://johnjames.blog/posts/graphql-the-enterprise-honeymoon-is-over

### TL;DR

After running Apollo GraphQL in a multi-team enterprise application, the author argues it often adds more schema, resolver, cache, error, observability, identity, file-transfer, and onboarding complexity than its benefits justify. Existing backends-for-frontends can shape REST data, while downstream REST services still overfetch. Commenters disputed the premise that field selection is GraphQL’s primary value, emphasizing typed contracts, schema evolution, federation, and colocated component fragments. Several agreed those strengths depend heavily on Relay-like compilers and mature tooling that many Apollo deployments lack.

### Comment pulse

- Advocates said fragments colocate data requirements with UI components, enabling composition and safer changes across large teams.
- Critics noted OpenAPI, Protobuf, and runtime validators provide strong contracts without GraphQL’s nested authorization and partial-error semantics.
- Experienced users separated GraphQL from Apollo Client, arguing ecosystem choices can obscure the protocol’s intended development model.

### LLM perspective

- View: The case indicts a BFF-plus-Apollo architecture more convincingly than GraphQL across every deployment model.
- Impact: Teams choosing it for overfetching alone may inherit complexity without exploiting composition, evolution, or federation.
- Watch next: Compare representative changes across REST and GraphQL using delivery time, incidents, authorization effort, and client coupling.
