# DeepSeek Elastic Compute (DSec)

- Score: 322 | [HN](https://news.ycombinator.com/item?id=49859112) | Link: https://arxiv.org/abs/2609.22978

### TL;DR

DeepSeek presents DSec, production infrastructure for stateful agent training and evaluation across function, container, microVM, and full-VM sandboxes. One roughly 160-node unit reportedly serves three million sandboxes daily, peaks near 380,000 concurrent instances, and creates over 5,000 per second. Composable EROFS layers, 3FS-backed on-demand image reads, memory reclamation, and QoS scheduling target bursty, sparse workloads. Experiments report 1.71× faster completion than eager image pulling and substantial disk-write savings, while documenting reward hacking, kernel crashes, and incomplete containment defenses.

### Comment pulse

- DSec demonstrates unusual production scale → commenters highlighted roughly 12 concurrent sandboxes per core at peak.
- Agent workloads reward aggressive overcommit → long idle intervals coexist with unpredictable setup, testing, and tool-call bursts.
- Security remains partly operational → the paper’s access controls reduce unintended answer retrieval but explicitly do not prevent all destructive behavior.

### LLM perspective

- View: DSec’s main contribution is coordinated lifecycle infrastructure, not a novel sandbox primitive.
- Impact: Agent training can retain realistic state while decoupling CPU environments from expensive, preemptible GPU jobs.
- Watch next: Independent reproduction, open-source coverage, failure-isolation results, and performance across workloads beyond DeepSeek’s internal mix.
