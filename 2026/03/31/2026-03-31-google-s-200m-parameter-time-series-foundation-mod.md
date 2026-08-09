# Google's 200M-parameter time-series foundation model with 16k context

- Score: 286 | [HN](https://news.ycombinator.com/item?id=47583045) | Link: https://github.com/google-research/timesfm

### TL;DR

Google Research’s TimesFM 2.5 is a pretrained forecasting model with 200 million parameters, down from 500 million, and context up to 16,000 points instead of 2,048. It supports point forecasts plus continuous quantiles out to a 1,000-step horizon through an optional 30-million-parameter head; covariates returned through XReg after launch. Apache-licensed checkpoints run through PyTorch or Flax, while BigQuery offers an official product integration. HN debated what a general time-series model can reliably learn across unrelated domains and how users should trust predictions without explanations.

### Comment pulse

- Shared trend, seasonal, and autoregressive motifs justify general pretraining — counterpoint: wars and other unseen external causes remain outside historical patterns.
- The underlying paper dates to 2024, but version 2.5 substantially changed size and context in September 2025.
- Readers wanted training-compute figures, simpler usage explanations, and comparisons with Nixtla, Prophet, and Chronos.

### LLM perspective

- **View:** A cross-domain temporal prior is a forecasting baseline, not a substitute for causal or domain-specific models.
- **Impact:** Smaller weights and longer context lower deployment barriers for labs and teams testing pretrained forecasts.
- **Watch next:** Independent benchmarks, covariate gains, uncertainty calibration, training cost, long-context scaling, and robustness to regime changes.
