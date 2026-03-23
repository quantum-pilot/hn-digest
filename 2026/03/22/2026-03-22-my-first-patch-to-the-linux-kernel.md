# My first patch to the Linux kernel

- Score: 209 | [HN](https://news.ycombinator.com/item?id=47444909) | Link: https://pooladkhay.com/posts/first-kernel-patch/

- TL;DR  
  An engineer building a VT-x hypervisor kept crashing Linux when vCPU threads migrated cores. The failures traced to a bad TSS base address in HOST_TR_BASE, coming from Linux’s KVM selftest helper get_desc64_base(). That function left-shifted small integer fields without casting, invoking C’s integer promotions, undefined behavior, and an effective sign extension that corrupted the upper 32 bits. Casting each field to uint64_t before shifting fixed it and produced the author’s first merged kernel patch. HN discusses C UB, signed/unsigned hazards, LLM limits, and kernel-contribution hurdles.

- Comment pulse  
  - LLMs help summarize logs but collapse on novel, multi-step debugging; people skilled at deep low-level reasoning become disproportionately valuable.  
  - Bug isn’t “sign extension in C” but undefined behavior from shifting promoted signed ints; C’s rules around shifts and promotions are treacherous.  
  - Several argue C’s implicit signed/unsigned conversions are a decades-old design mistake that should become compile-time errors—counterpoint: fixing this would break vast legacy code.

- LLM perspective  
  - View: This bug is archetypal UB; compiler sanitizers or formal tools could have surfaced it long before runtime crashes.  
  - Impact: Kernel selftests and hypervisors particularly need aggressive UB checks, since they manipulate CPU descriptors and privileged state directly.  
  - Watch next: Wider use of -fsanitize, static analyzers, and LLMs wired into compilers to propose standards-compliant rewrites, not guesses.
