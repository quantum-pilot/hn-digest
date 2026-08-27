# The compiler is your best friend

- Score: 127 | [HN](https://news.ycombinator.com/item?id=46445131) | Link: https://blog.daniel-beskin.com/2025-12-22-the-compiler-is-your-best-friend-stop-lying-to-it

### TL;DR

The essay argues that nulls, unchecked exceptions, casts, and hidden side effects “lie” to compilers by concealing runtime possibilities. Replacing them with Option and Result types, exhaustive unions, domain-specific wrappers, validated types, and a functional core lets compilation errors expose affected code paths and design flaws before production. HN readers broadly favored explicit types but disputed absolutism: unrecoverable states may still justify crashing, pure-core boundaries become difficult around stateful workflows, and an incorrect or overly elaborate model can make every change a fight.

### Comment pulse

- Explicit Result and union types reveal failure paths → unlike unchecked exceptions, signatures force callers to acknowledge them.
- Functional cores improve testing and auditability → real workflows may require deferred effects, snapshots, and transactional coordination.
- Strong typing depends on faithful models → complex domains can turn compiler guidance into friction and unsafe workarounds.

### LLM perspective

- View: Types work best as executable design constraints, not as a claim that runtime failure disappears.
- Impact: Teams trade earlier modeling effort for safer refactors and fewer silently propagated assumptions.
- Watch next: Evaluate defect rates and change costs, not type sophistication alone.
