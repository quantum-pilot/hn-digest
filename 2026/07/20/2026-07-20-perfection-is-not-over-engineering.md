# Perfection is not over-engineering

- Score: 184 | [HN](https://news.ycombinator.com/item?id=48979120) | Link: https://var0.xyz/posts/perfection-is-not-over-engineering.html

### TL;DR

The essay separates perfection from excess: perfection is the solution that uniquely fits explicit technical and product constraints, while over-engineering solves requirements users never had. Treating libraries, APIs, and internal systems as products should expose those needs; a three-person team splitting one domain into five microservices illustrates paying consistency and operational costs for hypothetical scaling. HN agreed quality is too often dismissed but challenged the definitions: deliberate partial coverage, changing requirements, edge-case costs, adaptability, and unnecessary complexity make “perfect” contingent rather than singular.

### Comment pulse

- Scope can be intentionally incomplete → a 90th-percentile solution may be correct when rare cases are excluded — counterpoint: operators inherit failures and later toil.
- Perfection can harm adaptability → requirements and user behavior change, so robust performance across scenarios may beat one configuration’s optimum.
- Vocabulary remains unsettled → commenters distinguished overbuilt capacity, unjustified complexity, and overcomplication, all reflecting costs beyond the actual requirement.

### LLM perspective

- **View:** A design is only optimal relative to a requirement model; uncertainty, reversibility, and learning speed belong inside that model.
- **Impact:** Teams should document edge cases, operational owners, revisit triggers, and evidence supporting architecture before invoking simplicity or perfection.
- **Watch next:** Compare total lifecycle cost across monolith and microservice designs, including incident load, migration effort, and requirements volatility.
