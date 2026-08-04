# Zeroserve: A zero-config web server you can script with eBPF

- Score: 180 | [HN](https://news.ycombinator.com/item?id=48425723) | Link: https://su3.io/posts/introducing-zeroserve

### TL;DR

ZeroServe serves a website and C-written eBPF middleware directly from one tarball, with TLS 1.3 and atomic hot reloads. Its unprivileged userspace runtime JIT-compiles scripts, cages memory accesses, preempts runaways, and uses a single-threaded io_uring event loop. Author-run, one-core HTTPS tests beat nginx for small static responses and small-body proxying, while nginx led large proxies. HN readers liked the experiment but disputed code-as-configuration and static hosting’s relevance, discussed external benchmarks, and suggested Rust scripts, SO_REUSEPORT multi-process scaling, kTLS, and lower-layer BPF integration.

### Comment pulse

- Configuration → Critics argued most operators prefer declarative built-ins over C — counterpoint: config formats often accumulate ad hoc control flow and automation layers.
- Scaling → Commenters proposed process forking with SO_REUSEPORT and kTLS; the author committed to the former, while lower-layer BPF remained exploratory.
- Use cases → Static hosting was dismissed as niche, but respondents cited converted blogs and scientific datasets using formats such as Zarr and Parquet.

### LLM perspective

- **View:** The distinctive bet is not eBPF speed alone, but making bounded imperative behavior the deployable configuration artifact.
- **Impact:** Adopters trade familiar directives for C toolchains, helper APIs, and a younger operational ecosystem with fewer established debugging practices.
- **Watch next:** HTTP/2 benchmarks, multicore SO_REUSEPORT results, kTLS feasibility, script-language support, fuzzing, and third-party security review.
