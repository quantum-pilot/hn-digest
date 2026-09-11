# Rust is tier-1 language at Microsoft

- Score: 673 | [HN](https://news.ycombinator.com/item?id=49643546) | Link: https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/

### TL;DR

Microsoft says Rust now receives Tier-1 internal engineering support alongside C++, C#, and TypeScript, covering secure toolchains, developer workflows, platform integration, production deployment, and compliance. Its production-ready rustc_codegen_utc backend connects Rust’s compiler to Microsoft’s native UTC/MSVC code-generation ecosystem, supporting Windows ABI compatibility, hardening, diagnostics, servicing, optimization, and hybrid Rust/C++ projects. Microsoft reports more than 100 internal repositories already use it. C++ remains dominant, so the strategy emphasizes shared infrastructure and long-term interoperability rather than immediate replacement.

### Comment pulse

- Rust looks institutionally mature → Microsoft is funding production tooling, not merely experimenting with isolated projects.
- Rewrite expectations drew skepticism → Automated conversion of complex C++ cannot rely on insufficient tests to prove equivalence.
- Scope correction → A billion-line conversion target cited in discussion was one employee’s ambition, not stated Microsoft policy.

### LLM perspective

- View: Tier-1 status matters because organizational support often determines adoption more than language features alone.
- Impact: Windows teams gain a paved memory-safe option while retaining established C++ tooling and mixed-language systems.
- Watch next: Backend availability, repository growth, interoperability quality, debugging parity, and production migration evidence.
