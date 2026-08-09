# Building a CLI for All of Cloudflare

- Score: 235 | [HN](https://news.ycombinator.com/item?id=47753689) | Link: https://blog.cloudflare.com/cf-cli-local-explorer/

### TL;DR

Cloudflare is rebuilding Wrangler into a CLI spanning more than 100 products and nearly 3,000 API operations, with an `npx cf` technical preview. To keep every interface synchronized, it created a TypeScript schema that can generate commands, configuration, bindings, SDK-facing schemas, documentation, and agent tooling while enforcing conventions such as `get`, `--force`, and `--json`. A new Local Explorer beta exposes simulated KV, R2, D1, Durable Objects, and Workflows through the same API shape as remote resources. Commenters prioritized permission diagnostics, short-lived scoped credentials, exact corrective errors, and consistent environment handling.

### Comment pulse

- Developers wanted `cf permissions check` to list missing and unnecessary scopes, ideally creating the correctly scoped key automatically.
- Agent-first CLI design made sense because agents consume commands well — counterpoint: they diagnose failures poorly, making prescriptive error messages essential.
- Security requests favored narrow, short-lived tokens or a proxy that delegates limited host permissions to containers without exposing broad credentials.

### LLM perspective

- **View:** A generated CLI can convert schema consistency into agent reliability, but only if generated semantics receive deliberate human tuning.
- **Impact:** One local-and-remote command surface reduces dashboard dependence, documentation drift, and custom integration work across Cloudflare’s expanding platform.
- **Watch next:** Full API coverage, Wrangler migration, stable naming, permissions tooling, environment interoperability, credential lifetimes, and Local Explorer parity.
