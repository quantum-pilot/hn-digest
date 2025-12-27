# How uv got so fast

- Score: 967 | [HN](https://news.ycombinator.com/item?id=46393992) | Link: https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html

### TL;DR
uv’s big speedup over pip comes less from Rust and more from treating Python packaging as a well-specified system built on recent standards. PEPs 518/517/621/658 enabled static, declarative metadata so uv can resolve dependencies without executing arbitrary setup.py code and can fetch wheel metadata with HTTP range requests. It also drops legacy features (eggs, pip.conf, permissive parsing), favors wheels and a global hardlinked cache, and uses PubGrub. Rust then adds smaller wins via zero-copy caching, cheaper concurrency, and no interpreter startup. HN debates how much credit belongs to design vs Rust, and veers into meta-discussion about LLM-shaped prose.

---

### Comment pulse
- Design-first, greenfield approach → Main speed gain is from rethinking packaging as a systems problem, enabled by new PEPs, not simply “Rust rewrite.”  
- Language choice still matters → Rust brings faster TOML parsing, better concurrency, and attracts certain engineers—counterpoint: without benchmarks, attributing exact shares of speed is speculative.  
- AI-smell backlash → Some readers find the prose LLM-like and off-putting; others warn against over-attributing any polished writing to AI.

---

### LLM perspective
- View: uv exemplifies how strict specs plus willingness to drop legacy afford bigger gains than micro-optimizing existing tools.  
- Impact: Encourages other ecosystems to standardize metadata, ban code-on-import, and treat “compatibility forever” as an explicit, costly choice.  
- Watch next: Benchmarks isolating design vs Rust effects, pip adopting PubGrub/parallelism, and tooling to safely migrate away from legacy Python packages.
