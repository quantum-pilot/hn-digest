# We found a bug in Go's ARM64 compiler

- Score: 674 | [HN](https://news.ycombinator.com/item?id=45516000) | Link: https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/

### TL;DR

Cloudflare traced rare Go crashes on ARM64 to asynchronous preemption occurring between two instructions that partially adjusted the stack pointer for large frames. Garbage collection then unwound a temporarily inconsistent stack and interpreted unrelated data as a parent frame, causing fatal errors or segmentation faults. Production scale, core dumps, a shared Netlink call site, and a standard-library reproducer narrowed the fault to compiler-generated epilogues. Fixed Go releases construct the offset in a temporary register, then update the stack pointer with one indivisible instruction.

### Comment pulse

- Commenters praised the debugging narrative and noted how rarely engineers can justify suspecting the compiler.
- Technical discussion considered assembler-level safeguards, safe points, and alternative single-update instruction sequences.

### LLM perspective

- View: The breakthrough came from treating scale-generated rarity as evidence and reducing it to one unsafe instruction boundary.
- Impact: One-instruction runtime races can survive ordinary testing yet become routine across sufficiently large fleets.
- Watch next: Similar multi-instruction stack-pointer transformations deserve auditing beyond the specific compiler path that was patched.
