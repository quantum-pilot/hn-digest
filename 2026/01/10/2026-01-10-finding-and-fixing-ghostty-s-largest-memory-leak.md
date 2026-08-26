# Finding and fixing Ghostty's largest memory leak

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46568794) | Link: https://mitchellh.com/writing/ghostty-memory-leak-fix

### TL;DR

Ghostty’s largest known leak reached 37 GB after ten days because scrollback pruning reused oversized mmap-backed pages while resetting only their recorded size. Later cleanup misclassified those allocations as standard pooled pages and skipped munmap. Claude Code’s multi-codepoint graphemes and heavy primary-screen scrollback triggered the old bug at scale, but did not cause it. The merged fix destroys non-standard pages instead of recycling them, adds regression coverage and macOS VM tags, and ships in nightlies before version 1.3. HN praises the diagnosis while questioning release timing and reuse policy.

### Comment pulse

- Conservative fix → preserving the standard-page assumption avoids mixing a worldview change with urgent leak repair.
- Release cadence → users expected a patch release for severe memory growth, though nightlies already contain the fix.
- Reproductions matter → Claude Code amplified the pattern, but other Unicode-heavy terminal workloads produced similar failures.

### LLM perspective

- View: Metadata describing resource ownership is dangerous when it can diverge from the underlying allocation.
- Impact: Terminal developers should test rare allocation classes under realistic, high-volume scrollback workloads.
- Watch next: Version 1.3 adoption, memory plateaus, non-Claude reproductions, and benchmarks for oversized-page reuse.
