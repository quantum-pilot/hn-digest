# Qwen 3.8 27B is excellent, but it defaults to overthinking things

- Score: 793 | [HN](https://news.ycombinator.com/item?id=49324985) | Link: https://simonwillison.net/2026/Aug/16/qwen-38-27b/

### TL;DR

Qwen 3.8 27B is a 27-billion-parameter, vision-capable Apache-2 model that fits a Q4 build into roughly 17GB and runs locally with 262,144-token context. It produced strong SVGs, accurate pelican bounding boxes, useful code, tool calls, and agent work, but its default xhigh reasoning spent 22,276 thinking tokens and 21 minutes on one drawing. Disabling reasoning was much faster but sometimes less correct; MTP boosted one Spark benchmark about 72%. Commenters celebrated consumer-hardware capability while asking for automatic task-sensitive reasoning effort.

### Comment pulse

- Local capability is the headline → multimodal, long-context, tool-using models now handle useful work on existing consumer hardware.
- Overthinking follows evaluator incentives → under-answering is punished while verbosity is cheap, though extra test-time compute can compensate for smaller models.
- Manual reasoning controls are fragile → injected guidance and unsupported flags can degrade benchmark performance; per-message effort offers a cleaner path.

### LLM perspective

- View: The model’s quality-to-size ratio is exceptional; poor default effort selection, not capability, blocks daily-driver use.
- Impact: Local users gain privacy and autonomy but must trade memory bandwidth, latency, and answer quality task by task.
- Watch next: Independent benchmarks, adaptive reasoning selection, faster MLX serving, and robust MTP support will determine practical adoption.
