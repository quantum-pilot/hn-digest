# A free and open-source rootkit for Linux

- Score: 152 | [HN](https://news.ycombinator.com/item?id=46666288) | Link: https://lwn.net/SubscriberLink/1053099/19c2e8180aeb0438/

### TL;DR

Singularity is an MIT-licensed Linux kernel rootkit published as a security-research testbed, not an endorsement or reported active threat. Once installed after an existing compromise, it uses Ftrace hooks to conceal its module, selected processes, files, logs, and TCP traffic, while granting hidden processes root access. Its defenses have limits: offline disk inspection, external network monitoring, compile-time Ftrace removal, and observable refusal to disable Ftrace can expose it. HN discussion mixed licensing jokes with practical detection and safer filesystem-remapping alternatives.

### Comment pulse

- Defenders can compile kernels without Ftrace → the project’s central hooking mechanism may disappear entirely.
- Kernel hacking inspires legitimate tooling → commenters suggested namespaces, bind mounts, LD_PRELOAD, proot, or upstream fixes instead of VFS hooks.
- Open licensing drew jokes → malicious redistribution could still violate attribution terms, while copyleft would create absurd compliance obligations.

### LLM perspective

- View: Adversarial transparency gives defenders concrete evasion behaviors to reproduce and test.
- Impact: Kernel defenders gain a realistic lab target, while operators see why host-only monitoring cannot establish trust.
- Watch next: Track researcher-submitted detections, kernel-update breakage, and any evidence of deployment in real compromises.
