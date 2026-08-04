# Scriptc by Vercel: TypeScript-to-Native compiler, no JavaScript engine in binary

- Score: 268 | [HN](https://news.ycombinator.com/item?id=49063175) | Link: https://github.com/vercel-labs/scriptc

### TL;DR

ScriptC compiles ordinary TypeScript through the real TypeScript checker into native executables, using typed IR and LLVM or C backends instead of bundling Node or V8. It claims roughly 2.4ms startup, 170–200KB static binaries, 1–4MB typical memory use, broad Node and web APIs, and byte-for-byte differential testing against Node across 800-plus programs. Unsupported constructs fail explicitly; an optional QuickJS engine handles npm JavaScript and any-typed code. Commenters see a niche for dependency-light CLI tools but strongly question the week-old, agent-generated codebase’s correctness, scope, and long-term maintenance.

### Comment pulse

- Velocity raises verification concerns → commenters cite roughly 918,000 lines landed in one week and contrast Porffor’s slower progress toward Test262 compatibility.
- npm compatibility reintroduces a runtime → most packages ship JavaScript plus declarations, so projects may need bundled QuickJS — counterpoint: focused CLIs can stay static.
- Maintenance matters more than launch spectacle → skeptics compare prior Vercel experiments that accumulated commits rapidly, then went quiet without demonstrated production adoption.

### LLM perspective

- View: Differential tests establish behavioral evidence, but they cannot substitute for language-coverage metrics, audits, provenance, or sustained issue resolution.
- Impact: Successful compilation could shrink serverless cold starts and CLI distribution, while dynamic dependencies preserve much of JavaScript’s runtime burden.
- Watch next: Track Test262 coverage, reproducible benchmarks, independent security review, real deployments, contributor retention, and whether Vercel uses it internally.
