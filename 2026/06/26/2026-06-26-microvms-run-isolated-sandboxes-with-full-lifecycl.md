# MicroVMs: Run isolated sandboxes with full lifecycle control

- Score: 237 | [HN](https://news.ycombinator.com/item?id=48642510) | Link: https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/

### TL;DR

AWS Lambda MicroVMs provides per-user Firecracker environments for untrusted or AI-generated code, combining VM isolation with snapshot-based near-instant launch, stateful memory and disk, dedicated endpoints, and automatic suspend/resume. The ARM64 service offers up to 16 vCPUs, 32GB memory and disk, and eight hours of runtime across five regions, complementing event-driven Lambda functions. HN saw a crowded sandbox market and debated native-cloud pricing versus startups or self-hosting, while flagging short lifecycles, bursty CPU scaling, GPU sharing, and narrowly scoped IAM/network access as unresolved needs.

### Comment pulse

- Native clouds may squeeze wrapper startups → commenters questioned reseller value, security, and markups — counterpoint: bare-metal providers can match or beat AWS pricing.
- Session duration mismatches agent work → eight hours suits bursts, but some workflows unpredictably persist for days or months.
- Firecracker does not solve every utilization problem → highly bursty workloads need rapid CPU resizing; GPU sharing and encoding remain difficult.

### LLM perspective

- **View:** AWS productizes proven isolation; differentiation rests on lifecycle orchestration, economics, and secure defaults rather than virtualization alone.
- **Impact:** Coding tools and analytics services can outsource sandbox operations, while specialized vendors must justify portability or deeper capabilities.
- **Watch next:** Evaluate resume latency, snapshot semantics, egress controls, role scoping, burst utilization, and suspended-state pricing under real agent workloads.
