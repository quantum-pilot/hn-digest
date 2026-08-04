# GhostLock, a stack-UAF that has existed in all Linux distributions for 15 years

- Score: 391 | [HN](https://news.ycombinator.com/item?id=48834309) | Link: https://nebusec.ai/research/ionstack-part-2/

### TL;DR

GhostLock (CVE-2026-43499) is a Linux kernel priority-inheritance futex bug present from 2.6.39 through the 7.1 release candidates. On a proxy-lock rollback, rtmutex cleanup clears the requeuing thread’s state instead of the actual waiter’s, leaving a dangling pointer into a returned kernel-stack frame. VEGA and Google turned that unprivileged primitive into a reportedly 97%-reliable root escalation and container escape on kernelCTF. The fix was issued and backported; users should install patched kernels. HN discussion stressed that local access still matters because browser exploits can supply the first stage.

### Comment pulse

- Local does not mean low impact → sandboxed native execution can chain into kernel control, so browser and kernel updates both matter.
- Android exploitation is build-specific → compiler-dependent stack layouts require retuning; unsupported devices in community tests froze, powered off, or boot-looped.
- Common isolation cannot contain kernel compromise → SELinux and containers share the vulnerable kernel — counterpoint: full virtualization can preserve a separate boundary.

### LLM perspective

- **View:** A 15-year lifetime shows concurrency ownership assumptions can evade lock correctness tooling even when the final fix is tiny.
- **Impact:** Long-lived enterprise kernels and poorly updated phones need explicit backports; version age alone does not indicate safety.
- **Watch next:** Confirm vendor advisories, backport status, the follow-up null-dereference fix, and whether stack randomization is enabled on deployed kernels.
