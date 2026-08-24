# Rust in the kernel is no longer experimental

- Score: 920 | [HN](https://news.ycombinator.com/item?id=46213585) | Link: https://lwn.net/Articles/1049831/

### TL;DR

Linux kernel maintainers agreed to remove Rust’s experimental label, signaling that the language is a permanent supported option for kernel development. The decision does not mean a Rust rewrite, stable internal APIs, or abandonment of architectures without Rust toolchains; today it mainly strengthens the path for new drivers and components. Commenters welcomed the milestone and noted some distributions already enable Rust, but highlighted continuing integration work when C-side interfaces change and concern about concentrated maintainer responsibility around Miguel Ojeda.

### Comment pulse

- Distribution support is already tangible → some kernels ship Rust enabled without exposing a new userspace contract.
- Core integration stays asymmetric → Rust bindings absorb C subsystem churn, and unsupported architectures still constrain shared code.
- Maintainer bandwidth worries readers → institutional commitment needs more than one clearly recognized lead.

### LLM perspective

- View: This is a governance milestone, not a rewrite mandate.
- Impact: Driver authors can treat Rust as durable infrastructure.
- Watch next: Additional maintainers, architecture coverage and upstream Rust drivers.
