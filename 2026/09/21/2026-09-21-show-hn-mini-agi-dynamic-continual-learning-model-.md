# Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM

- Score: 270 | [HN](https://news.ycombinator.com/item?id=49783133) | Link: https://github.com/volotat/mini-AGI/

### TL;DR

Mini-AGI is a toy byte-level language model designed to train continually on one 8GB GPU. It pages experts and optimizer state between disk, RAM, and VRAM, grows or prunes its expert pool, and limits shared-trunk learning to reduce interference. The author reports retaining 99.84% of progress against chance after a 524,000-character single-subject probe, but weights are not yet released and generated samples remain weak. HN readers praised the experiment while challenging its name, evaluation depth, and long-term catastrophic-forgetting claim.

### Comment pulse

- The forgetting result is narrow → slowing trunk updates may delay interference without proving retention over indefinite growth and pruning.
- Current generations show toy-level capability → commenters found repetition, incoherent answers, and illegal chess continuations despite improving loss.
- The implementation remains an interesting experiment → consumer-hardware continual training invites replication — counterpoint: calling it AGI substantially overstates demonstrated capability.

### LLM perspective

- View: The project tests an unusual memory architecture; it does not yet establish general intelligence or durable continual learning.
- Impact: Hobbyists gain a concrete, affordable platform for studying paging, routing, and sequential training.
- Watch next: Release weights, add standard baselines, run long-horizon retention tests, and ablate growth, pruning, and trunk rates.
