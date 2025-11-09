# Making Democracy Work: Fixing and Simplifying Egalitarian Paxos

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45854862) | Link: https://arxiv.org/abs/2511.02743

- TL;DR
  - EPaxos* revisits leaderless Egalitarian Paxos: it fixes subtle bugs, simplifies failure recovery, and provides a proof of correctness. It preserves the 2‑message “fast path” when operations commute, and generalizes fault thresholds with an optimal node-count bound n ≥ max{2e+f−1, 2f+1}. HN discussants welcome the cleanup and push for machine-checked proofs (TLA+, Verus), citing Cassandra’s Accord as a real-world derivative. Others clarify the Paxos/Multi‑Paxos leader terminology, and explain how EPaxos infers conflicts and orders them via dependencies for linearizable replay.

- Comment pulse
  - Formal verification desired → specify and check EPaxos* in TLA+/Verus; Cassandra’s Accord is undergoing similar proof efforts.
  - Paxos naming debate → Lamport’s “Paxos” spans single and multi‑decree; most deployments use a leader for performance — counterpoint: some insist Paxos is leaderless.
  - How EPaxos orders → replicas detect conflicts via read/write sets, build dependencies, ensure linearizability; recovery can insert a no‑op barrier enabling consistent replay.

- LLM perspective
  - View: Correctness proof plus simpler recovery makes EPaxos‑style protocols more adoptable beyond papers.
  - Impact: Geo‑replicated databases and services can reduce leader hotspots, tolerate failures, and exploit commutative workloads for lower latency.
  - Watch next: Release TLA+/Verus artifacts; produce reference implementation; benchmark against Raft/Multi‑Paxos and Accord under heterogeneity, failures, and conflict rates.
