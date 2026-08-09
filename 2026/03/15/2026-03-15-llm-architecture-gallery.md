# LLM Architecture Gallery

- Score: 192 | [HN](https://news.ycombinator.com/item?id=47388676) | Link: https://sebastianraschka.com/llm-architecture-gallery/

### TL;DR

Sebastian Raschka’s gallery turns 38 open-weight LLM architectures released from 2024 through March 2026 into comparable visual cards covering scale, active parameters, decoder type, attention, and defining choices. The collection makes the field’s convergence visible: sparse mixture-of-experts dominates large models, while GQA, MLA, QK-Norm, sliding-window attention, DeltaNet, and Mamba hybrids trade memory, context, and throughput differently. HN welcomed the modular overview as a bridge from basic neural networks to real systems, with one commenter noting that architecture can alter effective prompting patterns.

### Comment pulse

- Presentation wins → readers compared it favorably with the Neural Network Zoo and valued zoomable, side-by-side diagrams.
- Modular fact sheets bridge theory and practice → statisticians can trace how reusable components become production model families.
- Architecture affects prompting → longer context and attention design can change which input structures work best.

### LLM perspective

- **View:** The gallery is strongest as a taxonomy; benchmark quality still determines whether architectural novelty matters.
- **Impact:** Researchers and deployers gain a shared vocabulary for comparing capacity, memory, and serving tradeoffs.
- **Watch next:** Corrections, new model cards, and controlled tests linking architecture to latency and prompt behavior.
