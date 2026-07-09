# Cloudflare Meerkat - Globally distributed consensus

- Score: 202 | [HN](https://news.ycombinator.com/item?id=48831565) | Link: https://blog.cloudflare.com/meerkat-introduction/

- TL;DR  
Cloudflare’s Meerkat is a globally distributed, leaderless consensus system built on QuePaxa, an asynchronous protocol that avoids Raft/Paxos-style timeouts and leader elections. It globally orders all operations (including many reads), favoring robustness on messy networks over raw latency, and is aimed at infrastructure use cases rather than databases. HN finds the write-up unfocused on what’s novel, but sees Meerkat as the first major QuePaxa deployment and is cautiously optimistic about Cloudflare’s ability to run and verify it.  
*Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Novelty unclear → blog reads like Raft/Paxos explainer; Meerkat’s real differentiator (QuePaxa, async no-timeout liveness) is buried—counterpoint: still valuable as public deployment.  
  - Async consensus appeal → no leaders or timeouts, better under flaky networks; concern shifts to long-tail latencies and tricky failure behaviors instead of bounded-timeout stalls.  
  - Practical doubts → many round trips and serialized reads hurt performance; seen as niche, non-database tool, though Cloudflare is one of few able to run it.

- LLM perspective  
  - View: Meerkat tests whether fully async consensus can be competitive enough to matter outside research prototypes.  
  - Impact: If stable, infrastructure like config, coordination, and key management may standardize on timeout-free leaderless consensus.  
  - Watch next: Independent benchmarks, real incident reports, and formal verification artifacts will reveal whether QuePaxa holds up at Cloudflare scale.
