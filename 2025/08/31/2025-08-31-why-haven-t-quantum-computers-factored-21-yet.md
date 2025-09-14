# Why haven't quantum computers factored 21 yet?

- Score: 340 | [HN](https://news.ycombinator.com/item?id=45082587) | Link: https://algassert.com/post/2500

- TL;DR
    - Factoring 21 hasn’t happened not from QC stagnation but because Shor’s cost jumps ~100× vs 15. For 15, most multiplies are 1, the first multiply is free, and 2k mod 15 reduces to cheap circular shifts. For 21, none apply: constants alternate 4/16; conditional multiply needs ~41 Toffolis each, totaling ~2405 entangling gates; error correction magnifies costs. Hence ‘factor 21’ is a poor benchmark; HN shifts to PQ readiness and scale estimates, urging focus on QEC and buildable architectures.

- Comment pulse
    - PQ crypto now: theoretical QC attacks suffice; symmetric costs ~sqrt speedup; key exchange is urgent due to harvest-now-decrypt-later risk.
    - Estimates: RSA‑2048 ~7B Toffolis, ~1e6 physical qubits, ~week runtime at 1MHz with surface codes — counterpoint: timelines uncertain; materials breakthroughs may be required.
    - Many ‘factored 21’ papers precompile structure, sidestepping real modular multiplication; satire and critiques highlight this.

- LLM perspective
    - View: Small-number demos hide discontinuities; benchmark Shor by modular-multiplication depth and error-corrected cycles, not N value.
    - Impact: Resource estimates guide PQ adoption and hardware roadmaps; shifts focus from toy factoring to QEC, connectivity, and throughput.
    - Watch next: Demonstrations of increasing-distance surface codes with net logical gain; faster, lower-Toffoli modular multiply; modular architectures linking million-qubit systems.
