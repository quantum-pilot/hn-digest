# How I turned Zig into my favorite language to write network programs in

- Score: 308 | [HN](https://news.ycombinator.com/item?id=45716109) | Link: https://lalinsky.com/2025/10/26/zio-async-io-for-zig.html

### TL;DR

After rewriting an AcoustID index in Zig, the author found networking and concurrency less convenient than in Go or callback-heavy Qt. He built Zio to provide Go-style cooperative concurrency through fixed-stack, stackful coroutines: apparently synchronous reads suspend tasks while background I/O proceeds. Zio supports asynchronous network and file operations, synchronization primitives, channels, signals, and single- or multithreaded runtimes. The author claims exceptional early performance but withholds benchmarks, acknowledges multithreaded robustness is still developing, and plans integration with Zig’s forthcoming I/O interface.

### Comment pulse

- Readers debated stackful memory costs, stack sizing, branch prediction, cancellation, and timeout design.
- Some questioned adopting Zio during Zig’s I/O transition; others viewed the future interface as compatible evolution.

### LLM perspective

- View: Zio’s synchronous style is compelling, but fixed stacks trade callback complexity for memory and safety obligations.
- Impact: If robust, it could make Zig practical for complete network services rather than only performance-critical components.
- Watch next: Reproducible benchmarks, timeout semantics, stack-overflow defenses, fairness, and Zig 0.16 integration.
