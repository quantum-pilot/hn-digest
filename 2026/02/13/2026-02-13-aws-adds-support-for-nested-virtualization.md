# AWS Adds support for nested virtualization

- Score: 291 | [HN](https://news.ycombinator.com/item?id=46997133) | Link: https://github.com/aws/aws-sdk-go-v2/commit/3dca5e45d5ad05460b93410087833cbaa624754e

### TL;DR

An AWS SDK for Go changelog adds nested virtualization to EC2, letting virtual machines run inside non-bare-metal instances. The supplied material offers little rollout detail; one commenter says support is limited to c8i, m8i, r8i, and flex variants, with Virtual Secure Mode disabled when nesting is enabled. Discussion centered on Firecracker, sandboxing, CI runners, and uniform development environments that previously needed bare metal or workarounds. Enthusiasm was tempered by questions about instance cost, performance loss, and the complexity and reliability of nested VMX.

### Comment pulse

- MicroVM workloads gain a simpler AWS path → Firecracker, isolated build runners, and test environments can avoid bare-metal-only deployment.
- Operational uniformity may justify slower execution → counterpoint: commenters cite large penalties from existing software workarounds and want AWS benchmarks.
- Availability appears narrow → commenters interpret the Intel-only instance list as a cautious first step, not a broad EC2 rollout.

### LLM perspective

- View: The changelog confirms capability, but the supplied evidence cannot establish broad availability, pricing, or performance.
- Impact: Teams can consolidate nested test and sandbox workloads inside EC2 while accepting another virtualization layer.
- Watch next: AWS documentation, regional rollout, benchmarks, supported hypervisors, VSM implications, failure modes, and expansion beyond listed Intel instances.
