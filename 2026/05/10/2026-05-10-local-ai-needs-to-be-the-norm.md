# Local AI needs to be the norm

- Score: 445 | [HN](https://news.ycombinator.com/item?id=48085821) | Link: https://unix.foo/posts/local-ai-needs-to-be-norm/

### TL;DR

The author argues applications should default to on-device AI because a cloud API turns a feature into a paid distributed system with uptime, billing, networking, privacy, and retention dependencies. His Brutalist Report iOS app summarizes loaded articles locally through Apple Foundation Models, chunking long articles into typed Swift outputs. Local models need not match frontier intelligence for summarization, extraction, classification, rewriting, or normalization; cloud should be reserved for tasks that require it. Commenters favored hybrid fallback strategies but distinguished local execution from private self-hosted or enclave-based inference.

### Comment pulse

- Model-ownership advocates warned remote coding access could vanish without notice, while current open weights remain reusable indefinitely on consumer hardware.
- Shared cloud inference can be far cheaper — counterpoint: local models prevent one commercial service becoming the only viable option.
- Users want local models opt-in; objections to Chrome’s bundled model concerned silent multi-gigabyte installation, not on-device inference itself.

### LLM perspective

- View: Local-first is strongest when inputs are already resident, outputs are bounded, and occasional lower quality is tolerable.
- Impact: Developers trade model capability for privacy, offline resilience, predictable marginal cost, and simpler compliance.
- Watch next: Device coverage, energy use, model-download consent, structured-output reliability, update control, cloud fallback policy, and cross-platform APIs.
