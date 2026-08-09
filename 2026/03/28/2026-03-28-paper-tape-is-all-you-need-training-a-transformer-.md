# Paper Tape Is All You Need – Training a Transformer on a 1976 Minicomputer

- Score: 131 | [HN](https://news.ycombinator.com/item?id=47518568) | Link: https://github.com/dbrll/ATTN-11

### TL;DR

ATTN/11 trains a genuine but minimal transformer entirely in PDP-11 assembly on a 1976 PDP-11/34A. The one-layer, one-head, 1,216-parameter encoder learns to reverse eight digits, reaching 100% training accuracy after 350 SGD steps in 5.5 minutes. A 6,179-byte binary uses 19.2 KB inside 32 KB memory, enabled by hand-tuned layer rates, Q8 activations, Q15 gradients, Q16 accumulators, and lookup-table softmax and loss. It omits feed-forward layers, normalization, and a decoder. Despite the title, no paper-tape reader was used; object code was deposited through the console.

### Comment pulse

- The author argued ideas, not hardware, were limiting: historical Crays could theoretically train surprisingly large models given modern algorithms and months.
- Readers valued the project as controlled time travel, separating architectural insight from today’s abundant compute and data.
- Hardware enthusiasts emphasized the difficulty of 32 KB constraints and proposed ports to other vintage or homebrew processors.

### LLM perspective

- **View:** The demonstration proves algorithmic possibility, not that 1970s systems could support modern-scale language modeling.
- **Impact:** Constraint-driven implementations reveal which optimizer state, precision, and architectural components are essential versus customary.
- **Watch next:** Test-set generalization, cycle-accurate reproducibility, wider tasks, scaling curves, and performance without hardware multiply/divide.
