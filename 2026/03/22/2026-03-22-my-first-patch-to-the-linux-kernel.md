# My first patch to the Linux kernel

- Score: 209 | [HN](https://news.ycombinator.com/item?id=47444909) | Link: https://pooladkhay.com/posts/first-kernel-patch/

### TL;DR

While building a Type-2 hypervisor, the author traced multicore crashes to a Linux KVM selftest helper that reconstructed the x86 Task State Segment base incorrectly. An 8-bit field was promoted to signed int before a 24-bit left shift; certain values corrupted upper address bits, giving VM exits an invalid kernel stack and cascading into dead cores or reboots. Casting each component to uint64_t before shifting fixed the calculation, and the patch merged. Commenters praised the debugging but corrected the explanation: standard C classifies the overflowing signed shift as undefined behavior.

### Comment pulse

- Core migration supplied the clue → pinning the hypervisor worked, while more virtual CPUs made the failure reproducible.
- The fix is sound, but the semantics matter → the invalid signed left shift invokes undefined behavior before any later conversion.
- LLMs helped summarize logs but failed at root-cause analysis → the cited assistant blamed hardware after declaring the code bug-free.

### LLM perspective

- **View:** Borrowed kernel code still needs adversarial review when reused outside its original execution paths.
- **Impact:** A tiny integer-expression bug can invalidate privileged CPU state and paralyze an entire multicore system.
- **Watch next:** Compiler diagnostics, sanitizers, backports, nearby descriptor helpers, and tests covering high-bit base fields.
