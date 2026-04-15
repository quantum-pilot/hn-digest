# Lean proved this program correct; then I found a bug

- Score: 376 | [HN](https://news.ycombinator.com/item?id=47759709) | Link: https://kirancodes.me/posts/log-who-watches-the-watchers.html

### TL;DR
A Lean-verified DEFLATE/zlib implementation (`lean-zip`) was fuzzed by a Claude-driven setup with AFL++, sanitizers, and custom exploits. The core *verified* compression/decompression pipeline showed no memory-safety issues across ~106M executions, but fuzzing uncovered (1) a heap buffer overflow in Lean 4’s C++ runtime array allocator, reachable via unvalidated read sizes, and (2) an out-of-memory denial-of-service in an *unverified* ZIP archive parser. The episode underlines that formal proofs only cover what’s specified, and that runtimes/specs remain critical parts of the trusted base.

---

### Comment pulse
- Title is misleading → bugs were in Lean runtime and unverified parser, not the proved core or kernel — counterpoint: users care about the whole binary’s behavior.  
- Spec gaps are central → you can fully prove code meets a flawed or incomplete specification, so “verified” can still diverge from human intent.  
- Desired next step → machine-checkable “operating envelopes” and runtime guards so systems can detect when execution leaves the domain that the proofs actually cover.

---

### LLM perspective
- View: Combine proof assistants with AI-guided fuzzing to repeatedly probe the borders of verified components and their trusted runtimes.  
- Impact: Runtime/VM authors, spec writers, and security teams must treat runtimes and parsers as first-class verification targets, not afterthoughts.  
- Watch next: Verified runtimes, auto-derived proof domains/assumptions, and tools that fuzz both implementations and their specifications for missing constraints.
