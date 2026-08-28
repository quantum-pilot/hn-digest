# The future of 32-bit support in the kernel

- Score: 263 | [HN](https://news.ycombinator.com/item?id=45095475) | Link: https://lwn.net/SubscriberLink/1035727/4837b0d3dccf1cbb/

### TL;DR

Linux architecture maintainer Arnd Bergmann argues 32-bit systems are obsolete for new products but still needed for existing embedded hardware, especially Arm. He expects armv7 support to remain for at least a decade while older architectures fade sooner. Proposed milestones include dropping high-memory support around 2027 and nommu around 2028, after further discussion. A 32-bit user space on a 64-bit kernel is his preferred compatibility path. Remaining complications include year-2038 bugs, legacy applications, big-endian support, and identifying active hardware users.

### Comment pulse

- Some readers fear losing Linux's role on understandable or salvageable hardware; others say RTOSes, BSDs, and older kernels cover those niches.
- Commenters stressed that most 10–15-year-old PCs are already 64-bit, while legacy binaries remain a user-space compatibility concern.

### LLM perspective

- View: This is gradual maintenance triage, not a single switch ending 32-bit Linux.
- Impact: Removing rarely used paths can simplify memory management while shifting preservation toward stable kernels and compatibility layers.
- Watch next: Concrete users must surface before high-memory, nommu, board-file, and legacy syscall removal deadlines solidify.
