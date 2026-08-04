# What xAI's Grok build CLI sends to xAI: A wire-level analysis

- Score: 395 | [HN](https://news.ycombinator.com/item?id=48877371) | Link: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547

### TL;DR

A wire-level test of Grok Build CLI 0.2.93 found two distinct outbound paths: files the agent read, including canary secrets, entered model requests and session archives, while a separate storage pipeline uploaded complete tracked repositories as git bundles, including unread files and history. Captures showed successful multi-gigabyte transfers to an xAI-named Google Cloud Storage bucket even with model-improvement disabled. The author did not prove training use. After publication, xAI reportedly disabled uploads server-side and promised deletion; its `/privacy` option affects retention, not transmission. HN readers emphasized sandboxing and questioned consent.

### Comment pulse

- Bulk upload crossed expectations → commenters distinguished necessary model context from storage of unread files and history — counterpoint: some assumed full workspace trust.
- Sandboxing is the practical defense → restrict workspace mounts and network destinations so proprietary runners cannot inspect unrelated files or contact auxiliary services.
- Open runners offer auditability, not confidentiality → providers can reconstruct exposed code through ordinary tool calls, even without an obvious bulk-upload endpoint.

### LLM perspective

- **View:** The strongest evidence is reproducible transmission and acceptance; motive, training use, and universal behavior remain unproven.
- **Impact:** Default repository archiving can breach confidentiality, consume bandwidth, and invalidate assumptions that only task-relevant context leaves the machine.
- **Watch next:** Verify upload disablement, deletion completion, and whether privacy controls block transmission rather than merely changing retention.
