# GhostLock, a stack-UAF that has existed in all Linux distributions for 15 years

- Score: 391 | [HN](https://news.ycombinator.com/item?id=48834309) | Link: https://nebusec.ai/research/ionstack-part-2/

- TL;DR  
  GhostLock is a Linux kernel stack use-after-free present for ~15 years, affecting mainstream distros and Android. It enables powerful local privilege escalation from sandboxes, and researchers chained it with a Firefox IonMonkey JIT bug to achieve web-to-root on Pixel devices. The public PoC requires per-kernel tuning and often just crashes or boot-loops phones; a fully turnkey LPE script was withheld. Many systems, especially rarely-updated Android devices, will remain vulnerable. Containerization and SELinux don’t help once the kernel falls.  

  *Content unavailable; summarizing from title and comments.*

- Comment pulse  
  - PoC instability on devices → Testers report boot loops, freezes, and hung kernels on various Android versions (including Samsung flagships) due to highly layout-dependent stack targeting.  
  - Severity debate → Some dismiss it as “just LPE”; others note it undermines browser/container sandbox assumptions, effectively reducing required exploit chains to two bugs.  
  - Hard to weaponize everywhere → Enterprise distros and non-Pixel phones need careful per-kernel porting; some hope to repurpose the technique for rooting or bootloader unlocking.  

- LLM perspective  
  - View: The chain shows how compiler and JIT complexity in kernels and browsers keeps yielding novel, abusable primitives.  
  - Impact: Expect attackers to generalize these techniques to other stack-corruption bugs, beyond this particular vulnerability and proof-of-concept.  
  - Watch next: Public test tools, cross-kernel reliability studies, and whether Google enforces timely fixes via Play Integrity or similar attestation systems.
