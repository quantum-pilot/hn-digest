# What functional programmers get wrong about systems

- Score: 187 | [HN](https://news.ycombinator.com/item?id=46953491) | Link: https://www.iankduncan.com/engineering/2026-02-09-what-functional-programmers-get-wrong-about-systems/

### TL;DR

An experienced Haskell developer argues that production correctness belongs to the set of concurrently deployed versions, not any single well-typed program. Rolling releases, irreversible schema changes, retained messages, event logs, and semantic drift create compatibility obligations beyond a type checker’s scope. Proposed defenses include expand-and-contract migrations, version-aware codecs, schema registries, compatibility checks, runtime deployment inventories, temporal databases, and content-addressed code, while acknowledging each limit. Commenters agreed cross-version systems need explicit reasoning, but objected that the essay understates functional programming’s local benefits and targets a familiar distributed-systems problem.

### Comment pulse

- Discussion fixated on suspected AI authorship and low information density—counterpoint: the author cited old drafts, parental leave, and human revisions.
- Practitioners argued FP still removes many local failures; system-level gaps add obligations rather than negate types, purity, sum types, or checked errors.
- Several recommended model checking, especially TLA+, for global properties, though adoption and schema identifiers remain practical stumbling blocks.

### LLM perspective

- View: The strongest thesis is additive: local proof and deployment compatibility are distinct layers, and production systems need both.
- Impact: Teams can turn temporal compatibility from tribal knowledge into CI checks and explicit retention, migration, and rollout policy.
- Watch next: Tooling that unifies running-version inventory, schema registries, database migrations, queue retention, semantic contracts, and model checking.
