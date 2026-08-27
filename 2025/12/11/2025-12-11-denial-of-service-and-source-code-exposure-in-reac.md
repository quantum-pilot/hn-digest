# Denial of service and source code exposure in React Server Components

- Score: 340 | [HN](https://news.ycombinator.com/item?id=46236924) | Link: https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components

### TL;DR

React disclosed two follow-up Server Components flaws: high-severity denial of service through a crafted request causing an infinite deserialization loop, and medium-severity exposure of Server Function source under specific stringification conditions. Neither enables remote code execution, and runtime environment secrets are not exposed, though hardcoded secrets inside affected functions may be. Earlier fixes were incomplete; users of vulnerable React Server DOM packages must upgrade to 19.0.3, 19.1.4, or 19.2.3 rather than relying on hosting mitigations. Client-only React applications are unaffected.

### Comment pulse

- Critics see opaque client-server boundaries and deep serialization as unjustified complexity that enlarges the security surface.
- A technical counterpoint says splitting is deterministic; these flaws arise from JavaScript dynamism inside a bounded serializer.

### LLM perspective

- View: The repeated patching exposes a protocol-hardening problem more directly than a failure of server rendering itself.
- Impact: Teams must inventory transitive RSC packages and verify deployed versions, even after completing last week’s emergency update.
- Watch next: Further serializer variants, production-bundle leak tests, and clearer framework documentation of affected dependency paths.
