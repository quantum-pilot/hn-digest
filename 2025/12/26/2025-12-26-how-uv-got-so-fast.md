# How uv got so fast

- Score: 1245 | [HN](https://news.ycombinator.com/item?id=46393992) | Link: https://nesbitt.io/2025/12/26/how-uv-got-so-fast.html

### TL;DR
uv is dramatically faster than pip not mainly because it’s written in Rust, but because it exploits a decade of new Python packaging standards and drops legacy behavior. Static metadata (PEP 518/517/621/658) removes `setup.py` code execution from the hot path; uv further skips eggs, `pip.conf`, bytecode compilation, permissive parsing, and multi-index probing. It adds parallel downloads, metadata-only resolution, global hardlink caches, and a PubGrub solver. Rust then amplifies this via zero-copy caches, no GIL, and single-binary startup.  
  

### Comment pulse
- Design and standards, not Rust alone → Greenfield, spec-driven tooling unlocked 10× speed; compiled single-binary Rust mainly fixes bootstrapping and startup — counterpoint: without benchmarks, weighting factors is speculative.  
- Governance and incentives → A commercial, opinionated project can aggressively drop legacy paths; community FOSS tools get stuck balancing compatibility, politics, and many stakeholders.  
- Meta: writing and claims → Some readers see LLM-edited, list-heavy prose and shaky “Rust-specific” labeling (e.g., zero-copy) as undermining the otherwise useful architectural analysis.  


### LLM perspective
- View: The key lesson is to standardize away dynamic metadata first; only then does a fast implementation meaningfully matter.  
- Impact: Package managers across ecosystems can justify breaking changes to drop legacy paths once static manifests and wheel-like formats are ubiquitous.  
- Watch next: Benchmarked comparisons isolating standards, design choices, and language/runtime effects; pip’s adoption of PubGrub-style resolution and more aggressive wheel-first strategies.
