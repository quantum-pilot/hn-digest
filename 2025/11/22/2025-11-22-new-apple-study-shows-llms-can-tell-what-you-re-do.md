# New Apple Study Shows LLMs Can Tell What You're Doing from Audio and Motion Data

- Score: 64 | [HN](https://news.ycombinator.com/item?id=46015578) | Link: https://9to5mac.com/2025/11/21/apple-research-llm-study-audio-motion-activity/

### TL;DR

Apple researchers tested language-model fusion of sensor clues across 12 everyday activities in 20-second Ego4D samples. The models never received raw audio or motion. Smaller audio and inertial models first produced captions, labels, and predictions; Gemini 2.5 Pro and Qwen-32B then fused those text outputs in closed-set or open-ended prompts. Zero- and one-shot F1 scores beat chance without task-specific training, suggesting a flexible fusion layer when aligned data are limited. Researchers released prompts and sample identifiers for reproduction.

### Comment pulse

- Late fusion is flexible → language models combine heterogeneous outputs without aligned task training — counterpoint: simpler classifiers may be cheaper and sufficient.
- Privacy risk extends beyond raw recordings → stored motion-derived descriptions can reveal activities as inference improves.

### LLM perspective

- View: The novelty is textual sensor fusion, not direct understanding of raw signals.
- Impact: Activity recognition may improve with sparse training data while expanding surveillance inferences.
- Watch next: Baseline comparisons, per-class errors, on-device cost, consent controls, and real-world validation.
