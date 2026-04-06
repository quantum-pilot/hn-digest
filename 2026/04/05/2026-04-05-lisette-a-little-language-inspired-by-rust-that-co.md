# Lisette a little language inspired by Rust that compiles to Go

- Score: 252 | [HN](https://news.ycombinator.com/item?id=47646843) | Link: https://lisette.run/

### TL;DR
Lisette is a Rust-inspired, expression-oriented language that compiles to Go, aiming to bring algebraic data types, pattern matching, Hindley–Milner type inference, and “no nil” safety to the Go ecosystem. It interoperates directly with Go packages, compiles to readable Go, and offers strong compile-time checks with high-quality diagnostics. HN commenters like the design, error messages, and choice of Go as a backend, but question semantic mismatches with Go APIs, real-world adoption paths, and why not just use Rust or Go directly.

---

### Comment pulse
- Best fit: teams tied to Go’s runtime/GC and ecosystem wanting stronger types and ergonomics — counterpoint: if greenfield, many would rather choose Rust.
- Go backend is attractive (small core, GC, goroutines), but (T, error) vs Result<T, E> and typed nil semantics require careful, sometimes awkward mapping.
- Some want syntax to match Rust exactly; others argue minor syntactic drift is fine since the real value is Rust-like types on Go.

---

### LLM perspective
- View: Lisette’s niche is “modern type system for Go shops,” not “Rust replacement,” especially for large existing Go deployments.
- Impact: Could normalize ADTs, exhaustive matching, and nil-less APIs in Go-heavy backends and tooling, influencing future Go design discussions.
- Watch next: Robust Go interop (both directions), debug tooling, performance benchmarks, and guidance for incrementally adding Lisette to mixed codebases.
