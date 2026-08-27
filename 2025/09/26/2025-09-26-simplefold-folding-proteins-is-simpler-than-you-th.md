# SimpleFold: Folding proteins is simpler than you think

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45389267) | Link: https://github.com/apple/ml-simplefold

### TL;DR

Apple’s repository accompanies a 2025 preprint for SimpleFold, a protein-structure model using general-purpose transformer layers and flow matching instead of specialized triangle attention or pair-representation biases. The team scaled variants to three billion parameters and trained on experimental PDB structures plus more than 8.6 million distilled predictions, claiming competitive benchmark and ensemble performance. Released code supports PyTorch and Apple-focused MLX inference, evaluation, and training. Commenters stressed that architectural simplicity does not mean raw-data independence or state-of-the-art accuracy, because most supervision came from predictions produced by complex upstream models.

### Comment pulse

- Supporters viewed the simpler scaling baseline as a foundation onto which useful domain-specific machinery could later be added.
- Skeptics emphasized distillation dependence and said the paper’s reported metrics remain behind leading systems.

### LLM perspective

- View: SimpleFold simplifies the student architecture, not the knowledge pipeline that created its training targets.
- Impact: Easier local inference could broaden experimentation, while inherited prediction biases may constrain novelty and reliability.
- Watch next: Results on remote proteins, experimental-only training, accuracy gaps, inference cost, and independent benchmark replication.
