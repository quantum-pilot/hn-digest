# Why Twilio Segment moved from microservices back to a monolith

- Score: 115 | [HN](https://news.ycombinator.com/item?id=46257714) | Link: https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices

### TL;DR

Segment split its destination queue into services and repositories to isolate partner outages and tests. Past 140 integrations, library versions diverged, autoscaling became bespoke, three engineers mostly maintained the system, and every destination added overhead. The team consolidated code into one repository and service, used Centrifuge for delivery, and recorded HTTP fixtures, shrinking hour-long tests to milliseconds. Deployments accelerated, but fault isolation and cache efficiency worsened, while dependency changes gained wider blast radius. HN said the deeper lesson concerns tooling, coupling, and organizational discipline, not a universal architecture choice.

### Comment pulse

- Some called the fleet a distributed monolith because shared libraries forced coordinated upgrades — counterpoint: security fixes and communication contracts couple separate services too.
- Monorepos and microservices are independent choices; one team used Bazel dependency queries to test affected targets while deploying services separately.
- Readers blamed flaky integration tests, weak autoscaling, and ownership structure as much as topology, while practitioners reported success with both extremes.

### LLM perspective

- View: Service boundaries help when components differ in lifecycle and ownership; repeated global changes expose boundaries drawn too finely.
- Impact: Consolidation shifts cost from operations and coordination toward larger blast radius, shared scaling, and stricter test discipline.
- Watch next: Destination crash containment, cache hit rates, Centrifuge behavior, build growth, dependency upgrades, and team velocity.
