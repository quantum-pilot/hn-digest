# Just Use Go

- Score: 182 | [HN](https://news.ycombinator.com/item?id=48062997) | Link: https://blainsmith.com/articles/just-fucking-use-go/

### TL;DR

The essay urges backend teams to choose Go’s deliberate simplicity over framework-heavy stacks: a small language, capable standard library, cheap goroutines, built-in formatting, testing and profiling, reproducible modules, embedded assets, and single-binary deployment can cover ordinary web services without Kubernetes or microservices. Explicit errors and monoliths are presented as disciplines, not shortcomings. HN broadly accepted Go as a reliable “minivan,” but rejected universalism: repetitive error blocks, weak nil and enum handling, and thinner application libraries remain real costs, while Rust, .NET, and JVM native tooling now offer similar deployment advantages.

### Comment pulse

- Explicit error values reveal control paths → counterpoint: repetitive blocks create visual noise that can hide the one exceptional case.
- Go shines when its standard library fits → production migrations and richer domain modeling may favor .NET or other ecosystems.
- Static binaries, fast builds, embedded resources, and simple tooling remain compelling → competing runtimes have narrowed, not erased, that operational lead.

### LLM perspective

- **View:** “Boring” succeeds when problem fit matters more than language expressiveness or ecosystem breadth.
- **Impact:** Small teams can reduce build and deployment surface, but may reimplement missing higher-level facilities.
- **Watch next:** Compare service maintenance costs, failures, memory, reproducibility, and onboarding—not syntax alone.
