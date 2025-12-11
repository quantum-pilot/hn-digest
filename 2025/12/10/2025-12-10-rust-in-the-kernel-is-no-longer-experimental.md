# Rust in the kernel is no longer experimental

- Score: 920 | [HN](https://news.ycombinator.com/item?id=46213585) | Link: https://lwn.net/Articles/1049831/

### TL;DR
Linux kernel maintainers agreed at the 2025 Maintainers Summit that Rust is now a core, permanent part of the kernel rather than an experiment. The “experimental” tag will be removed, signaling that Rust driver code can be relied on long‑term, even though core kernel infrastructure and the syscall ABI remain C-based. Commenters discuss which distros already ship kernels with Rust enabled, architecture and GCC support gaps, and how far maintainers must go to avoid breaking Rust code.

---

### Comment pulse
- Rust driver support is now mature enough for real modules with little boilerplate; some distros already ship kernels with CONFIG_RUST and Rust-based features enabled.  
- Rust is now “here to stay” symbolically; kernel policy still only stabilizes user‑space ABI — counterpoint: some assume this promises stronger Rust API stability.  
- Architectures lacking usable Rust toolchains aren’t dropped; Rust currently targets drivers on supported arches, while core kernel remains C until broader compiler/arch coverage exists.  

---

### LLM perspective
- View: This milestone mainly affects social trust: kernel people now treat Rust as a normal option, not a risky experiment.  
- Impact: Driver authors gain confidence to invest in Rust infrastructure, abstractions, and training, expecting their code to live across many kernel releases.  
- Watch next: Watch for more subsystems accepting Rust, additional architectures/toolchains (e.g., GCC Rust) landing, and clearer documentation of Rust-specific kernel stability expectations.
