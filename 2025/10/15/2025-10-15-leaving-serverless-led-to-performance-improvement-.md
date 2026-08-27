# Leaving serverless led to performance improvement and a simplified architecture

- Score: 289 | [HN](https://news.ycombinator.com/item?id=45590756) | Link: https://www.unkey.com/blog/serverless-exit

### TL;DR

Unkey says replacing Cloudflare Workers with stateful Go services cut latency sixfold while simplifying caching, analytics batching, and self-hosting. The team retained global deployment and autoscaling through AWS Fargate and Global Accelerator, but regained predictable in-memory state and direct database flushing. Commenters broadly recognized the architectural friction, while some argued Lambda remains cheap and effective when workloads fit its constraints. Others cautioned that dependency locality, not the serverless label alone, may explain much of the improvement.

### Comment pulse

- Serverless constraints can manufacture extra infrastructure → stateless invocations complicate caching, uploads, batching, and local development.
- Workload fit remains decisive → advocates report excellent Lambda economics, while critics emphasize platform coupling and ambiguous terminology.

### LLM perspective

- View: The strongest result is architectural simplification; the sixfold latency claim remains Unkey's own comparison.
- Impact: Latency-sensitive teams may reconsider stateful services when serverless glue exceeds its operational benefit.
- Watch next: Compare equivalent regions, dependency placement, tail latency, reliability, and total costs across both architectures.
