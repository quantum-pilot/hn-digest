# Beyond OpenMP in C++ and Rust: Taskflow, Rayon, Fork Union

- Score: 118 | [HN](https://news.ycombinator.com/item?id=45402820) | Link: https://ashvardanian.com/posts/beyond-openmp-in-cpp-rust/

### TL;DR

The author benchmarks fork-join parallelism and argues that general task pools pay heavily for mutexes, allocations, pessimistic compare-and-swap paths, and false sharing. His roughly 300-line C++ and Rust library, Fork Union, reached within about 20% of OpenMP on a tiny reduction benchmark, while Taskflow, Rayon, and asynchronous executors lagged sharply. He calls the results directional, acknowledges possible memory-ordering bugs, and notes that later releases added NUMA features. Discussion highlights busy-wait CPU use and uneven-workload behavior.

### Comment pulse

- One adopter reported a useful speedup but also 100% CPU consumption from busy waiting.
- The author attributes the largest initial gain over Rayon and Taskflow to eliminating heap-allocated promise and result objects.

### LLM perspective

- View: Specializing for fork-join work buys speed by deliberately rejecting broader scheduler capabilities.
- Impact: Suitable workloads may gain lower overhead, while idle power, nesting, and maintenance become explicit tradeoffs.
- Watch next: Cross-platform benchmarks, ablation results, memory-model review, and improved sleep scheduling.
