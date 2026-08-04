# The Coming Loop

- Score: 299 | [HN](https://news.ycombinator.com/item?id=48643180) | Link: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/

### TL;DR

Outer harness loops keep coding tasks alive after an agent declares completion, restarting sessions, changing context, delegating work, and judging whether to continue. Ronacher finds them excellent for verifiable or disposable work—ports, benchmarks, security scans, and research—but says current models compound defensive checks, local fixes, duplication, and weak invariants in durable systems. Competitive and security pressure may make loops unavoidable, creating codebases humans cannot explain or maintain without models. HN identified specifications and taste as the human bottlenecks, while debating software’s shift from comprehensible machine to managed organism.

### Comment pulse

- Clarity precedes automation → commenters said agents cannot skip the exploratory failures required to understand a problem well enough for a precise specification.
- Goal-driven work tolerates ugly paths → exploits and research prioritize outcomes — counterpoint: lasting features must preserve future changeability, which demands taste.
- Strict tools can strengthen loops → one developer argued Rust’s compiler shifts validation into machine-checkable feedback, despite making human work more demanding.

### LLM perspective

- **View:** The outer loop changes accountability: completion becomes an orchestration verdict, so responsibility can diffuse even when throughput rises.
- **Impact:** Teams may trade comprehensibility for speed, then require permanent model access for diagnosis, review, and repair.
- **Watch next:** Measure long-term defect rates, review burden, architectural drift, model dependency, and human recovery time after loop-generated changes.
