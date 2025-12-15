# GraphQL: The enterprise honeymoon is over

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46264704) | Link: https://johnjames.blog/posts/graphql-the-enterprise-honeymoon-is-over

### TL;DR
An engineer argues that, in typical enterprises already using REST-based backends-for-frontends, GraphQL’s headline benefit—avoiding overfetching—is marginal while costs are large: slower implementation, harder observability and error semantics, fragile caching and ID conventions, awkward file handling, steeper onboarding, and complex auth. HN comments counter that GraphQL’s real strengths are strong typed contracts and UI data composition (especially with Relay-style tooling), yet others report serious authorization and organizational friction, concluding that GraphQL is powerful but best reserved for specific, high-coordination frontends.

---

### Comment pulse
- Pro-GraphQL view: its type system, strict contracts, schema evolution, and fragment colocation/composition drastically reduce UI coupling and bugs—counterpoint: OpenAPI/Protobuf + codegen already give strong contracts.
- Several argue the article misframes GraphQL as “overfetching fix”; they see it as a typed RPC layer plus client-side impedance-mismatch solver, especially when paired with compilers like Relay.
- Others highlight real-world pain: complex authz through nested resolvers, hard-to-evolve schemas at scale, and enterprise customers (e.g., GitHub’s) actively preferring REST over GraphQL.

---

### LLM perspective
- View: Use GraphQL mainly when you have many independently-evolving UI components that must compose data safely and quickly across teams.
- Impact: Most enterprises may gain more by solid REST/BFFs, OpenAPI+codegen, and simple caching than by introducing GraphQL’s operational complexity.
- Watch next: Better Relay-like tooling, auth-focused GraphQL frameworks, and comparisons against tRPC/gRPC for large frontends should guide future adoption.
