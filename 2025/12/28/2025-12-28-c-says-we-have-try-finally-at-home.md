# C++ says “We have try. . . finally at home”

- Score: 107 | [HN](https://news.ycombinator.com/item?id=46408984) | Link: https://devblogs.microsoft.com/oldnewthing/20251222-00/?p=111890

### TL;DR

Chen explains that C++ lacks a `try { … } finally { … }` construct, but achieves similar behavior via RAII: putting cleanup in destructors or utilities like `wil::scope_exit`, which run when scope exits. However, semantics diverge when cleanup code itself throws: Java/C#/JS/Python replace the original exception (Python retains it as context), while C++ calls `std::terminate` if a destructor throws during stack unwinding. HN discussion branches into RAII vs `finally`, error-reporting from destructors, C++ readability, and “defer”-style alternatives.

---

### Comment pulse

- RAII is “try/finally at home” → idiomatic C++ uses destructors for cleanup; complaints often come from forcing other-language patterns onto C++.

- Destructors vs `finally` → RAII centralizes cleanup, but destructors can’t safely signal failures like file-close errors—counterpoint: that’s exactly why `finally`-style code is still useful.

- Alternatives and ergonomics → libraries (absl::Cleanup, Rust DropGuard) and language features (Swift/Go `defer`, C++ macros) provide inline scope-exit hooks without new keywords.

---

### LLM perspective

- View: Treat RAII as mandatory in C++, reserving `finally`-like helpers for non-resource logic or complex multi-step invariants.

- Impact: Library authors, not end-users, should encapsulate tricky destructor/exception behavior behind safe, well-documented scope guards.

- Watch next: Better diagnostics and guidelines for destructor exceptions; possible standardized `defer`/scope-guard patterns in future C++ revisions.
