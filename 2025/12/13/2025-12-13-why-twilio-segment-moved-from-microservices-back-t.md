# Why Twilio Segment moved from microservices back to a monolith

- Score: 115 | [HN](https://news.ycombinator.com/item?id=46257714) | Link: https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices

### TL;DR

Segment’s destination pipeline grew beyond 140 services, repositories, and queues, turning shared-library upgrades, dependency drift, autoscaling, tests, and on-call work into a linear operational burden. It consolidated destinations into one service and monorepo, introduced Centrifuge for queueing, and recorded external HTTP interactions so the full test suite ran in milliseconds. Shared-library improvements increased from 32 to 46 year-over-year, but fault isolation and caching worsened. Commenters disputed whether microservices or deficient tooling and organization caused the original pain.

### Comment pulse

- Shared libraries revealed coupling → commenters debated whether this made the fleet a distributed monolith or merely reflected unavoidable dependencies.
- Architecture labels obscure organizational fit → tightly connected domains favor global changes, while independent lifecycles can favor services.
- Monorepos need not imply monoliths → build graphs can test affected services independently, albeit with substantial tooling investment.

### LLM perspective

- View: The successful change aligned deployment boundaries with a small team’s actual coordination boundary.
- Impact: Fewer units reduced operational toil while concentrating blast radius and cache inefficiency.
- Watch next: Measure incident severity, deployment frequency, Centrifuge behavior, and isolation mechanisms after consolidation.
