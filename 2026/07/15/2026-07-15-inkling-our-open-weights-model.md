# Inkling: Our Open-Weights Model

- Score: 585 | [HN](https://news.ycombinator.com/item?id=48924912) | Link: https://thinkingmachines.ai/news/introducing-inkling/

### TL;DR

Thinking Machines Lab released Inkling, an open-weights multimodal Mixture-of-Experts model with 975B total parameters, 41B active, a 1M-token context window, and controllable reasoning effort. Trained on 45T text, image, audio, and video tokens, it targets customization rather than overall benchmark leadership; full weights and Tinker fine-tuning are available. A 12B-active Small preview often approaches the larger model. HN welcomed a competitive US-made audio-capable option, but urged workload-specific testing and questioned benchmark comparisons, practical long-context performance, local hardware demands, and the open-weights business model.

### Comment pulse

- National ecosystem mattered → commenters saw a rare competitive non-Chinese open model, while naming Arcee, AllenAI, Reflection, and Meta alternatives.
- Tinker suggested a viable business → enterprises keep specialized weights while the vendor monetizes fine-tuning infrastructure — counterpoint: LoRA offers unclear differentiation.
- Scale constrained accessibility → enthusiasts requested sub-100B models for home inference and warned useful context may collapse beyond 150K–200K tokens.

### LLM perspective

- **View:** The differentiator is the customization stack plus native multimodality, not a single leaderboard win.
- **Impact:** Organizations can own tuned checkpoints while outsourcing expensive post-training and deployment plumbing.
- **Watch next:** Inkling-Small’s weight release, independent audio tests, and quality curves beyond 200K context.
