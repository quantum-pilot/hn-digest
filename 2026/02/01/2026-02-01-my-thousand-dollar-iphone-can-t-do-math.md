# My thousand dollar iPhone can't do math

- Score: 80 | [HN](https://news.ycombinator.com/item?id=46849258) | Link: https://journal.rafaelcosta.me/my-thousand-dollar-iphone-cant-do-math/

### TL;DR

An expense-app experiment exposed a device-specific inference failure on the author’s replacement iPhone 16 Pro Max. Apple Intelligence support stalled during download, while several local MLX models produced endless gibberish. Identical code, model, prompt and iOS version worked on an iPhone 15 Pro and MacBook; intermediate tensors began equal but later diverged by roughly an order of magnitude. A subsequent iPhone 17 Pro Max also worked. The author therefore suspects that particular iPhone 16’s hardware or ML compute stack, not his code, was defective.

### Comment pulse

- Skeptics initially blamed vibe-coded software or nondeterministic floating-point accumulation; replies stressed that every comparison device produced the same valid output.
- Readers clarified that the test was not asking an LLM to calculate; it used arithmetic merely to expose broken tensor inference.
- Some speculated about wider predictive-text failures, but the article establishes only one faulty handset.

### LLM perspective

- View: Cross-device reproduction was the decisive debugging move; it separated application logic from one physical execution environment.
- Impact: Device-specific accelerator faults can masquerade as model or framework bugs and consume days without hardware comparison.
- Watch next: Apple’s hardware diagnosis, recurrence reports and minimal tensor tests that isolate Metal, accelerator or memory faults.
