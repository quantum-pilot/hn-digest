# Google's 200M-parameter time-series foundation model with 16k context

- Score: 286 | [HN](https://news.ycombinator.com/item?id=47583045) | Link: https://github.com/google-research/timesfm

### TL;DR
Google’s TimesFM 2.5 is a 200M‑parameter, decoder‑only “foundation model” for time‑series forecasting. It takes up to 16k past data points and outputs point forecasts plus optional quantiles over horizons up to 1k steps. The new release shrinks the model (from 500M) while extending context and adding a separate 30M “quantile head,” with PyTorch/Flax implementations and BigQuery integration. HN discussion centers on whether a single generic model can meaningfully forecast diverse domains and how much it actually helps versus classical methods.

### Comment pulse
- General model skepticism → Model really learns reusable patterns (trend, seasonality, ARMA‑like dynamics); cannot foresee exogenous shocks—counterpoint: lack of explanations makes trusting forecasts hard.  
- Practical value → At Google Ads, generic time‑series models significantly outperformed naive extrapolation, giving useful 95% intervals across many campaigns.  
- Ecosystem questions → Not brand‑new; 2.5 is a late‑2025 update. People ask about training cost, and compare with Nixtla, Prophet, and Amazon Chronos.

### LLM perspective
- View → Treat this as a strong, general “default forecaster” that encodes decades of time‑series tricks into one model.  
- Impact → Leveling up forecasting for teams that lack in‑house statisticians; easier experimentation across many series without per‑project modeling.  
- Watch next → Independent benchmarks vs Chronos/Prophet/Nixtla, open training‑compute stats, and tooling for interpretability and scenario stress‑testing.
