# Unsloth Dynamic 3.0 GGUFs

- Score: 252 | [HN](https://news.ycombinator.com/item?id=49365443) | Link: https://unsloth.ai/docs/basics/dynamic-3.0-ggufs

### TL;DR

Unsloth released revised Dynamic v3.0 GGUF post-training quants for Qwen3.8-27B, compatible with most inference engines. It claims over 10% better top-1 accuracy than other providers at equal size on some smaller formats, supported by KL divergence and a held-out 300-prompt, 32-token trajectory comparison with BF16. Changes include diverse coding, chat, and multilingual calibration plus finer layer and method selection. A 6.2GB one-bit build reportedly retains about 72% top-1 accuracy. Builds at or below 8.37GB omit MTP to save roughly 500MB, available separately.

### Comment pulse

- Users requested versioned filenames or embedded metadata because revised artifacts currently look identical on disk.
- Local-model users valued privacy and called Qwen3.8-27B usable, while still placing frontier systems ahead.
- Tiny quants split opinion: some reported workable coding, while others found accumulated errors disastrous and wanted longer task benchmarks.

### LLM perspective

- View: The evaluation is more thoughtful, but vendor metrics remain proxies for sustained task quality.
- Impact: Better compression could make a capable 27B model practical on tighter local memory budgets.
- Watch next: Versioned artifacts, independent coding tests, long-horizon divergence, and MTP memory-speed trade-offs.
