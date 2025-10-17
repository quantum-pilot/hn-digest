# Upcoming Rust language features for kernel development

- Score: 310 | [HN](https://news.ycombinator.com/item?id=45601982) | Link: https://lwn.net/Articles/1039073/

- TL;DR
  - Rust‑for‑Linux is catalyzing Rust language work. Talks highlighted three kernel‑critical features: generalized field projections (including Pin) to safely project subfields and enable RCU‑friendly APIs; arbitrary self types via an opt‑in Receiver trait so methods can take smart pointers; and in‑place initialization (init keyword, &out references, or guaranteed heap construction). Kernel maintainers prioritize stabilizing features they already use, then structural changes. HN debated Rust’s complexity vs C++, cited Binder/Asahi progress, and discussed heap‑init naming and semantics.

- Comment pulse
  - Rust feels complex → C++ is worse; the lightweight clones RFC may be dropped for ergonomics; tooling like clippy nudges idioms.
  - Kernel Rust is token? → Binder passes AOSP tests; Asahi and others building drivers; upstream focuses on infrastructure first — counterpoint: few in-tree drivers today.
  - Structural pinning decision → projecting Pin<T> to fields now always yields Pin<&mut Field>; unblocks RCU/pin ergonomics debates.

- LLM perspective
  - View: These features shift unsafe boilerplate into compiler-checked primitives; biggest win is RCU-safe access and smart-pointer methods.
  - Impact: Kernel driver ergonomics, fewer bespoke macros; also benefits async/Future heap allocation and non-kernel smart-pointer libraries.
  - Watch next: Stabilization timelines, Crater runs for Receiver; field-projection RFC landing; Debian 14 Rust version; benchmarks of heap-init vs pin_init!.
