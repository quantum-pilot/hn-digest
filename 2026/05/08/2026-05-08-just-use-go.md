# Just Use Go

- Score: 182 | [HN](https://news.ycombinator.com/item?id=48062997) | Link: https://blainsmith.com/articles/just-fucking-use-go/

- TL;DR  
  Article is a profanity-laced plea to stop over-engineering backends and “just use Go.” It celebrates Go’s intentionally boring design, powerful standard library-as-framework, cheap goroutines, built-in tooling (fmt/vet/test/pprof), simple dependency management, static self-contained binaries, and VPS-friendly monolith deployments instead of microservices. Explicit `if err != nil` error handling is defended as clarity, not boilerplate. HN discussion mostly agrees Go is practical and robust, but criticizes its ergonomics, null handling, missing enums, and now-less-unique deployment advantages versus Rust, .NET, and Java.

- Comment pulse  
  - Go-style explicit errors feel noisy to some; fans argue they aid static analysis and clarity, and that long functions, not checks, are the real smell.  
  - Supporters liken Go to a minivan: unexciting but dependable for backends—yet gripe about null handling, missing enums, and “bonkers” repetitive error boilerplate.  
  - Skeptics say single static binaries are no longer unique; Rust, .NET, and Java offer similar deployment with better performance, type systems, and richer web ecosystems.

- LLM perspective  
  - View: Go stays compelling for small-to-medium backend services where simplicity, fast builds, and low-ceremony deployment outweigh language elegance.  
  - Impact: Teams without strong ops or language specialists can ship safer monoliths instead of chasing complex microservice or JS-heavy stacks.  
  - Watch next: whether Go adds ergonomics (enums, better nil tools) without losing simplicity, and how it competes with Rust/.NET backends.
