# Extract-0: A specialized language model for document information extraction

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45427634) | Link: https://arxiv.org/abs/2509.22906

- TL;DR
  - Extract-0 is a 7B model specialized for document information extraction. Trained on ~280k synthetic examples with LoRA SFT and GRPO using a semantic-similarity reward, it reports a 0.573 mean reward on 1,000 tasks, claiming to beat GPT-4.1 and o3. HN likes the narrow, low-cost approach but flags likely evaluation leakage from train/test slicing within the same dataset and synthetic-only distribution. Calls for external benchmarks and real-world docs temper the headline.

- Comment pulse
  - Evaluation is flawed → Test set is a slice of the training CSV with chunk-level splits; likely data leakage and inflated “beats GPT-4” metrics.
  - Specialized small models matter → Narrow fine-tunes can beat generalists on defined tasks at lower cost — counterpoint: generalists generalize better to unseen formats.
  - Pipeline is interesting → LoRA+GRPO with semantic-sim reward fits ambiguous extraction; needs tests on DocBench, real contracts, low-quality scans.

- LLM perspective
  - View: Specialized IE models can excel, but claims require cross-domain, document-level splits and external benchmarks to rule out leakage.
  - Impact: If validated, 7B LoRA adapters enable cheap, on-prem extraction for enterprises handling PDFs, forms, and filings.
  - Watch next: Release weights, publish reproducible eval scripts, add DocBench/DocLayNet/contract datasets, and include OCR/noise robustness and out-of-distribution tests.
