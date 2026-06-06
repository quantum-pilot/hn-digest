# Coreutils for Windows

- Score: 193 | [HN](https://news.ycombinator.com/item?id=48372853) | Link: https://github.com/microsoft/coreutils

### TL;DR
Microsoft is shipping a preview “Coreutils for Windows” package: a single multi-call binary bundling Rust-based uutils coreutils, findutils, and grep, installable via WinGet. It aims to let Linux/macOS/WSL users run the same commands and pipelines natively on Windows, but must tiptoe around CMD/PowerShell built-ins, PATH, and aliases, so behavior can vary by shell. The project documents Windows caveats (CRLF, no `/dev/null`, no POSIX signals, ACL-based permissions) and omits strictly POSIX-centric utilities.

---

### Comment pulse
- Windows should adopt LF, `/`, UTF‑8, and POSIX semantics → decades of incompatibilities (CRLF, UTF‑16, path quirks) keep causing friction—counterpoint: ecosystem and backward compatibility make a full switch implausible.  
- Command-name conflicts feel messy → users want predictable resolution; maintainers prioritize not breaking CMD while tolerating some PowerShell overrides with heuristics for DOS vs GNU behavior.  
- Users rely on classic tools (head, tail, tr, uniq, cut) → many are actually included here; broader, up-to-date GNU-style tooling on Windows is still desired.

---

### LLM perspective
- View: A first-party, documented Unix-like toolchain lowers the “Windows is different” tax for developers and automation.  
- Impact: Improves cross-platform scripts, dev onboarding, and basic agent/tooling portability without requiring WSL or Cygwin.  
- Watch next: How they resolve name conflicts, expand command coverage, and integrate with PowerShell profiles and Windows Terminal defaults.
