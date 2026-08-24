# GraphQL: The enterprise honeymoon is over

- Score: 159 | [HN](https://news.ycombinator.com/item?id=46264704) | Link: https://johnjames.blog/posts/graphql-the-enterprise-honeymoon-is-over

### TL;DR

After several years using Apollo Client and Server in a multi-team enterprise application, John James argues GraphQL is often a net cost when a Backend for Frontend already shapes REST data. Downstream overfetching remains, while schemas, resolvers, synchronization, cache behavior, identifier conventions, binary transfers, onboarding, authorization, and partial-error semantics add work. HTTP 200 responses containing execution errors also complicate default observability. James still sees valid niches, including pages needing different field subsets, but concludes reliability and delivery speed usually outweigh saving a few fields.

### Comment pulse

- Critics said the article understates GraphQL’s strongest benefits: typed contracts, schema evolution, resolver composition, federation, and component-colocated data requirements.
- Others replied that OpenAPI, Protocol Buffers, or runtime schemas can provide contracts without GraphQL’s operational and cognitive overhead.
- Practitioners agreed nested authorization and ecosystem complexity can be costly — counterpoint: Relay-style fragment masking makes large UI composition substantially easier.

### LLM perspective

- View: The disagreement is partly architectural: GraphQL’s value rises when clients exploit composition, not merely field pruning.
- Impact: Teams choosing Apollo without colocated fragments may absorb GraphQL’s costs while missing its strongest workflow benefit.
- Watch next: Comparative production evidence on authorization, schema evolution, observability, and Relay-style component composition.
