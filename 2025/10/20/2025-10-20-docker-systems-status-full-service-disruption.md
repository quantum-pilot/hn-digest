# Docker Systems Status: Full Service Disruption

- Score: 323 | [HN](https://news.ycombinator.com/item?id=45640877) | Link: https://www.dockerstatus.com/pages/incident/533c6539221ae15e3f000031/68f5e1c741c825463df7486c

### TL;DR

Docker reported widespread failures across Hub, Registry, authentication, builds, Scout, Testcontainers Cloud, billing, and related SaaS products beginning at 07:16 UTC. It identified an underlying cloud-provider problem, saw error rates recover while processing backlog, and marked the incident resolved at 10:05 UTC. A Docker representative linked the disruption to the concurrent AWS incident and promised a postmortem. Users reported broken builds, especially at the Docker authentication endpoint, and discussed temporary mirrors, private registries, and pull-through caches as ways to reduce dependency on one public registry.

### Comment pulse

- Some builds recovered through AWS or Google mirrors, though commenters reported intermittent failures there too.
- Operators recommended caching or mirroring base images to survive outages, deletions, and rate limits.
- CI systems may hide immutable Docker Hub dependencies inside third-party actions.

### LLM perspective

- View: Public image registries are supply-chain infrastructure, even when teams treat them as incidental build inputs.
- Impact: Authentication failure can halt builds and deployments without affecting already running cached containers.
- Watch next: Docker's promised postmortem and wider adoption of pinned, mirrored, locally cached dependencies.
