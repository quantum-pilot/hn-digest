# Launch HN: Airweave (YC X25) – Let agents search any app

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45427482) | Link: https://github.com/airweave-ai/airweave

- TL;DR
    - Airweave is an open-source platform that turns SaaS apps, databases, and docs into a single, semantically searchable layer for AI agents via REST or MCP. It syncs data from 25+ connectors, extracts entities, embeds into Qdrant, and exposes per-tenant search with OAuth2; SDKs provided, self-hosted or managed. HN focused on RBAC: founders worry about leakage from “public but unindexed” links and shared docs. Airweave indexes everything but isolates via per-user syncs; unified ACL dedupe is planned. It currently avoids runtime tool-calls.

- Comment pulse
    - Permissioning and RBAC are hard → app models differ, ACL mapping breaks; teams want partitions, confidentiality inference — counterpoint: per-user syncs reduce leakage, raise cost.
    - Index-everything vs tool-calling → Airweave embeds all sources for low-latency, unified semantics; skeptics prefer passthrough credentials to avoid leaks.
    - Connector coverage and quality → prioritized by user demand; private e2e tests maintain fidelity. Onyx founder notes Drive service-account permissions; Cursor integration praised.

- LLM perspective
    - View: Agents need robust, permission-aware knowledge layers; per-user indexing is pragmatic but costly and duplicative.
    - Impact: Startups can ship agent features faster; enterprises will demand provable ACL parity, audit logs, and on-prem deployment.
    - Watch next: Benchmarks on permission-respecting recall/latency, unified ACL sync rollout, connector roadmap, privacy reviews, and cost per-seat vs per-GB.
