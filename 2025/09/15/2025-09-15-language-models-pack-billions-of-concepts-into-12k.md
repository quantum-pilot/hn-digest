# Language models pack billions of concepts into 12k dimensions

- Score: 357 | [HN](https://news.ycombinator.com/item?id=45245948) | Link: https://nickyoder.com/johnson-lindenstrauss/

- TL;DR
    - The post argues that language models fit many “concepts” into ~12k dimensions by leveraging quasi-orthogonality and the Johnson–Lindenstrauss (JL) lemma. It fixes a toy “near-orthogonal vectors” optimization (avoiding a degenerate “basis replication” minimum), finds max pairwise angles ≈76.5°, and reports low empirical JL constants, implying vast capacity. HN pushes back: this is spherical coding without citations, plots look inconsistent, and capacity extrapolations and orthogonality focus are likely overoptimistic; others note cosine-based training and SAE/superposition results support near-orthogonal features.

- Comment pulse
    - This is spherical codes → prior literature exists; missing citations and possible axis errors undermine claims — counterpoint: rediscovery happens; clarify axes and publish code/data.
    - Capacity claim is too optimistic → ranking preservation with small ε matters more than near-orthogonality; extrapolations look shaky — counterpoint: cosine-based objectives make near-orthogonality practically relevant.
    - LLMs don’t store orthogonal concepts in one layer → dense superposition; SAEs recover sparse, near-orthogonal features across layers.

- LLM perspective
    - View: Treat as a spherical-coding/JL capacity intuition; interesting fix to loss-pathology, but measured “C” and angles need rigorous validation.
    - Impact: If low C is reproducible, smaller embeddings suffice for retrieval/semantic search; training still constrained by task-specific geometry.
    - Watch next: Independent replications, standardized cosine-distance benchmarks, SAE layer-wise analyses, clarified plots with uncertainty, and comparisons to known spherical code bounds.
