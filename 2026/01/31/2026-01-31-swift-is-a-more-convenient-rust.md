# Swift is a more convenient Rust

- Score: 127 | [HN](https://news.ycombinator.com/item?id=46841374) | Link: https://nmn.sh/blog/2023-10-02-swift-is-the-more-convenient-rust

### TL;DR
The article argues Swift and Rust share core ideas—value semantics, enums with pattern matching, option types, error handling without exceptions, LLVM backends—but differ in defaults and positioning: Rust is “bottom‑up” systems-first and fast by default, while Swift is “top‑down,” hiding similar concepts behind familiar C-style syntax and prioritizing convenience, especially for app/UI work. HN commenters broadly accept the high-level comparison but point out factual errors, weak cross‑platform reality, and significantly worse tooling and ergonomics versus Rust today.

---

### Comment pulse
- Swift ergonomics/tooling lag Rust → Xcode/SwiftPM scaling issues, slow type inference, performance cliffs, weaker lints/macros; Cargo and Rust tooling feel more reliable — counterpoint: some find Xcode excellent overall.  
- Several technical claims are wrong → Rust didn’t “invent” ownership; example with `Box` in recursive enums is unnecessary/incorrect, undermining trust in the comparison.  
- Cross‑platform Swift is immature → ecosystem, docs, and DX remain Apple‑centric; Linux/Windows stories feel weak compared with Rust or Go.

---

### LLM perspective
- View: Treat Swift as a pragmatic, Apple-first high-level language that borrows Rust-ish safety, not a true Rust substitute.  
- Impact: Systems, infra, and CLI work still favor Rust; Swift shines for Apple platforms and some shared UI/server code.  
- Watch next: Swift on Android/embedded, SwiftPM and tooling on Linux/Windows, and Rust’s ergonomics improvements competing for “convenient but safe” territory.
