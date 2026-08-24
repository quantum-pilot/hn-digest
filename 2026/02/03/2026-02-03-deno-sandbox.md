# Deno Sandbox

- Score: 291 | [HN](https://news.ycombinator.com/item?id=46874097) | Link: https://deno.com/blog/introducing-deno-sandbox

### TL;DR

Deno Sandbox beta offers sub-second Linux microVMs for running unreviewed, potentially hostile code through JavaScript or Python SDKs. VM egress allowlists block unapproved hosts, while outbound proxies replace secret placeholders only for approved destinations; sandboxes can then deploy directly to Deno Deploy. Ephemeral instances support snapshots and persistent volumes, two regions, 2 vCPUs, 768 MB–4 GB memory, and a 30-minute maximum lifetime, billed by CPU time and memory. Commenters liked the design but noted authorized code can still spend credentials or may expose them through reflective endpoints and reversible transformations.

### Comment pulse

- Placeholder secrets limit permanent theft → malicious code can still consume authorized APIs, so quotas, scope, and per-sandbox accounting remain necessary.
- Host allowlists create policy work → reflected or transformable responses may leak keys — counterpoint: tighter request-aware proxies can inject credentials contextually.
- Product is runtime-neutral → Python and shell workloads work too, while direct Deno deployment, snapshots, volumes, and sub-second boot tighten the agent loop.

### LLM perspective

- View: Deno combines compute isolation with credential and network controls, addressing failures a VM boundary alone cannot contain.
- Impact: Agent platforms gain managed execution and deployment; security teams inherit egress taxonomy, proxy correctness, abuse monitoring, and vendor dependence.
- Watch next: Security audits, TCP secrets, response scrubbing, quotas, regions, lifetime limits, case studies, and competitor comparisons.
