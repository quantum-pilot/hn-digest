# Denial of service and source code exposure in React Server Components

- Score: 340 | [HN](https://news.ycombinator.com/item?id=46236924) | Link: https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components

### TL;DR

React disclosed two DoS CVEs and one source exposure flaw in React Server Components; none bypasses the earlier React2Shell code-execution fix. Crafted requests can trap deserialization in an infinite loop, while a narrower Server Function case can reveal function source and hardcoded secrets, but not runtime environment secrets. Earlier patches were incomplete. Affected users should immediately move to 19.0.3, 19.1.4, or 19.2.3; client-only projects are unaffected. Commenters debated whether the flaws indict RSC architecture or its serializers.

### Comment pulse

- Developers blamed opaque client-server boundaries and sparse documentation for weak mental models, questioning whether RSC benefits justify its operational complexity.
- Defenders said splitting is deterministic and imports are statically guarded — counterpoint: critics viewed repeated serializer flaws as evidence of excessive architectural risk.
- Some objected to React framing follow-up CVEs as normal; others considered that context useful rather than evasive.

### LLM perspective

- View: Immediate patching matters more than the broader architecture debate.
- Impact: Any RSC deployment may face DoS; source exposure additionally requires a stringifying Server Function.
- Watch next: Further serializer audits, framework backports, production bundle checks, and clearer RSC security documentation.
