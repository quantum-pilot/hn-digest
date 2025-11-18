# Compiling Ruby to machine language

- Score: 148 | [HN](https://news.ycombinator.com/item?id=45957629) | Link: https://patshaughnessy.net/2025/11/17/compiling-ruby-to-machine-language

- TL;DR
  - Pat Shaughnessy previews Ruby 3.x JIT internals: YJIT counts method/block entries (30/120-call thresholds, tunable) and compiles hot YARV instruction ranges into “YJIT blocks.” Example: getlocal_WC_1/_0 become ARM64 loads into x1/x9. For opt_plus, YJIT inserts branch stubs, waits for runtime types, then specializes via Basic Block Versioning; ZJIT explores a different strategy. HN recalls MacRuby/LLVM and Apple’s shift to Swift, wishes for VB6-like dev ease, mentions Sorbet, and welcomes the book update plus clarifications from the author.

- Comment pulse
  - MacRuby compiled Ruby via LLVM and bridged Objective‑C; Apple’s Swift shift ended it → commenters miss GUI-friendly speed — counterpoint: Swift tooling improved, ergonomics differ.
  - How are types tracked? YJIT defers, observes runtime types, and specializes block versions (Basic Block Versioning) for int/float/string cases.
  - Related tools: Stripe’s Sorbet compiler noted; multiple readers praise Pat and anticipate the new Ruby Under a Microscope edition.

- LLM perspective
  - View: Clear, step-by-step look at YJIT’s counters, blocks, and branch stubs; bridges VM ops to emitted machine code.
  - Impact: Production Ruby (Rails) gains predictable warmup and type-specialized paths; ops can tune --yjit-call-threshold to balance latency vs. throughput.
  - Watch next: ZJIT’s method-based pipeline and HIR/LIR quality vs YJIT’s BBV; cross-arch codegen parity; polymorphic call-site behavior under load.
