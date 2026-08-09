# Google releases Gemma 4 open models

- Score: 1046 | [HN](https://news.ycombinator.com/item?id=47616361) | Link: https://deepmind.google/models/gemma/gemma-4/

### TL;DR

Google released Gemma 4 weights in E2B, E4B, 26B A4B, and 31B variants, adding thinking, function calling, audio and vision understanding, 140-language support, and fine-tuning. Google positions the smaller models for offline mobile and IoT use and the larger pair for consumer-GPU coding and agents. Its published benchmarks show large gains over Gemma 3 27B, including 80.0% LiveCodeBench for 31B, but HN’s first-day tests were mixed: 26B impressed some laptop users, while runtime flags, quantizations, tool setup, and 31B failures complicated comparisons.

### Comment pulse

- Early quants appeared quickly, but setup remained rough for nondevelopers and correct chat templates, reasoning flags, and EOS handling mattered.
- One wrong timestamp exposed harness ambiguity: generating tool commands is not executing them—counterpoint: another user obtained the correct answer unaided.
- Benchmark tables drew criticism for inconsistent axes, omitted competitors, and results that did not cleanly predict hardware-specific usefulness.

### LLM perspective

- **View:** Release-day model quality cannot be separated from rapidly changing runtimes, templates, quantizations, and multimodal adapters.
- **Impact:** Local developers gain new consumer-hardware options, while edge builders get compact multimodal models for private offline applications.
- **Watch next:** Stable official quants, 16/24GB performance, tool-call reliability, 31B runtime fixes, and independent matched-setting benchmarks.
